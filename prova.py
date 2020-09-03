# This method breaks up text into words for us
def break_words(sentence):
    words = sentence.split(" ")
    return words

print(break_words("lola is vrery hot"))