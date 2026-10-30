# meminta input dari pengguna
angka1 = float(input("Masukan angka pertama:"))
angka2 = float(input("Masukan angka kedua:"))

#menentukan angka maksimal
if angka1 >  angka2:
    maksimal = angka1
else:
    makismal = angka2

    #menampilkan hasil
    print(f"Angka maksimal adalah: {21}")







    #SOAL LATIHAN NOMOR 2

    #menampilka menu pilihan
    print("---PILIHAN MENU---")
    print("1. Menghitung keliling lingkaran")
    print("2. Menghitung luas lingkaran")
    pilihan = input("masukan pilihan anda(1 atau 2):")

    #meminta input jari-jari

jari_jari = float(input("Masukan nilai jari jari:"))
phi = 3.14

#memproses berdasarkan pilihan
if pilihan =="1":
    keliling = 2*phi*jari_jari
    print(f"keliling lingkaran adalah: {keliling}")
elif pilihan == "2":
    luas = phi*jari_jari*jari_jari
    print(f"luas lingkaran adalah: {luas}")
else:
    print("pilihantidak valid! Silahkan pilih angka 1 atau 2.")