from abc import ABCMeta, abstractmethod
from six import with_metaclass


class GeographicPoint(object):

    def __init__(self, coordinate_1, coordinate_2):
        self.north = coordinate_1
        self.east = coordinate_2

    @property
    def north(self):
        return self.__north

    @north.setter
    def north(self, value):
        if not 0 < value < 90:
            raise ValueError
        self.__north = str(value) + "deg N"

    @property
    def east(self):
        return self.__east

    @east.setter
    def east(self, value):
        if not 0 < value < 180:
            raise ValueError
        self.__east = str(value) + "deg E"


class MeteoStation(with_metaclass(ABCMeta)):

    def __init__(self, place, altitude):
        self.place = place
        self.altitude = altitude

    @abstractmethod
    def measure_temperature(self, temperature_value):
        pass


class MeteoStationMetric(MeteoStation):

    def measure_temperature(self, temperature_value):
        metric_temperature = str(float(temperature_value)) + "C"
        return metric_temperature


class MeteoStationImperial(MeteoStation):

    def measure_temperature(self, temperature_value):
        imperial_temperature = str((temperature_value * 9 / 5) + 32) + "F"
        return imperial_temperature


def print_measurement(station, temperature):
    print(
        station.__class__.__name__,
        "\n Location:",
        station.place.north,
        station.place.east,
        "\n Altitude:",
        station.altitude,
        "\n Temperature:",
        station.measure_temperature(temperature)
    )


point_1 = GeographicPoint(20, 30)
point_2 = GeographicPoint(42, 27)

station_1 = MeteoStationMetric(point_1, 200)
station_2 = MeteoStationImperial(point_2, 1000)

print_measurement(station_1, 25)
print_measurement(station_2, 25)
