# OiEvents

AI to maximize operation efficiency for Oi Events

How to tackle the problem:

1. Get shipping rates from (https://www.freightos.com/freight-resources/ocean-freight-explained/)
2. Start with scenario 1: New York, Singapore, Hanoi. (Test case: Far Far Short).
3. Test theory 1: Idle containers without cost is most efficient. Avoid demmurage costs at all costs because it is very expensive.
4. Price range are given per FCL 40' containers, consider transit times as well for events set up times.
5. Main cost is in dollars, time isn't a constraint.
6. Second cost will be carbon footprint.
7. Try with minimax? need to consult Kacper.
8.

scenario 1:
New York -> Singapore -> Hanoi (most and last idle) -> (new year) New York -> ...
Assumptions:

1. Hanoi has no demurrage cost for all 6 containers. But cost to re-pick up via land transport is doubled.
2. At max 2 containers can be stored in New York without demurrage costs.
3. At max 1 container can be stored in Singapore without demurrage costs.
4. You can source materials at any city. (completely eliminate shipping costs at the start)
5. Costs reduction between 20' FCL and 40' FCL is minimal. But when is it worth it?
6. Upon research, if we are doing FCL, then weight makes no difference in cost of operation.
   Questions to answer:
7. Maximum cost: What is the total cost to transport 6 FCL 40' containers city to city / door to door and idle in Hanoi.
8. Idle costs:

MDP Problem Specs:
Q Learning/ Fitted Q
Model-free policy search since scraping data (sample sufficient) to get boundaries of reward given constraints of the world.
Not model based because optimization of inaccurate models might lead to disaster.
Deterministic control policy since when the scrape finds the next best value it overrides previous episode search.
Structure-less optimization: Black box Optimizer
Episode-based policy search
Heuristics: what's the cost-to-go: minimum cost to reach goal after 10 years:
Goals: 1. Minimizing carbon footprint. 2. Minimizing operation costs with least paid shipping. 3. Maximizing cashflow. 4. Maximizing carbon offset opportunities

Policy for operations for Carbon Footprint Optimzation:

Code specs:
Python code for MDP formulation and everything. Visualization to web app: A world map with planes, maritime, or land travel icon going from cities to cities,
visualize contaners being left behind, and a carbon footprint count and year count.

Use JupyterNotebook to comment on code and possible later Visualization.
Constructors for these objects: World, venue, mode of transport, event, material

Constructor for World:
int numCities
int year
array (venues) venues
array (transportIter) usedTransports
int netCarbon
int totalEventsHosted

Constructor for Venue:
string address
string cityName
string countryName
int allowedIdleTEUs
array (modeTransport) possibleTransports
int netCarbon

Constructor for Mode of transport (transportIter) - one iteration of transport from venue to venue.
string destination (cityName)
string origin (cityName)
int year (keeps track of which year it is)
string typeTransport (enum: maritime, landFuel, or landElectric, air)
int distanceTravelled (in kms)
int cargoVolume if maritime: (0 < cargoVolume, and only whole numbers) TEU: twenty-foot equivalent unit / if land ( 0 < cargoVolume < tonnes)
string typeContainer (20ft or 40ft) if typeContainer == 40ft, cargoVolume cannot be odd.
int carbonEmissions (in tonnes)

Note:
For rail co2 emissions:
For vessel c02 emissions: http://co2cal.oocl.com/co2cal/SearchSummary.aspx?sessionId=38c0ab13-26b3-4132-a42b-553e3e13d622
For land co2 emissions: https://www.ecotransit.org/calculation.en.html

Constructor for events:
string type (enum: business, entertainment, Pavilions)
string sizeEvent
list (Materials) requiredMaterials

Constructor for material:
string type (enum: aluminium, flooring, fabric, bamboo )
int size (if alum -> enum: ; if flooring -> enum: ; if fabric -> enum: ; if bamboo -> enum: )
