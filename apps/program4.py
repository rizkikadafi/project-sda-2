from utils.app import *

from data_structure.linked_list import SLinkedList

def panel_success(value: tuple, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""
    
    addition_success = Group(
        Text("\nData mahasiswa dengan:\n", justify="center", style="text_success"),
        Align.center(Text(f"Nama    : {value[0]}\nNIM     : {value[1]}", style="text_success")),
        Text("\nBerhasil ditambahkan!\n", justify="center", style="text_success")
    )

    deletion_success = Group(
        Text("\nData mahasiswa dengan:\n", justify="center", style="text_success"),
        Align.center(Text(f"Nama    : {value[0]}\nNIM     : {value[1]}", style="text_success")),
        Text("\nBerhasil dihapus!\n", justify="center", style="text_success")
    )

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(addition_success, title="[title_success]INFO", style="success")
        case "deletion":
            panel = Panel(deletion_success, title="[title_success]INFO", style="success")

    return panel

def panel_empty_data(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(Text("\nLinked List Kosong! Tidak ada data yang bisa dihapus!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
        case "display_data":
            panel = Panel(Text("\nLinked List Kosong! Tidak ada data yang bisa ditampilkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")

    return panel

def panel_not_found_data(data, case: str) -> Panel:
    """Panel untuk menampilkan infor ketika data yang dicari tidak ditemukan."""

    panel = Panel("None")
    match case:
        case "nama":
            panel = Panel(Padding(Text(f"Mahasiswa dengan nama [{data}] tidak ditemukan!", justify="center", style="text_warning"), pad=(1, 0, 1, 0)), title="[title_warning]INFO", style="warning")
        case "nim":
            panel = Panel(Padding(Text(f"Mahasiswa dengan NIM [{data}] tidak ditemukan!", justify="center", style="text_warning"), pad=(1, 0, 1, 0)), title="[title_warning]INFO", style="warning") 

    return panel

def table_data(data: SLinkedList) -> Table:
    """Tabel untuk menampilkan data."""

    table = Table(title="[text_title]Data Mahasiswa", style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]NIM", style="text_default", min_width=20)
    table.add_column("[text_title]Nama", style="text_default", min_width=20)

    data_mhs = data.traverse()
    for i in range(data.size):
        mhs = next(data_mhs)
        table.add_row(f"{i+1}", f"{mhs[1]}", f"{mhs[0]}")

    return table

def search_data(data, linked_list: SLinkedList, based_on: str):
    """Fungsi untuk menampilkan data yang dicari."""

    result_table = Table(title="[text_title]Hasil Pencarian", style="default")
    result_table.add_column("[text_title]No.", style="text_default", justify="center")
    result_table.add_column("[text_title]NIM", style="text_default", min_width=20)
    result_table.add_column("[text_title]Nama", style="text_default", min_width=20)

    match based_on:
        case "nama":
            count = 1
            for data_mhs in linked_list.traverse():
                if data_mhs[0] == data:
                    result_table.add_row(f"{count}", f"{data_mhs[1]}", f"{data_mhs[0]}")
                    console.print(result_table, justify="center")
                    return
                count += 1

            console.print(Padding(panel_not_found_data(data, case="nama"), pad=(1, 0, 0, 0)))

        case "nim":
            count = 1
            for data_mhs in linked_list.traverse():
                if data_mhs[1] == data:
                    result_table.add_row(f"{count}", f"{data_mhs[1]}", f"{data_mhs[0]}")
                    console.print(result_table, justify="center")
                    return
                count += 1

            console.print(Padding(panel_not_found_data(data, case="nim"), pad=(1, 0, 0, 0)))

def delete_data(data, linked_list: SLinkedList, based_on: str):
    """Fungsi untuk menghapus data tertentu."""

    result_table = Table(title="[text_title]Penghapusan Data")
    result_table.add_column("[text_title]No.", style="text_default", justify="center")
    result_table.add_column("[text_title]NIM", style="text_default", min_width=20)
    result_table.add_column("[text_title]Nama", style="text_default", min_width=20)

    match based_on:
        case "nama":
            count = 1
            for data_mhs in linked_list.traverse():
                if data_mhs[0] == data:
                    result_table.add_row(f"{count}", f"{data_mhs[1]}", f"{data_mhs[0]}")
                    console.print(result_table, justify="center")

                    if Confirm.ask("[bold]\nApakah anda yakin ingin menghapus data tersebut"):
                        linked_list.remove(data_mhs)
                        console.print(panel_success(data_mhs, operation="deletion"))
                        return
                    else:
                        return
                count += 1
            else:
                console.print(panel_not_found_data(data, case="nama"))

        case "nim":
            count = 1
            for data_mhs in linked_list.traverse():
                if data_mhs[1] == data:
                    result_table.add_row(f"{count}", f"{data_mhs[1]}", f"{data_mhs[0]}")
                    console.print(result_table, justify="center")

                    if Confirm.ask("[bold]\nApakah anda yakin ingin menghapus data tersebut"):
                        linked_list.remove(data_mhs)
                        console.print(panel_success(data_mhs, operation="deletion"))
                        return
                    else:
                        return
                count += 1
            else:
                console.print(panel_not_found_data(data, case="nim"))

def main():
    menu = {
        1: "Tambah Data",
        2: "Tampilkan Data",
        3: "Cari Data",
        4: "Hapus Data",
        5: "Keluar Program"
    }
    
    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    searching_options = {
        1: "Cari berdasarkan Nama",
        2: "Cari berdasarkan NIM"
    }

    searching_options_str = "\n[text_default]"
    for i, k in searching_options.items():
        searching_options_str += f"{i}. {k}\n"

    deletion_options = {
        1: "Hapus berdasarkan Nama",
        2: "Hapus berdasarkan NIM"
    }

    deletion_options_str = "\n[text_default]"
    for i, k in deletion_options.items():
        deletion_options_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")
    panel_description = Panel(program4.description, title="[text_title]Deskripsi Program", title_align="left", style="default")
    panel_searching_options = Panel(searching_options_str, title="[text_title]Opsi Pencarian Data", title_align="left", style="default")
    panel_deletion_options = Panel(deletion_options_str, title="[text_title]Opsi Penghapusan Data", title_align="left", style="default")

    linked_list = SLinkedList()

    while True:
        console.clear()
        console.rule(program4.title, style="default")
        console.print(Padding(panel_description, pad=(1, 0, 0, 0)))
        
        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()])

        import getpass
        match opt:
            case 1: # case 1: Tambah data
                print()
                console.rule("[text_title]Prompt Penambahan Data", style="default")

                while True:
                    nama = Prompt.ask("[bold]\nMasukkan Nama Mahasiswa")
                    if not nama.replace(" ", "").isalpha():
                        console.print("[prompt.invalid]Nama hanya boleh berisi karakter alphabet!")
                        continue
                    break

                while True:
                    nim = Prompt.ask("[bold]\nMasukkan NIM Mahasiswa")
                    if not nim.isdecimal():
                        console.print("[prompt.invalid]NIM hanya boleh berisi angka!")
                        continue

                    available = True
                    for data in linked_list.traverse():
                        if data[1] == nim:
                            console.print("[prompt.invalid]NIM yang dimasukkan sudah digunakan")
                            available = False
                            break

                    if available:
                        break

                linked_list.append((nama, nim))

                console.print(Padding(panel_success((nama, nim), operation="addition"), pad=(1, 0, 0, 0)))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 2: # case 2: Tampilkan data
                if linked_list.empty():
                    console.print(Padding(panel_empty_data(operation="display_data"), pad=(1, 0, 0, 0)))
                else:
                    console.print(table_data(linked_list), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 3: # case 3: Cari data
                console.clear()
                console.rule(program4.title)
                
                if linked_list.empty():
                    console.print(Padding(panel_empty_data(operation="display_data"), pad=(1, 0, 0, 0)))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.print(Padding(panel_searching_options, pad=(1, 0, 0, 0)))

                opt = IntPrompt.ask("\n[bold]Pilih opsi pencarian data", choices=[str(i) for i in searching_options.keys()])

                match opt:
                    case 1: # opsi pencarian data 1: berdasarkan nama
                        searching = Prompt.ask("\n[bold]Masukkan Nama mahasiswa")

                        search_data(searching, linked_list, based_on="nama")
                        
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

                    case 2: # opsi pencarian data 1: berdasarkan nim
                        searching = Prompt.ask("\n[bold]Masukkan NIM mahasiswa")

                        search_data(searching, linked_list, based_on="nim")
                        
                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 4:
                console.clear()
                console.rule(program4.title, style="default")

                if linked_list.empty():
                    console.print(Padding(panel_empty_data(operation="deletion"), pad=(1, 0, 0, 0)))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.print(Padding(panel_deletion_options, pad=(1, 0, 0, 0)))

                opt = IntPrompt.ask("\n[bold]Pilih opsi Penghapusan data", choices=[str(i) for i in deletion_options.keys()])

                match opt:
                    case 1: # opsi pencarian data 1: berdasarkan nama
                        delete = Prompt.ask("\n[bold]Masukkan Nama mahasiswa")

                        delete_data(delete, linked_list, based_on="nama")

                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

                    case 2: # opsi pencarian data 1: berdasarkan nim
                        delete = Prompt.ask("\n[bold]Masukkan NIM mahasiswa")

                        delete_data(delete, linked_list, based_on="nim")

                        getpass.getpass("\nKlik 'Enter' untuk melanjutkan")

            case 5:
                return program4.stop()

title = "[text_title]Program 4: Implementasi Linked List4\n" # untuk di tampilkan sebagai judul
name = "Implementasi Linked List" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 4 merupakan program implementasi struktur data linked list.
🔷 Struktur data linked list pada program ini digunakan untuk menampung data nama dan NIM mahasiswa.
🔷 Program ini memiliki fitur untuk menambahkan dan menampilkan data serta mencari dan menghapus data berdasarkan nama ataupun NIM.\n""" # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
