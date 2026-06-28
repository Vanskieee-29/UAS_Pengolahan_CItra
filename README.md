# Aplikasi Pengolahan Citra Digital

## Implementasi Pengolahan Citra Digital pada Dataset Wajah Selebriti Menggunakan Python dan OpenCV

---

## Deskripsi Proyek

Aplikasi Pengolahan Citra Digital merupakan aplikasi desktop berbasis **Python**, **OpenCV**, dan **Tkinter** yang dikembangkan untuk mengimplementasikan berbagai teknik dasar pengolahan citra digital pada dataset wajah selebriti.

Pengguna dapat mengunggah gambar wajah, kemudian memilih berbagai metode pengolahan citra melalui antarmuka grafis (GUI). Hasil pengolahan akan ditampilkan secara langsung dan dapat disimpan sebagai file gambar.

Proyek ini dibuat sebagai **Tugas Ujian Akhir Semester (UAS)** Mata Kuliah **Pengolahan Citra Digital**.

---

# Fitur Aplikasi

Aplikasi menyediakan beberapa metode pengolahan citra sebagai berikut.

## 1. Preprocessing

* Konversi RGB ke Grayscale
* Konversi Citra Biner (Binary)

## 2. Image Enhancement

* Histogram Equalization
* Contrast Stretching
* Brightness Adjustment

## 3. Image Filtering

* Mean Filter
* Median Filter
* Gaussian Filter

## 4. Edge Detection

* Sobel Edge Detection
* Canny Edge Detection

## 5. Image Segmentation

* Threshold Segmentation
* K-Means Segmentation

## 6. Face Detection

* Deteksi Wajah menggunakan Haar Cascade OpenCV

---

# Struktur Folder

```text
UAS_Pengolahan_Citra/
│
├── dataset/
│   └── celebrity_faces/
│
├── haarcascade/
│
├── output/
│
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── preprocessing.py
│   ├── enhancement.py
│   ├── filtering.py
│   ├── edge_detection.py
│   ├── segmentation.py
│   ├── face_detection.py
│   ├── style.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

# Teknologi yang Digunakan

* Python 3.12
* OpenCV
* NumPy
* Pillow (PIL)
* Tkinter
* Matplotlib

---

# Cara Instalasi

Pastikan Python telah terpasang pada komputer.

Install seluruh library yang dibutuhkan menggunakan perintah berikut:

```bash
py -m pip install -r requirements.txt
```

atau install secara manual:

```bash
py -m pip install opencv-python numpy pillow matplotlib
```

---

# Cara Menjalankan Program

Masuk ke folder proyek kemudian jalankan perintah berikut:

```bash
py src/main.py
```

---

# Alur Penggunaan

1. Jalankan aplikasi.
2. Klik tombol **Upload Image**.
3. Pilih gambar wajah selebriti.
4. Pilih metode pengolahan citra yang diinginkan.
5. Hasil pengolahan akan ditampilkan pada panel **Processed Image**.
6. Klik **Save Result** apabila ingin menyimpan hasil pengolahan.

---

# Dataset

Dataset yang digunakan merupakan kumpulan gambar wajah selebriti yang dikumpulkan secara mandiri.

Karakteristik dataset:

* Format gambar JPG/PNG
* Satu gambar untuk setiap selebriti
* Kombinasi selebriti Indonesia dan internasional
* Menggunakan gambar dengan wajah yang terlihat jelas agar proses deteksi wajah dapat berjalan dengan baik.

---

# Metode yang Diimplementasikan

| No | Metode                        | Status |
| -- | ----------------------------- | ------ |
| 1  | Grayscale                     | ✓      |
| 2  | Binary                        | ✓      |
| 3  | Histogram Equalization        | ✓      |
| 4  | Contrast Stretching           | ✓      |
| 5  | Brightness Adjustment         | ✓      |
| 6  | Mean Filter                   | ✓      |
| 7  | Median Filter                 | ✓      |
| 8  | Gaussian Filter               | ✓      |
| 9  | Sobel Edge Detection          | ✓      |
| 10 | Canny Edge Detection          | ✓      |
| 11 | Threshold Segmentation        | ✓      |
| 12 | K-Means Segmentation          | ✓      |
| 13 | Face Detection (Haar Cascade) | ✓      |

---

# Hasil Program

Aplikasi mampu menghasilkan beberapa keluaran berupa:

* Citra Grayscale
* Citra Biner
* Hasil Peningkatan Kontras
* Hasil Peningkatan Kecerahan
* Hasil Filtering
* Hasil Deteksi Tepi
* Hasil Segmentasi
* Hasil Deteksi Wajah

---

# Penulis

**Nama : Askaria Davan Dafyanza**

Program Studi Teknik Industri Otomotif

Universitas Pelita Bangsa

Mata Kuliah Pengolahan Citra Digital

Tahun 2026
