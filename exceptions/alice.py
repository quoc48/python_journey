from pathlib import Path
import word_count as wc

filenames = ['alice.txt', 'avatar.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    wc.count_word(path)
