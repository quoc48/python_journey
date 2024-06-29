from pathlib import Path

def read_file(path):
    """Read and display content on the screen"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"\nThe file {path} does not exit.")
        pass
    else:
        lines = contents.splitlines()
        print(f"\nThe content of file {path}:")
        for line in lines:
            print(line)


files = ['people.txt', 'dogs.txt', 'cats.txt', 'rats.txt']
for file in files:
    path = Path(file)
    read_file(path)