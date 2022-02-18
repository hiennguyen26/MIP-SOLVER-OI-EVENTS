import requests
from bs4 import BeautifulSoup as bs

#

Host = "https://www.ecotransit.org"
Url = "https://www.ecotransit.org/calculation.en.html"
Post = "https://www.ecotransit.org/singlefrontend/jspa/result.jsp"
Connection = "keep-alive"


# FormFields Test 2
formfields = {
    "lang": "en",
    "style": "smarty",
    "json": {
        "ViewMode": "standard",
        "MainFields": {
            "IntermodalTransferType": "None",
            "CargoUnit": "teu",
            "CargoWeight": 2,
            "CargoVolumeWeight": "Average",
            "FerryRouting": "Normal",
            "FerryClass": "RoPaxMixed",
            "CargoTonsPerTeu": 10,
        },
        "DefaultValueChanges": [],
        "OriginLocation": {
            "LocationId": 0,
            "Id": 46249,
            "Name": "[vn] Hŕ Noi",
            "Type": "City",
            "Sidetrack": True,
            "Harbour": False,
            "Longitude": "105.854694",
            "Latitude": "21.02425",
            "Country": "vn",
        },
        "DestinationLocation": {
            "LocationId": 1,
            "Id": 46432,
            "Name": "[us] New York",
            "Type": "City",
            "Sidetrack": True,
            "Harbour": False,
            "Longitude": "-74.005439",
            "Latitude": "40.711857",
            "Country": "us",
        },
        "Road": True,
        "Rail": True,
        "Air": True,
        "Sea": True,
        "InlandWaterways": True,
    },
}

# FormFields Test 1
# formFields = {
#     "lang": "en",
#     "style": "smarty",
#     "json": {
#         "ViewMode": "standard",
#         "MainFields": {
#             "IntermodalTransferType": "None",
#             "CargoUnit": "teu",
#             "CargoWeight": 100,
#             "CargoVolumeWeight": "Average",
#             "FerryRouting": "Normal",
#             "FerryClass": "RoPaxMixed",
#             "CargoTonsPerTeu": 10,
#         },
#         "DefaultValueChanges": [],
#         "OriginLocation": {
#             "LocationId": 0,
#             "Id": 46249,
#             "Name": "[vn] Hŕ Noi",
#             "Type": "City",
#             "Sidetrack": True,
#             "Harbour": False,
#             "Longitude": "105.854694",
#             "Latitude": "21.02425",
#             "Country": "vn",
#         },
#         "DestinationLocation": {
#             "LocationId": 1,
#             "Id": 46432,
#             "Name": "[us] New York",
#             "Type": "City",
#             "Sidetrack": True,
#             "Harbour": False,
#             "Longitude": "-74.005439",
#             "Latitude": "40.711857",
#             "Country": "us",
#         },
#         "Road": True,
#         "Rail": False,
#         "Air": False,
#         "Sea": False,
#         "InlandWaterways": True,
#     },
# }

page = requests.get(Url)

# Path to calculation_headers.rtf: C:\Users\Hien\Desktop\Northeastern\Spring 2021\CS4100 CS AI\Excercises\calculation_headers.rtf

soup = bs(page.content, "html.parser")

# request post
r = requests.post(Url, data=formfields)
print(r.text)


# Div class for downloading the CSV
# <div class="file_download_div">
#     CSV DOWNLOAD
#     <img class="file_download_img" onclick="resultDisplayControl.setParams('&amp;showTables=1&amp;showGraphs=1&amp;displayMode=PrintVersion&amp;emissions=PrimaryEnergy,CarbonDioxide,NitrogenOxides,NonMethanHydroCarbons,Particles,SulfurDioxides&amp;chains=Road,Rail,Air,Sea,InlandWaterways&amp;printVersion=1&amp;viewMode=standard');window.open('../singlefrontend/csvResult?jsessionid=' + globalAjaxRequestJSessionId,'_blank');" title="Download as csv-file" src="../singlefrontend/images/Exel_button.jpg">
# </div>

# results = soup.find(id="#TODO")


def calculateCarbon(freightAmount, weight, origin, destination, transportMode):
    return 0