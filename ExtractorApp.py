# Modul ExtractorApp : Method Utama dalam Menjalankan Ekstraksi

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
from ExtractorData import *

# Melakukan highlight terhadap matched word dengan tampilan bold
def BoldMatches(sentence, matches):
    return sentence.replace(matches, "<b>"+matches+"</b>")

# Memulai Proses Ekstraksi Data dari beberapa Input Files
def BeginExtraction(keyword, method, files):
    listOfResult = []         # menyimpan daftar teks dari seluruh teks yang dipilih
    # Struktur listOfResult: (namafile, teks, extractedSentence)
    # Struktur extractedSentence : (sentencePattern, jumlah, tanggal)

    # Algoritma Utama
    for i in range(len(files)):
        extractedSentence = []  # menyimpan daftar kalimat yang sudah terekstraksi
        text = []               # menyimpan string dari sebuah text yang dibaca
        sentence = []           # menyimpan daftar kalimat yang telah diparsing  
        sentencePattern = []    # menyimpan daftar kalimat yang mempunyai pattern
        
        text = ReadText(files[i])
        text = text.lower()
        articleDate = ArticleDate(text)
        sentence = sent_tokenize(text)

        # Pattern Matching
        if (method == "Algoritma Boyers-Moore"):
            sentencePattern = GetPatternBMSentence(sentence, keyword)
        elif (method == "Algoritma Knuth-Morris-Pratt"):
            sentencePattern = GetPatternKMPSentence(sentence, keyword)
        elif (method == "Regular Expression"):
            sentencePattern = GetPatternRegex(sentence, keyword)

        # Jika tidak ditemukan kalimat yang mengandung keyword
        if (len(sentencePattern) == 0):
            print("Pencarian tidak ditemukan")
            listOfResult.append((files[i], text, sentencePattern, 0))

        # Jika ditemukan kalimat yang mengandung keyword
        else:
            # Extraction Data
            for j in range(len(sentencePattern)):
                jumlah = FindNumber(sentencePattern[j])
                tanggal = FindDate(sentencePattern[j])
                if not(jumlah == "Tidak diketahui"):
                    sentencePattern[j] = BoldMatches(sentencePattern[j],jumlah)
                if not(tanggal == "Tidak diketahui"):
                    sentencePattern[j] = BoldMatches(sentencePattern[j],jumlah)
                else:
                    tanggal = articleDate
                sentencePattern[j] = BoldMatches(sentencePattern[j], keyword)
                extractedSentence.append((sentencePattern[j].capitalize(), jumlah, tanggal.capitalize()))

            listOfResult.append((files[i], text, extractedSentence, len(sentencePattern)))
    return listOfResult
