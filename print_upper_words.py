def print_upper_words(str):
    """For a list of words, print out each word on a separate line, but in all uppercase."""

    for word in str:
        print(word.upper())

def print_upper_e_words(str):
    """Only prints words that start with the letter ‘e’ (either upper or lowercase)."""

    for word in str:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_starts(str, starts_with):
    """Pass in a set of letters, and it only prints words that start with one of those letters."""

    for word in str:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break