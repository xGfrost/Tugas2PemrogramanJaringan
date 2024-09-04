# Modul konversi nilai
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

nilai = int(input("Masukkan nilai: "))
huruf = konversi_nilai(nilai)
print(f"Nilai huruf: {huruf}")
