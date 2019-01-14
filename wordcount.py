# put your code here.
def count_words(filename):
    """
    Count the number of words separated by commas and output on screen
    """
    word_dict = {}
    word_list = []
    the_file = open(filename)
    for line in the_file:
        line = line.rstrip()
        word_list = word_list + line.split(" ")
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    for word in word_dict:
        print(word, word_dict[word])

count_words("twain.txt")