/*
==========================================================
||                      Tipe Data                       ||
==========================================================
*/
// Tipe Data (Number)
const hexa = document.getElementById("hexa");
const bine = document.getElementById("bine");
const octa = document.getElementById("octa");
hexa.textContent = 0xFF; // basis 16
bine.textContent = 0b011111111; // basis 2
octa.textContent = 0o377; // basis 8

// Tipe Data (Logical)
const bool = document.getElementById("bool");
bool.textContent = true; // basis 8

// Tipe Data (String)
const str = document.getElementById("str");
const burung = "🕊️";
// str.textContent = `Happy Sunday ${burung}`;
str.textContent = `Happy Sunday ` + burung;

// Esc Sequence
/*
    \n  Enter
    \t  TAB
    \'  '
    \"  "
    \\  \
*/

/* 
==========================================================
||                          Variabel                    ||
==========================================================
*/

let nama_variabel; // Deklarasi
nama_variabel = "Kevin Setiadi Wijaya"; // Assign Value
let nomor_telp = '0812-3456-7890';

data_diri = "Nama\t: " + nama_variabel + '\n' + 'Nomor\t: ' + nomor_telp;

/* 
==========================================================
||                          Operator                    ||
==========================================================

__________________________________________________________________________________________
| Operator Aritmatika | Deskripsi               | Augmented Assignments | Operator Unary |
| :-----------------: | :---------------------: | :-------------------: | :------------: |
|         +           | Pertambahan             |         +=            |     ++         |
|         -           | Pengurangan             |         -=            |     --         |
|         *           | Perkalian               |         *=            |  (Tidak Ada)   |
|         /           | Pembagian               |         /=            |  (Tidak Ada)   |
|         %           | Modulo (Sisa Bagi)      |         %=            |  (Tidak Ada)   |
|         **          | Eksponensial (Pangkat)  |         **=           |  (Tidak Ada)   |
------------------------------------------------------------------------------------------
__________________________________________________________________________________________________
| Operator Perbandingan | Deskripsi                               | Contoh (a=5, b='5') | Hasil  |
| :-------------------: | :-------------------------------------: | :-----------------: | :----: |
|         ==            | Sama dengan (Loose Equality)            |       a == b        |  true  |
|         ===           | Sama dengan (Strict Equality)           |       a === b       |  false |
|         !=            | Tidak sama dengan (Loose Inequality)    |       a != b        |  false |
|         !==           | Tidak sama dengan (Strict Inequality)   |       a !== b       |  true  |
|         >             | Lebih besar dari                        |       a >  b        |  false |
|         <             | Lebih kecil dari                        |       a <  b        |  false |
|         >=            | Lebih besar dari atau sama dengan       |       a >= b        |  true  |
|         <=            | Lebih kecil dari atau sama dengan       |       a <= b        |  true  |
--------------------------------------------------------------------------------------------------
______________________________________________________________
| Operator Logika | Simbol | Contoh (a=true, b=false) | Hasil |
| :-------------: | :----: | :----------------------: | :---: |
|       DAN       |   &&   |         a && b           | false |
|       ATAU      |   ||   |         a || b           | true  |
|       TIDAK     |   !    |         !a               | false |
|                 |        |         !b               | true  |
---------------------------------------------------------------
*/
parseFloat()

