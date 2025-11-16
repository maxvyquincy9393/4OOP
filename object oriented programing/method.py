# ==========================
# CLASS
# ==========================
class Hero:

    # --------------------------
    # CLASS VARIABLE (milik class)
    # Shared oleh semua object
    # --------------------------
    jumlah_hero = 0

    # --------------------------
    # CONSTRUCTOR
    # Membuat OBJECT baru
    # --------------------------
    def __init__(self, InputName, Input_health, Input_power, Input_Armor):

        # --------------------------------
        # INSTANCE VARIABLE / ATRIBUT
        # Milik masing-masing object
        # --------------------------------
        self.name = InputName      # atribut
        self.health = Input_health # atribut
        self.power = Input_power   # atribut
        self.Armor = Input_Armor   # atribut

        # update class variable (bukan atribut)
        Hero.jumlah_hero += 1


    # --------------------------
    # METHOD (aksi)
    # Tanpa return
    # --------------------------
    def siapa(self):
        print("My name is", self.name)


    # --------------------------
    # METHOD dengan argumen
    # mengubah atribut object
    # --------------------------
    def healtup(self, up):
        self.health += up

    def powerup(self, up):
        self.power += up


    # --------------------------
    # METHOD dengan return
    # Mengambil nilai atribut
    # --------------------------
    def get_health(self):
        return self.health

    def get_power(self):
        return self.power



# ==========================
# MEMBUAT OBJECT
# ==========================
hero1 = Hero("sniper", 100, 100, 100)   # OBJECT hero1 dibuat dari class Hero

# ==========================
# MEMANGGIL METHOD OBJECT
# ==========================
hero1.siapa()          # method
hero1.healtup(100)     # method dengan argumen
hero1.powerup(900)     # method dengan argumen

# membuat OBJECT hero kedua
hero2 = Hero("defender", 100, 50, 1000)


# ==========================
# MELIHAT ATRIBUT OBJECT
# ==========================
print(hero1.__dict__)   # semua ATTRIBUT hero1

# ==========================
# MENGGUNAKAN METHOD RETURN
# ==========================
print("increase health :", hero1.get_health())
print("increase attack :", hero1.get_power())

# atribut hero2
print(hero2.__dict__)

# melihat CLASS VARIABLE
print("Total hero:", Hero.jumlah_hero)
