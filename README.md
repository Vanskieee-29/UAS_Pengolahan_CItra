# Aplikasi Pengolahan Citra Digital

## Implementasi Pengolahan Citra Digital pada Dataset Wajah Selebriti Menggunakan Python dan OpenCV

---

**Nama : Askaria Davan Dafyanza**

Program Studi Teknik Informatika

Universitas Pelita Bangsa

Mata Kuliah Pengolahan Citra

---

## Deskripsi Proyek

Aplikasi Pengolahan Citra Digital merupakan aplikasi desktop berbasis **Python**, **OpenCV**, dan **Tkinter** yang dikembangkan untuk mengimplementasikan berbagai teknik dasar pengolahan citra digital pada dataset wajah selebriti.

Pengguna dapat mengunggah gambar wajah, kemudian memilih berbagai metode pengolahan citra melalui antarmuka grafis (GUI). Hasil pengolahan akan ditampilkan secara langsung dan dapat disimpan sebagai file gambar.

Proyek ini dibuat sebagai **Tugas Ujian Akhir Semester (UAS)** Mata Kuliah **Pengolahan Citra**.

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

<img width="1920" height="1200" alt="messigray" src="https://github.com/user-attachments/assets/98f72154-8465-480b-b83b-e4cbeb09ffa1" />
<img width="1920" height="1200" alt="messibinary" src="https://github.com/user-attachments/assets/a9608a10-1020-4d1a-bc89-1f89babbe220" />
<img width="1920" height="1200" alt="messihistogram" src="https://github.com/user-attachments/assets/a3e90449-74c8-4274-ad95-feeff8e4c00d" />
<img width="1920" height="1200" alt="messicontrast" src="https://github.com/user-attachments/assets/8978c7a3-35d1-4269-8aef-2e1e1026509e" />
<img width="1920" height="1200" alt="messibrightness" src="https://github.com/user-attachments/assets/d1bc8fc2-ff48-4e1b-a9d0-06852798b8bf" />
<img width="1920" height="1200" alt="messimean" src="https://github.com/user-attachments/assets/0398c4b5-beee-48df-b2c7-c568f09462b5" />
<img width="1920" height="1200" alt="messimedian" src="https://github.com/user-attachments/assets/ba26e76e-3f55-4c6d-b9e8-7cd154211756" />
<img width="1920" height="1200" alt="messigaussian" src="https://github.com/user-attachments/assets/02290f4c-0361-4f02-9c4c-cd7710a21c39" />
<img width="1920" height="1200" alt="messisobel" src="https://github.com/user-attachments/assets/b40173a5-f7e5-4898-be8f-eab186518133" />
<img width="1920" height="1200" alt="messicanny" src="https://github.com/user-attachments/assets/30889e2d-d6a9-41b8-8573-239436d75144" />
<img width="1920" height="1200" alt="messithreshold" src="https://github.com/user-attachments/assets/47e83e87-7035-4008-a5d5-c03006bb2069" />
<img width="1920" height="1200" alt="messikmeans" src="https://github.com/user-attachments/assets/a6f62205-d01e-4ec4-a1a5-f2efda193eba" />
<img width="1920" height="1200" alt="messifacedetection" src="https://github.com/user-attachments/assets/f2de1eb8-cb96-42ed-b8c4-3ec7e40ccd1b" />

---
