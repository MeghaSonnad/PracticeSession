class WordLengthPrint:
    def __init__(self,words):
        self.words=words
    
    def word_lengths(self):
        word_list=self.words.split()
        word_length=[[word.upper(),len(word)]for word in word_list]
        for pair in word_length:
            print(pair,end=' ')

wordPrint=WordLengthPrint("the quick brown fox jumps over the lazy dog")
wordPrint.word_lengths()

