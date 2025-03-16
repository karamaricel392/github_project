import random

def get_random_number(n):
    return random.randint(0, n)

def get_random_word(words):
    return words[get_random_number(len(words)-1)]

def get_random_sentence(words):
    sentence = ""
    for i in range(get_random_number(5)):
        sentence += " " + get_random_word(words)
    return sentence

def main():
    words = ["apple", "banana", "cherry"]
    print(get_random_sentence(words))

if __name__ == "__main__":
    main()
