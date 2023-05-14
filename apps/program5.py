from utils.app import *

from data_structure.array import Array

def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""
    
    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(Text(f"\nData [{value}] telah dimasukkan ke antrian!\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
        case "deletion":
            panel = Panel(Text(f"\nData [{value}] telah dihapus dari antrian!\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
        case "emptying":
            panel = Panel(Text(f"\nSeluruh data telah dihapus!\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")

    return panel

def full_data_panel(value) -> Panel:
    """Panel untuk menampilkan info ketika data penuh."""

    panel = Panel(Text(f"\nAntrian telah penuh! [{value}] tidak dimasukkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
    return panel

def empty_data_panel(operation: str) -> Panel:
    """Panel untuk menampilkan info ketika data kosong."""

    panel = Panel("None")
    match operation:
        case "deletion":
            panel = Panel(Text("\nAntrian Kosong! Tidak ada data yang bisa dihapus!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
        case "display_data":
            panel = Panel(Text("\nAntrian Kosong! Tidak ada data yang bisa ditampilkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")

    return panel

def not_found_data_panel(data) -> Panel:
    """Panel untuk menampilkan info ketika data yang dicari tidak ditemukan."""

    panel = Panel(Padding(Text(f"Data [{data}] tidak ada di dalam antrian!", justify="center", style="text_warning"), pad=(1, 0, 1, 0)), title="[title_warning]INFO", style="warning")

    return panel

def table_data(data: Array, opt: str, searching_data=None) -> Table:
    """Tabel untuk menampilkan data."""

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)

    match opt:
        case "full_data_normal":
            table.title = "[text_title]Data pada Antrian"
            for i in range(data.size()):
                table.add_row(f"{i+1}", data._array[i])
        case "full_data_ascending":
            table.title = "[text_title]Data pada Antrian (Ascending)"
            data_ascending = sorted(sorted(data._array), key=lambda s: s.lower())
            for i in range(data.size()):
                table.add_row(f"{i+1}", data_ascending[i])
        case "full_data_descending":
            table.title = "[text_title]Data pada Antrian (Descending)"
            data_descending = sorted(sorted(data._array, reverse=True), key=lambda s: s.lower(), reverse=True)
            for i in range(data.size()):
                table.add_row(f"{i+1}", data_descending[i])
        case "searching_data":
            table.title="[text_title]Hapus Data"
            table.add_row(f"{data._array.index(searching_data)+1}", searching_data)
        case "top_data":
            table.title="[text_title]Antrian Terdepan"
            table.add_row("1", data._array[0])

    return table

def main():
    menu = {
        1: "Tambah data",
        2: "Hapus data",
        3: "Tampilkan data",
        4: "Keluar program"
    }

    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    delete_opt = {
        1: "Hapus data pertama",
        2: "Hapus data berdasarkan nama",
        3: "Hapus seluruh data",
    }

    delete_opt_str = "\n[text_default]"
    for i, k in delete_opt.items():
        delete_opt_str += f"{i}. {k}\n"

    display_opt = {
        1: "Ascending",
        2: "Descending",
        3: "Normal"
    }

    display_opt_str = "\n[text_default]"
    for i, k in display_opt.items():
        display_opt_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")
    panel_delete_opt = Panel(delete_opt_str, title="[text_title]Opsi Hapus Data", title_align="left", style="default")
    panel_searching_opt = Panel(display_opt_str, title="[text_title]Opsi Tampilan Data", title_align="left", style="default")

    while True:
        max_size = IntPrompt.ask("\n" + r"[bold]Masukkan maksimum data \[bilangan bulat di atas 0]")

        if max_size > 0:
            break

        console.print("[prompt.invalid]Harap masukkan bilangan bulat positif (lebih besar dari 0)!")

    array = Array(max_size)

    while True:
        console.clear()
        console.rule(program5.title, style="default")

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("\n[bold]Pilih Menu", choices=[str(i) for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                while True:
                    data = Prompt.ask("\n[bold]Masukkan data yang ingin ditambah")
                    if data != "":
                        break

                    console.print("[prompt.invalid]Input data tidak boleh kosong!")

                if array.full():
                    console.print(full_data_panel(data))
                    getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                else:
                    array.append(data)

                    console.print(success_panel(data, operation="addition"))
                    getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 2:
                if array.empty():
                    console.print(empty_data_panel(operation="deletion"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program5.title, style="default")

                console.print(Padding(panel_delete_opt, pad=(1, 0, 0, 0)))

                opt = IntPrompt.ask("\n[bold]Pilih opsi untuk menghapus data", choices=[str(i) for i in delete_opt.keys()])

                match opt:
                    case 1:
                        console.print(table_data(array, opt="top_data"), justify="center")
                        if Confirm.ask(f"\n[bold]Apakah anda yakin ingin menghapus data tersebut dari antrian"):
                            data = array.popleft()
                            console.print(success_panel(data, operation="deletion"))
                        else:
                            continue

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                    case 2:
                        data = Prompt.ask("\n[bold]Masukkan data yang ingin dihapus")
                        if data not in array._array:
                            console.print(not_found_data_panel(data))
                        else:
                            console.print(table_data(array, opt="searching_data", searching_data=data), justify="center")
                            if Confirm.ask(f"\n[bold]Apakah anda yakin ingin menghapus data tersebut dari antrian"):
                                array.remove(data)
                                console.print(success_panel(data, operation="deletion"))
                            else:
                                continue

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
                    case 3:
                        if Confirm.ask(f"\n[bold]Apakah anda yakin ingin menghapus seluruh data"):
                            array._array.clear()
                            console.print(success_panel(array, operation="emptying"))
                        else:
                            continue

                        getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 3:
                if array.empty():
                    console.print(empty_data_panel(operation="display_data"))
                    getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
                    continue

                console.clear()
                console.rule(program5.title, style="default")

                console.print(Padding(panel_searching_opt, pad=(1, 0, 0, 0)))

                opt = IntPrompt.ask("\n[bold]Pilih opsi untuk menampilkan data", choices=[str(i) for i in display_opt.keys()])

                match opt:
                    case 1:
                        console.print(table_data(array, opt="full_data_ascending"), justify="center")
                    case 2:
                        console.print(table_data(array, opt="full_data_descending"), justify="center")
                    case 3:
                        console.print(table_data(array, opt="full_data_normal"), justify="center")

                getpass.getpass("\nKlik 'enter' untuk melanjutkan")
            case 4:
                return program5.stop()

title = "[text_title]Program 5: Implementasi Antrian (Queue)\n" # untuk di tampilkan sebagai judul
name = "Implementasi Antrian dengan Array (2)" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 5 merupakan program implementasi struktur data Antrian dengan menggunakan Array. 
🔷 Program ini memiliki fitur untuk menambahkan, menampilkan, dan menghapus data. 
🔷 Pada menu untuk menampilkan data terdapat opsi untuk menampilkan data secara ascending ataupun descending. 
🔷 Pada menu untuk menghapus data terdapat opsi untuk data terdepan atau berdasarkan nama. 
🔷 Pada program ini maksimal data dibatasi dan dapat ditentukan oleh user.\n""" # deskripsi program

program5 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program5.start()
