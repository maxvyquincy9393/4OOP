class Bank:
    def __init__(self, saldo_awal=0):
        self.saldo = saldo_awal

    def deposit(self, jumlah):
        self.saldo += jumlah

    def withdraw(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak cukup.")
        else:
            self.saldo -= jumlah


bank = Bank(0)  # saldo awal

while True:
    print("\n=== BANK DIGITAL ===")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Cek Saldo")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah deposit: "))
        bank.deposit(jumlah)
        print("Deposit berhasil.")

    elif pilihan == "2":
        jumlah = int(input("Masukkan jumlah withdraw: "))
        bank.withdraw(jumlah)

    elif pilihan == "3":
        print("Saldo saat ini:", bank.saldo)

    elif pilihan == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid.")
