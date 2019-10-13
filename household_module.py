from participants_list_module import Participants
from chores_list_module import ChoresList, Chore

class Household() :

    ## Constants used for validation
    MINIMUM_NAME_LENGTH = 3     # Used to validate household name 
    MAXIMUM_NAME_LENGTH = 10

    MINIMUM_HOUSEHOLD_SIZE = 2  # Used to validate the number of people in
                                # a household.  
    MAXIMUM_HOUSEHOLD_SIZE = 5
    
    MINIMUM_CHORES_DONE = 1     # Used to validate the number of chores done
    MAXIMUM_CHORES_DONE = 50


    ## Constructor for the Household class. Initialises all the
    # attributes including the chore log. 
    #  
    # @param the_household_name a string containing the household name
    # @param the_participants a Participants object containing
    #        a set of the participants' names
    # @param the_chores a ChoresList object containing a set of chores
    #
    def __init__(self, the_household_name, the_participants, the_chores) :
        self.household_name = the_household_name
        self.participants = the_participants
        self.chores = the_chores
        self.chore_log = {}   # This will still call the setter for the chore log

       
    ## Return the household_name.
    #          
    @property
    def household_name(self):
        return self._household_name


    ## Sets the household name attribute.
    #  @param name the household name        
    @household_name.setter
    def household_name(self, name) :
        try:
            self.is_valid_name(name)
            self._household_name = name
        except ValueError as err :
            raise
 
                               
    ## Return the participant names.
    # Note: The participants attribute is a Participants object.
    #       Use the Participants class to create this object.
    # 
    @property
    def participants(self):
        return self._participants


    ## Sets the participant names.
    #  @param names a Participants object which is a set of the team names       
    @participants.setter
    def participants(self, the_participants) :
        self._participants = Participants(the_participants)
 
        
    ## Return the chores.
    # 
    @property
    def chores(self):
        return self._chores


    ## Sets the chores.
    #  @param the_chores a ChoreList object      
    @chores.setter
    def chores(self, the_chores) :
        try :
            self._chores = ChoresList(the_chores)
        except (ValueError, TypeError) as err :
            raise

    ## Return the chore log.
    # 
    @property
    def chore_log(self):
        return self._chore_log


    ## Setter for the dictionary containing the log of tasks done.
    #  key : partcipant's name,
    #  value :  dictionary containing the chore name and the number of times completed.
    #  @param the_chore_log an empty dictionary       
    @chore_log.setter
    def chore_log(self, the_chore_log) :
        self._chore_log = Household.initialise_log(self.participants.participants, \
                                                  self.chores.chores)


    def __str__(self):
        return self.household_name
    

    ## Generate a string representation of the chore log.
    #
    #  @return a string containting the information in the chore log
    def chore_log_string(self) :
        chore_log_string = "TO BE COMPLETED"
            
        return chore_log_string


    ## Update the chore log.
    #   @param name a string containing the name of the participant.
    #   @param chore  a string containing the name of the chore.
    #   @param number_completed the number to add on to the existing total.
    #
    # The format of the chore log is:
    # 
    # {"fred" : {"chore1": 0, "chore2": 0}, walt : {"chore1": 0, "chore2": 0}}
    #
    def update_log(self, name, chore, number_completed ) :
        return
        
    ## Check the name contains only characters from the alphabet and check that it is the right length.
    # 
    # @param name the string to be validated
    # @return True if the string conforms to the validation conditions, raise ValueError if
    #         it does not.
    #
    @staticmethod
    def is_valid_name(name) :
        h_name_length = len(name)
        if (h_name_length < Household.MINIMUM_NAME_LENGTH) or (h_name_length > Household.MAXIMUM_NAME_LENGTH):
            raise ValueError("The length of the name must be at least 3 characters and a maximum of 10 characters long")
        else:
            for i in name:
                if not i.isalnum():
                    raise ValueError("Your household name should be alphanumeric")    
        return True


    @staticmethod
    def initialise_log(the_participants, the_chores) :
 
        # Create a dictionary where the keys are the participant names
        # and the values are another dictionary containing all the chore names
        # as keys and the number of times completed as values.
        #
        # Example:
        # 
        # {"fred" : {"chore1": 0, "chore2": 0}, walt : {"chore1": 0, "chore2": 0}}
        
        household_log = {}

        return household_log
            

## main method
#
# Contains some simple tests
#
def main():
    print("\nTest 1: Create a valid household")    
    try:
        h = Household("House1", {"personA","personB","personC"},
                      {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
        print("\n\tVALID: ", h)
    except Exception as err:
        print("\tERROR: ", err)

    print("\nTest 2: Create a household with an invalid name 'a'")    
    try:
        h = Household("a", {"personA","personB","personC"}, {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
        print("\n\tVALID: ", 2)
    except Exception as err:
        print("\tERROR: ", err)

    print("\nTest 3: Create a household with an invalid name '***'")    
    try:
        h = Household("***", {"personA","personB","personC"}, {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
        print("\n\tVALID: ", h)
    except Exception as err:
        print("\tERROR: ", err)

    print("\nTest 4: Create a household with an invalid name 12*'a'")    
    try:
        h = Household(12*"a", {"personA","personB","personC"}, {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
                      
        print("\n\tVALID: ", h)
    except Exception as err:
        print("\tERROR: ", err)

    print("\nTest 5: Create a household with an invalid name ' '")    
    try:
        h = Household(" ", {"personA","personB","personC"}, {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
        print("\n\tVALID: ", h)
    except Exception as err:
        print("\tERROR: ", err)
    
    print("\nTest 6: Update the log for a participant (valid)")    
    try:
        h = Household("House1", {"personA","personB","personC"},
                      {Chore("wash up", 4), Chore("vacuum stairs", 2), Chore("dusting",1),
                       Chore("empty bin", 2)})
        h.update_log("personA", "wash up", 49)
        print("\n\tVALID: ", h)
    except Exception as err:
        print("\tERROR: ", err)


if __name__ == "__main__":
    main()
    
