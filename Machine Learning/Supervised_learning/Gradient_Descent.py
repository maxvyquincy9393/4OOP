import numpy as np

# Data sederhana : luas rumah(x) dan harga (y)
x = np.array([2104,1600,2400,1416,3000]) # fitur
y = np.array([400,330,369,232,540])     # target

# inisialisasi parameter
theta0 = 0.0    #   intercept
theta1 = 0.0    # slope
alpha = 0.0001    # learning rate
m = len(x)

# gradient decent loop
for epoch in range(1000):
    # prediksi
    y_pred = theta0 + theta1 * x

    # hitung error
    error = y_pred - y

    # rumus aslinya
    # # θj := θj - α * (1/m) * Σ (hθ(x(i)) - y(i)) * xj(i)
    # Di sini ada 2 parameter: θ0 dan θ1
    """Bayangkan kamu latihan lempar bola ke keranjang 🏀.

    Kalau bola meleset sedikit → koreksi gaya lemparan sedikit.

    Kalau meleset jauh → koreksi lebih besar.

    Kalau kamu kumpulin semua lemparan dari 100 kali percobaan, lalu hitung rata-rata error dan koreksi gaya sekali besar → itu batch gradient descent.

    Jadi bukan koreksi per lemparan, tapi koreksi setelah melihat semua lemparan sekaligus."""

    # Update 00 ( intercept )
    theta0 = theta0 - alpha * (1/m) * np.sum(error)

    # update 01 ( slope )
    theta1 = theta1 - alpha * (1/m) * np.sum(error)

# Hasil parameter
print("theta0:", theta0)
print("theta1:", theta1)
