# returns a dictionary with each word in the text and its length
def count_words(text):
    words = [''.join(char for char in word if char.isalpha()) for word in text.lower().split()]
    words_and_length = {word: len(word) for word in words}
    return words_and_length


# driver code to test the above function
some_text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

print(count_words(some_text))