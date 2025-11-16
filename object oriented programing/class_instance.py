class Hero:
    # class variable (milik class, dipakai bersama oleh semua object)
    jumlah = 0

    # constructor → otomatis jalan saat object dibuat
    def __init__(self, InputName, health, InputPower, InputArmor):
        # instance variable (milik masing-masing object)
        self.name = InputName       # nama hero
        self.health = health        # HP hero
        self.power = InputPower     # attack power
        self.armor = InputArmor     # armor value

        # class variable ditambah setiap kali buat object baru
        Hero.jumlah += 1

        # hanya untuk melihat bahwa hero baru dibuat
        print("Membuat hero dengan nama:", InputName)


# membuat object Hero pertama
hero1 = Hero("quincy", 100, 12, 122)

# __dict__ menampilkan semua attribute milik hero1 dalam bentuk dictionary
print(hero1.__dict__)

# class variable → total hero yang sudah dibuat
print(Hero.jumlah)
