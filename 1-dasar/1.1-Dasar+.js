console.clear();

// Array = []
// Bisa Semua Tipe Data
const array = [];

// Operation
array.push("*Value");       // Menambah Nilai
console.log(typeof(array))

array[array.length] = ["Badminton","Shuttle"];  // Menambah nilai di index tertentu
console.log(`Panjang Array ${array.length}`);   // array.length untuk pendapat panjang array
console.log(`Nilai dari array [1][0] = ${array[1][1]}`); // mengambil nilai array[1][1]
console.table(array); // => agar Output berbentuk table
delete array[0]; // Menghilangkan Nilai dalam index tertentu

console.table(array); // => agar Output berbentuk table
console.log(typeof(array))

// Object (Mirip Array namun Index dapat berupa String)
const person = {};
person["nama_lengkap"] = "Kevin Setiadi";
person["TTL"] = "2006-09-21";
person["gender"] = "male";

delete person['gender'];
console.table(person);

const mobil ={
    "merk": "BMW",
    "keluaran": 1994
};
console.table(mobil);

console.log(`Merk\t\t:${mobil.merk}`)
console.log(`Keluaran\t:${mobil.keluaran}`)

// Percabangan (if, Else if, else)
const nilai = 85
process.stdout.write("Kamu mendapat Nilai: ",);
if(nilai >= 85){
    console.log("A");
}else if(array<=45){
    console.log("D");
}else{
    console.log("Ga niat");
}

