class Mobil:
    def __init__(self, mesin : str, warna, kecepatan : int):
        self.mesin = mesin
        self.warna = warna
        self.kecepatan = kecepatan


    def machine(self):
        return f"mobil ini mengguankan mesin {self.mesin}"

    def color(self):
        return f"mobil ini menggunakan warna {self.warna}"

    def velo(self):
        return f"mobil ini memiliki kecepatan maximal yaitu {self.kecepatan} km/h"

    def info(self):
        return f"mobil ini adalah mobil dengan merek {self.mesin}, menggunakan warna {self.warna}, dan memiliki kecepatan {self.kecepatan} km/h"


bugati = Mobil("V8", "kuning", 380)
print(bugati.info())