from utils.app import *

from data_structure.linked_list import SLinkedList

def main():
    menu = {
        1: "Tambah Data",
        2: "Tampilkan Data",
        3: "Cari Data",
        4: "Hapus Data",
        5: "Keluar Program"
    }

    linked_list = SLinkedList()

    count = 0
    while True:
        if count > 0:
            program4.clear()
            print(program4.title)

        print("Menu Program:")
        for i, k in menu.items():
            print(f"{i}. {k}")

        opt = program4.prompt_options("\nPilih menu", [i for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                print("\nPrompt Penambahan Data:")
                while True:
                    nama = input("Masukkan Nama Mahasiswa: ")
                    if not nama.replace(" ", "").isalpha():
                        print("Nama yang anda masukkan tidak valid!")
                        continue
                    break
                while True:
                    nim = input("Masukkan NIM Mahasiswa: ")
                    if not nim.isdecimal():
                        print("NIM yang anda masukkan tidak valid!")
                        continue

                    available = True
                    for data in linked_list.display():
                        if data[1] == nim:
                            print(f"NIM yang dimasukkan sudah digunakan")
                            available = False
                            break

                    if available:
                        break

                linked_list.append((nama, nim))

                print("\nData berhasil ditambahkan")
                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if linked_list.empty():
                    print("\nData Kosong! Tidak ada data yang bisa ditampilkan!")
                else:
                    print("\nBerikut adalah data dalam linked list: ")
                    for data in linked_list.display():
                        print(f"{data[1]}: {data[0]}")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                options = {
                    1: "Cari berdasarkan Nama",
                    2: "Cari berdasarkan NIM"
                }

                program4.clear()
                print(program4.title)

                print("Opsi Pencarian Data:")
                for i, k in options.items():
                    print(f"{i}. {k}")

                opt = program4.prompt_options("\nPilih menu", [i for i in options.keys()])

                match opt:
                    case 1:
                        searching = input("\nMasukkan Nama mahasiswa: ")
                        found = False

                        for data in linked_list.display():
                            if data[0] == searching:
                                print(f"\nHasil pencarian:\n{data[1]}: {data[0]}")
                                found = True
                                break

                        if not found:
                            print(f"Mahasiswa dengan nama [{searching}] tidak ditemukan!")
                        
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    case 2:
                        searching = input("\nMasukkan NIM mahasiswa: ")
                        found = False

                        for data in linked_list.display():
                            if data[1] == searching:
                                print(f"\nHasil pencarian:\n{data[1]}: {data[0]}")
                                found = True
                                break

                        if not found:
                            print(f"Mahasiswa dengan NIM [{searching}] tidak ditemukan!")

                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                options = {
                    1: "Hapus berdasarkan Nama",
                    2: "Hapus berdasarkan NIM"
                }

                program4.clear()
                print(program4.title)

                print("Opsi Penghapusan Data:")
                for i, k in options.items():
                    print(f"{i}. {k}")

                opt = program4.prompt_options("\nPilih menu", [i for i in options.keys()])

                match opt:
                    case 1:
                        delete = input("\nMasukkan Nama mahasiswa: ")

                        for data in linked_list.display():
                            if data[0] == delete:
                                print(f"\nData:\n{data[1]}: {data[0]}")
                                confirm = program4.prompt_options("\nApakah anda yankin ingin menghapus data tersebut?", ["y", "n"])
                                if confirm == "y":
                                    linked_list.remove(data)
                                    print("\nData berhasil dihapus")
                                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                                    break
                                else:
                                    break
                        else:
                            print(f"Data Mahasiswa dengan nama [{delete}] tidak ditemukan!")
                            getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

                    case 2:
                        delete = input("\nMasukkan NIM mahasiswa: ")

                        for data in linked_list.display():
                            if data[1] == delete:
                                print(f"\nData:\n{data[1]}: {data[0]}")
                                confirm = program4.prompt_options("\nApakah anda yankin ingin menghapus data tersebut?", ["y", "n"])
                                if confirm == "y":
                                    linked_list.remove(data)
                                    print("\nData berhasil dihapus")
                                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                                    break
                                else:
                                    break
                        else:
                            print(f"Data Mahasiswa dengan nama [{delete}] tidak ditemukan!")
                            getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 5:
                return program4.stop()

        count += 1

title = "[bold #9ee5ff]Program 4: Implementasi Linked List4\n" # untuk di tampilkan sebagai judul
name = "Implementasi Linked List" # untuk di tampilkan di list menu
description = """[bold]
🔷 Program 4 merupakan program implementasi struktur data linked list.
🔷 Struktur data linked list pada program ini digunakan untuk menampung data nama dan NIM mahasiswa.
🔷 Program ini memiliki fitur untuk menambahkan dan menampilkan data serta mencari dan menghapus data berdasarkan nama ataupun NIM.\n""" # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
