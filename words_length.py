# return a list of lengths for the sentence provided
def words_length(sentence):
    return list(len(word) for word in sentence.split())
