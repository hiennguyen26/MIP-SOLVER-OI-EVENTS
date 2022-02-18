# Dictionary to hold all information in relation to material specs.
# TODO: Encode information on subassemblies

# function to calculate cost to source per kilo


def calculateSourceCostAlum(weight):
    cost = weight * 1000 * 3.2
    return cost


# function to calculate cost to source per kilo
def calculateSourceCostFlooring(weight):
    cost = weight * 1000 * 4.5
    return cost


ModuleInfo = {  # Refered to OI MATERIAL DISTRIBUTION PRODUCT SHEET
    # costSource includes cost to make individual modules (90% value) and cost to ship anywhere in the world (10%), regardless of distance.
    # weight is in tonnes
    "Module1Std": {
        "weight": 0.042058,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(42.058),
    },
    "Module2Std": {
        "weight": 0.035703,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(35.703),
    },
    "Module3Std": {
        "weight": 0.027853,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(27.853),
    },
    "Module4Std": {
        "weight": 0.032598,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(32.598),
    },
    "Module1Raised": {
        "weight": 0.043473,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(43.473),
    },
    "Module2Raised": {
        "weight": 0.037118,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(37.118),
    },
    "Module3Raised": {
        "weight": 0.029269,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(29.269),
    },
    "Module4Raised": {
        "weight": 0.034013,
        "material": "Flooring",
        "costSource": calculateSourceCostFlooring(34.013),
    },
    "5000x2400": {
        "weight": 0.021814,
        "material": "Aluminium",
        "costSource": calculateSourceCostAlum(21.814),
    },
    "2400x1200": {
        "weight": 0.01490,
        "material": "Aluminium",
        "costSource": calculateSourceCostAlum(10.490),
    },
    "1500x1200": {
        "weight": 0.007808,
        "material": "Aluminium",
        "costSource": calculateSourceCostAlum(7.808),
    },
    "1200x1200": {
        "weight": 0.006914,
        "material": "Aluminium",
        "costSource": calculateSourceCostAlum(6.914),
    },
    "1200x200": {
        "weight": 0.004232,
        "material": "Aluminium",
        "costSource": calculateSourceCostAlum(4.232),
    },
}


# Product categories and how many modules does each need.
ProductCart = {  # Refered to OI MATERIAL DISTRIBUTION PRODUCT SHEET
    "10Pavilions": {
        "Module1Std": 128,
        "Module2Std": 128,
        "Module3Std": 128,
        "Module4Std": 64,
        "Module1Raised": 32,
        "Module2Raised": 32,
        "Module3Raised": 32,
        "Module4Raised": 32,
        "5000x2400": 80,
        "2400x1200": 240,
        "1500x1200": 160,
        "1200x1200": 80,
        "1200x200": 80,
    },
    "MainStage": {
        "Module1Std": 2,
        "Module3Std": 2,
        "Module1Raised": 10,
        "Module2Raised": 14,
        "Module3Raised": 12,
        "Module4Raised": 8,
    },
    "360Stage": {
        "Module1Std": 16,
        "Module2Std": 16,
        "Module4Std": 16,
        "Module3Raised": 16,
        "Module4Raised": 8,
    },
    # Seedling Booth -> for 8 startups
    "StartupBooth": {
        "Module1Std": 2,
        "Module3Std": 2,
        "Module4Std": 2,
        "5000x2400": 2,
        "2400x1200": 4,
    },
    # Sapling Booth -> 4 startups
    "SMEBooth": {
        "Module1Std": 4,
        "Module2Std": 6,
        "Module3Std": 2,
        "2400x1200": 14,
        "1500x1200": 8,
        "1200x1200": 4,
    },
    # Grove Booth -> 1 Corp Tech
    "CorporateBoothTech": {
        "Module2Std": 5,
        "Module3Std": 25,
        "Module4Std": 5,
        "2400x1200": 15,
        "1500x1200": 34,
        "1200x1200": 17,
        "1200x200": 26,
    },
    # Forest Booth -> 1 Corp Showcase
    "CorporateBoothAuto": {
        "Module1Std": 27,
        "Module2Std": 9,
        "2400x1200": 21,
        "1500x1200": 12,
        "1200x1200": 3,
    },
    # Acorn Booth -> 1 Corp Speciality
    "CorporateBoothOctagonal": {
        "Module1Std": 27,
        "Module2Std": 9,
        "5000x2400": 1,
        "2400x1200": 41,
    },
    # Event Amenities
    "TriangularBillBoard": {"5000x2400": 6},
    "HangoutHut": {"5000x2400": 3},
}

# Function to get total weight of a product.


def getProductWeight(product):
    accum = 0
    for module in ProductCart[product].keys():
        accum += ModuleInfo[module]["weight"] * ProductCart[product][module]
    return accum


# Module getter Function:
def moduleGetter(event):
    modules = {}
    for product in event.requiredEventObjects.keys():
        for module in ProductCart[product].keys():
            if module in modules.keys():
                modules[module] += (
                    ProductCart[product][module] *
                    event.requiredEventObjects[product]
                )

            else:
                modules[module] = (
                    ProductCart[product][module] *
                    event.requiredEventObjects[product]
                )
    return modules

# Get empty modules.


def getEmptyModules():
    modules = {}
    for m in ModuleInfo.keys():
        modules[m] = 0
    return modules
