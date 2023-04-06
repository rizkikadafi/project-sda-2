from utils.app import *

def main():
    print("doing some task")

    if Confirm.ask("[bold]Keluar Program?"):
        return program3.stop()

title = "[bold #9ee5ff]Program 3: Title Program 3\n" # untuk di tampilkan sebagai judul
name = "Konversi Sistem Bilangan" # untuk di tampilkan di list menu
description = """[bold]
🔷.\n""" # deskripsi program

program3 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program3.start()
