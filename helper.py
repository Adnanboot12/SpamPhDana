import random

def read_words_from_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def random_word():
    words = read_words_from_file("Data/words.txt")
    if not words:
        print("Error: No words found in the file.")
        return ""

    return random.choice(words)

def random_phone_number():
    # Menghasilkan nomor telepon acak dengan 10 digit
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

def random_single_number():
    return str(random.randint(0, 9))
