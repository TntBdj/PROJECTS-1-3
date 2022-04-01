def Story1():
    print (f"When {Name} went out {Verbing1} they found the most {Adj1} {Noun1}. Unfortunately, the {Noun1} turned into {Num} {Nouns1} and everyone decided to start {Verbing2}. It was extremely {Adj2} for everyone what saw.") 

def Story2():
    print (f"What an {Adj1} day today. It was about {Num} degree’s outside and the {Noun1} was {Verbing1}. With this temperature, of course {Name} would be {Verbing2} outside. They are an absolute menace to society.")

def Story3():
    print (f"Did you hear? {Name} actually got a girl’s number. Not only one, but about {Num} girls liked when they saw him {Verbing1}. Its so unlikely because he is {Adj1} and so {Adj2}. Maybe if I saw him {Verbing1} i’d give him my number. ")

while True:
    Story = input("What story do you want to write? (1), (2), (3), or (q) to quit: " )
    if Story == "1" or Story == "2" or Story == "3":
        Adj1 = input("First adjective: ")
        Adj2 = input("Second adjective: ")
        Noun1 = input("Enter noun: ")
        Nouns1 = input("plural noun: ")
        Name = input("Enter name: ")
        Verbing1 = input("Verb ending in ing: ")
        Verbing2 = input("Verb ending in ing: ")
        Num = input("Enter a number: ")
    if Story == "1":
        Story1()
    elif Story == "2":
        Story2()
    elif Story == "3":
        Story3()
    elif Story == "q":
        print ("Thank you for playing. See you next time!")
        break
    else:
        print("Input invalid.")
