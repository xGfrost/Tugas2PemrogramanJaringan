def hitung_genap_ganjil(bilangan):
    genap = []
    ganjil = []
    for num in bilangan:
        if num % 2 == 0:
            genap.append(num)
        else:
            ganjil.append(num)
    return genap, ganjil

# Input jumlah bilangan
jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))

# Input bilangan
bilangan = []
for i in range(jumlah_bilangan):
    bil = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(bil)

genap, ganjil = hitung_genap_ganjil(bilangan)
print(f"Terdapat data: {bilangan}")
print(f"Jumlah bilangan genap: {len(genap)} yaitu {genap}")
print(f"Jumlah bilangan ganjil: {len(ganjil)} yaitu {ganjil}")
