from collections import deque

stack = deque()

def menu():
    print("\n=== PROGRAM STACK ===")
    print("1. Append (Tambah di kanan)")
    print("2. AppendLeft (Tambah di kiri)")
    print("3. Pop (Hapus dari kanan)")
    print("4. PopLeft (Hapus dari kiri)")
    print("5. Clear (Hapus semua)")
    print("6. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.append(data)
        print("Stack =", list(stack))

    elif pilihan == "2":
        data = input("Masukkan data: ")
        stack.appendleft(data)
        print("Stack =", list(stack))

    elif pilihan == "3":
        if stack:
            print("Data yang dihapus:", stack.pop())
        else:
            print("Stack kosong!")
        print("Stack =", list(stack))

    elif pilihan == "4":
        if stack:
            print("Data yang dihapus:", stack.popleft())
        else:
            print("Stack kosong!")
        print("Stack =", list(stack))

    elif pilihan == "5":
        stack.clear()
        print("Stack dikosongkan.")

    elif pilihan == "6":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")
