import enchant

class Dictionary_():
    
    def __init__(self):
        self.dictionary = enchant.Dict("en_US")
        self.jumble_list = []
        
    def dict_checker(self, word_dictionary):
        try:
            result = self.dictionary.check(word_dictionary)
            return result
        except ValueError:
            return False

    def letter_eliminate(self, word):
        word_length = len(word)
        if word_length > 2:
            word_two_letter = word.replace(word[word_length-1],'')
            return word_two_letter
        else:
            return ''
    
    def list_updater(self, word):
        if (self.dict_checker(word)): 
            self.jumble_list.append(word)
        
    def three_letter_solver(self, u_input):
        word_length = len(u_input)
        second_letter = u_input.replace(u_input[0],'').replace(u_input[word_length-1],'')
        jumble_word = ''
        two_letter_word_ = ''
        
        for letter in u_input:
            u_input=letter+second_letter+u_input.replace(letter,'').replace(second_letter,'')
            jumble_word = u_input
            two_letter_word_ = self.letter_eliminate(jumble_word)
            self.list_updater(jumble_word)
            self.list_updater(two_letter_word_)
                
            jumble_word=letter+u_input[word_length-1]+u_input[word_length-2]
            two_letter_word_ = self.letter_eliminate(jumble_word)
            second_letter=letter
            self.list_updater(jumble_word)
            self.list_updater(two_letter_word_)
                
    def two_letter_solver(self, two_word):
        jumble_two_word = two_word
        self.list_updater(jumble_two_word)
        jumble_two_word = two_word[1] + two_word[0]
        self.list_updater(jumble_two_word)
    
    def jumble_solver(self, w_input):
        word_length = len(w_input)
        
        if word_length == 1 or word_length > 3:
            return "Please enter two or three-letter words!"
        elif word_length == 2:
            self.two_letter_solver(w_input)
            return self.jumble_list
        else:
            self.three_letter_solver(w_input)
            return self.jumble_list
            