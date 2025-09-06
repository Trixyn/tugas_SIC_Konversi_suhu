def konversi_suhu(nilai, dari, ke):
    """
    Fungsi untuk mengkonversi suhu dari satu satuan ke satuan lainnya.
    
    Parameter:
    nilai (float): nilai suhu yang akan dikonversi
    dari (str): satuan asal ("c", "f", "k")
    ke (str): satuan tujuan ("c", "f", "k")
    
    Return:
    float: hasil konversi suhu atau None jika input tidak valid
    str: pesan error jika input tidak valid
    """
    
    # Validasi input satuan
    satuan_valid = ['c', 'f', 'k']
    dari = dari.lower()
    ke = ke.lower()
    
    if dari not in satuan_valid or ke not in satuan_valid:
        return None, "Error: Satuan harus 'c', 'f', atau 'k' (tidak case sensitive)"
    
    # Validasi nilai suhu
    if dari == 'k' and nilai < 0:
        return None, "Error: Kelvin tidak boleh negatif"
    
    # Konversi ke Celsius sebagai perantara
    if dari == 'c':
        celsius = nilai
    elif dari == 'f':
        celsius = (nilai - 32) * 5/9
    elif dari == 'k':
        celsius = nilai - 273.15
    
    # Konversi dari Celsius ke satuan tujuan
    if ke == 'c':
        hasil = celsius
    elif ke == 'f':
        hasil = (celsius * 9/5) + 32
    elif ke == 'k':
        hasil = celsius + 273.15
        # Validasi kembali untuk Kelvin setelah konversi
        if hasil < 0:
            return None, "Error: Hasil konversi ke Kelvin tidak boleh negatif"
    
    return hasil, None