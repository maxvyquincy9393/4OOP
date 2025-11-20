# ========================================
# CONTOH OOP DASAR - SISTEM PERPUSTAKAAN
# ========================================
# file ini mendemonstrasikan 4 pilar utama OOP:
# 1. Encapsulation ( enkapsulasi) Menyembunyikan data internal
# 2. Inheritance (Pewarisan) - Class anak untuk mewarisi dari class induk
# 3. Polymorphism (Polimorfisme ) - Satu interface, banyak implementasi
# 4. Abstraction ( Abstraksi ) - menyembunyiikan kompleksitas


# ========================================
# 1. ENCAPSULATION
# ========================================
# Enkapsulasi = membungkus data dan method dalam satu unit ( class )
# Tujuan : melindungi data dari akses langusng ,  kontrol via method

class Book:
    """
    Class book mendemonstrasikan enkapsulasi
    - Datta disembunyikan dengan underscore
    - akses data melalui getter/setter
    """

    def __init__(self, title, author, isbn):
        """
        constructor : METHOD YANG DIPANGGIL SAAT OBJECT DIBUAT
        args:
            title : judul buku
            author : penulis
            isbn : nomor buku
        """

        # public atribut (bisa diakses langsung)
        self.title = title
        self.author = author

        # Private attribute ( pakai __ di depan, tidak bisa diakses dari luar

        self.__isbn = isbn

        # protected attribute ( pakai _ di depan, untuk internal lass dan subcalss
        self._available = True

        # getter method -  mengambil nilai private atribute

    def get_isbn(self):
        """
                    Getter method untuk mengambil ISBN
                    Returns: ISBN buku (string)
        """
        return self.__isbn

        # setter method - unutk mengubah nilai protected attribute
    def set_available(self, status):
        """
            settter method untuk mengubah status ketersedian
            args :
                status: boolean (True = tersedia False = dipinjam)
        """

        # validasi input sebelim set value
        if isinstance(status, bool):       # digunakan untuk mengecek apakah sebuah objek merupakan instance (objek) dari class/tipe tertentu
            self._available = status
        else:
            raise ValueError("status is not boolean")

    def get_info(self):
        """
            method untuk mendapatkan informasi buku
            return : string informasi buku
        """

        # conditional : ubah bolean menjadi text yang readable

        status = "Tersedia" if self._available else "Dipinjam"
        return f"{self.title} : oleh {self.author} : {status}"

# ========================================
# 2. INHERITANCE (Pewarisan)
# ========================================
# inheritance = class anak mewarusu properties dan method dari class induk
# tujuan : code reuse , stukur hirarki jelas

class EBook(Book):
    """
    ebook adalah child class dari book
    - mewarisi semua atribute dan method dari book
    - bisa menambah atribute dan method baru
    - bisa override metrhod dari parent
    """

    def __init__(self, title, author, isbn, file_size):
        """
        consturctor child class
        args :
        title, author , isbn : diteruskan ke parent
        file_size : attribute tambahakn khuss untuk ebook
        """

        # super() : memanggil emtod dari parent class
        # ini akan memanggil __init__ dari book

        super().__init__(title,author,isbn)

        # atribute tambahan khsus ebook
        self.file_size = file_size

    # override method dari parent - menimpa method get_info
    def get_info(self):
        """
        overrude method get_info dari parent
        menambahkan info file size untuk ebook
        """

        # panggil method parent dulu
        basic_indo = super().get_info()
        # tambahkan info spesifik ebook
        return f"{basic_indo} | File : {self.file_size} MB"

class PhysicalBook(Book):   # juga mewarisi dari book
    """
        PhysicalBook adalah child class kedua dari Book
        Menunjukkan bahwa satu parent bisa punya banyak child
    """

    def __init__(self,title,author,isbn, shelf_location):
        """Counsturctor dengan atribute tambahan lokasi rak """

        # panggil const parent
        super().__init__(title,author,isbn)
        # atribute khusus physical book
        self.shelf_location = shelf_location

    # override method get_info()
    def get_info(self):
        """Override untuk menambahkan info lokasi rak"""
        basic_info = super().get_info()
        return f"{basic_info} | Rak : {self.shelf_location}"

# ========================================
# 3. POLYMORPHISM (Polimorfisme)
# ========================================
# Polymorphism = satu interface, banyak bentuk
# Object berbeda bisa diperlakukan sama karena punya interface yang sama
class Library:
    """
    CLASS library mendemonstrasikan polymorphism
    bisa menampung berbagai jenis Book ( ebook , fisik dll)

    """

    def __init__(self,name):
        """
        consturctor Libary
        args :
        name : nama perpustakaan
        """
        self.name = name
        self.books = []

    def add_book(self,book):
        """
        method untuk menambah buku
        polymorphism : mernerima semua object yang instance dari book
        args :
        book : object book atau turunanannya ( ebook, physical book )
        """

        # instance() = cek apakah objek adalah instance dari class tertentu

        if isinstance(book,Book):
            self.books.append(book)
            print(f"Buku ditambahkan : {book.title}")
        else:
            print(f"object bukan instance dari Book")


    def display_all_books(self):
        """
        polymorphism in action!
        method get_info() akan dipanggil sesuai tipe object:
        -Book.get_info() untuk book
        - EBook.get_info() untuk ebook
        - PhysicalBook.get_info() untuk fisik
        """

        print(f"\n koleksi {self.name} : ")
        print("="*60)

        #loop through semua buku

        for idx, book in enumerate(self.books,1):
            # polymorphism get info() berbeda tergantung tipe object
            # python otomatis memanggil method yang sesuai
            print(f"{idx}. {book.get_info()}")

# ========================================
# 4. ABSTRACTION (Abstraksi)
# ========================================
# Abstraction = menyembunyikan detail implementasi, tampilkan yang penting
# Pakai abstract class untuk mendefinisikan "kontrak" yang harus diikuti

from abc import ABC, abstractmethod # import untuk absctract class
class LibraryItem(ABC):
    """
    Abstract class untuk item perpustakaan
    - tidak bisa di instantiate langsung ( tidak bisa buat object )
    - harus di inherit oleh class lain
    - memaksa child classs implemend metod tertentu
    """

    #@abstractmethod = decorator untuk method abstract
    # method ini harus di implement oleh semua anak class

    @abstractmethod
    def get_borrowing_period(self):
        """
               Abstract method: tidak punya implementasi di parent
               Child class WAJIB implement method ini
               Returns: string periode peminjaman
               """
        pass  # pass = placeholder, tidak ada implementasi

    #method biasa ( bukan abstract ) bisa punya implementasi
    def display_title(self):
        """
        method concrete ( punya implementasi )
        bisa dipakai langusng oleh child class
        """
        return f"item : {self.title}"

class Magazine(LibraryItem):
    """
    magazine nebgimplemntasi abstract class libraryitem
    wajib implement get_browsing_period()
    """
    def __init__(self,title):
        self.title = title


    # implement abstract method ( wahib )
    def get_borrowing_period(self):
        """Implementation untuk magazine"""
        return "7 hari"

class DVD(LibraryItem):
    """
    DVD mengimplentasi abstract class libraryitem
    implementasi bsia berbeda dengan magazine
    """
    def __init__(self,title):
        self.title = title

    # implement abstract method dengan implementasi berbeda
    def get_borrowing_period(self):
        """Implementation untuk DVD"""
        return "3 hari"

# ========================================
# TESTING - MENJALANKAN SEMUA CONTOH
# ========================================
# if __name__ == "__main__": = kode ini hanya jalan kalau file dijalankan langsung
# (tidak jalan kalau file di-import ke file lain)

if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRASI 4 PILAR OOP")
    print("=" * 60)

    # ========================================
    # 1. Test Encapsulation
    # ========================================
    print("\n1️⃣  ENCAPSULATION")
    print("-" * 60)

    # buat object book ( instalisasi )
    book1 = Book("Python Crash Coourse", "Eric Matthers", "978-1593279288")

    # akses public atribute ( bisa langsung )
    print(f"Public attribute : {book1.title}")

    # akses private attribute ( harus via getter)
    #book1.__isbn akan error! harus pakai getter

    print(f"Private attribute (Via getter) : {book1.get_isbn()}")

    # ubah protected attribute via setter
    book1.set_available(False) # ubah jadi tak tersedia
    print(f"Info : {book1.get_info()}")

    # ========================================
    # 2. Test Inheritance
    # ========================================
    print("\n2️⃣  INHERITANCE")
    print("-" * 60)

    # buat object dari child class
    # ebook punya semua yang book punya, plus file size
    ebook = EBook("clean code", "Robert Martin", "978-0132350884", 2)
    physical = PhysicalBook("Design Pattern", "Gang of Four", "978-0132350884", "A-12")

    # ========================================
    # 3. Test Polymorphism
    # ========================================
    print("\n3️⃣  POLYMORPHISM")
    print("-" * 60)

    # buat library
    library = Library("Perpustakaan F1")

    # add berbagai jenis buku ( book, ebook, fisik)
    #polymorphism : library.add_book() menerima semua buku

    library.add_book(book1)
    library.add_book(ebook)
    library.add_book(physical)

    # displat semua - polymorphism dalam action
    # setiap obejt akan panggil get_info versi mereka sendiri
    library.display_all_books()

    # ========================================
    # 4. Test Abstraction
    # ========================================
    print("\n4️⃣  ABSTRACTION")
    print("-" * 60)

    # buat object dari concrete class ( bukan abstract class )
    magazine = Magazine("National Geographic")
    dvd = DVD("The F1")

    # PANGGIL METHOD - IMPLEMENTASINYA BERBEDA
    print(f"{magazine.display_title()} - Periode pinjam : {magazine.get_borrowing_period()}")
    print(f"{dvd.display_title()} - periode pinjam : {dvd.get_borrowing_period()}")

    # tidak bisa buat object dari abstract class!
    # item = library item("something") # ini akan error

    print("\n" + "=" * 60)
    print("semua demo selesai")
    print("=" * 60)