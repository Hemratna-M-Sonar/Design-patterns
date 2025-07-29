from abc import ABC, abstractmethod
 
class Burger(ABC):
    @abstractmethod 
    def prepare(self):
        pass
class BasicBurger(Burger):
    def prepare(self):
        print("Created a basic burger")
class StandardBurger(Burger):
    def prepare(self):
        print("Created a standard burger")
class PremiumBurger(Burger):
    def prepare(self):
        print("Created a premium burger")
class BasicWheatBurger(Burger):
    def prepare(self):
        print("Created a basic wheat burger")
class StandardWheatBurger(Burger):
    def prepare(self):
        print("Created a standard wheat burger")
class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Created a premium wheat burger")
 
 
class GarlicBread(ABC):
    @abstractmethod
    def prepare(self):
        pass
 
class BasicGarlicBread(Burger):
    def prepare(self):
        print("Created a basic garlic bread")
class CheeseGarlicBread(Burger):
    def prepare(self):
        print("Created a cheese garlic bread")
class BasicWheatGarlicBread(Burger):
    def prepare(self):
        print("Created a basic wheat garlic bread")
class CheeseWheatGarlicBread(Burger):
    def prepare(self):
        print("Created a cheese wheat garlic bread")
 
 
class Factory(ABC):
    @abstractmethod
    def createBurger(self):
        pass
    @abstractmethod
    def createGarlicBread(self):
        pass
class Singh(Factory):
    def createBurger(self, type):
        if type=="basic":
            return BasicBurger()
        elif type == "standard":
            return StandardBurger()
        elif type == "premium":
            return PremiumBurger()
        else:
            print("Invalid type")
            return
    def createGarlicBread(self, type):
        if type=="basic":
            return BasicGarlicBread()
        elif type == "cheese":
            return CheeseGarlicBread()
        else:
            print("Invalid type")
            return
class King(Factory):
    def createBurger(self, type):
        if type=="basic":
            return BasicWheatBurger()
        elif type == "standard":
            return StandardWheatBurger()
        elif type == "premium":
            return PremiumWheatBurger()
        else:
            print("Invalid type")
            return
    def createGarlicBread(self, type):
        if type=="basic":
            return BasicWheatGarlicBread()
        elif type == "cheese":
            return CheeseWheatGarlicBread()
        else:
            print("Invalid type")
            return
 
 
def main():
    burgerType = "basic"
    garlicBreadType = "cheese"
    factory:Factory = King()
    burger:Burger = factory.createBurger(burgerType)
    garlicbread:GarlicBread = factory.createGarlicBread(garlicBreadType)
    burger.prepare()
    garlicbread.prepare()
main()