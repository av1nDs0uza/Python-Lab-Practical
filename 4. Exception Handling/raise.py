class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 25:
            raise Exception('Coffee Too Hot ')
        elif self.__temperature < 15:
            raise ValueError('Coffee Too Cold ')
        else:
            print('Coffee Ok to Drink')

cup = CoffeeCup(int(input("Enter the temperature of the coffee:")))
cup.drink_coffee()