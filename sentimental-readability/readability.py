from cs50 import get_string


def count_letters(string):
    count = 0
    for i in range(len(string)):
        if string[i].isalpha():
            count += 1
    return count


def count_words(string):
    count = 1
    for i in range(len(string)):
        if string[i].isspace():
            count += 1
    return count


def count_sentences(string):
    count = 0
    for i in range(len(string)):
        if (string[i] == '.' or string[i] == '?' or string[i] == '!'):
            count += 1
    return count


def main():
    string = get_string("Text: ").lower()

    L = (count_letters(string) / count_words(string)) * 100
    S = (count_sentences(string) / count_words(string)) * 100

    index = (0.0588 * L) - (0.296 * S) - 15.8

    if index < 1:
        print("Before Grade 1")
    elif (index >= 16):
        print("Grade 16+")
    else:
        print(f"Grade {round(index)}")


main()
