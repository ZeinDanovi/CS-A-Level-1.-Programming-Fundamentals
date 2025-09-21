import random 


def chooses_the_word():
    wordlist = ["banana","apple","orange","grape","melon","kiwi","mango","pear","plum","peach","eheheh,","hegawheag","hgeghega","hbjdshedf"]  #list of words
    chosenword = wordlist[random.randint(1,len(wordlist) - 1 )]   
    return chosenword
chosenword = chooses_the_word() 

def make_hidden_array():
    hiddenarray = []
    for i in range(1,len(chosenword) + 1 ):
        hiddenarray.append(chosenword[i-1])
    return hiddenarray

hiddenarray = make_hidden_array() #array of the randomly selected word 
print(hiddenarray)

#creates a starting array the length of the chosen word that is just underscores
def starting_array(input): 
    start = []
    for i in range(1,len(input) + 1 ):
        start.append("_")
    return start

start = starting_array(chosenword) #starting array of underscores 

def letter_checker(letter):
    for i in range(1,len(chosenword) + 1):
        if letter == hiddenarray[i-1]:
            start[i-1] = hiddenarray[i-1]
    return start


attempts = 3
for i in range(1,4):
    test = input("enter letter")
    currentposition = start
    if currentposition != letter_checker(test):
        attempts = attempts - 1 
        print(attempts)
    print(letter_checker(test))
    
    





