# imports
import location
from haversine import haversine, Unit
import pycountry_convert as pcountry


class transportIter:
    # constructing the class Venue:
    def __init__(
        self,
        # both are venues
        destination,
        origin,
        # in hours
        # timeToGetThere,
        departureDate,
    ):
        self.destination = destination
        self.origin = origin
        self.departureDate = departureDate
        # self.timeToGetThere = timeToGetThere

    # function to calculate carbon emissions per TransportIter object
    def calculateCarbonEmissions(self, weight):
        shippingCarbonCost = 0
        # average freight ship emits 1240.2 grams of CO2 per ton-mile.
        # nautical:
        if self.checkSameContinent() == False:
            x = 0.0012402
            shippingCarbonCost = x * weight * self.calculateDistance()
        # land:
        # constant u * distance + constant w * tonnes kg
        if self.checkSameContinent() == True:
            # average freight truck in the U.S. emits 161.8 grams of CO2 per ton-mile.
            y = 0.0001618
            shippingCarbonCost = y * weight * self.calculateDistance()
        return shippingCarbonCost

    # function to check if the transportIter is in the same continent
    def checkSameContinent(self):
        originContinent = pcountry.country_alpha2_to_continent_code(
            self.origin.countryName
        )
        destinationContinent = pcountry.country_alpha2_to_continent_code(
            self.destination.countryName
        )
        if originContinent == destinationContinent:
            return True
        else:
            return False

    # function to calculate distance or nautical miles between two coordinates.
    def calculateDistance(self):
        distance = 0
        # if two locations are not in the same continent, calculate nautical miles:
        if self.checkSameContinent() == False:
            # use haversine function to calculate nautical miles with haversine(lyon, paris, unit=Unit.NAUTICAL_MILES)
            distance = haversine(
                self.origin.coordinates,
                self.destination.coordinates,
                unit=Unit.NAUTICAL_MILES,
            )
        else:
            # if two locations are in the same continent, calculate km:
            # use haversine function to calculate distance in km with haversine(lyon, paris)
            distance = haversine(
                self.origin.coordinates, self.destination.coordinates, unit=Unit.MILES
            )
        return distance

    # function to calculate shipipng cost per TransportIter object by per kilo transfered in distance
    def calculateShippingCost(self, weight):
        # if self.calculateDistance -- uses nautical miles unit -> nauticalDistance == True
        shippingCost = 0
        # Cost per ton-nautical mile $5 per ton-nm
        # nautical:
        if self.checkSameContinent() == False:
            x = 5.00
            shippingCost = x * self.calculateDistance() * weight
        # Cost per ton-mile $0.3 per ton-nm
        # land:
        if self.checkSameContinent() == True:
            y = 0.30
            shippingCost = self.calculateDistance() * y * weight
        return shippingCost


# Create objects for Transport Iters
# newYork2Berlin = transportIter(location.StorageNYC, location.VenueBerlin)
# print(newYork2Berlin.checkSameContinent())
# print(newYork2Berlin.calculateShippingCost(12.22))

# Test case 1 check list:
