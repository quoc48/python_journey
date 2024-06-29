from pathlib import Path

def count_word(path):
    """Count the approximate number of words in a files."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        add_missing_file(path)
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

def add_missing_file(path):
    missing_files = Path('missing_files.txt')
    existing_content = missing_files.read_text().splitlines()
    unique_lines = set(existing_content)
    content = str(path)
    if content not in unique_lines:
        with missing_files.open(mode='a') as file:
            file.write(content + '\n')