
nomor = int(input('Masukkan Nomor Permulaan : '))

nomorinput = int(input('Masukkan Nomor Akhir Loop : '))

while nomor < nomorinput:
    nomor += 1
    print(f'Angka Sekarang = {nomor}')

    if nomor == nomorinput:
        print('========================================')
        print('Angka Yang Dispesifikasi sudah tercapai, Looping telah Selesai.')
        break

    print('--------------------')

print('Prosedur Berhasil Dijalankan')
print('Hello, my name is not your name')