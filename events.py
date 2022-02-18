from enum import Enum
from transportIter import transportIter
import location
import datetime
from datetime import date
import module
from datetime import timedelta


class TypeEvent(Enum):
    FullPerformance = 1
    Business = 2
    Entertainment = 3
    LiveMarkets = 4


class Events:
    # init constructor
    def __init__(
        self,
        eventName,
        typeEvent,
        Venue,
        sizeEvent,
        # dateHost,
        yearsSigned,
        dateSigned,
        requiredEventObjects,
    ):
        # enum: LiveMarkets, Entertainment, or Business
        self.eventName = eventName
        self.typeEvent = typeEvent
        self.Venue = Venue
        self.sizeEvent = sizeEvent
        # self.dateHost = dateHost
        self.yearsSigned = yearsSigned
        self.dateSigned = dateSigned
        # enum: Stages, Startup Booth, Meeting Area, VIP Area, ...
        self.requiredEventObjects = requiredEventObjects
        self.netCarbon = 0  # updated after the transportation has finished

    def moduleGetter(self):
        modules = {}
        for product in self.requiredEventObjects.keys():
            for m in module.ProductCart[product].keys():
                if m in modules.keys():
                    modules[m] += (
                        module.ProductCart[product][m]
                        * self.requiredEventObjects[product]
                    )

                else:
                    modules[m] = (
                        module.ProductCart[product][m]
                        * self.requiredEventObjects[product]
                    )
        return modules


# #################### Test Cases for Events ##################### #:
# Europe regions:

# Test Case 3:
# Paris Full Performance Event with Pavilions and Business with focus in exhibition for startups and 3 stages
# Pavilions || Business: 2 Stages, Exhibition: 120 seed startups, 48 SME, 20 Corprates (10 Auto, 10 Tech), 20 Hangout Huts and 5 TriangularBillBoard
eventParis = Events(
    "Paris",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueParis,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 1, 5),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 20,
        "SMEBooth": 12,
        "CorporateBoothTech": 10,
        "CorporateBoothAuto": 10,
        "TriangularBillBoard": 5,
        "HangoutHut": 20,
    },
)

# Rome very small lux Business conference and some exhibition and mainly area to meeting
eventRome = Events(
    "Rome",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueRome,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 1, 25),
    requiredEventObjects={
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 20,
        "SMEBooth": 10,
        "CorporateBoothTech": 2,
        "CorporateBoothAuto": 2,
        "TriangularBillBoard": 5,
        "HangoutHut": 20,
    },
)

eventBerlin = Events(
    "Berlin",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueBerlin,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 2, 12),
    requiredEventObjects={
        "MainStage": 1,
        "360Stage": 1,
        "StartupBooth": 20,
        "SMEBooth": 15,
        "CorporateBoothTech": 5,
        "CorporateBoothAuto": 2,
        "TriangularBillBoard": 10,
        "HangoutHut": 30,
    },
)

eventHelsinki = Events(
    "Helsinki",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueHelsinki,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 2, 23),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 50,
        "SMEBooth": 12,
        "CorporateBoothTech": 30,
        "CorporateBoothAuto": 30,
        "TriangularBillBoard": 5,
        "HangoutHut": 50,
    },
)


# Asia regions:
# Full Performance Events ######:
# Test Case 1
# Hanoi Full Performance Event with Pavilions and Business with focus in exhibiton for startups
# Pavilions || Business: 2 Stages, Exhibition: 200 seed startups, 20 SME, 5 Corprates (2 Auto, 3 Tech), 15 Hangout Huts and 10 TriangularBillBoard
eventHanoi = Events(
    "Hanoi",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueHanoi,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2021, 3, 1),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 1,
        "360Stage": 1,
        "StartupBooth": 25,
        "SMEBooth": 5,
        "CorporateBoothTech": 3,
        "CorporateBoothAuto": 2,
        "TriangularBillBoard": 10,
        "HangoutHut": 15,
    },
)

# Singapore Full Performance Event with Pavilions and Business with focus in exhibition for startups and 3 stages
# Pavilions || Business: 3 Stages, Exhibition: 40 seed startups, 40 SME, 50 Corprates (25 Auto, 25 Tech), 50 Hangout Huts and 20 TriangularBillBoard
eventSingapore = Events(
    "Singapore",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueSingapore,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2021, 3, 18),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 8,
        "SMEBooth": 10,
        "CorporateBoothTech": 25,
        "CorporateBoothAuto": 25,
        "TriangularBillBoard": 20,
        "HangoutHut": 50,
    },
)

# Test Case 2
# Bali Full Performance Event with Pavilions and Entertainment with focus in 3 stages and some exhibition
eventBali = Events(
    "Bali",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueBali,
    sizeEvent=15000,
    yearsSigned=5,
    dateSigned=date(2020, 3, 29),
    requiredEventObjects={
        "MainStage": 2,
        "360Stage": 1,
        "TriangularBillBoard": 20,
        "HangoutHut": 50,
    },
)

# Ho Chi Minh City Full Performance Event with Pavilions and Entertainment with focus in 3 stages and some exhibition
eventHCMC = Events(
    "Ho Chi Minh",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueHoChiMinh,
    sizeEvent=15000,
    yearsSigned=5,
    dateSigned=date(2020, 4, 4),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 1,
        "360Stage": 1,
        "StartupBooth": 25,
        "SMEBooth": 5,
        "CorporateBoothTech": 3,
        "CorporateBoothAuto": 2,
        "TriangularBillBoard": 10,
        "HangoutHut": 15,
    },
)

# Bali Full Performance Event with Pavilions and Entertainment with focus in 3 stages and some exhibition
eventThaiLand = Events(
    "Bangkok",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueBangkok,
    sizeEvent=15000,
    yearsSigned=5,
    dateSigned=date(2020, 4, 13),
    requiredEventObjects={
        "MainStage": 1,
        "360Stage": 1,
        "StartupBooth": 20,
        "SMEBooth": 15,
        "CorporateBoothTech": 5,
        "CorporateBoothAuto": 2,
        "TriangularBillBoard": 10,
        "HangoutHut": 30,
    },
)

eventJarkatar = Events(
    "Jarkatar",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueJarkata,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 4, 25),
    requiredEventObjects={"10Pavilions": 1, "MainStage": 3},
)

eventHongKong = Events(
    "Hong Kong",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueHongKong,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 5, 3),
    requiredEventObjects={"10Pavilions": 1, "MainStage": 3},
)

eventManila = Events(
    "Manila",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueManila,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 5, 12),
    requiredEventObjects={
        "MainStage": 3,
        "360Stage": 1,
        "StartupBooth": 10,
        "TriangularBillBoard": 50,
        "HangoutHut": 50,
    },
)

eventBeijing = Events(
    "Beijing",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueBeijing,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 5, 25),
    requiredEventObjects={
        "MainStage": 3,
        "360Stage": 1,
        "StartupBooth": 50,
        "SMEBooth": 25,
        "CorporateBoothTech": 50,
        "CorporateBoothAuto": 50,
        "TriangularBillBoard": 10,
        "HangoutHut": 50,
    },
)


# Americas regions:
# Full Performance Events ######:
# Test Case 1
# NYC Full Performance Event with Pavilions and Business with focus in exhibition for startups and 3 stages
# Pavilions || Business: 3 Stages, Exhibition: 320 seed startups, 80 SME, 50 Corprates (25 Auto, 25 Tech), 50 Hangout Huts and 20 TriangularBillBoard
eventNYC = Events(
    "New York",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueNYC,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2021, 6, 13),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 40,
        "SMEBooth": 20,
        "CorporateBoothTech": 25,
        "CorporateBoothAuto": 25,
        "TriangularBillBoard": 20,
        "HangoutHut": 50,
    },
)

# Test Case 2
eventLA = Events(
    "Los Angeles",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueLAX,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 6, 28),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 50,
        "SMEBooth": 35,
        "CorporateBoothTech": 25,
        "CorporateBoothAuto": 25,
        "TriangularBillBoard": 20,
        "HangoutHut": 50,
    },
)

# Test Case 3
eventHouston = Events(
    "Houston",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueHouston,
    sizeEvent=3500,
    yearsSigned=5,
    dateSigned=date(2020, 7, 13),
    requiredEventObjects={
        "MainStage": 1,
        "360Stage": 1,
        "StartupBooth": 10,
        "SMEBooth": 25,
        "CorporateBoothTech": 15,
        "CorporateBoothAuto": 9,
        "TriangularBillBoard": 10,
        "HangoutHut": 15,
    },
)

eventSanHose = Events(
    "San Jose",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueSanJose,
    sizeEvent=1000,
    yearsSigned=5,
    dateSigned=date(2020, 7, 26),
    requiredEventObjects={
        "MainStage": 3,
        "360Stage": 1,
        "TriangularBillBoard": 50,
        "HangoutHut": 50,
    },
)

eventBuenosAires = Events(
    "Buenos Aires",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueBuenosAires,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 8, 5),
    requiredEventObjects={
        "MainStage": 2,
        "360Stage": 2,
        "TriangularBillBoard": 50,
        "HangoutHut": 100,
    },
)

# African regions:
eventCapeTown = Events(
    "CapeTown",
    typeEvent=TypeEvent.Business,
    Venue=location.VenueCapeTown,
    sizeEvent=10000,
    yearsSigned=5,
    dateSigned=date(2020, 8, 17),
    requiredEventObjects={
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 20,
        "SMEBooth": 5,
        "CorporateBoothTech": 3,
        "CorporateBoothAuto": 6,
        "TriangularBillBoard": 10,
        "HangoutHut": 55,
    },
)

eventZimbabwe = Events(
    "Harare",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueZimbabwe,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 10, 12),
    requiredEventObjects={
        "MainStage": 5,
        "360Stage": 2,
        "TriangularBillBoard": 50,
        "HangoutHut": 120,
    },
)

eventSeychelles = Events(
    "Victoria",
    typeEvent=TypeEvent.FullPerformance,
    Venue=location.VenueVictoria,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 10, 28),
    requiredEventObjects={
        "10Pavilions": 1,
        "MainStage": 2,
        "360Stage": 1,
        "StartupBooth": 8,
        "SMEBooth": 10,
        "CorporateBoothTech": 25,
        "CorporateBoothAuto": 25,
        "TriangularBillBoard": 20,
        "HangoutHut": 50,
    },
)

eventSenegal = Events(
    "Dakar",
    typeEvent=TypeEvent.Entertainment,
    Venue=location.VenueDakar,
    sizeEvent=20000,
    yearsSigned=5,
    dateSigned=date(2020, 11, 5),
    requiredEventObjects={
        "MainStage": 1,
        "360Stage": 3,
        "TriangularBillBoard": 50,
        "HangoutHut": 150,
    },
)


# print(module.moduleGetter(eventEurope))


# creates all the transportIters for a list of events
# Test Case 1:
EventsListCase1 = [eventNYC, eventHanoi, eventSingapore]

# Test Case 2:
EventsListCase2 = [
    eventNYC,
    eventHanoi,
    eventSingapore,
    eventBali,
    eventHCMC,
    eventBeijing,
    eventHongKong,
    eventManila,
    eventJarkatar,
]

# Test Case 3:
# Americas:
EventsListCase3 = [
    eventNYC,
    eventLA,
    eventSanHose,
    eventHouston,
    # Asia:
    eventHanoi,
    eventSingapore,
    eventBali,
    eventHCMC,
    eventBeijing,
    eventHongKong,
    eventManila,
    eventJarkatar,
    # Europe:
    eventBerlin,
    eventParis,
    eventRome,
    eventHelsinki,
    # Africa:
    eventCapeTown,
    eventZimbabwe,
    eventSeychelles,
    eventSenegal,
]

# create all transportIters for all events in a list
# endDate & timeDelta could be implemented to


def createTransportIters(listEvents, listStorage, listOfTimeSteps, currentDate):
    listTransportIter = []
    for event in listEvents:
        dates = generateEventDates(event, currentDate)
        for d in dates:
            d = fitInTimeSteps(d, listOfTimeSteps)
            for storages in listStorage:
                if storages.Venue.locationName != event.Venue.locationName:
                    iter = transportIter(event.Venue, storages.Venue, d)
                    listTransportIter.append(iter)
    return listTransportIter


# Generate event instances of an event
def generateEventDates(event, currentDate):
    eventDates = []
    for i in range(event.yearsSigned):
        thisDate = event.dateSigned + timedelta(weeks=52 * i)
        # print(thisDate)
        if thisDate < currentDate:
            continue
        else:
            eventDates.append(thisDate)
    return eventDates

# Check to see if date fits in a timestep in the list of timesteps. EG: flooring the timestep.


def fitInTimeSteps(date, listOfTimeSteps):
    for i in range(len((listOfTimeSteps)) - 1):
        if date < listOfTimeSteps[i + 1]:
            return listOfTimeSteps[i]
    return listOfTimeSteps[-1]


# eventName,
# typeEvent,
# Venue,
# sizeEvent,
# # dateHost,
# yearsSigned,
# dateSigned,
# requiredEventObjects,
