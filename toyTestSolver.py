from pulp import *

event_locations = ["New York City", "Hanoi", "Los Angeles", "Singapore", "Berlin"]
event_demand = {
    "New York City": 0,
    "Hanoi": 25,
    "Los Angeles": 60,
    "Singapore": 50,
    "Berlin": 65,
}
storage_locations = ["New York City", "Hanoi", "Los Angeles"]
stored_modules = {"New York City": 20, "Hanoi": 45, "Los Angeles": 10}
shipping_dollar_costs_base = [  # events
    # nyc, vtn, la, sing, ber
    [0, 400, 50, 400, 300],  # nyc
    [400, 0, 350, 100, 400],  # hanoi  # storage
    [50, 350, 0, 350, 300],
]  # la
shipping_carbon_costs_base = [  # events
    # nyc, vtn, la, sing, ber
    [0, 600, 73, 580, 460],  # nyc
    [768, 0, 579, 120, 600],  # hanoi  # storage
    [73, 579, 0, 500, 600],
]  # la
sourcing_costs = {
    "New York City": 700,
    "Hanoi": 500,
    "Los Angeles": 900,
    "Singapore": 360,
    "Berlin": 879,
}

# Create cost dicts
shipping_dollar_costs = makeDict(
    [storage_locations, event_locations], shipping_dollar_costs_base
)
shipping_carbon_costs = makeDict(
    [storage_locations, event_locations], shipping_carbon_costs_base
)

# Define problem
prob = LpProblem("Carbon_Minimization", LpMinimize)

# Decision variables
routes = [(s, e) for s in storage_locations for e in event_locations]
route_vars = LpVariable.dicts(
    "Route", (storage_locations, event_locations), 0, None, LpInteger
)
source_vars = LpVariable.dicts("Source", event_locations, 0, None, LpInteger)

# Objective function
prob += lpSum(
    [source_vars[e] * sourcing_costs[e] for e in event_locations]
    + [route_vars[s][e] * shipping_carbon_costs[s][e] for (s, e) in routes]
)

# Constraints
cost_limits = {
    "New York City": 2000,
    "Hanoi": 2000,
    "Los Angeles": 2000,
    "Singapore": 2000,
    "Berlin": 2000,
}
for (s, e) in routes:
    prob += lpSum(shipping_dollar_costs[s][e] * route_vars[s][e]) <= cost_limits[e]

for e in event_locations:
    prob += (
        lpSum(source_vars[e] + [route_vars[s][e] for s in storage_locations])
        >= event_demand[e]
    )

# Commands to run and get the vars
# Run Solver
prob.solve()
for v in prob.variables():
    print(v, v.value())

print(prob)
