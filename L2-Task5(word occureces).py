def count_word_occurrences(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'()[]{}')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    count_word_occurrences(file_path)