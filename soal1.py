arrBerat = []
bMin = float()
bMax = float()

def hitungMinMax(arrBerat):
    print('Berat balita minimum : ', min(arrBerat),'Kg')
    print('Berat balita maksimum : ', max(arrBerat),'Kg')
    # Definisikan Proses Mencari Berat Maximum Dan Minimum


def rerata(arrBerat):
    total = sum(arrBerat)
    return total/len(arrBerat)

    # Definisikan Proses Mencari Rerata Dari Total Berat

    # Return Hasil Rerata


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    k=float(input())
    arrBerat.append(k)
    # Inisialisasi Input Data Berat

    # Masukkan Data Berat Ke Array (arrBerat)

hitungMinMax(arrBerat)
print('Rerata berat balita : ', rerata(arrBerat),'Kg')
# Panggil procedur hitungMinMax(arrBerat)


# Print Data Minimum, Maximum, dan Rerata Berat
