class Book:
    def __init__(self,judul,penulis):
        self.judul = judul
        self.penulis = penulis
        self.halaman = 0

    def info(self):
        print(self.judul)
        print(self.penulis)
        print(self.halaman)

class Lemari:
    def __init__(self):
        self.daftar_buku = []

    def tambah(self,book):
        self.daftar_buku.append(book)

    def hapus(self):
        self.daftar_buku.pop()

    def lihat_semua(self):
        for buku in self.daftar_buku:
            print("Judul : ", buku.judul, "penulis :", buku.penulis)

b1 = Book("di caprico","quincy")
lemari = Lemari()
lemari.tambah(b1)
lemari.lihat_semua()
