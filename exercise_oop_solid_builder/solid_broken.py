# interface segregation
class Kitchen(object):
    def bake(self, product, time):
        print("{} baked for {} minutes".format(product, time))

    def fry(self):
        pass

    def boil(self):
        pass

    def mix(self, product, time):
        print("{} mixed for {} minutes".format(product, time))

    def cut(self):
        pass

    def flavour(self):
        pass

    def clean_kitchen(self):
        pass

    def supply_fridge(self):
        pass


class CakeShop(object):

    def __init__(self):
        # dependency inversion
        self.kitchen = Kitchen()
        self.baking_time_overall = 0

    def mix(self, flower, time):
        self.kitchen.mix(flower, time)

    def bake(self, cake, time):
        self.kitchen.bake(cake, time)
        self.baking_time_overall += time

    # open closed
    # single responsibility

    def oven_utilization(self):
        pass

    def save_statistics(self):
        pass


class CakeShopLocal(CakeShop):
    """
    This CakeShop has no baking. Cake arrives already done.
    """
    # liskow substitution
    def bake(self):
        return 0


shop = CakeShop()
shop.mix("flower type 500", 10)
shop.bake("cake1", 45)
shop.bake("cake2", 40)
shop.bake("cake3", 35)
print(shop.baking_time_overall)
