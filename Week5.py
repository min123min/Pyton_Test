import datetime # SEE: https://docs.python.org/3/library/datetime.html and the extras module for details

"""
    =========== Exercise 1 =============
    Write the estimate_planks function so that it returns the correct
    number of planks (use integer division to avoid complication).

    Example:


"""
# class Contractor:
#     def __init__(self, plank_length = 1):
#         """A Demo class representing a construction Contractor.
        
#         Attributes
#         ----------
#         plank_length(int): The length of wooden planks in feet; Default: 1
        
#         Methods
#         -------
#         estimate_planks: Estimates the amount of planks needed to build a structure based on provided length.
#         """
#         self.plank_length = plank_length
    
#     def estimate_planks(self, length):
#         """Estimates the amount of planks needed to build the structure, based on the length

#         Parameters
#         ----------
#         length(int): How long the structure that needs to be built is.
#         """
#         number_of_planks = None # Just a dummy value, replace with the real calculation
#         return f"You need {number_of_planks} plank(s) of wood to build this wall"

# dave = Contractor(2)
# print(dave.estimate_planks(10)) # Should be 5 planks

# billy = Contractor(5)
# print(billy.estimate_planks(225)) # Should be 45 planks

"""
    =========== Exercise 2 =============
    Write a user class that has 3 attributes and 1 method:
        Attributes:
            1. name(str): users full name
            2. birthday(datetime.date): Users birthday as a datetime object
            3. premium (boolean): True or false based on if user is a premium user or not
        Method:
            1. next_birthday: A method that returns a string of the users birthday this year, if it is today then return 'Happy Birthday!' instead.
    
"""
class User:
    def __init__(self , name, sign_up_date, birthday, premium_member):
        self.name = name
        # self.age = age
        self.sign_up_date = sign_up_date
        self.birthday = birthday
        self.premium_member = premium_member
        
    def next_birthday(self):
        pass
        
john = User("John Doe", datetime.date(2020,10,26),datetime.date(1995,10,25), True)
# print(john.next_birthday()) # You will have to validate this yourself
print("John Doe" in john.name)  # Should print True
print(john.premium_member) # Should Print True



