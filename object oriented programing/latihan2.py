# ====================================================
# GAME PERTARUNGAN SEDERHANA MENGGUNAKAN OOP
# ====================================================

class Hero:

    # ----------------------------------------------------
    # CONSTRUCTOR
    # Dipanggil saat object Hero dibuat.
    # Menerima 4 input lalu disimpan sebagai atribut hero.
    # ----------------------------------------------------
    def __init__(self, InputName, health, attackpower, defencepower):
        # -----------------------------
        # INSTANCE VARIABLE / ATRIBUT
        # -----------------------------
        self.name = InputName  # nama hero
        self.health = health  # darah
        self.attackpower = attackpower  # kekuatan serangan
        self.defencepower = defencepower  # kekuatan bertahan (defense)

    # ----------------------------------------------------
    # METHOD attackk()
    # Digunakan hero1 untuk menyerang hero2.
    # 'Hero' yang diterima parameter = target yang diserang.
    # ----------------------------------------------------
    def attackk(self, Hero):
        print(self.name + " ATTACKING " + Hero.name)

        # memanggil method 'attacked' milik hero yang diserang
        # self = penyerang
        # self.attackpower = attackpower penyerang
        Hero.attacked(self, self.attackpower)

    # ----------------------------------------------------
    # METHOD attacked()
    # Dipanggil ketika hero ini DISERANG oleh hero lain.
    # self = korban
    # lawan = penyerang
    # attackpower = kekuatan serangan penyerang
    # ----------------------------------------------------
    def attacked(self, enemy, attackpower):
        print(self.name + " ATTACKED By " + enemy.name)

        # --------------------------------------------
        # LOGIC DAMAGE:
        # damage = attackpower PENYERANG / defence KORBAN
        #
        # Semakin besar defencepower korban,
        # semakin kecil damage yang diterima.
        # --------------------------------------------
        damage_diterima = attackpower / self.defencepower

        print("serangan diterima :", damage_diterima)

        # kurangi darah korban
        self.health -= damage_diterima

        # tampilkan darah sisa
        print("darah", self.name, "tersisa :", self.health)


# ====================================================
# MEMBUAT OBJECT HERO
# ====================================================

# sniper:
#   - HP = 100
#   - Attack = 70
#   - Defence = 50
sniper = Hero("quincy", 100, 70, 50)

# maverick:
#   - HP = 200
#   - Attack = 50
#   - Defence = 200
maverick = Hero("maverick", 200, 50, 200)

# ====================================================
# PERTARUNGAN DIMULAI
# ====================================================

# sniper menyerang maverick
sniper.attackk(maverick)

print("\n")

# giliran maverick menyerang sniper
maverick.attackk(sniper)
