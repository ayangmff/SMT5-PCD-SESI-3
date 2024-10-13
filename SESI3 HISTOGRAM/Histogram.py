# Import library yang diperlukan
import imageio
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk mengonversi gambar RGB menjadi grayscale
def rgb_to_grayscale(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])  # Konversi menggunakan rumus luminansi

# Membaca gambar berwarna (RGB)
image_path = 'C:\\Users\\lenovo\\Downloads\\photo_6167803359428460692_y.jpg'  # Ganti dengan path file gambar yang ingin digunakan
image_rgb = imageio.imread(image_path)

# Mengonversi gambar menjadi grayscale
image_gray = rgb_to_grayscale(image_rgb)

# Menghitung histogram untuk gambar grayscale
histogram, bin_edges = np.histogram(image_gray, bins=256, range=(0, 255))

# Menampilkan gambar grayscale
plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Gambar Grayscale')
plt.axis('off')

# Menampilkan histogram
plt.subplot(2, 1, 2)
plt.plot(bin_edges[0:-1], histogram)
plt.title('Histogram Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Menyimpan hasil plot histogram
plt.savefig('histogram_grayscale.png')

# Menampilkan hasil plot
plt.show()

# Menjawab pertanyaan:
total_pixels_per_intensity = histogram
dominant_intensity = np.argmax(histogram)

print(f"Jumlah total piksel untuk setiap intensitas: {total_pixels_per_intensity}")
print(f"Intensitas yang paling dominan: {dominant_intensity} dengan jumlah piksel {histogram[dominant_intensity]}")
