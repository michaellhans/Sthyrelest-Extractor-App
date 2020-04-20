# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

from nltk.tokenize import sent_tokenize, word_tokenize
import re

# Kamus Regular Expression
countAble= '(?:kasus|orang|manusia|korban|jiwa|pasien)'
numberFirstFormat = "(?:(?:\d{1,3}\.?)*(?:\d+) %s)" % (countAble)
# print(numberFirstFormat)
numberEnum = '(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|puluh|ribu|juta)'
numberSecondFormat = "(?:(?:%s )+%s %s)" % (numberEnum, numberEnum, countAble)
# print(numberSecondFormat)
genericNumber = re.compile("(?:%s|%s)" % (numberFirstFormat, numberSecondFormat))

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

# Construct Format for Time
timeFirstFormat = '(?:\d{2}:\d{2} wib)'
timeSecondFormat = '(?:pukul \d{2}\.\d{2} wib)'
timeThirdFormat = '(?:pagi|siang|sore|malam)'

# Combination of Date and Time
dateTimeFull = "(?:%s,? (?:%s|%s))" % (dateFirstFormat, timeFirstFormat, timeSecondFormat)

genericDate = "(?:%s|%s|%s)" % (dateFirstFormat, dateSecondFormat, dateThirdFormat)
genericTime = "(?:%s|%s|%s)" % (timeFirstFormat, timeSecondFormat, timeThirdFormat)
genericDateTime = re.compile("(?:%s|%s|%s)" % (dateTimeFull,genericDate, genericTime))
# print(dateFirstFormat)

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
    if (len(angka) == 0):
        return "Tidak diketahui"
    else:
        return angka[0]

# Mengekstrak data tanggal dari sebuah kalimat
def FindDate(sentence):
    tanggal = re.findall(genericDateTime, sentence)
    if (len(tanggal) == 0):
        return "Tidak diketahui"
    else:
        return tanggal[0]

# Kamus Data
pattern = []            # menyimpan nilai dari pattern
text = []               # menyimpan string dari sebuah text yang dibaca
sentence = []           # menyimpan daftar kalimat yang telah diparsing
sentencePattern = []    # menyimpan daftar kalimat yang mempunyai pattern

# Algoritma Utama
print("IF2211 - Strategi Algoritma")
print("Tugas Kecil 4 - Ekstraksi Informasi")
print("Sthyrelest - Data Extractor Application")
print("Created by: 13518056 / Michael Hans")
print()
pattern = input("Masukkan pattern yang diinginkan: ")
fileName = input("Masukkan nama file yang ingin dibaca: ")
print()
text = ReadText(fileName)
text = text.lower()
sentence = sent_tokenize(text)

# Pattern Matching
for i in range(len(sentence)):
    if (RegexPatternMatching(sentence[i], pattern)):
        sentencePattern.append(sentence[i])

for i in range(len(sentencePattern)):
    print(str(i+1)+". ",sentencePattern[i].capitalize())
    jumlah = FindNumber(sentencePattern[i])
    tanggal = FindDate(sentencePattern[i])
    print("Jumlah   : ", jumlah.capitalize())
    print("Tanggal  : ", tanggal.capitalize())
    print()
    # if (RegexPatternMatching(sentence[i], pattern)):
    #     print(pattern,"ditemukan")
    #     jumlah = FindNumber(sentence[i])
    #     tanggal = FindDate(sentence[i])
    #     print("Jumlah: ", jumlah)
    #     print("Tanggal: ", tanggal)
    # else:
    #     print(pattern,"tidak ditemukan")
    # print()
