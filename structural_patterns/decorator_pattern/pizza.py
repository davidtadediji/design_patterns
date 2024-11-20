

class Pizza:

    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class CheeseDecorator(Pizza):

    cheese_cost = 50

    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_description(), pizza.get_cost())
        self.pizza = pizza

    def get_description(self):
        return f"{self.pizza.get_description()} with cheese"

    def get_cost(self):
        return self.pizza.get_cost() + self.cheese_cost


class PepperoniDecorator(Pizza):
    pepperoni_cost = 40

    def __init__(self, pizza: Pizza):
        super().__init__(pizza.get_description(), pizza.get_cost())
        self.pizza = pizza

    def get_description(self):
        return f"{self.pizza.get_description()} and pepperoni"

    def get_cost(self):
        return self.pizza.get_cost() + self.pepperoni_cost



plain_pizza = Pizza("Plain Pizza", 150)
cheese_pizza = CheeseDecorator(plain_pizza)
pepperoni_cheese_pizza = PepperoniDecorator(cheese_pizza)

print(pepperoni_cheese_pizza.get_description())  # Output: Plain Pizza, Cheese, Pepperoni
print(pepperoni_cheese_pizza.get_cost())
