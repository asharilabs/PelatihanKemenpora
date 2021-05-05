buah = ['mangga', 'apel', 'jeruk', 'duren']
for x in buah:
    print(x)

buah.append('delima')
print('-------')
# print(list(reversed(buah)))

# namasaya = 'Galih'
# print('nama saya adalah %s' %namasaya)

# angka = 11
# #print ('%d adalah angka keberuntungan %s' %(angka, namasaya))
# print(f'{angka} adalah angka keberuntungan {namasaya} --- new format')

text = 'pada hari minggu kuturut ayah ke kota'
print (text)
print ('banyak huruf a adalah %d' %text.count('a'))
print ('panjang text %d' %len(text))
print (text[0:6])
print (text[::-1])