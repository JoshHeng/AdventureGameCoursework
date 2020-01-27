#Importing Libraries
import random #For randomly shuffling the questions
import csv  #For reading excel file

def start(): #Function to handle the game start
    global username
    initializeVariables()
    print("Welcome to Joshua's Space Adventure Game!")
    username = input("Please enter your username: ").capitalize()

def printtext(text): #Prints a body of text, replacing all the placeholders
    text = text.replace("%playername%", username) #Replaces all the %playername% placeholders with the actual player name
    text = text.replace("%newline%", "\n") #Replaces all the %newline% placeholders with an actual new line
    text = text.replace("â€", "'") #Replaces apostrophes (which change because excel writes csv files in utf-8 and python reads csv files in ascii
    text = text.replace('â€™', "'")
    text = text.replace("|", ",") #Replaces | with commas (as using commas will break the CSV (Comma Separated Value) files
    print(text) #Prints the resulting text
    
def initializeVariables(): #Initializes all of the variables
    #Declaring everything is global so they can be read by other functions
    global questionnumber
    global questionbank
    global hitpoints
    global scenelist
    hitpoints = 100
    #Initializes the question bank list
    questionbank = []
    with open('questions.csv') as questionsfile: #Converts the questions csv file into a variable for use within the program
        questionsreader = csv.reader(questionsfile)
        rownum = 0
        for row in questionsreader:
            if rownum != 0:
                questionbank.append([row[1],row[0],row[2],row[3]])
            rownum = rownum + 1
    random.shuffle(questionbank) #Shuffles the question bank so they are in a random order
    questionnumber = 0 #Sets the questionumber to 0 so the questions start at 0
    #Initializes the scene list dictionary
    scenelist = {}
    with open('scenes.csv') as scenesfile: #Converts the scenes csv file into a variable for use within the program
        scenesreader = csv.reader(scenesfile)
        rownum = 0
        for row in scenesreader:
            if rownum != 2:
                if row[1] == "normal":
                    scenelist[row[0]] = [row[1],row[2],row[3],row[4]]
                elif row[1] == "decision":
                    if row[15] != "":
                        scenelist[row[0]]=[row[1],row[2],{row[9]:[row[10],row[11]],row[12]:[row[13],row[14]],row[15]:[row[16],row[17]]}]
                    else:
                        scenelist[row[0]]=[row[1],row[2],{row[9]:[row[10],row[11]],row[12]:[row[13],row[14]]}]
                elif row[1] == "question":
                    scenelist[row[0]] = [row[1],row[2],row[5],row[6],row[7],row[8]]
            rownum = rownum + 1
    #Scene variable example:
    #scenelist["S1"] = ["decision","You are an astronaut in space and are walking around the space station to get to your lab when you see an unidentified organism sliding along the corridor. What do you do?\nType in ‘F’ to fight or ‘H’ to hide.",{"f":["","S1A"],"h":["","S1B"]}]
    #Scene format:
        #decision - scenelist["CODE"] = ["decision","TEXT",{"ANS":["TEXT","CODE"],"ANS":["TEXT","CODE"]}]
        #question - scenelist["CODE"] = ["question","TEXT",["CORRTEXT","CORRSCENECODE","INCORRTEXT","INCORRSCENECODE","INCORRHITPOINTS?","INCORRHITPOINTS"]]
        #normal - scenelist["CODE"] = ["normal","TEXT","CODE"]
            
def main(): #The main loop for the program
    loopAAA = True #Sets a verification loop to true
    while loopAAA == True:
        start() #Calls the start function
        scenecode = "S1" #Sets the scenecode to S1
        loopAAB = True #Sets a verification loop to true
        while loopAAB == True: #This loop repeats for the whole of the game
            scenecode = scene(scenecode) #Calls the scene function
            if scenecode == "end": #If the scenecode reads 'end' then the loop will stop
                loopAAB = False
            if hitpoints == 0: #If the user runs out of hitpoints, the game will end
                print("\n\nYou lose - you ran out of hitpoints and the aliens killed you!\n")
                loopAAB = False
        loopAAC = True #Sets a verification loop to true
        while loopAAC == True:
            userinput = input("\n\n\nThere are many different endings; would you like to play again?\nType 'Y' or 'N' ").lower() #Asks the user if they would like to re-play the game
            if userinput == "y":
                print("\nRestarting game...") #If the user enters Y then the game will restart
                loopAAC = False
            elif userinput == "n":
                print("\nThank you for playing!") #If the user enters N then the game will quit
                loopAAC = False
                loopAAA = False
            else:
                print("\nUnrecognised command, please try again!") #If the user enters anything else then it will ask the question again
                loopAAC = True

def question(): #Called whenever a question is needed, returns True or False
    global questionnumber #Sets the questionnumber to global so the function can write to it
    loopBAA = True #Sets a verification loop to true
    while loopBAA == True:
        printtext(questionbank[questionnumber][1]) #Calls the printtext function to the question
        userinput = input().lower() #Gets the user's input
        if questionbank[questionnumber][0] == "number": #If the question is a number then the program will verify that the input is a number
            try: 
                userinput=float(userinput)
                if userinput == float(questionbank[questionnumber][2]):
                    print("Correct!")
                    questionnumber = questionnumber+1
                    loopBAA = False
                    return True
                else:
                    print("Incorrect - the answer was",questionbank[questionnumber][2])
                    questionnumber = questionnumber+1
                    loopBAA = False
                    return False
            except:
                print("Your number was recognised, please try again!") 
        elif questionbank[questionnumber][0] == "truefalse": #If the question is a true/false question, the program will verify that the user input is true or false
            if userinput == "true" or userinput == "t":
                loopBAA = False
                if questionbank[questionnumber][2] == "TRUE":
                    print("Correct!")
                    questionnumber = questionnumber + 1
                    return True
                elif questionbank[questionnumber][2] == "FALSE":
                    print("Incorrect - the answer was false")
                    questionnumber = questionnumber + 1
                    return False
            elif userinput == "false" or userinput == "f":
                loopBAA = False
                if questionbank[questionnumber][2] == "TRUE":
                    print("Incorrect - the answer was true")
                    questionnumber = questionnumber + 1
                    return False
                elif questionbank[questionnumber][2] == "FALSE":
                    print("Correct!")
                    questionnumber = questionnumber + 1
                    return True
            else:
                print("Your answer was not recognised. Please enter 'True' or 'False'.")
        elif questionbank[questionnumber][0] == "text": #If the question is a text question, the program will check if it is right
            if userinput == questionbank[questionnumber][2]:
                print("Correct!")
                questionnumber = questionnumber + 1
                loopBAA = False
                return True
            else:
                try:
                    if userinput == questionbank[questionnumber][3]:
                        print("Correct!")
                        questionnumber = questionnumber + 1
                        loopBAA = False
                        return True
                    else:
                        print("Incorrect - the answer was",questionbank[questionnumber][2].capitalize())
                        questionnumber = questionnumber + 1
                        loopBAA = False
                        return False
                except:
                    print("Incorrect - the answer was",questionbank[questionnumber][2].capitalize())
                    questionnumber = questionnumber + 1
                    loopBAA = False
                    return False

def scene(scenecode): #This function is called whenever a new scene is started
    global hitpoints #Declares the variable hitpoints to global so it can be written to
    loopCAA = True #Sets a verification loop to true
    print("\n\n") #Displays the top text which includes the username and amount of hitpoints
    print("Username:",username,"     -     Hit Points:",hitpoints)
    print("\n")
    while loopCAA == True:
        printtext(scenelist[scenecode][1]) #Prints the main text
        if scenelist[scenecode][0] == "decision": #If the scene is a decision the program will ask the user to input a decision
            userinput = input().lower()
            try: #Tries to do the following for the decision, but if the decision does not match a key in the dictionary in the variable then the program will loop
                printtext(scenelist[scenecode][2][userinput][0]) #Prints the decision text
                loopCAA = False
                return scenelist[scenecode][2][userinput][1] #Returns the scenecode for that decision
            except:
                print("\nYou did not enter a valid option!")
        elif scenelist[scenecode][0] == "question": #If the scene is a question then the program will call the question function
            loopCAA = False
            success = question()
            if success == True:
                printtext(scenelist[scenecode][2]) #If the question was correct then the program will print the correct text and return the correct scene
                return scenelist[scenecode][3]
            elif success == False:
                printtext(scenelist[scenecode][4]) #If the question was incorrect then the program will print the incorrect text and return the incorrect scene
                return scenelist[scenecode][5]
        elif scenelist[scenecode][0] == "normal": #If the scene is normal the program will check if hitpoints was lost from the variable, if it is the program will remove the hitpoints and inform the user of the removal
            if scenelist[scenecode][3] != "":
                print("You lost",scenelist[scenecode][3],"hit points")
                hitpoints = hitpoints - int(scenelist[scenecode][3])
            loopCAA = False
            return scenelist[scenecode][2] #Returns the scenecode for that scene
        
main() #Calls the main function
