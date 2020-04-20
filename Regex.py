# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

import re

# Kamus Regular Expression
# number = "\d*"
number = r"(\d{4}) Orang"
numberWords = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh", "puluh"]
bulanPanjang = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]
bulanSingkat = ["jan", "feb", "mar", "apr", "mei", "jun", "jul", "ags", "sept", "okt", "nov", "des"]
monthLong = ["january", "february", "maret", "april", "may", "june", "july", "augustus", "september", "october", "november","december"]
countAble = ["kasus", "orang", "manusia", "korban", "jiwa"]

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

#
def FindNumber(sentence):
    angka = re.findall(number, sentence)
    return angka[0]

def FindDate(sentence):
    date = re.findall(date, sentence)
    return date[0]

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
    jumlah = FindNumber(text)
    # tanggal = findDate(date)
    print("Jumlah: ", jumlah)
    # print("Tanggal: ", tanggal)
else:
    print(pattern,"tidak ditemukan")

