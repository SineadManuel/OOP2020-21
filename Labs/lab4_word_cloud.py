# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurrence of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 10px">Four score</span>')
        fo.write('<span style="font-size: 60px">and</span>')
        fo.write('<span style="font-size: 10px">seven years ago</span>')
        fo.write('<span style="font-size: 20px">our</span>')
        fo.write('<span style="font-size: 10px">fathers brought forth</span>')
        fo.write('<span style="font-size: 20px">on</span>')
        fo.write('<span style="font-size: 30px">this</span>')
        fo.write('<span style="font-size: 10px">continent</span>')
        fo.write('<span style="font-size: 70px">a</span>')
        fo.write('<span style="font-size: 20px">new</span>')
        fo.write('<span style="font-size: 10px">nation</span>')
        fo.write('<span style="font-size: 20px">conceived</span>')
        fo.write('<span style="font-size: 40px">in</span>')
        fo.write('<span style="font-size: 10px">liberty</span>')
        fo.write('<span style="font-size: 40px">dedicated</span>')
        fo.write('<span style="font-size: 80px">to</span>')
        fo.write('<span style="font-size: 90px">the</span>')
        fo.write('<span style="font-size: 10px">proposition</span>')
        fo.write('<span style="font-size: 130px">that</span>')
        fo.write('<span style="font-size: 10px">all men</span>')
        fo.write('<span style="font-size: 30px">are</span>')
        fo.write('<span style="font-size: 10px">created equal. Now</span>')
        fo.write('<span style="font-size: 80px">we</span>')
        fo.write('<span style="font-size: 10px">engaged</span>')
        fo.write('<span style="font-size: 30px">great</span>')
        fo.write('<span style="font-size: 10px">civil war testing whether</span>')
        fo.write('<span style="font-size: 40px">nation</span>')
        fo.write('<span style="font-size: 20px">or</span>')
        fo.write('<span style="font-size: 10px">any</span>')
        fo.write('<span style="font-size: 20px">so can long</span>')
        fo.write('<span style="font-size: 10px">endure.</span>')
        fo.write('<span style="font-size: 20px">We</span>')
        fo.write('<span style="font-size: 10px">met battlefield</span>')
        fo.write('<span style="font-size: 50px">of</span>')
        fo.write('<span style="font-size: 10px">war</span>')
        fo.write('<span style="font-size: 50px">have</span>')
        fo.write('<span style="font-size: 10px">come dedicate portion field as final resting-place</span>')
        fo.write('<span style="font-size: 50px">for</span>')
        fo.write('<span style="font-size: 10px">those</span>')
        fo.write('<span style="font-size: 30px">who</span>')
        fo.write('<span style="font-size: 60px">here</span>')
        fo.write('<span style="font-size: 20px">gave</span>')
        fo.write('<span style="font-size: 10px">their lives might ive.</span>')
        fo.write('<span style="font-size: 30px">It is</span>')
        fo.write('<span style="font-size: 10px">altogether fitting proper should do this. But larger sense</span>')
        fo.write('<span style="font-size: 30px">cannot</span>')
        fo.write('<span style="font-size: 10px">dedicate consecrate hallow ground.</span>')
        fo.write('<span style="font-size: 20px">The</span>')
        fo.write('<span style="font-size: 10px">brave men</span>')
        fo.write('<span style="font-size: 20px">living</span>')
        fo.write('<span style="font-size: 30px">dead</span>')
        fo.write('<span style="font-size: 10px">struggled consecrated</span>')
        fo.write('<span style="font-size: 20px">it far</span>')
        fo.write('<span style="font-size: 10px">above poor power add detract. world will little note nor '
                 'remember</span>')
        fo.write('<span style="font-size: 20px">what</span>')
        fo.write('<span style="font-size: 10px">say here but never forget</span>')
        fo.write('<span style="font-size: 30px">they</span>')
        fo.write('<span style="font-size: 10px">did here.</span>')
        fo.write('<span style="font-size: 30px">us</span>')
        fo.write('<span style="font-size: 20px">rather be</span>')
        fo.write('<span style="font-size: 10px">unfinished work which fought thus nobly advanced. task remaining '
                 'before</span>')
        fo.write('<span style="font-size: 20px">-- from these</span>')
        fo.write('<span style="font-size: 10px">honored take increased</span>')
        fo.write('<span style="font-size: 20px">devotion</span>')
        fo.write('<span style="font-size: 10px">cause last full measure highly resolve</span>')
        fo.write('<span style="font-size: 30px">shall</span>')
        fo.write('<span style="font-size: 20px">not</span>')
        fo.write('<span style="font-size: 10px">died vain under God birth freedom government</span>')
        fo.write('<span style="font-size: 20px">people</span>')
        fo.write('<span style="font-size: 10px">by perish earth</span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()

    # opens the input file gettisburg.txt
    # remember to open in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        # your code goes here:
        with open("gettisburg.txt", "r") as file:
            # Reading each line
            for line in file:

                # Reading each word
                for word in line.split():

                    # Checking for duplicate words
                    if word in my_dict:
                        my_dict[word] = my_dict[word]
                    else:
                        my_dict[word] = 1

                    self.add_to_dict(word, my_dict)

        # Display dictionary
        print(my_dict)

        return my_dict


    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurrence counter to 1
    # returns a dictionary
    def add_to_dict(self, word_in_line, the_dict):
        # your code goes here

        # Counter
        i = 0

        # Reading the words in the dictionary
        for word_in_dict in the_dict:

            # Counter i prevents comparing word_in_line to itself
            if i != len(the_dict) - 1:

                # Comaparing words to find duplicates
                if word_in_line == word_in_dict:
                    the_dict[word_in_dict] = the_dict[word_in_dict] + 1

            # Incrementing counter
            i = i + 1

        return the_dict


wc = WordCloud()
