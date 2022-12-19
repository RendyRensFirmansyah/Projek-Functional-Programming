from functools import reduce
import os

lisUsia = []
lisNama = []
total_pendapatan = [0]

def clearSystem():
    os.system("cls")

def menu():
    print("==========================================")
    print("       KOS BEBAS JALAN SEMERU JEMBER      ")
    print("==========================================")
    print("\t1. Pemesanan                            ")
    print("\t2. Cek Usia                             ")
    print("\t3. Cek Nama Pemesan Kos                 ")
    print("\t4. Cek Pendapatan                       ")
    print("==========================================")
    print()
    print("Pilih 1 untuk melakukan pemesanan")
    print("Pilih 2 untuk melihat usia pemesan")
    print("Pilih 3 untuk melihat daftar nama pemesan")
    print("Pilih 4 untuk melihat total pendapatan")
    print()
    inputOption = int(input("Pilih option : "))
    return displayPemesanan() if inputOption == 1 else cekUsia() if inputOption == 2 else cekNama() if inputOption == 3 else cekPendapatan() if inputOption == 4 else print("Inputan tidak diketahui")
    
def kamar1():
    global lamaHari, jenisKamar, jumlahakhir,pesanHari
    jenisKamar = "Kamar Kos + KM Luar"
    hargaKamar = 30000
    h1 = lambda x : x * hargaKamar
    print("\tKamar yang dipilih adalah", jenisKamar)
    lamaHari = int(input("\tLama Pemesanan (Berapa hari/bulan) : "))
    pesanHari = h1(lamaHari)
    total_pendapatan.append(pesanHari)  
def kamar2():
    global lamaHari, pesanHari, jenisKamar
    jenisKamar = "Kamar Kos + KM Dalam"
    hargaKamar = 60000
    h2 = lambda x : x * hargaKamar
    print("\tKamar yang dipilih adalah", jenisKamar)
    lamaHari = int(input("\tLama Pemesanan (Berapa hari/bulan) : "))
    pesanHari = h2(lamaHari)
    total_pendapatan.append(pesanHari)
#-------------------------------------------------------------------------------------------------------
def kamar3():
    global lamaHari, pesanHari, jenisKamar
    jenisKamar = "Kamar Kos + KM Dalam + AC"
    hargaKamar = 120000
    h3 = lambda x : x * hargaKamar
    print("\tKamar yang dipilih adalah", jenisKamar)
    lamaHari = int(input("\tLama Pemesanan (Berapa hari/bulan) : "))
    pesanHari = h3(lamaHari)
    total_pendapatan.append(pesanHari)
def kamar4():
    global lamaHari, pesanHari, jenisKamar
    jenisKamar = "Kamar Kos + KM Dalam + AC + Dapur"
    hargaKamar = 250000
    h4 = lambda x : x * hargaKamar
    print("\tKamar yang dipilih adalah", jenisKamar)
    lamaHari = int(input("\tLama Pemesanan (Berapa hari/bulan) : "))
    pesanHari = h4(lamaHari)
    total_pendapatan.append(pesanHari)
def percabangan():
    optionKamar = int(input("\tPilih Jenis Kamar : "))
    return kamar1() if optionKamar == 1 else kamar2() if optionKamar == 2 else kamar3() if optionKamar == 3 else kamar4() if optionKamar == 4 else print("Maaf nomor yang anda inputkan tidak diketahui")    

def displayPemesanan():
    global total
    clearSystem()
    print("\t============================================")
    print("\t|                                          |")
    print("\t|        PEMESANAN KOS BEBAS SEMERU        |")
    print("\t|           HARIAN ATAU BULANAN            |")
    print("\t|                                          |")
    print("\t============================================")
    print()
    print("SELAMAT DATANG, SILAHKAN MEMESANAN KAMAR KOS JIKA ANDA BERKENAN.")
    print()
    input("\tTekan >>>ENTER<<< Untuk Melakukan Pemesanan")

    clearSystem()
    print("\t============================================")
    print("\t|                                          |")
    print("\t|        PEMESANAN KOS BEBAS SEMERU        |")
    print("\t|           HARIAN ATAU BULANAN            |")
    print("\t|                                          |")
    print("\t============================================")
    print()
    namaPemesan = input("\tMasukkan Nama Lengkap : ")
    lisNama.append(namaPemesan)
    print()
    genderOption = input("\tJenis Kelamin : ")
    print()
    usiaPemesan = int(input("\tMasukkan Usia : "))
    lisUsia.append(usiaPemesan)
    print()
    alamatPemesan = input("\tMasukkan Alamat : ")
#---------------------------------------------------------------------------------------------------
    print()
    print("\t================= PILIH JENIS KAMAR KOS =================")
    print("\t1. Kamar Kos + KM Luar                = Rp.30.000  / hari")
    print("\t2. Kamar Kos + KM Dalam               = Rp.60.000  / hari")
    print("\t3. Kamar Kos + KM Dalam + AC          = Rp.120.000 / hari")
    print("\t4. Kamar Kos + KM Dalam + AC + Dapur  = Rp.250.000 / hari")
    print("\t=========================================================")
    print()
    percabangan()
    total = """  
	===============================================================
	\tSUB TOTAL PEMESANAN KAMAR KOS :
	=============================================================== 
	\tNama          : {}
	\tJenis Kelamin : {}
	\tUmur          : {}
	\tAlamat        : {}
	\tJenis Kamar   : {}
	\tSelama        : {} hari
	\tTotal Harga   : RP.{}
	================================================================
	\t~~ TERIMA KASIH TELAH MEMESAN JASA KOSAN KAMI ~~
	================================================================
		""".format( namaPemesan, genderOption, usiaPemesan, alamatPemesan, jenisKamar, lamaHari, pesanHari)
    print()
    clearSystem()
    print(total)
    statusTanya()

def cekUsia():
    inputCek = int(input("Inputkan usia yang akan dicek : "))
    cek = list(filter(lambda x : x == inputCek, lisUsia))
    print("Daftar Usia ",inputCek," Tahun : ", cek)
    # print(lisUsia)
    statusTanya()
    
def cekPendapatan():
    jumlah = reduce(lambda x,y : x+y, total_pendapatan)
    print("Pendapatan sewa kos anda adalah sebesar Rp.",jumlah)
    statusTanya()

def cekNama():
    print("Berikut daftar nama pemesan kos : ",lisNama)
    statusTanya()
    
def statusTanya():
    input("Tekan ENTER untuk kembali ke menu")
    clearSystem()
    menu()
    
clearSystem()    
menu()