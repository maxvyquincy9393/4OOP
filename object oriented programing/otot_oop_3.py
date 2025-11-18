class AkunBank:
    def __init__(self,saldo = 0):
        self.saldo = saldo

    def deposit(self,jumlah : int):
        self.saldo += jumlah

    def tarik(self,jumlah):
        if jumlah > self.saldo:
            print("saldo tidak cukup")
        else:
            self.saldo -= jumlah

bank = AkunBank(0)
while True:
    print("Akun Bank")
    print("1. cek saldo")
    print("2. deposit")
    print("3. tarik")
    print("4. exit")

    pilihan = int(input("pilihan kamu adalah : "))
    if pilihan == 1:
        print(f"saldo kamu saat ini : {bank.saldo}")
    elif pilihan == 2:
        jumlah = int(input("Masukkan jumlah deposit: "))
        bank.deposit(jumlah)
    elif pilihan == 3:
        jumlah = int(input("Masukkan jumlah deposit: "))
        bank.tarik(jumlah)
    elif pilihan == 4:
        break
    else:
        print("pilihan tidak ditemukan")
