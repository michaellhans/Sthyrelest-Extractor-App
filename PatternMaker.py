number = "\d*"
bulanPanjang = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]
bulanSingkat = ["jan", "feb", "mar", "apr", "mei", "jun", "jul", "ags", "sept", "okt", "nov", "des"]
monthLong = ["january", "february", "maret", "april", "may", "june", "july", "augustus", "september", "october", "november","december"]
countAble = ["kasus", "orang", "manusia"]

def Literal(pattern):
    result = '[' + pattern + ']'
    return result

def PatternMaker():
    global countAble
    for pattern in countAble:
        pattern = number + ' ' + pattern
        print(pattern)
    return countAble

print(countAble)
print(PatternMaker())