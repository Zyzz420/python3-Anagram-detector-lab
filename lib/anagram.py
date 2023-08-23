# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        anagrams = []
        for word in word_list:
            if self.is_anagram(word):
                anagrams.append(word)
        return anagrams

    def is_anagram(self, other_word):
        other_word = other_word.lower()
        return sorted(self.word) == sorted(other_word)