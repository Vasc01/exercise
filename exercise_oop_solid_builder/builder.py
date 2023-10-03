class CarExtras(object):
    def __init__(self):
        self.wheels = ()
        self.color = ()
        self.engine = ()

    def price_list(self):
        return "Extra - Price\n{} - {}\n{} - {}\n{} - {}".format(self.wheels[0], self.wheels[1],
                                                                 self.color[0], self.color[1],
                                                                 self.engine[0], self.engine[1])


class CarExtrasBuilder(object):
    def __init__(self):
        self.car = CarExtras()

    def set_wheels(self, kind, price):
        self.car.wheels = (kind, price)
        return self

    def set_color(self, kind, price):
        self.car.color = (kind, price)
        return self

    def set_engine(self, kind, price):
        self.car.engine = (kind, price)
        return self

    def build(self):
        return self.car


new_car_extras = (CarExtrasBuilder()
                  .set_wheels("alloy wheels", 1500)
                  .set_color("white color", 0)
                  .set_engine("engine with start-stop system", 500)
                  .build()
                  )
print(new_car_extras.price_list())
