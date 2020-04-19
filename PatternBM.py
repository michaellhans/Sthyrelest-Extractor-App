# IF2211 - Strategi Algoritma
# Tugas Kecil 4 - Ekstraksi Informasi dengan KMP
# Created by: 13518056 / Michael Hans

# Fungsi / Prosedur
# Mengembalikan string dari pembacaan pada sebuah fileName
def ReadText(fileName):
    f = open("test/"+fileName, "r")
    text = f.read()
    f.close()
    return text

# Mengembalikan posisi kemunculan terakhir character dalam pattern
def GetLastOccurance(pattern, character):
    position = -1
    n = len(pattern) - 1
    while ((n >= 0) and (position == -1)):
        if (pattern[n] == character):
            position = n
        else:
            n = n - 1
    return position

# Mengembalikan map berisi last occurance dari setiap karakter unik dari text dalam pattern
def BMLastOccurance(text, pattern):
    lastOccurance = {}
    uniqueText = list(set(text))
    for char in uniqueText:
        value = GetLastOccurance(pattern, char)
        lastOccurance.update({char : value})
    return lastOccurance

# Mencari banyaknya pattern dalam sebuah text
def BMPatternMatching(text, pattern, lastOccurance):
    count = 0
    lengthText = len(text)
    lengthPattern = len(pattern)
    i = lengthPattern - 1
    while (i < lengthText):
        j = lengthPattern - 1
        while ((j >= 0) and (i < lengthText)):
            if (text[i] == pattern[j]):
                i -= 1
                j -= 1
            else:
                lastPosition = lastOccurance.get(text[i])
                if (lastPosition < j):
                    i = i + (lengthPattern - 1) - lastPosition
                elif (lastPosition > j):
                    i = i + lengthPattern - j
                else:
                    i = i + 1
                j = lengthPattern - 1
        i += 1
        if (j < 0):
            count = count + 1
            i += 2*(lengthPattern - 1) + 1
    return count

# Kamus Data
pattern = []        # menyimpan nilai dari pattern
text = []           # menyimpan string dari sebuah text yang dibaca
lastOccurance = {}  # menyimpan kemunculan terakhir karakter unik dalam teks

# Algoritma Utama
pattern = input("Masukkan pattern yang diinginkan: ")
fileName = input("Masukkan nama file yang ingin dibaca: ")
text = ReadText(fileName)
lastOccurance = BMLastOccurance(text,pattern)
print(text)

# Pattern Matching
count = BMPatternMatching(text, pattern, lastOccurance)
print(pattern,"ditemukan sebanyak",count)