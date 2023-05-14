from utils.app import *

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

def table_data(data, opt: str) -> Table:
    """Tabel untuk menampilkan data."""

    table = Table(style="default")
    table.add_column("[text_title]No.", style="text_default", justify="center")
    table.add_column("[text_title]Data", style="text_default", min_width=20)
    match opt:
        case "top_data":
            table.title = "[text_title]Antrian Terdepan"

            table.add_row("1", data[0])
        case "all_data":
            table.title = "[text_title]Data dalam Antrian"

            for i in range(len(data)):
                table.add_row(f"{i+1}", data[i])

    return table

def main():
    menu = {
        1: "Tambah data ke antrian (enqueue)",
        2: "Hapus data terdepan dari antrian (dequeue)",
        3: "Tampilkan antrian",
        4: "Tampilkan panjang antrian",
        5: "Keluar Program"
    }

    menu_str = "\n[text_default]"
    for i, k in menu.items():
        menu_str += f"{i}. {k}\n"

    panel_menu = Panel(menu_str, title="[text_title]Menu Program", title_align="left", style="default")
    
    queue = []
    while True:
        console.clear()
        console.rule(program3.title, style="default")

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

                queue.append(data)
                console.print(success_panel(data, operation="addition"))

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 2:
                if len(queue) == 0:
                    console.print(empty_data_panel(operation="deletion"))
                else:
                    console.print(table_data(queue, opt="top_data"), justify="center")
                    if Confirm.ask("\n[bold]Apakah anda yakin ingin menghapus data tersebut!"):
                        data = queue.pop(0)
                        console.print(success_panel(data, operation="deletion"))
                    else:
                        continue

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 3:
                if len(queue) == 0:
                    console.print(empty_data_panel(operation="display_data"))
                else:
                    console.print(table_data(queue, opt="all_data"), justify="center")

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 4:
                panel_length_queue = Panel(Text(f"\nPanjang dari Antrian adalah {len(queue)}\n", justify="center", style="text_success"), title="[title_success]INFO", style="success")
                console.print(panel_length_queue)

                getpass.getpass("\nKlik 'Enter' untuk melanjutkan")
            case 5:
                return program3.stop()

title = "[text_title]Program 3: Implementasi Antrian (Queue)\n" # untuk di tampilkan sebagai judul
name = "Implementasi Antrian dengan Array" # untuk di tampilkan di list menu
description = """[text_default]
🔷 Program 3 merupakan program implementasi struktur data Antrian (Queue) dengan menggunakan array. 
🔷 Program ini memiliki fitur untuk menambahkan, menghapus, dan menampilkan data serta dapat melihat panjang dari antrian. 
🔷 Pada program ini maksimal data tidak dibatasi.\n""" # deskripsi program

program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()
