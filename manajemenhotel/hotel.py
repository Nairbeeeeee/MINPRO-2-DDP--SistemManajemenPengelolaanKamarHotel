
import pwinput
from prettytable import PrettyTable


role = {
    "admin":{"password":"admin123","role":"admin"},
    "user":{"password":"user123","role":"user"}
}

data_kamar = {
    "101": {"tipe": "Biasa", "harga": 100000, "status": "kosong"},
    "102": {"tipe": "Bagus", "harga": 200000, "status": "dibooking"},
    "103": {"tipe": "VIP", "harga": 300000, "status": "terisi"},
    "104": {"tipe": "VIP", "harga": 300000, "status": "kosong"},
    
}

pesanan = {}

def login():
    print("=" * 35)
    print("SELAMAT DATANG DI HOTEL KAMI")
    print("=" * 35)

    percobaan = 0
    while percobaan < 3:
        username = input("Masukkan Username: ")
        password = pwinput.pwinput("Masukkan Password: ", mask="*")
        
        if username in role and role[username]["password"] == password:
            print("Login Berhasil")
            return role[username]["role"]
        else:
            percobaan += 1
            sisa = 3 - percobaan
            print(f"Username atau Password salah! (sisa percobaan: {sisa})")

    print("Gagal Login coba lagi")
    return None
        

def tampilkan_menu(role):
    print("=======MENU UTAMA=======")
    print("1. Lihat Data Kamar")
    if role == "admin":
        print("2. Tambah Data Kamar")
        print("3. Ubah Data Kamar")
        print("4. Hapus Data Kamar")

    elif role == "user":
        print("2. Booking Kamar")
        print("3. Lihat / Ubah Pesanan")
        print("4. Pembayaran")

    print("5. Keluar")
    print("=" * 20)
    print("=" *20)

def lihat_data(data_kamar):
    if not data_kamar:
        print("Belum ada data kamar")
        return

    tabel = PrettyTable()
    tabel.field_names = ["Nomor Kamar", "Tipe Kamar", "Harga Kamar (Rp)", "Status Kamar"]

    for nomor, detail in data_kamar.items():
        tabel.add_row([nomor, detail["tipe"], detail["harga"], detail["status"]])
        
    print("\n=========DATA KAMAR HOTEL=========")
    print(tabel)


def tambah_data(data_kamar):
    nomor  = input("nomor kamar:")
    if nomor == "":
        print("Nomor kamar tidak boleh kosong")
        return
    if nomor in data_kamar:
        print("Kamar sudah ada di data")
        return

    print("\nPilih tipe kamar:")
    print("1. Biasa")
    print("2. Bagus")
    print("3. VIP")
    pilihan_tipe = input("Masukkan pilihan tipe kamar (1-3):")

    if pilihan_tipe in ["1", "Biasa"]:
        tipe = "Biasa"
        harga = 100000
    elif pilihan_tipe in ["2", "Bagus"]:
        tipe = "Bagus"
        harga = 200000
    elif pilihan_tipe in ["3", "VIP"]:
        tipe = "VIP"
        harga = 300000
    else:
        print("Pilihan kamar tidak valid")
        return
    
    status = "kosong"
    
    data_kamar[nomor] = {
        "tipe" : tipe,
        "harga" : harga,
        "status" : status
    }
    print(f"Data kamar {nomor} ({tipe}) berhasil ditambahkan")


def ubah_data(data_kamar):
    print("\n=========UBAH DATA KAMAR=========")
    nomor_dicari = input("Masukkan nomor kamar yang mau diubah: ")

    if nomor_dicari not in data_kamar:
        print("Nomor tidak ditemukan")
        return

    print(f"\nKamar {nomor_dicari} saat ini -> Tipe: {data_kamar[nomor_dicari]['tipe']}, Harga: Rp{data_kamar[nomor_dicari]['harga']:,}, Status: {data_kamar[nomor_dicari]['status']}")
    print("\nPilih TIpe Kamar Baru: ")
    print("1. Biasa (Rp100.000): ")
    print("2. Bagus (Rp200.000): ")
    print("3. VIP (Rp300.000): ")
    print("\nPilih Tipe Kamar Baru: ")

    pilihan_tipe = input ("Pilih tipe baru (1/2/3): ")

    tipe_harga = {
        "1" : ("Biasa",100000),
        "2" : ("Bagus",200000),
        "3" : ("VIP",300000),
    }

    if pilihan_tipe not in tipe_harga:
        print("Tipe kamar tidak valid!")
        return

    tipe_baru, harga_baru = tipe_harga[pilihan_tipe]

    print("\nPilih status kamar baru: ")
    print("1. Kosong")
    print("2. Terisi")
    print("3. Dibooking")
    pilihan_status = input("Pilih status (1/2/3) atau tekan enter untuk tidak mengubah: ")

    tipe_status = {
        "1" : "Kosong",
        "2" : "Terisi",
        "3" : "Dibooking"
    }

    data_kamar[nomor_dicari]["tipe"] = tipe_baru
    data_kamar[nomor_dicari]["harga"] = harga_baru

    if pilihan_status in tipe_status:
        data_kamar[nomor_dicari]["status"] = tipe_status[pilihan_status]

    print(f"Data Kamar {nomor_dicari} berhasil diperbarui")
    print(f"Tipe Baru : {tipe_baru}")
    print(f"Harga Baru : Rp{harga_baru}")
    print(f"Status : {data_kamar[nomor_dicari]['status']}")

def hapus_data(data_kamar):
    print("\n=========HAPUS DATA KAMAR=========")
    nomor_dicari = input("Masukkan nomor kamar yang mau dihapus:")

    if nomor_dicari in data_kamar:
        del data_kamar[nomor_dicari]
        print(f"Kamar {nomor_dicari} berhasil dihapus")
    else:
            print("Data kamar tidak ditemukan")


def booking_kamar(data_kamar, pesanan):
    print("\n=========BOOKING KAMAR=========")
    lihat_data(data_kamar)

    nomor = input("\nMasukkan nomor kamar yang ingin dibooking: ")

    if nomor not in data_kamar:
        print("Nomor kamar tidak ditemukan")
        return

    if data_kamar[nomor]["status"].lower() != "kosong":
        print(f"Kamar {nomor} tidak dapat dipesan karena berstatus '{data_kamar[nomor]['status']}'")
        return

    if data_kamar[nomor]["status"].lower() == "kosong":
        print(f"Kamar {nomor} berhasil dibooking")
        data_kamar[nomor]["status"] = "dibooking"

    durasi = input("Masukkan durasi menginap (dalam hari): ")
    if not durasi.isdigit() or int(durasi) <= 0:
        print("Durasi menginap harus berupa angka")
        return

    durasi = int(durasi)
    total_harga = data_kamar[nomor]["harga"] * durasi
    print(f"Total harga untuk kamar {nomor} selama {durasi} hari adalah: Rp.{total_harga}")

    pesanan["nomor"] = nomor
    pesanan["durasi"] = durasi
    pesanan["total_harga"] = total_harga

    data_kamar[nomor]["status"] = "dibooking"

    print("=========DETAIL PESANAN=========")
    print(f"Anda berhasil melakukan booking kamar {nomor} selama {durasi} hari")
    print(f"Total harga yang harus dibayar: Rp.{total_harga}")


def detail_pesanan(pesanan, data_kamar):
    print("\nRincian Pesanan Anda")
    if not pesanan:
        print("Anda belum memiliki pesanan")
        return False

    nomor = pesanan["nomor"]
    tipe = data_kamar[nomor]["tipe"]
    durasi = pesanan["durasi"]
    total_harga = pesanan["total_harga"]

    print(f"Nomor kamar : {nomor}")
    print(f"Tipe kamar : {tipe}")
    print(f"Durasi Menginap : {durasi}")
    print(f"Total Harga : Rp.{total_harga}")
    return True


def ubah_pesanan(data_kamar, pesanan):
    print("\nUbah Pesanan")
    if not detail_pesanan(pesanan, data_kamar):
        return

    print("\nPilihan Ubah Pesanan:")
    print("1. Ubah Durasi Hari")
    print("2. Pilih Kamar Lain")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        durasi = input("Masukkan durasi menginap yang baru (Hari): ")
        if not durasi.isdigit() or int(durasi) <= 0:
            print("Durasi menginap harus berupa angka!")
            return

        durasi_baru = int(durasi)
        nomor = pesanan["nomor"]

        pesanan["durasi"] = durasi_baru
        pesanan["total_harga"] = data_kamar[nomor]["harga"] * durasi_baru
        print(f"Pesanan Berhasil diperbarui! Total Biaya Pesanan Baru: Rp{pesanan['total_harga']}")
        return


    elif pilihan == "2":
        nomor_lama = pesanan["nomor"]
        data_kamar[nomor_lama]["status"] = "kosong"
        pesanan.clear()

        print("Pesanan sebelumnya dibatalkan. Silahkan pilih kamar baru.")
        booking_kamar(data_kamar, pesanan)
    else:
        print("Pilihan anda tidak valid!")

def bayar_pesanan(data_kamar, pesanan):
    print("\n ==========Pembayaran=========")
    if not detail_pesanan(pesanan, data_kamar):
        return
    
    total_harga = pesanan["total_harga"]
    nomor = pesanan["nomor"]

    bayar_input = input(f"\nTotal yang harus dibayar Rp{total_harga:,}\nMasukkan nominal uang:")
    if not bayar_input.isdigit():
        print("Pembayaran harus berupa angka!")
        return

    nominal_bayar = int(bayar_input)
    if nominal_bayar < total_harga:
        print(f"Uang Anda kurang Rp{total_harga - nominal_bayar:,}. Pembayaran gagal.")
        return

    kembalian = nominal_bayar - total_harga

    data_kamar[nomor]["status"] = "terisi"

    print("\n" + "=" * 35)
    print("=====STRUK PEMBAYARAN======")
    print("=" * 35)
    print(f"Kamar : {nomor}")
    print(f"Total Biaya : {total_harga: }")
    print(f"Uang Dibayar : {nominal_bayar: }")
    print(f"Kembalian : {kembalian: }")
    print("=" * 35)
    print("Transaksi Selesai! Selamat menikmati penginapan dan layanan kami. Terima Kasih")
    
    pesanan.clear()
    


def main():
    role = login()

    if role is None:
        return
    
    while True:
        tampilkan_menu(role)
        pilihan = input("Masukkan pilihan menu (1-5):")

        if pilihan == "1":
            lihat_data(data_kamar)
        elif pilihan == "2":
            if role == "admin":
                tambah_data(data_kamar)
            elif role == "user":
                booking_kamar(data_kamar, pesanan)
        elif pilihan == "3":
            if role == "admin":
                lihat_data(data_kamar)
                ubah_data(data_kamar)
            elif role == "user":
                ubah_pesanan(data_kamar, pesanan)
        elif pilihan == "4":
            if role == "admin":
                hapus_data(data_kamar)
                lihat_data(data_kamar)
            elif role == "user":
                bayar_pesanan(data_kamar, pesanan)
        elif pilihan == "5":
            print("\nTerima Kasih telah menggunakan layanan kami")        
            break
        else:
            print("Pilihan menu tidak valid!")
main()