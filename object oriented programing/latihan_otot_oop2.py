class Bangunan:
    def __init__(self, luas: int, alamat):
        self.luas = luas
        self.alamat = alamat

    def detail(self):
        return f"Bangunan ini memiliki luas {self.luas}, dam alamat berada di: {self.alamat}"

class Toko(Bangunan):
    def __init__(self, luas: int, alamat: str, nama_toko):
        super().__init__(luas, alamat)
        self.nama_toko = nama_toko

    def info(self):
        return f"Toko ini bernama {self.nama_toko} berlokasi di {self.alamat} dan memilki luas {self.luas} m"

TOKO1 = Toko(100, "new york", "Quincy caffe")
print(TOKO1.info())