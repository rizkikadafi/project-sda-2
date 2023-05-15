from utils.app import *

from data_structure.queue import Queue

def full_data_panel(value) -> Panel:
    """Panel untuk menampilkan info ketika data penuh."""

    panel = Panel(Text(f"\nAntrian telah penuh! [{value}] tidak dimasukkan!\n", justify="center", style="text_warning"), title="[title_warning]INFO", style="warning")
    return panel

def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(Text(f"\n[{value}] berhasil dimasukkan ke dalam Antrian.\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
        case "deletion":
            panel = Panel(Text(f"\n[{value}] berhasil dihapus dari Antrian!\n", justify="center", style="text_success"), title="[text_success]INFO", style="success")

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

def table_data(data: Queue, opt: str) -> Table:
    """Tabel untuk menampilkan data."""

    list_data = [i for i in data._queue] 

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)
    match opt:
        case "top_data":
            table.title = "[text_title]Antrian Terdepan"

            table.add_row("1", list_data[0])
        case "all_data":
            table.title = "[text_title]Data dalam Antrian"

            for i in range(len(list_data)):
                table.add_row(f"{i+1}", list_data[i])

    return table

def main():
    menu = {
        1: "Tambah data dalam antrian",
        2: "Hapus antrian terdepan",
        3: "Hapus antrian dari tengah atau belakang",
        4: "Lihat isi antrian",
        5: "Keluar program"
    }

    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")

    while True:
        max_size = IntPrompt.ask("\n" + r"[bold]Masukkan jumlah antrian maksimal \[bilangan bulat (positif)]")
        if max_size > 0:
            break

        console.print("[prompt.invalid]Harap masukkan bilangan bulat positif (lebih besar dari 0)!")

    obj = Queue(max=max_size)

    while True:
        console.clear()
        console.rule(program1.title, style="default")

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("[bold]\nPilih menu", choices=[str(i) for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                while True:
                    data = Prompt.ask("[bold]\nMasukkan data")
                    if data == "":
                        console.print("[prompt.invalid]Input tidak boleh kosong!")
                    else:
                        break
                if obj.full():
                    console.print(full_data_panel(data))
                else:
                    obj.enqueue(data)
                    console.print(success_panel(data, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if obj.empty():
                    console.print(empty_data_panel(operation="deletion"))
                else:
                    console.print(table_data(obj, opt="top_data"), justify="center")
                    if Confirm.ask("\n[bold]Apakah anda yakin ingin menghapus data tersebut!"):
                        data = obj.dequeue()
                        console.print(success_panel(data, operation="deletion"))
                    else:
                        continue

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if obj.empty():
                    console.print("[prompt.invalid]Tidak ada data yang bisa dihapus!")
                else:
                    console.print("[prompt.invalid]Data antrian tidak bisa dihapus dari tengah ataupun belakang!")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                if obj.empty():
                    console.print(empty_data_panel(operation="display_data"))
                else:
                    console.print(table_data(obj, opt="all_data"), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                return program1.stop()

title = "[text_title]Program 1: Implementasi Queue\n" # untuk di tampilkan sebagai judul
name = "Implementasi Queue Dengan Batasan" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 1 merupakan program implementasi struktur data antrian (Queue). 
🔷 Program ini memiliki fitur untuk menambah, menghapus, dan melihat isi antrian.
🔷 Pada program ini maksimal data antrian dibatasi dan dapat ditentukan oleh user.\n""" # deskripsi program

program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
