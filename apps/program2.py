from utils.app import *

from data_structure.queue import DQueue

def success_panel(value, operation: str) -> Panel:
    """Panel untuk menampilkan info ketika operasi tertentu berhasil dilakukan."""

    panel = Panel("None")
    match operation:
        case "addition":
            panel = Panel(Text(f"\n[{value}] telah dimasukkan ke Antrian.\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
        case "deletion":
            panel = Panel(Text(f"\n[{value}] telah keluar dari Antrian!\n", justify="center", style="text_success"), title="[text_success]INFO", style="success")

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

def table_data(data: DQueue, opt: str) -> Table:
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
        1: "Masukkan Data ke Antrian",
        2: "Hapus Data dari Antrian Terdepan",
        3: "Cek Antrian",
        4: "Banyak Data pada Antrian",
        5: "Keluar Program"
    }

    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")

    q = DQueue()

    while True:
        console.clear()
        console.rule(program2.title, style="default")

        console.print(Padding(panel_menu, pad=(1, 0, 0, 0)))

        opt = IntPrompt.ask("[bold]\nPilih menu", choices=[str(i) for i in menu.keys()])

        import getpass
        match opt:
            case 1:
                while True:
                    obj = Prompt.ask("[bold]\nMasukkan data yang ingin anda tambahkan")
                    if obj == "":
                        console.print("[prompt.invalid]Input tidak boleh kosong!")
                    else:
                        break

                q.enqueue(obj)
                console.print(success_panel(obj, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if q.empty():
                    console.print(empty_data_panel(operation="deletion"))
                else:
                    console.print(table_data(q, opt="top_data"), justify="center")
                    if Confirm.ask("\n[bold]Apakah anda yakin ingin menghapus data tersebut!"):
                        temp = q.dequeue()
                        console.print(success_panel(temp, operation="deletion"))
                    else:
                        continue

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if q.empty():
                    console.print(empty_data_panel(operation="display_data"))
                else:
                    console.print(table_data(q, opt="all_data"), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                panel_length_queue = Panel(Text(f"\nPanjang dari Queue adalah {q.size()}\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
                console.print(panel_length_queue)

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                return program2.stop()

title = "[text_title]Program 2: Implementasi Queue\n" # untuk di tampilkan sebagai judul
name = "Implementasi Queue Tanpa Batasan" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 2 merupakan program Implementasi struktur data Antrian (Queue). 
🔷 Program ini memiliki fitur untuk menambahkan, menghapus, dan menampilkan isi antrian. 
🔷 Pada program ini maksimal data pada antrian tidak dibatasi.\n""" # deskripsi program

program2 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program2.start()
