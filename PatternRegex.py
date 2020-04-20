# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

import re

# Fungsi / Prosedur
# Mengembalikan string dari pembacaan pada sebuah fileName
def ReadText(fileName):
    f = open("test/"+fileName, "r")
    text = f.read()
    f.close()
    return text

# Mencari pattern dalam text dengan metode regex
def RegexPatternMatching(text, pattern):
    found = re.search(pattern, text)
    return found

# Kamus Data
pattern = []        # menyimpan nilai dari pattern
text = []           # menyimpan string dari sebuah text yang dibaca

# Algoritma Utama
pattern = input("Masukkan pattern yang diinginkan: ")
fileName = input("Masukkan nama file yang ingin dibaca: ")
text = ReadText(fileName)
print(text)

# Pattern Matching
if (RegexPatternMatching(text, pattern)):
    print(pattern,"ditemukan")
else:
    print(pattern,"tidak ditemukan")
