import sys
sys.path.append("apps")

from apps.utils.load import Load
from apps import program1, program2, program3, program4, program5

title = "[text_title]Project SDA 2[/]"
description = """[text_default]
[italic]Project SDA 2[/], merupakan project mata kuliah [italic]Struktur Data dan Algoritma[/] yang berisi program-program implementasi struktur data [italic]Antrian (Queue)[/] dan [italic]Senarai Berantai (Linked List)[/].
"""

programs = Load(title=title, description=description)
programs.add([program1, program2, program3, program4, program5])

if __name__ == "__main__":
    programs.run()
