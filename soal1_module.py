from soal1_funnction import seleksi_kriteria

nilai = int(input("Masukkan nilai: "))
kriteria, kategori = seleksi_kriteria(nilai)
print(f"Kriteria nilai: {kriteria}, Kategori: {kategori}")