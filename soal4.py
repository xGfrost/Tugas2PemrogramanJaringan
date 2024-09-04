import matplotlib.pyplot as plt

# Fungsi untuk mengonversi nilai angka menjadi huruf
def konversi_nilai(nilai):
    if nilai >= 88:
        return "A"
    elif nilai >= 77:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 45:
        return "D"
    else:
        return "E"

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_kuis, nilai_uts, nilai_uas):
    return (nilai_tugas * 0.2) + (nilai_kuis * 0.1) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

# Data mahasiswa (Nama, Nilai Tugas, Nilai Kuis, Nilai UTS, Nilai UAS)
data_mahasiswa = [
    ("Hadi", 70, 50, 60, 70),
    ("Fadel", 85, 80, 78, 85),
    ("Furqon", 90, 88, 87, 92),
    ("Aileen", 58, 60, 55, 63),
    ("Atma", 70, 65, 68, 72)
]

# Menghitung nilai akhir dan konversi ke huruf
hasil = []
jumlah_nilai_huruf = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

for mahasiswa in data_mahasiswa:
    nama, nilai_tugas, nilai_kuis, nilai_uts, nilai_uas = mahasiswa
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_kuis, nilai_uts, nilai_uas)
    nilai_huruf = konversi_nilai(nilai_akhir)
    hasil.append((nama, nilai_tugas, nilai_kuis, nilai_uts, nilai_uas, nilai_akhir, nilai_huruf))
    jumlah_nilai_huruf[nilai_huruf] += 1

# Menampilkan tabel
print("No.\tNama\t\tN.Tugas\tN.Kuis\tN.UTS\tN.UAS\tNilaiAkhir\tNilai Huruf")
for i, mahasiswa in enumerate(hasil):
    print(f"{i+1}\t{mahasiswa[0]}\t\t{mahasiswa[1]}\t{mahasiswa[2]}\t{mahasiswa[3]}\t{mahasiswa[4]}\t{mahasiswa[5]:.2f}\t\t{mahasiswa[6]}")

# Menampilkan jumlah nilai huruf
print(f"\nJumlah A: {jumlah_nilai_huruf['A']}")
print(f"Jumlah B: {jumlah_nilai_huruf['B']}")
print(f"Jumlah C: {jumlah_nilai_huruf['C']}")
print(f"Jumlah D: {jumlah_nilai_huruf['D']}")
print(f"Jumlah E: {jumlah_nilai_huruf['E']}")

# Plot grafik batang
plt.bar(jumlah_nilai_huruf.keys(), jumlah_nilai_huruf.values(), color=['blue', 'green', 'orange', 'red', 'purple'])
plt.title('Distribusi Nilai Huruf Mahasiswa')
plt.xlabel('Nilai Huruf')
plt.ylabel('Jumlah')
plt.show()
