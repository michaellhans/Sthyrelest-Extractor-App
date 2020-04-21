# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

from PatternBM import *
from PatternKMP import *
from PatternRegex import *
from ExtractorData import *

def BeginExtraction(keyword, method, files):
    pattern = []            # menyimpan nilai dari pattern
    listOfResult = []         # menyimpan daftar teks dari seluruh teks yang dipilih
    
    sentencePattern = []    # menyimpan daftar kalimat yang mempunyai pattern

    # Algoritma Utama
    for i in len(files):
        text = []               # menyimpan string dari sebuah text yang dibaca
        sentence = []           # menyimpan daftar kalimat yang telah diparsing  
        text = ReadText(files[i])
        text = text.lower()
        sentence = sent_tokenize(text)
        # Pattern Matching
        if (choice == 1):
            sentencePattern = GetPatternBMSentence(sentence, pattern)
        elif (choice == 2):
            sentencePattern = GetPatternKMPSentence(sentence, pattern)
        elif (choice == 3):
            sentencePattern = GetPatternRegex(sentence, pattern)

        if len(sentencePattern) == 0:
            print("Pencarian tidak ditemukan")
        else:
            # Extraction Data
            for i in range(len(sentencePattern)):
                print(str(i+1)+". ",sentencePattern[i].capitalize())
                jumlah = FindNumber(sentencePattern[i])
                tanggal = FindDate(sentencePattern[i])
                print("Jumlah   : ", jumlah.capitalize())
                print("Tanggal  : ", tanggal.capitalize())
                print()