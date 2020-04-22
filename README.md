# Sthyrelest Data Extractor (Covid-19 Data Extractor)

Sthyrelest Data Extractor (Covid-19 Data Extractor) merupakan aplikasi berbasis web yang berfungsi untuk melakukan ekstraksi data terhadap suatu pembacaan artikel dari suatu file. Secara umum, aplikasi ini akan menerima masukan dari pengguna berupa keyword yang ingin dicari dalam artikel yang ingin diekstrak. Hasil ekstraksi informasi berupa data bertipe jumlah dan tanggal kejadian dari keyword yang dimasukkan.

## Getting Started

Instruksi-instruksi berikut ini akan membimbing Anda dalam tahap instalasi aplikasi dan cara menjalankannya.

### Prerequisites

Berikut ini adalah persiapan environment yang dibutuhkan untuk menjalankan aplikasi.

```
- Flask Framework for Integration
- HTML and CSS for Front End
- Natural Language Toolkit (NLTK)
- Regular Expression Library
- Python 3.x.x for Back End
```

### Installing

Berikut ini adalah langkah-langkah dalam penginstallan aplikasi:
1. Install library Flask terlebih dahulu menggunakan command sebagai berikut.
```
pip install Flask
```
2. Install library NLTK untuk sentence tokenizer menggunakan command sebagai berikut.
```
pip install nltk
```
3. Lakukan penginstalan data pada NLTK dengan menjalankan terminal python. Jalankan dengan command sebagai berikut.
```
python
```
4. Ketik dua buah command berikut, kemudian ikuti penginstallan yang telah diarahkan.
```
import nltk
nltk.download('popular')
```
5. Lakukan penginstalan Regular Expression dengan command sebagai berikut pada terminal biasa.
```
pip install regex
```
6. Semua prerequisites sudah disiapkan dengan baik.

## How to Run Program
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python Application.py
```
2. Tunggu kira-kira 5-15 detik. Localhost Flask akan dijalankan. Untuk menampilkan aplikasi web, buka browser kemudian masuk ke laman berikut ini.
```
localhost:5000
```
3. Bila muncul tampilan tanpa adanya error message, maka program berhasil dijalankan.

## Guideline: How To Use
1. Pilih file-file yang ingin diekstrak datanya.
2. Pastikan bahwa file-file tersebut bertipe text dan berada pada directory ./test
3. Anda bisa memilih satu atau lebih file yang ingin diextract
4. Untuk memilih file lebih dari satu, gunakan `Ctrl + Click` saat memilih file
5. Pilih salah satu dari tiga metode yang disediakan, yaitu:
- Algoritma Boyers-Moore
- Algoritma Knutt-Morris-Pratt
- Regular Expression
6. Tekan tombol Extract untuk memulai pengekstrakan
7. Untuk melakukan pengekstrakan kembali, tekan tombol Home untuk kembali ke Menu Awal

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Integrasi Backend dan FrontEnd
* HTML - Front End dari Aplikasi
* CSS - Front End dari Aplikasi
* [Python](https://www.python.org/) - Back End dari Aplikasi

## Testing

Untuk menjalankan testing pada program pengekstrak, dapat dijalankan program secara command line interface sebagai berikut.
1. Untuk menjalankan program, pastikan command sudah berada dalam directory `./src`, lalu jalankan command sebagai berikut.
```
python BackEndTest.py
```
2. Masukkan input-input yang bersesuaian sesuai dengan yang diminta oleh program.

## Authors

**13518056 - Michael Hans** - *Designer, Programmer, and Tester*

## Acknowledgments

* Dosen IF2211 K1, Masayu Leylia Khodra
* Dosen IF2211 K2, Nur Ulfa Maulidevi
* Dosen IF2211 K3, Rinaldi Munir
* IF2211 Strategi Algoritma Tahun Ajaran 2019-2020