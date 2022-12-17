import os, time

def clearSystem():
    os.system("cls")
    
def diplayPemesanan():
	print("\t============================================")
	print("\t|                                          |")
	print("\t|            PEMESANAN KOS PUTRA           |")
	print("\t|            HARIAN ATAU BULANAN           |")
	print("\t|                                          |")
	print("\t============================================")
	print()
	print("SELAMAT DATANG, SILAHKAN MEMESANAN KAMAR KOS JIKA ANDA BERKENAN.")
	print()
	input("\tTekan >>>ENTER<<< Untuk Melakukan Pemesanan")

	clearSystem()
	print("\t============================================")
	print("\t|                                          |")
	print("\t|            PEMESANAN KOS PUTRA           |")
	print("\t|            HARIAN ATAU BULANAN           |")
	print("\t|                                          |")
	print("\t============================================")

	namaPemesan = input("Masukkan Nama Lengkap : ")
	print()
	genderOption = input("Jenis Kelamin : ")
	print()
	usiaPemesan = input("Masukkan Usia : ")
	print()
	alamatPemesan = input("Masukkan Alamat : ")
	print()
	def percabangan():
		global optionKamar
		optionKamar = int(input("Pilih Jenis Kamar : "))
		return kamar1() if optionKamar == 1 else kamar2() if optionKamar == 2 else kamar3() if optionKamar == 3 else kamar4() if optionKamar == 4 else print("Maaf nomor yang anda inputkan tidak diketahui")
	def kamar1():
		global lamaHari, pesanHari
		jenisKamar = "Kamar Kos + KM Luar"
		hargaKamar = 30000
		h1 = lambda x : x * hargaKamar
		print("Kamar yang dipilih adalah", jenisKamar)
		lamaHari = int(input("Lama Pemesanan (Berapa hari/bulan) : "))
		pesanHari = h1(lamaHari)
	def kamar2():
		global lamaHari, pesanHari
		jenisKamar = "Kamar Kos + KM Dalam"
		hargaKamar = 60000
		h2 = lambda x : x * hargaKamar
		print("Kamar yang dipilih adalah", jenisKamar)
		lamaHari = int(input("Lama Pemesanan (Berapa hari/bulan) : "))
		pesanHari = h2(lamaHari)
	def kamar3():
		global lamaHari, pesanHari
		jenisKamar = "Kamar Kos + KM Dalam + AC"
		hargaKamar = 120000
		h3 = lambda x : x * hargaKamar
		print("Kamar yang dipilih adalah", jenisKamar)
		lamaHari = int(input("Lama Pemesanan (Berapa hari/bulan) : "))
		pesanHari = h3(lamaHari)
	def kamar4():
		global lamaHari, pesanHari
		jenisKamar = "Kamar Kos + KM Dalam + AC + Dapur"
		hargaKamar = 250000
		h4 = lambda x : x * hargaKamar
		print("Kamar yang dipilih adalah", jenisKamar)
		lamaHari = int(input("Lama Pemesanan (Berapa hari/bulan) : "))
		pesanHari = h4(lamaHari)

	print("================= PILIH JENIS KAMAR KOS =================")
	print("1. Kamar Kos + KM Luar                = Rp.30.000  / hari")
	print("2. Kamar Kos + KM Dalam               = Rp.60.000  / hari")
	print("3. Kamar Kos + KM Dalam + AC          = Rp.120.000 / hari")
	print("4. Kamar Kos + KM Dalam + AC + Dapur  = Rp.250.000 / hari")
	print("=========================================================")
	percabangan()
	print()

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
		""".format( namaPemesan, genderOption, usiaPemesan, alamatPemesan, optionKamar, lamaHari, pesanHari)
	print(total)
 
def statusTanya():
	status = input("Apakah ingin memesan lagi [y atau t]? : ")
	return diplayPemesanan() if status == "y" or "Y" else print("Terima kasih telah menggunakan layanan kami.")
    
diplayPemesanan()
statusTanya()
