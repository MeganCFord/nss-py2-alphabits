
class Alphabits:
    '''
    This app asks the user to type the alphabet in order, one letter at a time. It error handles if the input is incorrect, and exits when the whole alphabet is completed correctly.

    Arguments: none

    Methods: print_intro, start_turn, return_list, add_char, list_length
    '''
    def __init__(self):
        self.alphabet_to_check_against = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.user_alphabet = []

    def print_intro(self):
        '''
        prints the intro string.
        Arguments: none
        '''
        print("CAN YOU TYPE THE ALPHABET IN ORDER?")

    def start_turn(self):
        '''
        checks to make sure the game is not over by checking the alphabet_to_check_against length against the user_alphabet length. if the lengths are equal, this function congratulates the user and ends the game.

        Arguments: none
        '''
        if len(self.user_alphabet) < len(self.alphabet_to_check_against):
            self.add_char()
        elif len(self.user_alphabet) == len(self.alphabet_to_check_against):
            print("Congratulations, you typed the whole alphabet!\nGoodbye!")

    def return_list(self):
        '''
        prints the current list of correctly entered letters as a string joined from user_alphabet. runs inside add_char if the '?' character is typed.
        Arguments: none
        '''
        print("you've gotten as far as " + ", ".join(self.user_alphabet) + "...")

    def add_char(self):
        '''
        checks the user input to see if they've entered the correct character. if she hasn't, ask for input again, and if she has, add the character to the end of the user_alphabet list and start the next turn.
        Arguments: none
        '''
        char_to_add = input("what's the next letter? >").lower()
        index_to_check = self.list_length()

        print("you typed " + char_to_add + ".")

        if len(char_to_add) > 1:
            print("NOPE! Please type just one letter!")
            self.add_char()
        elif char_to_add == '?':
            # this character will print the current user list.
            self.return_list()
            self.add_char()
        elif char_to_add not in self.alphabet_to_check_against:
            print("NOPE! Please type a letter!")
            self.add_char()
            # here is where the correctness of the character is checked, by comparing the length of the current alphabet to the index of the entered character.
        elif self.alphabet_to_check_against.index(char_to_add) > index_to_check:
            print("NOPE! Wrong letter! you've guessed too far forward in the alphabet.")
            self.add_char()
        elif self.alphabet_to_check_against.index(char_to_add) < index_to_check:
            print("NOPE! Duplicate letter!")
            self.add_char()
        else:
            print("YEP! Good job!")
            self.user_alphabet.append(char_to_add)
            self.start_turn()

    def list_length(self):
        '''
        returns the length of the current user_alphabet list. Used as part of add_char to see if the correct character was entered.
        Arguments: none
        '''
        return len(self.user_alphabet)

if __name__ == '__main__':
    app = Alphabits()
    app.print_intro()
    app.start_turn()
