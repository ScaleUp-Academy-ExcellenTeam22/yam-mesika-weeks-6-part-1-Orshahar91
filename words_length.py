def words_length(sentence):
    """
    :param str sentence: Sentence string.
    :return: list of lengths for the sentence provided
    """
    return list(len(word) for word in sentence.split())
