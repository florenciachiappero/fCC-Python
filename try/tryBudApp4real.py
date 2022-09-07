class Category:
    
    def __init__(self, name):
        self.name  = name
        self.ledger = []


    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    

    def get_balance(self):
        cash = 0
        for item in self.ledger:
            cash += item['amount']
        return cash


    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.name):
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False


    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            
            total += item['amount']
        
        output = title + items + "Total: " + str(total)
        return output


    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0: 
                total += item['amount']
        return total


def main():
    food = Category("Food")
    food.deposit(900, "deposit")
    food.withdraw(105.55)
    print(food.get_balance())
    entertainment = Category("Entertainment")
    entertainment.deposit(900, "deposit")
    entertainment.withdraw(33.40)
    business = Category("Business")
    business.deposit(900, "deposit")
    business.withdraw(10.99)

    print(food)
    print(entertainment)


    print(create_spend_chart([food, entertainment, business]))



def create_spend_chart(categories):

    output = "Percentage spent by cateogry"
    x = len(categories)
    y = 100


    # Calculate total & expenses of each category
    total = 0
    expenses = []

    for item in categories:
        total += item.get_withdrawals()
    
    for item in categories:
        raw = item.get_withdrawals() / total
        expenses.append(int((raw/.1)*10))

    while y >= 0:
        output += "\n"
        output += str(y) + "| " if y == 100 else " " + str(y) + "| " if y < 100 and y > 0 else "  0| "

    #Loop through each category column and check if a bar value exists
        col = 0
        while col < x:
            if expenses[col] >= y: 
                output += "o  "
            else: output += " "*3
            col += 1
        y -= 10  

    output += "\n" + " "*4 + "-" + "-"*x*3

    name_length = 0
    for item in categories: 
        if len(item.name) > name_length: 
            name_length = len(item.name) 
    
    z = 0
    while z < name_length: 
        output += "\n" + " "*5
        for item in categories:
            try: output += item.name[z] + " "*2
            except: output += " "*3

        z += 1

    return output


if __name__ == "__main__":
    main()