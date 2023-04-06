from utils.app import *

def main():
    print("doing some task")

    if Confirm.ask("[bold]Keluar Program?"):
        return program4.stop()

title = "[bold #9ee5ff]Program 4: Title Program 4\n" # untuk di tampilkan sebagai judul
name = "Konversi Sistem Bilangan" # untuk di tampilkan di list menu
description = """[bold]
🔷.\n""" # deskripsi program

program4 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program4.start()
