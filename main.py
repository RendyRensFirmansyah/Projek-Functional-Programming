import os

rupiah_to_dollar = lambda x : x / float(15000)
rupiah_to_euro = lambda x : x / float(16500)
rupiah_to_riyal = lambda x : x / float(4000)
rupiah_to_ringgit = lambda x : x / float(3500)
rupiah_to_poundsterling = lambda x : x / float(18942)
rupiah_to_yen = lambda x : x / 0.0088
rupiah_to_yuan = lambda x : x / 0.00045

def menuConvert():
    print("========================================")
    print("           KONVERSI MATA UANG           ")
    print("========================================")
    print("| 1. Rupiah(IND) ke Dollar             |")
    print("| 2. Rupiah(IND) ke Euro               |")
    print("| 3. Rupiah(IND) ke Riyal(Arab)        |")
    print("| 4. Rupiah(IND) ke Ringgit            |")
    print("| 5. Rupiah(IND) ke Poundsterling      |")
    print("| 6. Rupiah(IND) ke Yen                |")
    print("| 7. Rupiah(IND) ke Yuan               |")
    print("========================================")

def conversiDollar():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_dollar(inputConvert), "Dollar")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()

def conversiEuro():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_euro(inputConvert), "Euro")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()
    
def conversiRiyal():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_riyal(inputConvert), "Riyal")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()
    
def conversiRinggit():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_ringgit(inputConvert), "Ringgit")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()

def conversiPoundsterling():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_poundsterling(inputConvert), "Poundsterling")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()

def conversiYen():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_yen(inputConvert), "Yen")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()
    
def conversiYuan():
    inputConvert = int(input("Masukkan nominal mata uang anda :"))
    print(rupiah_to_yuan(inputConvert), "Yuan")
    print("Tekan ENTER untuk kembali ke menu")
    input()
    os.system("cls")
    main_display()

def percabangan(): 
    inputProgram = int(input("Pilih konversi mata uang yang anda inginkan : "))
    return conversiDollar() if inputProgram == 1 else conversiEuro() if inputProgram == 2 else conversiRiyal() if inputProgram == 3 else conversiRinggit() if inputProgram == 4 else print("Menu tidak merespon")

def main_display():
    menuConvert()
    percabangan()
    
main_display()