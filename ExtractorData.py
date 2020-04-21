# Modul Extractor Data: Memanfaatkan Regular Expression

from nltk.tokenize import sent_tokenize, word_tokenize
import re

# Kamus Regular Expression
countAble= '(?:kasus|orang|manusia|korban|jiwa|pasien)'
numberFirstFormat = "(?:(?:\d{1,3}\.?)*(?:\d+) %s)" % (countAble)
numberEnum = '(?:satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|puluh|ribu|juta)'
numberSecondFormat = "(?:(?:%s )+%s %s)" % (numberEnum, numberEnum, countAble)
genericNumber = re.compile("(?:%s|%s)" % (numberFirstFormat, numberSecondFormat))

# Construct Format for Date
datenum = '(?:\d{1,2})'
tahun = '(?:\d{4})'
bulan = '(?:januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)'
bulanSingkat = '(?:jan|feb|mar|apr|mei|jun|jul|ags|sep|okt|nov|des)'
day = '(?:senin|selasa|rabu|kamis|jumat|sabtu|minggu)'
dateFirstFormat = "(?:%s, %s (?:%s|%s) %s)" % (day, datenum, bulan, bulanSingkat, tahun)
dateSecondFormat = "(?:\d{1,2}/\d{1,2}/\d{4})"
dateThirdFormat = '(?:kemarin|besok|hari ini|lusa)'
dateOtherFormat = "(?:%s|%s|%s|%s|%s)" % (day, datenum, bulan, bulanSingkat, tahun)

# Construct Format for Time
timeFirstFormat = '(?:\d{2}:\d{2} wib)'
timeSecondFormat = '(?:pukul \d{2}\.\d{2} wib)'
timeThirdFormat = '(?:pagi|siang|sore|malam)'

# Combination of Date and Time
dateTimeFull = "(?:%s,? (?:%s|%s))" % (dateFirstFormat, timeFirstFormat, timeSecondFormat)

# Combine all things into one regular expression
genericDate = "(?:%s|%s|%s)" % (dateFirstFormat, dateSecondFormat, dateThirdFormat)
genericTime = "(?:%s|%s|%s)" % (timeFirstFormat, timeSecondFormat, timeThirdFormat)
genericDateTime = re.compile("(?:%s|%s|%s)" % (dateTimeFull,genericDate, genericTime))

# Fungsi / Prosedur
# Mengembalikan string dari pembacaan pada sebuah fileName
def ReadText(fileName):
    f = open("test/"+fileName, "r")
    text = f.read()
    f.close()
    return text

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
      
# Mengekstrak data artikel dari sebuah teks
def ArticleDate(text):
    tanggal = re.findall(genericDateTime, text)
    if (len(tanggal) == 0):
        return "Tidak diketahui"
    else:
        return max(tanggal , key = len)