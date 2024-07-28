#Amy Zhang
#Computer Science 20
#April 15 2024
#Madlibs Program


#import packages
import random
import syllables

#start screen
print("Hello, welcome to Amy's MadLibs Program!")
print("Today you will be choosing between two types of haikus that you can input yourself, or randomize the selection for. Let's start!")
program_continue = True

while program_continue == True:
    #select modes
    user_mode = input("Choose your mode. (Custom/Random) ")
    user_choice = input("Choose your MadLib. (Emotional Haiku/Scenic Haiku) ")

    #Custom/Self-Enter Mode
    if user_mode == "Custom":
        #Madlibs #1: Scenic Haiku
        if user_choice == "Scenic Haiku":
            #explain to user what the format for the haiku is
            print("This haiku is about a specific time, place, or setting. When entering your prompts, be as creative and expressive as you would like.")
            print("However, this haiku follows a specific format. Your first line inputs will add to 4 syllables instead of 5, as we will input a 5th 1-syllable word automatically.")
            print("Your next line inputs will also add to be one syllable less (so in this case 6) as we will input a 7th 1-syllable word automatically.")
            print("Finally, your last line will also add up to 4 syllables and the same case applies: the 5th syllable is already accounted for.")
            print("It's alright if you forget, reminders will pop up to keep you on the right track.")
            print("Alright, let's get started.")
            
            #get user input for first line
            setting = input("Enter a word that is a time of year, day, or setting. ")
            adjective1 = input("Enter an adjective about your previous response. ")
            
            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line1 = syllables.estimate(setting) + syllables.estimate(adjective1)
                
                #syllable count over limit
                if syllables_count_line1 > 4:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line1 - 4} syllables over.")
                    
                    #determine if settings or adjectives are over
                    if syllables.estimate(setting) > syllables.estimate(adjective1):
                        #calculate syllables over
                        syllables_over = syllables.estimate(setting) - (4 - syllables.estimate(adjective1))
                        print(f"You are {syllables_over} syllable(s) over. Please enter another setting with {syllables_over} less syllable(s).")
                        
                        #input again
                        setting = input("Enter a word that is a time of year, day, or setting. ")
                        
                    elif syllables.estimate(adjectives) > syllables.estimate(setting):
                        #calculate syllables over
                        syllables_over = syllables.estimate(setting) - (4 - syllables.estimate(adjective1))
                        print(f"You are {syllables_over} syllable(s) over. Please enter another adjective with {syllables_over} less syllable(s).")
                    
                        #input again
                        adjective1 = input("Enter a different adjective about your setting response. ")
                        
                    else:
                        #calculate syllables over
                        syllables_over = syllables.estimate(setting) - (4 - syllables.estimate(adjective1))
                        print(f"You are {syllables_over} syllable(s) over. Please enter two new inputs with {syllables_over} less syllable(s).")
                        
                        #input again
                        setting = input("Enter a word that is a time of year, day, or setting. ")
                        adjective1 = input("Enter an adjective about your previous response. ")
                        
                #syllable count under limit
                elif syllables_count_line1 < 4:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {4 - (syllables_count_line1)} syllables under.")
                    
                    #input again
                    setting = input("Enter a word that is a time of year, day, or setting. ")
                    adjective1 = input("Enter an adjective about your previous response. ")
                    
                #syllable count equals limit, proceed 
                else:
                    proceed_indicate = True
            
            #get user input for second line
            noun1 = input("Enter a noun. ")
            adjective2 = input("Enter an adjective. ")
            adjective3 = input("Enter a different adjective. ")
            verb1 = input("Enter a verb. ")
            
            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line2 = syllables.estimate(noun1) + syllables.estimate(adjective2) + syllables.estimate(adjective3) + syllables.estimate(verb1)
                
                if syllables_count_line2 > 6:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line2 - 6} syllable(s) over.")
                
                    if syllables_count_line2 - 6 == 1:
                        #take away extra syllable 'a'
                        remove_a = True

                    elif syllables_count_line2 - 6 > 1:
                        #input again
                        noun1 = input("Enter a noun. ")
                        adjective2 = input("Enter an adjective. ")
                        adjective3 = input("Enter a different adjective. ")
                        verb1 = input("Enter a verb. ")
                    
                elif syllables_count_line2 < 6:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {syllables_count_line2 - 6} syllables(s) under.")
                
                    #input again but just adjectives
                    adjective2 = input("Enter an adjective. ")
                    adjective3 = input("Enter a different adjective. ")
                    
                else:
                    proceed_indicate = True 
            
            #get user input for third line
            preposition1 = input("Enter a preposition (e.g. under, over, above). ")
            noun2 = input("Enter a noun. ")
            
            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line3 = syllables.estimate(preposition1) + syllables.estimate(noun2)
                
                #syllable count over limit
                if syllables_count_line1 > 4:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line3 - 4} syllables over.")
                        
                    #input again
                    preposition1 = input("Enter a preposition (e.g. under, over, above). ")
                    noun2 = input("Enter a noun. ")
                    
                #syllable count under limit
                elif syllables_count_line1 < 4:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {4 - (syllables_count_line3)} syllables under.")
                    
                    #input again
                    preposition1 = input("Enter a preposition (e.g. under, over, above). ")
                    noun2 = input("Enter a noun. ")
                    
                #syllable count equals limit, proceed 
                else:
                    proceed_indicate = True

            #print haiku
            print(f"{adjective2}, {setting}time")
            
            if remove_a == True:
                print(f"{adjective2}, {adjective3} {noun1} {verb1}")
            else:
                print(f"A {adjective2}, {adjective3} {noun1} {verb1}")
                
            print(f"{preposition1} the {noun2}")

        #Madlib #2: Emotional Haiku
        elif user_choice == "Emotional Haiku":
            #explain to user what the format for the haiku is
            print("This haiku is about a specific emotion. When entering your prompts, be as moody and creative as you would like.")
            print("However, this haiku follows a specific format.")
            print("Your inputs for the first line will add to 5 syllables, as a haiku is supposed to.")
            print("But your next inputs for the second line will add to be one syllable less (so in this case 6 syllables) as we will input a 7th 1-syllable word automatically.")
            print("Finally, your last line will also add up to 4 syllables and the same case applies: the 5th syllable is already accounted for.")
            print("It's alright if you forget, reminders will pop up to keep you on the right track.")
            print("Alright, let's get started.")

            #get user input for first line
            emotion = input("Enter an emotion. ")
            adjective1 = input("Enter an adjective about your previous response. ")

            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line1 = syllables.estimate(emotion) + syllables.estimate(adjective1)
                
                #syllable count over limit
                if syllables_count_line1 > 5:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line1 - 5} syllables over.")
                    
                    #input again
                    emotion = input("Enter an emotion. ")
                    adjective1 = input("Enter an adjective about your previous response. ")
                    
                #syllable count under limit
                elif syllables_count_line1 < 5:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {5 - (syllables_count_line1)} syllables under.")
                    
                    #input again
                    emotion = input("Enter an emotion. ")
                    adjective1 = input("Enter an adjective about your previous response. ")
                    
                #syllable count equals limit, proceed 
                else:
                    proceed_indicate = True

            #get user input for second line
            noun1 = input("Enter a one-syllable noun. ")
            adjective2 = input("Enter a two-syllable adjective. ")
            adjective3 = input("Enter a different two-syllable adjective. ")
            verb1 = input("Enter a one-syllable verb that ends in 's'. ")
            
            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line2 = syllables.estimate(noun1) + syllables.estimate(adjective2) + syllables.estimate(adjective3) + syllables.estimate(verb1)
                
                if syllables_count_line2 > 6:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line2 - 6} syllable(s) over.")
                
                    if syllables_count_line2 - 6 == 1:
                        #take away extra syllable 'a'
                        remove_a = True

                    elif syllables_count_line2 - 6 > 1:
                        #input again
                        noun1 = input("Enter a noun. ")
                        adjective2 = input("Enter an adjective. ")
                        adjective3 = input("Enter a different adjective. ")
                        verb1 = input("Enter a verb. ")
                    
                elif syllables_count_line2 < 6:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {syllables_count_line2 - 6} syllables(s) under.")
                
                    #input again but just adjectives
                    adjective2 = input("Enter an adjective. ")
                    adjective3 = input("Enter a different adjective. ")
                    
                else:
                    proceed_indicate = True

            #get user input for third line
            preposition1 = input("Enter a two-syllable preposition (e.g. under, over, above). ")
            noun2 = input("Enter a two-syllable noun. ")

            proceed_indicate = False
            
            while proceed_indicate == False:
                #compute syllables
                syllables_count_line3 = syllables.estimate(f"{preposition1} {noun2}")
                
                #syllable count over limit
                if syllables_count_line3 > 4:
                    #tell user how many syllables over
                    print(f"Too many syllables. You are {syllables_count_line3 - 4} syllables over.")
                        
                    #input again
                    preposition1 = input("Enter a preposition (e.g. under, over, above). ")
                    noun2 = input("Enter a noun. ")
                    
                #syllable count under limit
                elif syllables_count_line3 < 4:
                    #tell user how many syllables under
                    print(f"Too little syllables. You are {4 - (syllables_count_line3)} syllables under.")
                    
                    #input again
                    preposition1 = input("Enter a preposition (e.g. under, over, above). ")
                    noun2 = input("Enter a noun. ")
                    
                #syllable count equals limit, proceed 
                else:
                    proceed_indicate = True

            #print haiku
            print(f"{adjective1} {emotion}")
            print(f"A {adjective2}, {adjective3} {noun1} {verb1}")
            print(f"{preposition1} the {noun2}")
        
        else:
            #error message
            print("Sorry, I don't understand.")

    #Random Mode
    elif user_mode == "Random":
        if user_choice == "Scenic Haiku":
            #read text files
            with open("adjectives.txt", "r") as adjectives_file:
                adjectives = adjectives_file.readlines()
            with open("emotions.txt", "r") as emotions_file:
                emotions = emotions_file.readlines()
            with open("nouns.txt", "r") as nouns_file:
                nouns = nouns_file.readlines()
            with open("prepositions.txt", "r") as prepositions_file:
                prepositions = prepositions_file.readlines()
            with open("settings.txt", "r") as settings_file:
                settings = settings_file.readlines()
            with open("verbs.txt", "r") as verbs_file:
                verbs = verbs_file.readlines()
            
            #select random and replace linebreak
            setting = random.choice(settings)
            setting = setting.strip("\n")
            adjective1 = random.choice(adjectives)
            adjective1 = adjective1.strip("\n")
            noun1 = random.choice(nouns)
            noun1 = noun1.strip("\n")
            adjective2 = random.choice(adjectives)
            adjective2 = adjective2.strip("\n")
            adjective3 = random.choice(adjectives)
            adjective3 = adjective3.strip("\n")
            verb1 = random.choice(verbs)
            verb1 = verb1.strip("\n")
            preposition1 = random.choice(prepositions)
            preposition1 = preposition1.strip("\n")
            noun2 = random.choice(nouns)
            noun2 = noun2.strip("\n")

            proceed_indicate1 = False
            
            while proceed_indicate1 == False:
                #compute syllables
                syllables_count_line1 = syllables.estimate(f"{adjective1} {setting}")
                
                #determine syllables in first line
                if syllables_count_line1 == 4:
                    proceed_indicate1 = True
                    proceed_indicate2 = False 
                    
                    while proceed_indicate2 == False:
                        #compute syllables for second line
                        syllables_count_line2 = syllables.estimate(f"A {adjective2}, {adjective3} {noun1} {verb1}")
                        
                        if syllables_count_line2 == 6:
                            proceed_indicate2 = True
                            proceed_indicate3 = False
                        
                            while proceed_indicate3 == False:
                                #compute syllables for third line
                                syllables_count_line3 = syllables.estimate(f"{preposition1} the {noun2}")
                                
                                if syllables_count_line3 == 5:
                                    proceed_indicate3 = True
                        
                                else:
                                    #change noun
                                    noun2 = random.choice(nouns)
                                    noun2 = noun2.strip("\n")
 
                        else:
                            #change noun and adjectives
                            noun1 = random.choice(nouns)
                            noun1 = noun1.strip("\n")
                            adjective2 = random.choice(adjectives)
                            adjective2 = adjective2.strip("\n")
                            adjective3 = random.choice(adjectives)
                            adjective3 = adjective3.strip("\n")
                
                else:
                    #change adjective
                    adjective1 = random.choice(adjectives)
                    adjective1 = adjective1.strip("\n")
                    
            #print haiku
            print(f"{adjective1}, {setting}time")
            print(f"A {adjective2}, {adjective3} {noun1} {verb1}")
            print(f"{preposition1} the {noun2}")

        #Madlib #2: Emotional Haiku
        elif user_choice == "Emotional Haiku":
            #read text file
            with open("adjectives.txt", "r") as adjectives_file:
                adjectives = adjectives_file.readlines()
            with open("emotions.txt", "r") as emotions_file:
                emotions = emotions_file.readlines()
            with open("nouns.txt", "r") as nouns_file:
                nouns = nouns_file.readlines()
            with open("prepositions.txt", "r") as prepositions_file:
                prepositions = prepositions_file.readlines()
            with open("settings.txt", "r") as settings_file:
                settings = settings_file.readlines()
            with open("verbs.txt", "r") as verbs_file:
                verbs = verbs_file.readlines()
            
            #select random and replace linebreak
            emotion = random.choice(emotions)
            emotion = emotion.strip("\n")
            adjective1 = random.choice(adjectives)
            adjective1 = adjective1.strip("\n")
            noun1 = random.choice(nouns)
            noun1 = noun1.strip("\n")
            adjective2 = random.choice(adjectives)
            adjective2 = adjective2.strip("\n")
            adjective3 = random.choice(adjectives)
            adjective3 = adjective3.strip("\n")
            verb1 = random.choice(verbs)
            verb1 = verb1.strip("\n")
            preposition1 = random.choice(prepositions)
            preposition1 = preposition1.strip("\n")
            noun2 = random.choice(nouns)
            noun2 = noun2.strip("\n")

            proceed_indicate1 = False
            
            while proceed_indicate1 == False:
                #compute syllables
                syllables_count_line1 = syllables.estimate(f"{adjective1} {emotion}")
                
                #determine syllables in first line
                if syllables_count_line1 == 5:
                    proceed_indicate1 = True
                    proceed_indicate2 = False 
                    
                    while proceed_indicate2 == False:
                        #compute syllables for second line
                        syllables_count_line2 = syllables.estimate(f"A {adjective2}, {adjective3} {noun1} {verb1}")
                        
                        if syllables_count_line2 == 6:
                            proceed_indicate2 = True
                            proceed_indicate3 = False
                        
                            while proceed_indicate3 == False:
                                #compute syllables for third line
                                syllables_count_line3 = syllables.estimate(f"{preposition1} the {noun2}")
                                
                                if syllables_count_line3 == 5:
                                    proceed_indicate3 = True
                        
                                else:
                                    #change noun
                                    noun2 = random.choice(nouns)
                                    noun2 = noun2.strip("\n")
 
                        else:
                            #change noun and adjectives
                            noun1 = random.choice(nouns)
                            noun1 = noun1.strip("\n")
                            adjective2 = random.choice(adjectives)
                            adjective2 = adjective2.strip("\n")
                            adjective3 = random.choice(adjectives)
                            adjective3 = adjective3.strip("\n")
                
                else:
                    #change adjective
                    adjective1 = random.choice(adjectives)
                    adjective1 = adjective1.strip("\n")

            #print haiku
            print(f"{adjective1} {emotion}")
            print(f"A {adjective3}, {adjective2} {noun1} {verb1}")
            print(f"{preposition1} the {noun2}")
        
        else:
            #error message
            print("Sorry, I don't understand.")
        
    else:
        #error message
        print("Sorry, I don't understand.")

    #restart or end program
    stop_or_not = input("Restart? Yes/No ")
    if stop_or_not == "No":
            program_continue = False

print("Thank you and goodbye!")