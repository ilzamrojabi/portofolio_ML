# Program Manajemen Daftar Belanja

# Dictionary
daftar_belanja = {
    "Buah": [],
    "Sayuran": [],
    "Daging": [],
    "Lainnya": []
}

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Aplikasi Daftar Belanja ===")
    print("1. Tambah Item Belanja")
    print("2. Lihat Daftar Belanja")
    print("3. Hapus Item Belanja")
    print("4. Hitung Total Item")
    print("5. Keluar")

# Fungsi untuk menambahkan item ke daftar belanja
def tambah_item():
    print("\nKategori yang tersedia:")
    for kategori in daftar_belanja.keys():
        print(f"- {kategori}")

    kategori = input("\nMasukkan kategori: ").capitalize()

    if kategori not in daftar_belanja:
        print("Kategori tidak valid! Item akan dimasukkan ke 'Lainnya'")
        kategori = "Lainnya"

    item = input("Masukkan nama item: ").capitalize()
    jumlah = int(input("Masukkan jumlah: "))

    daftar_belanja[kategori].append({"nama": item, "jumlah": jumlah})
    print(f"'{item}' telah ditambahkan ke kategori '{kategori}'!")

# Fungsi untuk menampilkan daftar belanja
def lihat_daftar():
    print("\n=== DAFTAR BELANJA ANDA ===")
    for kategori, items in daftar_belanja.items():
        if items: #Hanya tampilkan kategori yang memiliki item
            print(f"\n{kategori}:")
            for idx, item in enumerate(items, 1):
                print(f"{idx}. {item['nama']} - {item['jumlah']} buah")

# Fungsi untuk menghapus item
def hapus_item():
    lihat_daftar()
    kategori = input("/nMasukkan kategori item yang akan dihapus: ").capitalize()

    if kategori not in daftar_belanja or not daftar_belanja[kategori]:
        print("Kategori tidak valid atau kosong!")
        return

    try:
        nomor = int(input("Masukkan nomor item yang akan dihapus: ")) -1
        if 0 <= nomor < len(daftar_belanja[kategori]):
            item_dihapus = daftar_belanja[kategori].pop(nomor)
            print(f"'{item_dihapus['nama']}' telah dihapus dari daftar belanja!")
        else:
            print("Nomor item tidak valid!")
    except ValueError:
        print("Masukkan nomor yang valid!")

# Fungsi untuk menghitung total item
def hitung_total():
    total = 0
    for items in daftar_belanja.values():
        for item in items:
            total += item['jumlah']
    print(f"\nTotal item dalam daftar belanja: {total} buah")

#program utama
def main():
    print("Selamat datang di aplikasi daftar Belanja")

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tambah_item()
        elif pilihan == "2":
            lihat_daftar()
        elif pilihan == "3":
            hapus_item()
        elif pilihan == "4":
            hitung_total()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi")

# Jalankan program utama
if __name__ == "__main__":
    main()