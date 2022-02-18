class LogisticsActions:
    # init constructor
    def __init__(self, actionType, pileMaterial):
        # Enum of logisticActions: Store, Source or Ship Materials.
        self.actionType = actionType
        self.pileMaterial = pileMaterial

    #checks if the venue has available capacity to store materials after the event. 
    def checkToStore():
        return None