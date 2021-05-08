# latihan di hari yang kedua
# buat suatu aplikasi sederhana di python
# jika saya memasukkan 1 --> 12 maka akan 
# menampilkan nama bulannya

# contoh: input index bulan = 12
# maka akan print = Desember

# definisi nama-nama bulan
namabulan = ['januari', 'februari', 'maret', 'april', 'mei', 'juni', 
            'juli','agustus', 'september', 'oktober', 'november', 'desember']
# input index
indexBul = int(input('masukkan index bulannya: '))

# olah data bulan input
# batasi input dari 1 sampe 12
if indexBul > 0 and indexBul < 13:
    print ('yaitu bulan %s' %namabulan[indexBul - 1])
else:
    print('dont know')