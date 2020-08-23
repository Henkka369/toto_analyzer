import requests
import json
import sys
from datetime import date
from progress_bar import printProgressBar

startDate = "2003-03-13"
endDate = "2003-09-13"
# Count days between given dates
d0 = date(int(startDate[:4]), int(startDate[5:7]), int(startDate[8:]))
d1 = date(int(endDate[:4]), int(endDate[5:7]), int(endDate[8:]))
delta = d1 - d0
span = delta.days
baseURL = "https://www.veikkaus.fi"
response = requests.get(baseURL + "/api/toto-info/v1/cards/date/" + startDate)
results = dict()

nextDate = ""
dayCounter = 0
noResults = 0
ties = 0
while nextDate != endDate:
    dayCounter += 1
    data = response.json()
    for card in data["collection"]:
        # Select events only from Finland and check if cancelled(no results)
        if card["country"] == "FI" and card["cancelled"] == False:
            race_info = requests.get(baseURL + "/api/toto-info/v1/card/" + str(card["cardId"]) + "/races").json()
            for race in race_info["collection"]:
                # Race without results
                try:
                    toteResult = race["toteResultString"].split("-")
                    startType = race["startType"]
                except:
                    noResults += 1
                # In case of multiple horses at same position
                try:
                    topThree = str(toteResult[0]).strip() + "," + str(toteResult[1]).strip() + "," + str(toteResult[2]).strip() + "," + startType.strip()
                except:
                    ties += 1
                if topThree in results:
                    results[topThree] = results[topThree] + 1
                else:
                    results[topThree] = 1
    # Data involves next date
    response = requests.get(baseURL + data["next"])
    nextDate = data["next"][-10:]
    printProgressBar(dayCounter, span, prefix = 'Edistyminen:', suffix = 'Valmiina', length = 50)

print("Hylättyjä tasapelejä: " + str(ties))
print("Lähtöjä ilman tuloksia: " + str(noResults))
print("Tuloksia haettu: " + str(len(results)) + " kpl")
# Write results in json-file
with open('data.json', "w") as fp:
    json.dump(results, fp, indent=4)
