class hamburger:

    # constructor for a normal hamburger
    def __init__(self):
        self.Bread_roll_type = 'French Torpedo Roll'
        self.Meat_type = 'Beef'
        self.Base_Hamburger_Price = 200

    #     Additional Toppings
    def Additional_toppings(self):
        Avaliable_toppings = ['lettuce', 'Tomato', 'Carrot', 'Pickels']
        for number, i in enumerate(Avaliable_toppings):
            print(f'Avalaiable Toppings Are \n{number} : {i}')
        Number_of_topings = int(input('How many toppings you want to add in your Burger : '))
        for j in range(0, Number_of_topings, 1):
            Tooping_name = int(input('enter the number of toping from above: '))
            if Tooping_name <= len(Avaliable_toppings):
                print(f'{Avaliable_toppings[Tooping_name]} is added ')
                self.Base_Hamburger_Price += 20
            else:
                print('We donot offer that one toping ')
        print(f'Total Bill is {self.Base_Hamburger_Price}')

    def Total_Price(self):
        return self.Base_Hamburger_Price


class Healthy_Burgers(hamburger):
    def __init__(self):
        self.Bread_roll_type = 'Brown rye bread roll'
        self.Base_Hamburger_Price = 300
        self.Meat_type = 'Wagyu'

    def Additional_toppings(self):
        Avaliable_toppings = ['lettuce', 'Tomato', 'Carrot', 'Pickels', 'Mashrooms', 'Anchovies']
        print(f'Avalaiable Toppings Are')
        for number, i in enumerate(Avaliable_toppings):
            print(f'{number + 1} : {i}')
        Number_of_topings = int(input('How many toppings you want to add in your Burger : '))
        for j in range(0, Number_of_topings, 1):
            Tooping_name = int(input('enter the number of toping from above: '))
            if Tooping_name <= len(Avaliable_toppings):
                print(f'{Avaliable_toppings[Tooping_name]} is added ')
                if Avaliable_toppings[Tooping_name] == 'Mashrooms' or Avaliable_toppings[Tooping_name] == 'Anchovies':
                    print(f' Price for Mashromms and Anchovies is 50 rupess per topping : ')
                    self.Base_Hamburger_Price += 50
                else:
                    self.Base_Hamburger_Price += 20
            else:
                print('We donot offer that one toping ')
        print(f'Total Bill is {self.Base_Hamburger_Price}')

    def Total_Price(self):
        return self.Base_Hamburger_Price


class Delux_Hamburger(hamburger):
    def __init__(self):
        self.Bread_roll_type = 'French Torpedo Roll'
        self.Meat_type = 'Beef'
        self.Base_Hamburger_Price = 350
        self.Chips = 'Chips'
        self.Cold_drinks = 'Cold_drinks'

    def Total_Price(self):
        return self.Base_Hamburger_Price


def runing():
    print('''HI WELCOME TO BILL's BURGERS \nWHAT WOULD YOU LIKE  ''')
    print("WE OFFER -----> ")
    offers = ['hamburgers', 'Delux_hamburger', "Healthy_Burgers"]
    for number, item in enumerate(offers):
        print(f'{number + 1} : {item}')
    selections = int(input("What would you like Just press the button: "))
    if selections <= len(offers):
        #        creating an object
        name = input("Enter your name: ")
        if selections == 1:
            name = hamburger()
            choice = input('Would you want to add some additional toopings on your burger : Y/N ').lower()
            if choice == 'y':
                name.Additional_toppings()
            else:
                print(f'your total bill is {name.Total_Price()}')
        if selections == 2:
            name = Delux_Hamburger()
            print(f'your total bill is {name.Total_Price()}')
        if selections == 3:
            name = Healthy_Burgers()
            choice = input('Would you want to add some additional toopings on your burger : Y/N ').lower()
            if choice == 'y':
                name.Additional_toppings()
            else:
                print(f'your total bill is {name.Total_Price()}')


if __name__ == "__main__":
    runing()
