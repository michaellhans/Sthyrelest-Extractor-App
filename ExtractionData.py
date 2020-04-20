# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

# from nltk.tokenize import sent_tokenize, word_tokenize
# data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# print(sent_tokenize(data))

import re

# Kamus Regular Expression
numberFirstFormat = '(?:(?:\d{1,3}\.?)(?:\d*) Orang)'
numberEnum = '(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|puluh|ribu|juta)'
numberSecondFormat = "(?:(?:%s )+%s)" % (numberEnum, numberEnum)
genericNumber = re.compile("(?:%s|%s)" % (numberFirstFormat, numberSecondFormat))
# countAble = ["kasus", "orang", "manusia", "korban", "jiwa"]

# Construct Date First Format
datenum = '(?:\d{1,2})'
tahun = '(?:\d{4})'
bulan = '(?:januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)'
day = '(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)'
dateFirstFormat = "(?:%s, %s %s %s)" % (day, datenum, bulan, tahun)

# Construct Date Second Format
dateSecondFormat = "(?:\d{1,2}/\d{1,2}/\d{4})"

# Construct Date Third Format
dateThirdFormat = '(?:kemarin|besok|hari ini|lusa)'

genericDate = re.compile("(?:%s|%s|%s)" % (dateFirstFormat, dateThirdFormat, dateSecondFormat))
print(dateFirstFormat)

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

# Mengekstrak data angka dari sebuah kalimat
def FindNumber(sentence):
    angka = re.findall(genericNumber, sentence)
    return angka

# Mengekstrak data tanggal dari sebuah kalimat
def FindDate(sentence):
    tanggal = re.findall(genericDate, sentence)
    return tanggal

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
    jumlah = FindNumber(text)
    tanggal = FindDate(text)
    print("Jumlah: ", jumlah)
    print("Tanggal: ", tanggal)
else:
    print(pattern,"tidak ditemukan")
