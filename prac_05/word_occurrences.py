def main():
    text = input("Text: ")
    words = text.split()
    word_counts = count_words(words)
    print_word_counts(word_counts)

def count_words(words):
    """Count the occurrences of each word in the given list of words."""
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def print_word_counts(word_counts):
    """Print the word counts sorted alphabetically and aligned."""
    max_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:<{max_length}} : {word_counts[word]}")

main()
