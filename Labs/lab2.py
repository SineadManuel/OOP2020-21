#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your name: ")
        print("Originally entered: " + message)


        # Enter your own print statements below:
        print("\nHello " + message + "!")


        # print only first and last of the sentence:
        print("\nFirst character: " + message[0])
        print("Last character: " + message[-1])


        # use slice notation:
        print("\nSlice notation: " + message[1:4:2])


        # escaping a character:
        print("\nEscape characters: He said \"That\'s fantastic!\"")


        # find all a's in the input word and count how many there are:
        print("\nFind 'a': ")
        print(message.find('a'))
        print("\nCount 'a': ")
        print(message.count('a'))


        # replace all occurences of the character a with the - sign
        print("\nReplace 'a' with '-':")

        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print(message.replace('a', '-'))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out:
        my_list = (list(message.split(" ")))
        print("\nSentence in list format:")
        print(my_list)


        # append a new element to the list and print:
        my_list.append("Sinead")
        print("\nAppended list:")
        print(my_list)


        # remove from the list in 3 ways:
        print("\nRemoving last element - Way 1:")
        del my_list[-1]
        print(my_list)

        #print("\nRemoving last element - Way 2:")
        #my_list.remove()
        #print(my_list)

        #print("\nRemoving last element - Way 3:")
        #my_list.pop()
        #print(my_list)


        # print the list 3 times by using multiplication:
        print("\nPrinting the list 3 times:")
        print(my_list * 3)


        # reverse the items in the list and print:
        print("\nReversed list:")
        my_list.reverse()
        print(my_list)


        # reverse the list with the slicing trick:
        print("\nReversed list (slicing trick):")
        my_list = my_list[::-1]
        print(my_list)


        # check if the word cake is in your input list:
        print("\nCake is in this sentence:")
        print("cake" in my_list)



tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
