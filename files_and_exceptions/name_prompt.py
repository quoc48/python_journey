from pathlib import Path

path = Path('guest.txt')

# Write the file
attempt = 1
names = ''
while attempt <= 5:
    name = input("Enter your name: ")
    names += (name + "\n")
    attempt += 1
path.write_text(names)

# Read the file and print out
print("\n--- Names inputted ---")
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)