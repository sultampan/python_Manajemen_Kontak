#Program Manajemen Kontak

kontak1 = {'nama' : "Sultan Syarif", 'HP' : "081327880335", 'email' : "sultansyarif630@gmail.com"}
kontak2 = {'nama' : "Sltn Suka Smash", 'HP' : "082226559144", 'email' : "seleba615@gmail.com"}
kontak = [kontak1, kontak2]

while True:
    print ("\nMenu Kontak")
    print ("1. Melihat Semua Kontak")
    print ("2. Menambah Kontak Baru")
    print ("3. Menghapus Kontak")
    print ("4. Keluar dari kontak")

    pilihan = input ("Masukkan pilihan menu kontak (1,2,3, atau 4): ")

    if pilihan == "1":
        #melihat semua kontak
        if kontak :
            for num, item in enumerate(kontak, start=1):
                print (num, "|", item ["nama"], "|" , item ["HP"], "|", item ["email"])
        else:
            print ("Kontak masih kosong!")
    elif pilihan == "2":
        # menambahkan kontak baru
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan nomor HP yang baru: ")
        email = input("Masukkan email yang baru: ")
        kontak_baru = {"nama" : nama, "HP" : HP, "email" : email}
        kontak.append(kontak_baru)
        print ("Anda berhasil menambahkan kontak baru!")
    elif pilihan == "3":
        #Menghapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(num, "|", item["nama"], "|", item["HP"], "|", item["email"])
        else:
            print("Kontak masih kosong!")
            continue
        i_hapus = int(input("Masukkan nomor kontak yang ingin dihapus: "))
        del kontak[i_hapus -1]
        print("kontak sudah dihapus!")

    elif pilihan == "4":
        #keluar dari menu kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")