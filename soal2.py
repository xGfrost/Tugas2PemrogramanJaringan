def hitung_total_pembelian(daftar_barang):
    total = 0
    print("Nama\t\tJumlah\tHarga")
    for barang in daftar_barang:
        nama, jumlah, harga = barang
        sub_total = jumlah * harga
        total += sub_total
        print(f"{nama}\t\t{jumlah}\t{sub_total}")
    return total

# Contoh input barang
daftar_barang = [
    ("Pasta gigi", 3, 4000),
    ("Gula", 2, 7500),
    ("Garam", 1, 2000)
]

total_pembelian = hitung_total_pembelian(daftar_barang)
print(f"Total pembelian: {total_pembelian}")
