# Ringkasan Notebook: NumPy dan Matplotlib

Notebook ini memberikan pengenalan dasar tentang dua pustaka Python yang populer untuk komputasi numerik dan visualisasi data: NumPy dan Matplotlib.

## NumPy

Bagian NumPy mencakup beberapa konsep inti:

- **Pembuatan Array**: Menunjukkan cara membuat array 1D dan 2D dari daftar Python.
- **Pengindeksan dan Pengirisan (Indexing and Slicing)**: Menjelaskan cara mengakses elemen array, termasuk elemen pertama, terakhir, dan sub-array. Ini juga mencakup pengirisan pada array 2D untuk mendapatkan baris atau kolom tertentu.
- **Pengindeksan Boolean (Boolean Indexing)**: Mendemonstrasikan cara memfilter array berdasarkan kondisi boolean, sebuah teknik yang sangat berguna dalam machine learning untuk memilih data.
- **Operasi Matematika**: Mencakup operasi matematika berdasarkan elemen (penjumlahan, perkalian), serta fungsi matematika universal seperti akar kuadrat (`np.sqrt`), jumlah (`np.sum`), dan rata-rata (`np.mean`).
- **`np.argsort()`**: Menjelaskan cara mendapatkan indeks yang akan mengurutkan array, yang berguna untuk menemukan *k* elemen terdekat dalam algoritma seperti KNN.

## Matplotlib

Bagian Matplotlib memperkenalkan komponen dasar untuk membuat visualisasi:

- **Plot Dasar**: Menunjukkan cara membuat plot garis sederhana menggunakan `plt.plot()`.
- **Scatter Plot**: Menjelaskan cara membuat scatter plot dengan kustomisasi untuk warna, bentuk penanda, ukuran, dan label.
- **Kustomisasi Plot**:
    - **Label dan Judul**: Cara menambahkan label sumbu-x dan sumbu-y, serta judul ke plot.
    - **Legenda**: Cara menampilkan legenda untuk mengidentifikasi berbagai set data dalam plot.
    - **Grid**: Cara menambahkan grid ke plot untuk keterbacaan yang lebih baik.
- **Layout**: Menyebutkan cara menyesuaikan tata letak plot untuk memastikan semua elemen pas dan terlihat rapi.
- **Contoh Visualisasi KNN**: Di akhir, ada contoh praktis yang menggabungkan NumPy dan Matplotlib untuk memvisualisasikan data training dan testing dalam konteks algoritma K-Nearest Neighbors (KNN). Ini menunjukkan bagaimana memplot titik data dari kelas yang berbeda (misalnya, 'Apel' dan 'Jeruk') untuk melihat distribusinya secara visual.
