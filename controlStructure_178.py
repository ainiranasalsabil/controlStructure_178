#no 1
#Fungsi ini meminta input dari pengguna dengan prompt "Masukan Nilai Mahasiswa : ".
nilai = int(input("Masukan Nilai Mahasiswa : "))
#kondisi pertama dalam percabangan if lebih besar atau sama dengan 90.
if nilai >=90:
    #jika nilai ≥ 90, maka mahasiswa dianggap memiliki kinerja yang sangat baik (Excellent performance).
    print("then Excellent performance")
elif nilai >=80:
    print("then  Very Good performance")
elif nilai >=70:
    print("then Good performance")
elif nilai >=60:
    print("then average performance")

#2
#Pendefinisian fungsi
def angkaTerbesar (a,b,c):
    #Kondisi pertama di dalam fungsi.
    if  a >= b and a >= c:
        return a
    #Jika kondisi pertama tidak terpenuhi, maka program akan mengecek kondisi kedua menggunakan elif (else if).
    elif b >= a and b >=c:
        return b
    #Jika kedua kondisi sebelumnya tidak terpenuhi, maka bagian else akan dieksekusi.
    else :
        return c
#Baris-baris ini digunakan untuk meminta input dari pengguna.
angka1 = int( input('angka pertama ='))
angka2 = int( input('angka kedua ='))
angka3 = int( input('angka ketiga ='))
print('angka terbesar adalah', angkaTerbesar(angka1,angka2,angka3))

#3
#Program meminta pengguna untuk memasukkan nilai n yang merupakan batas akhir dari deret Fibonacci yang akan dihasilkan.
n = int(input("Masukkan nilai n: "))
#Inisialisasi dua variabel, a dan b, untuk menyimpan dua angka pertama dari deret Fibonacci.
#a = 0 adalah angka pertama dalam deret Fibonacci, dan b = 1 adalah angka kedua.
a, b = 0, 1
#Mencetak teks "Deret Fibonacci:" sebagai judul sebelum mencetak deretnya.
print("Deret Fibonacci:")
#while adalah loop yang akan terus berjalan selama nilai a kurang dari atau sama dengan n (nilai yang dimasukkan oleh pengguna).
while a <= n:
    print(a, end=" ")
    a, b = b, a + b

#4
def angka_ganjil():
    #List comprehension digunakan untuk membuat daftar angka ganjil dari 1 hingga n. Fungsi range(1, n + 1) menghasilkan bilangan bulat dari 1 hingga n. 
    # Kondisi i % 2 != 0 memeriksa apakah angka i ganjil (tidak habis dibagi 2), sehingga hanya angka ganjil yang dimasukkan ke dalam daftar ganjil.
    n = int(input("Masukkan batas n untuk angka ganjil: "))
    ganjil = [i for i in range(1, n + 1) if i % 2 != 0]
    print("Angka ganjil hingga", n, "adalah:", ganjil)

# Memanggil fungsi
angka_ganjil()


#5 
# Function to print the pattern
#Kode ini mendefinisikan fungsi print_pattern(n) yang mencetak pola berdasarkan angka yang diberikan. 
# Untuk setiap angka dari 1 hingga n, angka tersebut dicetak sebanyak nilainya di setiap baris.
# for i in range(1, n + 1): Loop yang berjalan dari 1 hingga n.
# print((str(i) + ' ') * i): Mencetak angka i sebanyak i kali, dipisahkan oleh spasi.
# Program juga meminta input pengguna untuk nilai n, kemudian memanggil fungsi print_pattern(n) untuk mencetak polanya.
def print_pattern(n):
    for i in range(1, n + 1):
        # Print i, i times
        print((str(i) + ' ') * i)

# Get user input
n = int(input("Enter the value of n: "))
print_pattern(n)





 