## 
#  This application keeps track of the household chores completed in a shared
#  house over a number of weeks.
#
#  Author: Rae Harbird
#  Date: December 2019

from household_module import Household
from chores_list_module import ChoresList, Chore
from participants_list_module import Participants

## Constants used for validation

MENU_CHOICES = ['A', 'C', 'V', 'L', 'S', 'Q']

## Prints the menu for the application. 
#
def print_menu():
    menu_string = ("\n\nWelcome to Chore Chart:\n\n"
                 "\tAbout \t\t\t(A)\n"
                 "\tCreate Household \t(C)\n"
                 "\tView Household \t\t(V)\n"
                 "\tLog Chores Done \t(L)\n"
                 "\tShow Leaderboard \t(S) \n"
                 "\tQuit \t\t\t(Q)")
    print(menu_string)


## Prints a description of the application. 
#
#
def about() :
    about_string = ("\n\nWelcome to Chore Chart. "
                   "Chore Chart helps housemates (people sharing a house) "
                   "to keep a record of what needs doing every week and "
                   "who is doing it. The leaderboard shows who has earned "
                   "the most points for household tasks so far\n")
    print(about_string)


##  Creates a new household using the information entered by the user.
#   @param all_households a list of household objects
#
#
def create_household(all_households,participants_each_household,chores_each_household,household_text_file) :
    new_household_name = get_household_name()
    found = False
    household_obj = household_exists(new_household_name, all_households)
    
    if  household_obj == None:
        members_set = get_participants_names(new_household_name,participants_each_household)
        chores_set = get_chores(new_household_name,chores_each_household)
        household_obj = Household(new_household_name, members_set, chores_set)
        all_households.append(new_household_name)
        household_text_file.write(("{}, {}, ").format(household_obj, len(participants_each_household[new_household_name])))
        for member_of in range(len(participants_each_household[new_household_name])):
            household_text_file.write(("{}, ").format(participants_each_household[new_household_name][member_of]))
        household_text_file.write(("{0:.1g}, ").format(len(chores_each_household[new_household_name])/2))
        chores_in = 0
        while chores_in < len(chores_each_household[new_household_name]) - 1:
            household_text_file.write(("{}, ").format(chores_each_household[new_household_name][chores_in]))
            chores_in += 1
        household_text_file.write(("{} \n").format(chores_each_household[new_household_name][chores_in]))
        print(all_households)
    else:
       print("Household {} already exists, returning to the menu."
              .format(new_household_name))
        
    return 

##  Checks whether a household with a given name exists in the list of households.
#
#   @param all_households a list of household objects
#   @param household_name the household name to check
#   @return the household object if the household exists and None if it does not.
#
#
def household_exists(new_household_name, all_households) :
    h_obj = None

    for household in all_households :
        if household == new_household_name :
            h_obj = household

    return h_obj
        

##  Prompts the user for a household name and checks that the name is
#   reasonable.
#   @return a string containing the household name.
#
#   Invariants: a household name must be between the minimum and maximum length
#               and cannot be blank. The name must contain only alphanumeric
#               characters. 
#           
def get_household_name() :
    
    household_name = ""
    valid = False
    
    while not valid:
        household_name = input("\n\tEnter household name: ")
        try:
            Household.is_valid_name(household_name)
            valid = True
        except ValueError as err:
            print(err)

    return household_name


##  Prompts the user for the chore frequency and validates the number.
#   @return the chore frequency.
#
#   Invariants: the frequency must be between the minimum and maximum frequency.
#
def get_chore_frequency() :

    valid = False
    chore_frequency = 0
    
    
    while not valid :
        chore_frequency = input("\n\t\tTimes per week: ")
        try :
            Chore.is_valid_frequency(chore_frequency)
            valid = True
        except (TypeError, ValueError) as err:
            print(err)

    return int(chore_frequency)


##  Gets the names for the people in the household and stores them in a set
#
#   Invariants: duplicate names are not allowed
#
#   @return a set containing the names.
#
def get_participants_names(new_household_name,participants_each_household):
    household_names = set()
    participants_each_household[new_household_name] = []
    
    name = "AAA"    # dummy value so that we can start the while loop
    
    number_of_people = 1
    while name != "" :
        name = get_person_name(number_of_people)
 
        if name == "" :
            try :
                Participants.is_valid_length(household_names)
            except ValueError as err:
                print(err)
                name = "AAA"
        else:
            current_length = len(household_names)
            household_names.add(name)
            participants_each_household[new_household_name].append(name)
            if current_length < len(household_names) :
                number_of_people = number_of_people + 1
            else:
                print(("\n\t\tSorry, you already have a household member called {}, " + \
                      "try again.").format(name))       
        
    return household_names


##  Prompts the user for a person's name and validates it.
#   @param participant_number the number of participants entered so far.
#   @return a string containing the person's name.
#
#   Invariants: a person's name must be between the minimum and maximum length
#               and cannot be blank. The name must contain 
#               alphanumeric characters.
#
def get_person_name(participant_number) :
    
    # Finish when we have a valid answer which is either a blank or a valid name
    finish = False
    
    while not finish :
        person_name = input("\n\tEnter the name of participant {}: " \
                                    .format(participant_number)).strip()
        if is_blank(person_name) :
            finish = True
        else :
            try :
                participant_list_validation = []
                participant_list_validation.append(person_name)
                Participants.is_valid_naming(participant_list_validation)
                finish = True
            except ValueError as err:
                print(err)
                
    return person_name


##  Gets the chores.
#
#   Invariants: duplicate chore names are not allowed,
#               names must consist of words which are alphanumeric characters,
#               names must >= the minimum valid length,
#               names must be <= the maximum valid length,
#               chore frequency must be >= the minimum frequency,
#               chore frequency must be <= the maximum frequency
#
#   @return a list containing chore objects.
#
def get_chores(new_household_name,chores_each_household):

    chores_list = set()
    chores_each_household[new_household_name] = []
    new_chore = "AAA"    # dummy value so that we can start the while loop
    number_of_chores = 0

    while new_chore != "" :
        new_chore = get_chore(number_of_chores + 1)
        if new_chore == "" :
            try :
                ChoresList.is_valid_length(chores_list)
            except ValueError as err:
                print(err)
                new_chore = "AAA"
        else:
            try :
                ChoresList.is_unique(new_chore, chores_list)
                chore_frequency = get_chore_frequency()
                chore_obj = Chore(new_chore, chore_frequency)
                chores_list.add(chore_obj)
                chores_each_household[new_household_name].append(new_chore)
                chores_each_household[new_household_name].append(chore_frequency)
                number_of_chores = number_of_chores + 1
                
            except ValueError as err :
                print(err)

    return chores_list 


##  Prompts the user for a chore name and validates it.
#   @param chore_number the number of chores entered so far.
#   @return a string containing the chore name.
#
#   Invariants: a chore name must be between the minimum and maximum length
#               and cannot be blank. The name must be composed of alphanumeric characters.
#
def get_chore(chore_number) :
    
    # A valid answer is either a blank or a valid name
    valid_answer = False
    
    while not valid_answer :

        chore_name = input("\n\tEnter the name of chore {}: ".format(chore_number))

        if chore_name == "" :
            valid_answer = True
        else : 
            try :
                Chore.is_valid_chore_name(chore_name)
                valid_answer = True
            except ValueError as err :
                print(err)
                
    return chore_name


##  Validates the option choice.
#
#   @return True or False
#
#   Invariants: The option must be a valid choice from MENU_CHOICES
#
def is_valid_option(option):
    if is_blank(option):
        return False
    elif option[0].upper() in MENU_CHOICES:
        return True
    else:
        return False

##  Checks whether a string contains only whitespace
#
#   @param any_string a string
#   @return True or False
#
#
def is_blank(any_string):
    test_str = "".join(any_string.split())
    if len(test_str) == 0:
        return True
    else :
        return False


##  View household.
# @param all_households, a list of household objects
#
def view_household(all_households,participants_each_household,chores_each_household):

    which_household_view = get_household_name()
    household_exist_check = household_exists(which_household_view, all_households)

    if household_exist_check == None:
        print("\n\tThis household does not exist\n\t")
        print(all_households)
        view_household(all_households,participants_each_household,chores_each_household)
    else:
        print(("\n\t{}").format(which_household_view))
        print("\nParticipants:")
        members_list = participants_each_household[which_household_view]
        for member_number in range(len(members_list)):
            print(("\n\t{}. \t{}").format(member_number + 1, members_list[member_number]))
        print("\nWeekly Chores:")
        chores_and_frequencies = chores_each_household[which_household_view]
        number_for_chore = 0
        for chore_number in range(0,len(chores_and_frequencies),2):
            number_for_chore += 1
            print(("\n\t{}. \t{} ({})").format(number_for_chore, chores_and_frequencies[chore_number],chores_and_frequencies[chore_number + 1]))
        
            
    return    


##  Log chores.
# @param all_households, a list of household objects
#
def log_chores(all_households):
    
    print("Not implemented yet.")
        
    return    


##  Show the leaderboard for a house.
# @param all_households, a list of household objects
#
def show_leaderboard(all_households):
    print("Not implemented yet.")

    return 


    
##  Prints the menu, prompts the user for an option and validates the option.
#
#   @return a character representing the option.
#
def get_option():  
    option = '*'
    
    while is_valid_option(option) == False:
        print_menu()
        option = input("\nEnter an option: ")
   
    return option.upper()

# in the below function, the text file is opened for reading and split into its individual lines and each line into its words
# the commas at the end of each word are then removed so that each word/number can be validated correctly
# each word is then added to the text_file_line list to allow the validation tests to call indiviual words
def check_text_file(all_households,participants_each_household,chores_each_household):
    household_text_file = open("Households.txt","r")
    if household_text_file.mode == "r":
        contents = household_text_file.readlines()
        line_count = 0
        for line in contents:
            line_count += 1
            word_count = 0
            words_in_line = line.split()
            text_file_line = []
            for word in words_in_line:
                word_count += 1
                word_new = word.replace(',',"")
                text_file_line.append(word_new)
            text_file_household_name_validation(text_file_line,all_households,participants_each_household,chores_each_household)

# the first word of each line will be the household name, hence the 0th element of the text_file_line lost will be the household
# the test then checks whether the household is an appropriate name before appending it to the all_households list
def text_file_household_name_validation(text_file_line,all_households,participants_each_household,chores_each_household):
    try:
        Household.is_valid_name(text_file_line[0])
        valid = True
        all_households.append(text_file_line[0])
        text_file_participants_validation(text_file_line,all_households,participants_each_household,chores_each_household)
    except ValueError as err:
        print(err)
        print(("\n\nPlease correct the '{}' Household name the text file, first Quit the application").format(text_file_line[0]))
    
# if the household name was valid, the below function is called
# the first element of the text_file_line list is the number of participants
# this determines how many times the below for loop will be run.
# the first household participant name will always be the second element, so the for loop begins here
# for the stated number of participants in the first element, the for loop will add each of these paricipants to the
# household_names set and the dictionary, which are then used for validation
# the variable 'i' is a counter variable, which will keep track of what element number of the text_file_line we are validating

def text_file_participants_validation(text_file_line,all_households,participants_each_household,chores_each_household):
    number_of_members = int(text_file_line[1])
    household_names = set()
    participants_each_household[text_file_line[0]] = []
    i = 2
    for household_member in range(2,number_of_members + 2):
        i+=1
        household_names.add(text_file_line[household_member])
        participants_each_household[text_file_line[0]].append(text_file_line[household_member])
    try :
        Participants.is_valid_length(household_names)
        Participants.is_valid_naming(participants_each_household[text_file_line[0]])
    except ValueError as err:
        print(err)
        print(("\n\nPlease correct this on the '{}' Household in the text file, first Quit the application").format(text_file_line[0]))

    text_file_chores_validation(text_file_line,all_households,participants_each_household,chores_each_household,i,household_names)

# the value of 'i' will now be such that the ith element of the text_file_line list will be the elemtn containing the number of chores
# since we want to validate the chore and its frequency, we multiply the value of this element by two, this will give us the number of
# elements left in the text_file_line that needs to be validated.
def text_file_chores_validation(text_file_line,all_households,participants_each_household,chores_each_household,i,household_names):
    number_chores_and_frequencies = int(int((text_file_line[i])) * 2)
    chores_list = set()
    chores_each_household[text_file_line[0]] = []
    # j is another counter variable which, in the below for loop, will isolate the chore frequencies will i isolates the corresponding
    # chore
    j = i + 2
    for household_chore in range(i + 1, number_chores_and_frequencies + i + 1, 2):
        chores_each_household[text_file_line[0]].append(text_file_line[household_chore])
        chore_frequency = text_file_line[j]
        try :
            Chore.is_valid_frequency(chore_frequency)
            ChoresList.is_unique(text_file_line[household_chore], chores_list)
            chores_object = Chore(text_file_line[household_chore], chore_frequency)
            chores_list.add(chores_object)
            chores_each_household[text_file_line[0]].append(text_file_line[j])
            valid = True
        except (TypeError, ValueError) as err:
            print(err)
            print(("\n\tPlease correct the '{}' on the '{}' Household on the text file, first Quit the application").format(chore_frequency, text_file_line[0]))
        j += 2
    try :
        ChoresList.is_valid_length(chores_list)        
    except ValueError as err:
        print(err)
        
    household_object = Household(text_file_line[0], household_names, chores_list)
    
    

## The menu is displayed until the user quits
# 
def main() :
    
    all_households = []   
    option = '*'
    participants_each_household = {}
    chores_each_household = {}
    # the following household is for the purpose of creating a file of there isn't already one so that
    #the check_text_file function has a file to just read and run validation tests on
    household_text_file = open("Households.txt","a+")
    household_text_file.close()
    check_text_file(all_households,participants_each_household,chores_each_household)
    household_text_file.close()
    # now the file is opened so that it can be edited
    household_text_file = open("Households.txt","a+")
    
    while option != 'Q':
        option = get_option()        
        if option == 'A':
            about()
        elif option == 'C':
            create_household(all_households,participants_each_household,chores_each_household,household_text_file)
        elif option == 'V':
            view_household(all_households,participants_each_household,chores_each_household)
        elif option == 'L':
            log_chores(all_households)
        elif option == 'S':
            show_leaderboard(all_households)
            # print("\n\tNot implemented yet.\n")

    print("\n\nBye, bye.")

        
# Start the program
if __name__ == "__main__":
    main()
