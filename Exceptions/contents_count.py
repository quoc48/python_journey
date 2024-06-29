from pathlib import Path

path = Path('moby_dick.txt')
contents = path.read_text().lower()

count_number = contents.count('the')
print(f"\n{count_number} of word 'the' display in the file.")

count_number = contents.count('there')
print(f"\n{count_number} of word 'there' display in the file.")