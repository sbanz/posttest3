user = {
    "id" : "",
    "pass" : "",
}
login = {
    "id" : "",
    "pass" : "",
}
user_tetap = {
    "id" : "admin",
    "pass" : "123456",
}
def menu():
    print("""Pilih Menu :
    1. Buat Akun
    2. Login
    3. Keluar
    """)

menu_awal = True
while menu_awal:
    menu()
    pilih = input("Pilihan : ")
    print(40*"=")
    if pilih == "1":
        print("Masukkan ID dan password pengguna baru !!!")
        user["id"] = input("Masukkan ID pengguna : ")
        user["pass"] = input("Masukkan password : ")
        print("JANGAN LUPAKAN ID DAN PASSWORD !!!")
        menu_awal = input("Kembali ke menu awal? (y/n) = ") == 'y'
        print(40 * "=")
    elif pilih == "2":
        ulang = False
        coba = 1
        while ulang == False and coba <= 3:
            print("Masukkan ID dan password pengguna yang telah dibuat !!!")
            login["id"] = input("Masukkan ID pengguna : ")
            login["pass"] = input("Masukkan password : ")
            print(40 * "=")
            print()
            if login["id"] == user["id"] and login["pass"] == user["pass"]:
                print("Selamat datang, ", user["id"], " !!!")
                break
            elif login["id"] == user_tetap["id"] and login["pass"] == user_tetap["pass"]:
                print("Selamat datang, ", user_tetap["id"], " !!!")
                break
            else:
                print("ID atau password SALAH !!!")
                print(40 * "=")
                coba += 1
        if coba >= 3:
            print("Anda Telah menghabiskan semua kesempatan Login\nSilahkan Kembali ke menu awal.")
            break
        break
    else:
        break

print()
print("Terima Kasih !!!")