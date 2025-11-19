import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Konfigurasi Deteksi Tangan
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,            # Fokus pada 1 tangan dulu agar stabil
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Membuka Kamera
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    """
    Fungsi untuk menghitung jari yang terbuka dan menentukan gestur.
    Mengembalikan: (Total Jari, Nama Gestur)
    """
    
    # ID Titik Ujung Jari (Tips)
    finger_tips = [8, 12, 16, 20] # Telunjuk, Tengah, Manis, Kelingking
    # ID Titik Pangkal Jari (PIP Joints - buku jari kedua dari bawah)
    finger_pips = [6, 10, 14, 18]

    fingers_status = [] # 1 = Terbuka, 0 = Tertutup

    # 1. Logika Jempol (Thumb)
    # Jempol itu unik, dia bergerak ke samping.
    # Kita cek apakah ujung jempol (4) berada di sebelah kanan/kiri buku jarinya (3)
    # Perlu penyesuaian logika tergantung tangan kanan/kiri, tapi ini logika umum:
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers_status.append(1) # Anggap terbuka jika melebar ke kiri (untuk tangan kanan)
    else:
        fingers_status.append(0)

    # 2. Logika 4 Jari Lainnya
    # Bandingkan posisi Y ujung jari dengan Y pangkal jari.
    # Di OpenCV, koordinat Y 0 itu di atas. Jadi kalau Y Tip < Y PIP, berarti jari naik.
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers_status.append(1)
        else:
            fingers_status.append(0)

    total_fingers = fingers_status.count(1)
    gesture = "Tidak Diketahui"

    # --- LOGIKA PEMETAAN GESTUR ---
    # fingers_status urutannya: [Jempol, Telunjuk, Tengah, Manis, Kelingking]
    
    if total_fingers == 0:
        gesture = "BATU (Fist)"
    elif total_fingers == 5:
        gesture = "KERTAS (Open)"
    elif fingers_status == [0, 1, 1, 0, 0]: 
        gesture = "GUNTING (Victory)"
    elif fingers_status == [0, 1, 0, 0, 0]:
        gesture = "MENUNJUK (Point)"
    elif fingers_status == [1, 0, 0, 0, 0]:
        gesture = "JEMPOL (Ok/Good)" # Tergantung orientasi tangan
    elif fingers_status == [1, 0, 0, 0, 1]:
        gesture = "SHAKA (Call Me)"
    elif fingers_status == [0, 1, 0, 0, 1]:
        gesture = "ROCK & ROLL"
    elif fingers_status == [0, 0, 0, 0, 1]:
        gesture = "L"
    elif fingers_status == [1, 1, 0, 0, 0]:
        gesture = "Pistol"
    return total_fingers, gesture

print("Tekan 'q' untuk keluar...")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Gagal membaca frame kamera.")
        continue

    # Flip gambar agar seperti cermin (mirror)
    image = cv2.flip(image, 1)

    # Konversi BGR (OpenCV) ke RGB (MediaPipe)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Proses deteksi tangan
    results = hands.process(image_rgb)

    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            # 1. Gambar kerangka tangan (Skeleton)
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # 2. Analisis Gestur
            count, gesture_name = count_fingers(hand_landmarks)

            # 3. Tampilkan Teks di Layar
            # Kotak background untuk teks
            cv2.rectangle(image, (10, 10), (350, 80), (0, 0, 0), -1) 
            
            # Teks Gestur
            cv2.putText(image, f'Gestur: {gesture_name}', (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Tampilkan window
    cv2.imshow('Program Deteksi Hand Sign', image)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()