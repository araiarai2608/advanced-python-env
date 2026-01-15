import string

with open("text.txt", "r") as f:
    lines = f.readlines()

line_count = len(lines)
word_count = 0
words_dict = {}

for line in lines:
    line = line.lower()
    for ch in string.punctuation:
        line = line.replace(ch, "")
    words = line.split()
    word_count += len(words)

    for w in words:
        if w in words_dict:
            words_dict[w] += 1
        else:
            words_dict[w] = 1

with open("analysis.txt", "w") as f:
    f.write("Total lines: " + str(line_count) + "\n")
    f.write("Total words: " + str(word_count) + "\n")
    f.write("Word frequency:\n")

    for w in words_dict:
        f.write(w + ": " + str(words_dict[w]) + "\n")
