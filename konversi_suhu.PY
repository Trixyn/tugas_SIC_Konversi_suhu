from utils import konversi_suhu

print("KONVERSI SUHU")

# minta input dari user
nilai_input = input("masukkan nilai suhu: ")

# cek apakah input nilai adalah angka
if not nilai_input.replace('.', '').replace('-', '').isdigit():
    print("Error: Nilai suhu harus berupa angka")
else:
    nilai_input = float(nilai_input)
    
    dari_satuan = input("Dari satuan (C/F/K): ")
    ke_satuan = input("Ke satuan (C/F/K): ")
    
    # Panggil fungsi konversi
    hasil, pesan_error = konversi_suhu(nilai_input, dari_satuan, ke_satuan)
    
    # Tampilkan hasil
    if pesan_error:
        print("Error:", pesan_error)
    else:
        # Tampilkan hasil konversi
        print("Hasil:", nilai_input, dari_satuan.upper(), "=", format(hasil, ".2f"), ke_satuan.upper())