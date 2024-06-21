'''Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

Task 1: Define Budget Category Class - Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.'''

class BudgetCategory:
    '''Constructor and private attributes'''
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getters and setters for category name and budget
    
    def get_budget(self):
        return self.__allocated_budget
    
    def set_budget(self, new_budget):
        '''This Method will set a new budget for the chosen category'''
        self.__allocated_budget = new_budget


    def add_expense(self, amount):
        '''This method will add an expense to the category'''
        if amount > 0 and amount <= self.get_budget():
            self.set_budget(self.get_budget() - amount)
            print(f"You have added an expense to your budget. You now have a total of ${self.get_budget()}")
        elif amount > self.get_budget():
            print(f"This will exceed your budget of ${self.get_budget()}")
       
        

    def display_category_summary(self):
        '''Method to display the budget category details'''
        print(f"The current category is: {self.__category_name} and the allotted budget is ${self.get_budget()}")
        

# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()