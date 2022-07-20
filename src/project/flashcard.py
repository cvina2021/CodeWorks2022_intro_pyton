import random
#define the class
class Flashcard:
#define the class variables
    flashcards = []

#define the init function
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        self.flashcards.append(self)

#define the methods
    def toString(self):
        return self.word + " : " + self.definition

    def flash(self):
        qNum = random.randint(0, len(self.flashcards) -1)
        ans = input("What is " + self.flashcards[qNum].word + "?")
        if ans == self.flashcards[qNum].definition:
            print("Correct")
        else:
            print("Wrong")

    def get_all(self):
        for x in self.flashcards:
            print(x.toString())

#create 4 instance of this class and test all the methods
f1 = Flashcard("2+1", "3")
f1 = Flashcard("2+2", "4")
f1 = Flashcard("2+3", "5")
f1 = Flashcard("2+4", "6")
f1.flash()
f1.flash()
f1.get_all()

f2 = Flashcard("noun", "person, place, or thing")
f2 = Flashcard("two kinds of verb", "action and linking verb")
f2.flash()
f2.get_all()
