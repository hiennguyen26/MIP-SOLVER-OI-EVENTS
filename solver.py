# imports
import transportIter
from pulp import *
from math import sqrt
import module
import events
from events import createTransportIters as cti
import location
import datetime
from datetime import timedelta
import csv

# run the solver at a timestep with list of locations & events


def runSolver(
    eventsList, storage_locations, currentDate, endDate, timestep=timedelta(
        weeks=1)
):

    listOfTimeSteps = []
    datey = currentDate
    while datey <= endDate:
        listOfTimeSteps.append(datey.isoformat())
        datey += timestep

    listOfDateObjects = [datetime.date.fromisoformat(
        ts) for ts in listOfTimeSteps]

    # add in transportIterList
    # Test Case 1:
    transportIterList = cti(
        events.EventsListCase1,
        events.EventsListCase1,
        # location.StorageListCase1,
        listOfDateObjects,
        currentDate,
    )

    # Test Case 2:
    transportIterList2 = cti(
        events.EventsListCase2,
        events.EventsListCase2,
        # location.StorageListCase2,
        listOfDateObjects,
        currentDate,
    )

    # Test Case 3:
    transportIterList3 = cti(
        events.EventsListCase3,
        events.EventsListCase3,
        # location.StorageListCase3,
        listOfDateObjects,
        currentDate,
    )

    shipping_dollar_costs = {}
    shipping_carbon_costs = {}

    # add in event locations
    # Change this if you're testing a different test case (1-2-3)
    eventsList = events.EventsListCase3

    # Initiate an events instance list
    event_demand = {}  # add in event demand

    # Create a list of event instances in a list of date objects.
    # AMT: Set initial demand to 0? Routes only affect future storage
    for ts in listOfDateObjects:
        for e in eventsList:
            for d in events.generateEventDates(e, currentDate):
                d = events.fitInTimeSteps(d, listOfDateObjects)
                if d == ts:
                    if e not in event_demand.keys():
                        event_demand[e] = {}
                    event_demand[e][ts.isoformat()] = e.moduleGetter()
                else:
                    if e not in event_demand.keys():
                        event_demand[e] = {}
                    event_demand[e][ts.isoformat()] = module.getEmptyModules()

    # add in storage locations
    # Change this if you're testing a different test case (1-2-3)
    # storage_locations = location.StorageListCase1

    # TransportIterList to calculateShippingCost & Carbon Cost
    # Change transportIterList (1-2-3) if you're testing a different test case
    for t in transportIterList3:
        if t.origin.locationName not in shipping_dollar_costs:
            shipping_dollar_costs[t.origin.locationName] = {}
        if (
            t.destination.locationName
            not in shipping_dollar_costs[t.origin.locationName]
        ):
            shipping_dollar_costs[t.origin.locationName][
                t.destination.locationName
            ] = {}
        for m in module.ModuleInfo.keys():
            shipping_dollar_costs[t.origin.locationName][t.destination.locationName][
                m
            ] = t.calculateShippingCost(module.ModuleInfo[m]["weight"])
        if t.origin.locationName not in shipping_carbon_costs:
            shipping_carbon_costs[t.origin.locationName] = {}
        if (
            t.destination.locationName
            not in shipping_carbon_costs[t.origin.locationName]
        ):
            shipping_carbon_costs[t.origin.locationName][
                t.destination.locationName
            ] = {}
        for m in module.ModuleInfo.keys():
            shipping_carbon_costs[t.origin.locationName][t.destination.locationName][
                m
            ] = t.calculateCarbonEmissions(module.ModuleInfo[m]["weight"])

    # Define problem
    prob = LpProblem("Carbon_Minimization", LpMinimize)

    # Decision variables
    routes = []

    for ts in listOfTimeSteps:
        for e1 in eventsList:
            for e2 in eventsList:
                if e1.Venue.locationName != e2.Venue.locationName:
                    for m in module.ModuleInfo.keys():
                        routes.append((ts, e1, e2, m))
    # print(routes)
    # Shipping materials
    route_vars = LpVariable.dicts(
        "Ship",
        (
            # could be a problem
            [e1.Venue.locationName for e1 in eventsList],
            [e2.Venue.locationName for e2 in eventsList],
            module.ModuleInfo.keys(),
            listOfTimeSteps,
        ),
        0,
        None,
        LpInteger,
    )

    # Sourcing materials
    source_vars = LpVariable.dicts(
        "Source",
        (
            [e.Venue.locationName for e in eventsList],
            module.ModuleInfo.keys(),
            listOfTimeSteps,
        ),
        0,
        None,
        LpInteger,
    )

    # # Storing materials
    # storage_vars = LpVariable.dicts(
    #     "Store",
    #     (
    #         [s.locationName for s in storage_locations],
    #         module.ModuleInfo.keys(),
    #         listOfTimeSteps,
    #     ),
    #     0,
    #     None,
    #     LpInteger,
    # )

    # How much materials are at an event currently
    event_vars = LpVariable.dicts(
        "Store_at_Event",
        (
            [e.Venue.locationName for e in eventsList],
            module.ModuleInfo.keys(),
            listOfTimeSteps,
        ),
        0,
        None,
        LpInteger,
    )

    # lambdas to signify importance level per optimizations in the objective function
    lambdaCarbon = 0.0000001
    lambdaShip = 100

    # Objective function
    prob += lpSum(
        [
            source_vars[e.Venue.locationName][m][ts] *
            module.ModuleInfo[m]["costSource"]
            for e in eventsList
            for m in module.ModuleInfo.keys()
            for ts in listOfTimeSteps

        ]
        + [
            lambdaCarbon
            * route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts]
            * shipping_carbon_costs[e1.Venue.locationName][e2.Venue.locationName][m]
            for (ts, e1, e2, m) in routes
        ]
        # + [
        #     lambdaShip
        #     * shipping_dollar_costs[e1.Venue.locationName][e2.Venue.locationName][m]
        #     * route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts]
        #     for (ts, e1, e2, m) in routes
        # ]
    )

    # Constraints
    # Shipping Cost limits - max how much $$$$ each event organizer will pay for shipping.
    cost_limits = {
        "New York": 55000,
        "Hanoi": 55000,
        "Bali": 25000,
        "Los Angeles": 55000,
        "Singapore": 65000,
        "Paris": 65000,
        "Rome": 65000,
        "Berlin": 65000,
        "Ho Chi Minh": 65000,
        "Jarkatar": 25000,
        "Hong Kong": 25000,
        "Manila": 25000,
        "Beijing": 65000,
        "Houston": 65000,
        "San Jose": 15000,
        "Buenos Aires": 25000,
        "CapeTown": 65000,
        "Harare": 65000,
        "Victoria": 100000,
        "Dakar": 100000,
        "Helsinki": 65000,
    }

    # # AMT: Constraints for initial storage
    # for s in storage_locations:
    #     for m in module.ModuleInfo.keys():
    #         prob += storage_vars[s.locationName][m][listOfTimeSteps[0]
    #                                                 ] == s.getStoredCurrently(m)

    # Initial Event constraint
    for e in eventsList:
        for m in module.ModuleInfo.keys():
            prob += event_vars[e.Venue.locationName][m][listOfTimeSteps[0]
                                                        ] == e.Venue.getStoredCurrently(m)

    # Constraint for shipping costs to the next event can't go over some bound M
    for (ts, e1, e2, m) in routes:
        prob += (
            lpSum(
                shipping_dollar_costs[e1.Venue.locationName][e2.Venue.locationName][m]
                * route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts]
            )
            <= cost_limits[e1.eventName]
        )

    M = 150000
    # Constraint for a cap limit of sourcing:
    for y in range(2021, 2027):
        prob += lpSum([source_vars[e.Venue.locationName][m][ts] for e in eventsList for m in module.ModuleInfo.keys()
                       for ts in listOfTimeSteps if ts.startswith(str(y))]) <= M

    # Constraint for the number of materials in storage cannot be over capacity of storage
    # this has to be included, but the capacity of storage isn't per module.
    # for ts in listOfTimeSteps:
    #     for s in storage_locations:
    #         for m in module.ModuleInfo.keys():
    #             if not m in s.maxStorage:
    #                 for e in eventsList:
    #                     prob += route_vars[s.locationName][e.Venue.locationName][m][ts] <= 0
    #             else:
    #                 for e in eventsList:
    #                     prob += (
    #                         route_vars[s.locationName][e.Venue.locationName][m][ts]
    #                         <= s.maxStorage[m]
    #                     )

    # Constraint for the number of materials in closest storage and to source must meet the next event demand
    # for ename in [e.eventName for e in events]
    for ts in listOfTimeSteps:
        for e in eventsList:
            for m in e.moduleGetter().keys():
                prob += event_vars[e.Venue.locationName][m][ts] >= event_demand[e][ts][m]

    # Constraint for the number of materials to be stored in the next storage location of the next event.
    for ts in listOfTimeSteps:
        for e1 in eventsList:
            for m in module.ModuleInfo.keys():
                for e2 in eventsList:
                    if e1 != e2:
                        prob += (
                            route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts]
                            <= event_vars[e1.Venue.locationName][m][ts]
                        )

    # Constraint for updating materials stored at events:
    for i in range(len(listOfTimeSteps) - 1):
        for m in module.ModuleInfo.keys():
            for e1 in eventsList:
                currentTs = listOfTimeSteps[i]
                nextTs = listOfTimeSteps[i + 1]
                prob += (event_vars[e1.Venue.locationName][m][nextTs] == event_vars[e1.Venue.locationName][m][currentTs]
                         + lpSum([route_vars[e2.Venue.locationName][e1.Venue.locationName]
                                  [m][currentTs] for e2 in eventsList if e1 != e2])
                         - lpSum([route_vars[e1.Venue.locationName][e2.Venue.locationName]
                                  [m][currentTs] for e2 in eventsList if e1 != e2])
                         + source_vars[e1.Venue.locationName][m][currentTs]
                         )

    # # Constraint for an event to have storage always
    # for i in range(len(listOfTimeSteps) - 1):
    #     for m in module.ModuleInfo.keys():
    #         currentTs = listOfTimeSteps[i]
    #         nextTs = listOfTimeSteps[i + 1]
    #         prob += (event_vars[[e.Venue.locationName for e in eventsList]][m][nextTs] ==
    #                  event_vars[[e.Venue.locationName for e in eventsList]][m][currentTs] -
    #                  route_vars[[s.locationName for s in storage_locations]][
    #             [e.Venue.locationName for e in eventsList]
    #         ][m][currentTs]
    #             + route_vars[[s.locationName for s in storage_locations]][]
    #         )

    # # Constraint to make sure that the total materials present in the next event's storage is equal to the amount of previous storage ship to it and sourcing.
    # # minus what ever is shipped out of that event's storage too.
    # for i in range(len(listOfTimeSteps) - 1):
    #     for m in module.ModuleInfo.keys():
    #         currentTs = listOfTimeSteps[i]
    #         nextTs = listOfTimeSteps[i + 1]
    #         prob += (storage_vars[[s.locationName for s in storage_locations]][m][nextTs] ==
    #                  storage_vars[[s.locationName for s in storage_locations]][m][currentTs] -
    #                  route_vars[[s.locationName for s in storage_locations]][
    #             [e.Venue.locationName for e in eventsList]
    #         ][m][currentTs]
    #             + route_vars[[s.locationName for s in storage_locations]][]
    #         )

    # AMT: Break above into contraints for events w/ vs w/o storage, perhaps
    # a way forward to incorporating

    # Commands to run and get the vars
    # Run Solver
    prob.solve()
    for v in prob.variables():
        if v.value() != 0:
            print(v, v.value())
    print()
    # print(prob)
    print()
    # Objective function

    # print(prob)
    print()
    # print(source_vars)

    # print(shipping_carbon_costs)
    # print()
    print()
    print()
    # print(shipping_dollar_costs)
    # print(events.eventSingapore.moduleGetter())
    # print()
    # print()
    # print(events.eventHanoi.moduleGetter())
    # print()
    # print()
    # print(events.eventNYC.moduleGetter())
    # print()
    # print()
    # print(event_demand)

    print()
    print()

    # def getTotalOperationCost():
    #     totalCost = 0
    #     for e in eventsList:
    #         for m in module.ModuleInfo.keys():
    #             totalCost += (
    #                 source_vars[e.Venue.locationName][m]
    #                 * module.ModuleInfo[m]["costSource"]
    #             )
    #     return totalCost

    def getTotalCostSourced():
        costSource = 0
        for ts in listOfTimeSteps:
            for e in eventsList:
                for m in module.ModuleInfo.keys():
                    costSource += source_vars[e.Venue.locationName][m][ts].value() * \
                        module.ModuleInfo[m]["costSource"]
        return costSource

    def getTotalCarbonCost():
        totalCarbon = 0
        for ts in listOfTimeSteps:
            for e1 in eventsList:
                for e2 in eventsList:
                    if e1 != e2:
                        for m in module.ModuleInfo.keys():
                            totalCarbon += route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts].value() * \
                                shipping_carbon_costs[e1.Venue.locationName][e2.Venue.locationName][m]
        return totalCarbon

    def getTotalShippingCost():
        totalCost = 0
        for ts in listOfTimeSteps:
            for e1 in eventsList:
                for e2 in eventsList:
                    if e1 != e2:
                        for m in module.ModuleInfo.keys():
                            totalCost += route_vars[e1.Venue.locationName][e2.Venue.locationName][m][ts].value() * \
                                shipping_dollar_costs[e1.Venue.locationName][e2.Venue.locationName][m]
        return totalCost

    print(
        "Total carbon emissions in test case: " +
        str(getTotalCarbonCost()) + " tonnes CO2"
    )
    print("Total cost of shipping paid in test case: $" +
          str(getTotalShippingCost()))
    print("Total cost of sourcing: " + str(getTotalCostSourced()))


runSolver(None, None, datetime.date.today(),
          datetime.date.today() + timedelta(weeks=52 * 2))
