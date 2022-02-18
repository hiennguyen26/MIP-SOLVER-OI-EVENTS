from datetime import datetime
import events, location
class World:
    # init constructor
    def __init__(
        self,
        currentTime,
        listEvents,
        listStorage,
        netCarbon,
        totalCostofOperations, 
    ):
        self.currentTime = currentTime
        # array of venues within a year.
        self.listEvents = listEvents
        # array of transportIters
        self.listStorage = listStorage
        self.netCarbon = netCarbon
        self.totalCostofOperations = totalCostofOperations

    # display current world net carbon support function
    def display(self):
        print(
            "Number of participating cities in year "
            + str(self.currentTime)
            + "is "
            + str(self.events)
            + "with a net carbon of "
            + str(self.netCarbon)
            + "for "
            + str(self.totalEventsHosted)
            + " events hosted."
        )


#list of events
listOfEvents = []

#list of Storage
listOfStorage = []


#init world
worldTest = World(datetime.now(), listOfEvents, listOfStorage, 0, 0)



