from pathlib import Path

path = Path('programing.txt')
contents = "I love programming!\n"
contents += "I love create new game.\n"
contents += "I also love to work with data."

path.write_text(contents)