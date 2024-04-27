while True:  
    print("\nMenu Pilihan:")
    print("1. Hitung Usia Saat Ini")
    print("2. Hitung Sisa Tahun Angsuran")
    print("3. Hitung Berat Badan BMI")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1' :   # == adalah ciri buat menyammbungkan variable diatass
        tahun_lahir = int(input("Masukan tahun lahir anda : ")) #rumusnya pertama
        tahun_sekarang = 2024
        usia = tahun_sekarang - tahun_lahir
        print(f"\nUsia anda adalah ",usia)
     
    elif pilihan == '2' :
        total_angsuran = int(input("Masukan Total Angsuran : "))
        angsuran_total =int (input("masukan jumlah angsuran per bulan : "))
        bulan_bayar = int(input("Masukan jumlah bulan yang sudah dibayar : "))
        sisa_angsuran = total_angsuran - (angsuran_total*bulan_bayar)   # RUMUS MENGHITUNG ANGSURAN#
        print("Sisa angsuran anda adalah ",sisa_angsuran)
        print("\nMANGKANYA JANGAN NGUTANG")
    elif pilihan == '3' :
        berat_badan = int(input(f"Masukan Berat Badan anda :"))
        tinggi_badan_cm =int(input(f"Masukab Tinggi Badan anda :"))
        tinggi_badan_m = tinggi_badan_cm / 100
                #MenghitungBMI normal/gak normal#v
        bmi= berat_badan / (tinggi_badan_m ** 2)
     
        print(f"berat badan bmi anda adalah",bmi)
    
        if bmi< 18.5:
            print(f"\nKategori BMI Anda Adalah : Kurang Berat Badaan")
        elif bmi >= 18.5 and bmi < 25:
            print(f"\nKategori BMI Anda Adalah : Normal (Sehat)")
        elif bmi >= 25 and bmi< 30:
            print(f"\nKategori BMI anda adalah : Kelebihan Berat Badan") 
        else:
            print("\n=========ANDA OBESITAS=======")
        
    elif pilihan == '4' :
        print(f"Terima Kasih telah Meggunakan Program Ini!!!!")
        break
    else:
        print("\npilihlah yang benar") 