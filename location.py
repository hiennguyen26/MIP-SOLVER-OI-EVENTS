class Location:
    # constructing the class Venue:
    def __init__(
        self,
        coordinates,
        locationName,
        countryName,
        maxStorage,
        currentlyStored={}
        # closestPort,
        # closestStorage,
    ):
        self.coordinates = coordinates
        self.locationName = locationName
        # Country name is in Alpha-2 code
        self.countryName = countryName
        self.maxStorage = maxStorage
        self.currentlyStored = currentlyStored
        # self.closestPort = closestPort
        # self.closestStorage = closestStorage
    # Get currently stored materials in storage locations:

    def getStoredCurrently(self, module):
        if module in self.currentlyStored.keys():
            return self.currentlyStored[module]
        else:
            return 0

    # # Check if inputted coordinates are correct match with city and country names of a Venue.
    # def correctCityCountryNames(coordinates, venue):
    #     # return names of
    #     checkCity = scrapeCityName(coordinates)
    #     checkCountry = scrapeCountryName(coordinates)
    #     if checkCity == venue.cityName and checkCountry == venue.countryName:
    #         return True
    #     else:
    #         return False


class Venue(Location):
    pass
    # def __init__(self, *args, **kwargs):
    # super().__init__(args, kwargs)


class Storage(Location):
    pass
    # def __init__(self, *args, **kwargs):
    # self.fixedcost = kwargs["fixedCost"]
    # self.variablecost = kwargs["variableCost"]
    # super().__init__(args, kwargs)


# Create objects for venues and storage locations
# Storage locations have the same locations as Venues
###############################################################################################
######### Storage locations #########
# Test Case 1:
# Americas Region:
StorageNYC = Storage(
    (40.698563, -73.974563),
    "New York City Storage",
    "US",
    {
        "Module1Std": 350,
        "Module2Std": 350,
        "Module3Std": 350,
        "Module4Std": 350,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 500,
        "2400x1200": 500,
        "1500x1200": 500,
        "1200x1200": 500,
        "1200x200": 500,
    },
)

# Test Case 2:
StorageLAX = Storage(
    (34.0675098791498, -118.32149178249752),
    "Los Angeles City Storage",
    "US",
    {
        "Module1Std": 350,
        "Module2Std": 350,
        "Module3Std": 350,
        "Module4Std": 350,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 500,
        "2400x1200": 500,
        "1500x1200": 500,
        "1200x1200": 500,
        "1200x200": 500,
    },
)

# Test Case 3:
StorageBuenosAires = Storage(
    (-34.590653, -58.458878),
    "Buenos Aires City Storage",
    "AR",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageSanJose = Storage(
    (9.936222, -84.106007),
    "San Jose City Storage",
    "CR",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageHouston = Storage(
    (29.768345, -95.442354),
    "Houston City Storage",
    "US",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)

# Asian regions
# Test Case 1:
StorageSingapore = Storage(
    (1.279123, 103.863048),
    "Singapore Storage",
    "SG",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageHanoi = Storage(
    (21.031438, 105.851062),
    "Hanoi Storage",
    "VN",
    {
        "Module1Std": 15000,
        "Module2Std": 15000,
        "Module3Std": 15000,
        "Module4Std": 15000,
        "Module1Raised": 15000,
        "Module2Raised": 15000,
        "Module3Raised": 15000,
        "Module4Raised": 15000,
        "5000x2400": 15000,
        "2400x1200": 15000,
        "1500x1200": 15000,
        "1200x1200": 15000,
        "1200x200": 15000,
    },
)


# Test Case 2 - 3:
StorageBali = Storage(
    (-8.734318, 115.227654),
    "Bali Storage",
    "ID",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageBangkok = Storage(
    (13.859993, 100.601819),
    "Bangkok Storage",
    "TH",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageHoChiMinh = Storage(
    (10.797693, 106.716173),
    "Ho Chi Minh City Storage",
    "VN",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageJarkata = Storage(
    (-6.218745, 106.807171),
    "Jarkarta City Storage",
    "ID",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageHongKong = Storage(
    (22.333739, 114.183593),
    "Hong Kong City Storage",
    "HK",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageManila = Storage(
    (14.587498, 120.979513),
    "Manila City Storage",
    "PH",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageBeijing = Storage(
    (39.955253, 116.315393),
    "Beijing City Storage",
    "CN",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)

# European regions:
# Test Case 3:
StorageBerlin = Storage(
    (52.476660, 13.400650),
    "Berlin Storage",
    "DE",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageParis = Storage(
    (48.846782, 2.332685),
    "Paris Storage",
    "FR",
    {
        "Module1Std": 350,
        "Module2Std": 350,
        "Module3Std": 350,
        "Module4Std": 350,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 500,
        "2400x1200": 500,
        "1500x1200": 500,
        "1200x1200": 500,
        "1200x200": 500,
    },
)
StorageRome = Storage(
    (41.901392, 12.523464),
    "Rome Storage",
    "IT",
    {
        "Module1Std": 350,
        "Module2Std": 350,
        "Module3Std": 350,
        "Module4Std": 350,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 500,
        "2400x1200": 500,
        "1500x1200": 500,
        "1200x1200": 500,
        "1200x200": 500,
    },
)
StorageHelsinki = Storage(
    (60.180055, 24.929408),
    "Helsinki Storage",
    "FI",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)

# African regions:
# Test Case 3:
StorageCapeTown = Storage(
    (-33.933744, 18.437663),
    "Cape Town Storage",
    "ZA",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageZimbabwe = Storage(
    (-17.825496, 31.0688533),
    "Harare City Storage",
    "ZW",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageVictoria = Storage(
    (-4.626477, 55.455567),
    "Victoria City Storage",
    "SC",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)
StorageDakar = Storage(
    (14.726493, -17.434382),
    "Dakar City Storage",
    "SN",
    {
        "Module1Std": 150,
        "Module2Std": 150,
        "Module3Std": 150,
        "Module4Std": 150,
        "Module1Raised": 250,
        "Module2Raised": 250,
        "Module3Raised": 250,
        "Module4Raised": 250,
        "5000x2400": 350,
        "2400x1200": 350,
        "1500x1200": 350,
        "1200x1200": 350,
        "1200x200": 350,
    },
)


# creates all the transportIters for a list of events
# Test Case 1:
StorageListCase1 = [StorageNYC, StorageHanoi, StorageSingapore]

# Test Case 2:
StorageListCase2 = [
    StorageNYC,
    StorageHanoi,
    StorageSingapore,
    StorageBali,
    StorageHoChiMinh,
    StorageBeijing,
    StorageHongKong,
    StorageManila,
    StorageJarkata,
]

# Test Case 3:
# Americas:
StorageListCase3 = [
    StorageNYC,
    StorageLAX,
    StorageSanJose,
    StorageHouston,
    # Asia:
    StorageHanoi,
    StorageSingapore,
    StorageBali,
    StorageHoChiMinh,
    StorageBeijing,
    StorageHongKong,
    StorageManila,
    StorageJarkata,
    # Europe:
    StorageBerlin,
    StorageParis,
    StorageRome,
    StorageHelsinki,
    # Africa:
    StorageCapeTown,
    StorageZimbabwe,
    StorageVictoria,
    StorageDakar,
]
###############################################################################################


# Storage locations have the same locations as Venues
# Venue Locations #######################:
# Test Case 1:
# Americas Region:
VenueNYC = Venue((40.698563, -73.974563), "New York City", "US", 0, {})

# Test Case 2:
VenueLAX = Venue((34.0675098791498, -118.32149178249752),
                 "Los Angeles City", "US", 0, {})

# Test Case 3:
VenueBuenosAires = Venue((-34.590653, -58.458878),
                         "Buenos Aires City", "AR", 0)
VenueSanJose = Venue((9.936222, -84.106007), "San Jose City", "CR", 0, {})
VenueHouston = Venue((29.768345, -95.442354), "Houston", "US", 0, {})

# Asian regions
# Test Case 1:
VenueSingapore = Venue((1.279123, 103.863048), "Singapore", "SG", 0, {})
VenueHanoi = Venue((21.031438, 105.851062), "Hanoi", "VN", 0, {})


# Test Case 2 - 3:
VenueBali = Venue((-8.734318, 115.227654), "Bali", "ID", 0, {})
VenueBangkok = Venue((13.859993, 100.601819), "Bangkok", "TH", 0, {})
VenueHoChiMinh = Venue((10.797693, 106.716173),
                       "Ho Chi Minh City", "VN", 0, {})
VenueJarkata = Venue((-6.218745, 106.807171), "Jarkarta City", "ID", 0, {})
VenueHongKong = Venue((22.333739, 114.183593), "Hong Kong City", "HK", 0, {})
VenueManila = Venue((14.587498, 120.979513), "Manila City", "PH", 0, {})
VenueBeijing = Venue((39.955253, 116.315393), "Beijing City", "CN", 0, {})

# European regions:
# Test Case 3:
VenueBerlin = Venue((52.476660, 13.400650), "Berlin", "DE", 0, {})
VenueParis = Venue((48.846782, 2.332685), "Paris", "FR", 0, {})
VenueRome = Venue((41.901392, 12.523464), "Rome", "IT", 0, {})
VenueHelsinki = Venue((60.180055, 24.929408), "Helsinki", "FI", 0, {})

# African regions:
# Test Case 3:
VenueCapeTown = Venue((-33.933744, 18.437663), "Cape Town", "ZA", 0, {})
VenueZimbabwe = Venue((-17.825496, 31.0688533), "Harare City", "ZW", 0, {})
VenueVictoria = Venue((-4.626477, 55.455567), "Victoria City", "SC", 0, {})
VenueDakar = Venue((14.726493, -17.434382), "Dakar City", "SN", 0, {})
