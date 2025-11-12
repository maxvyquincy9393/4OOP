def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} asal {student[1]}")

def get_student():
    nama = input("nama : ")
    asal = input("asal : ")
    return (nama,asal)

if __name__ == "__main__":
    main()