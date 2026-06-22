def konversi_nilai(nilai):
    if nilai == "A":
        return 4
    elif nilai == "B":
        return 3
    elif nilai == "C":
        return 2
    elif nilai == "D":
        return 1
    elif nilai == "DE":
        return 1
    else:
        raise ValueError('Nilai harus A, B, C, D, E')

def hitung_ipk():
    total_nilai = 0
    total_sks = 0
    jumlah_mk = int(input('Jumlah mata kuliah : '))

    for a in range(jumlah_mk):
        print(f'\nMata Kuliah {a+1}')
        nama_mk = input('Nama Mata Kuliah: ')
        sks = int(input('SKS: '))
        nilai = input('NIlai Huruf: ').upper()
        total_nilai += konversi_nilai(nilai) *sks
        total_sks+= sks
    return total_nilai/total_sks
try:
    jumlah_mahasiswa = int(input('Masukkan Jumlah Mahasiswa: '))
    total_ipk = 0
    for a in range(jumlah_mahasiswa):
        print(f'\nMahasiswa ke-{a+1}')
        nama = input('Nama Mahasiswa')
        ipk = hitung_ipk()
        print(f'IPK {nama} = {ipk:.2f}')
        total_ipk += ipk
    rata_rata = total_ipk/jumlah_mahasiswa
    print(f'\nRata-rata IPK kelas: {rata_rata:.2f}')
except ValueError as r:
    print('Terjadi Kesalahan: ', r)  

