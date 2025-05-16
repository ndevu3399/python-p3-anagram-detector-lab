# your code goes here!
class Anagram:
    """
    This class is used to find anagrams of a given word.
    """
    def __init__(self, word):
        """
        Initializes the Anagram object with the word to find anagrams for.

        Args:
            word (str): The word for which anagrams will be searched.
        """
        self.word = word.lower()  # Store the word in lowercase
        self.sorted_word = sorted(self.word) # Pre-sort for efficiency

    def match(self, possible_anagrams):
        """
        Finds all anagrams of the word from a list of possible anagrams.

        Args:
            possible_anagrams (list): A list of words to check for being anagrams.

        Returns:
            list: A list of all anagrams of the word from the input list.
                   Returns an empty list if no anagrams are found.
        """
        anagrams = []
        for candidate in possible_anagrams:
            candidate_lower = candidate.lower() #store in lowercase
            #check the candidate is not the same as the word, and that the sorted versions match
            if candidate_lower != self.word and sorted(candidate_lower) == self.sorted_word:
                anagrams.append(candidate)
        return anagrams
        
if __name__ == '__main__':
    #example usage
    anagram_instance = Anagram("listen")
    result = anagram_instance.match(['enlists', 'google', 'inlets', 'banana', 'Listen', 'Listen'])
    print(result)  # Output: ['inlets']
    
    anagram_instance = Anagram("Listen")
    result = anagram_instance.match(['enlists', 'google', 'inlets', 'banana', 'Listen', 'listen'])
    print(result) # Output: ['enlists', 'inlets', 'listen']
