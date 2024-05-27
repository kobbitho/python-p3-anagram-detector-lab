# your code goes here!

class Anagram: #Anagram class to find words that are anagrams of a given word.

  def __init__(self, word): #initialize the anagram with a given word
    self.letters = sorted(list(word.lower()))  

  def match(self, words):
    matches = []
    for word in words:
      if sorted(list(word.lower())) == self.letters:  
        matches.append(word)
    return matches


