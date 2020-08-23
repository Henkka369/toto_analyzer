import json

toto_results = dict()
stop = 'a' # Stop flag for program
# Read Toto results from json-file
try:
    with open("data.json") as json_file:
        data = json.load(json_file)
        for key in data:
            # Convert string to tuple for easier handling
            values = key.split(",")
            topThree = (values[0], values[1], values[2], values[3])
            toto_results[topThree] = data[key]
except:
    print("Tiedostoa data.json ei löydy. Kokeile suorittaa data_fetch.py uudelleen.")
    stop = 'p'



def print_results(results_dict):
    printedLines = 20
    for result, count in results_dict:
        if printedLines == 0:
            break
        else:
            print(str(result) + " esiintyi " + str(count) + " kertaa")
            printedLines -= 1



def dict_maker(toto_results, resultType, startType):
    results_dict = dict()
    for trifecta in toto_results:
        if startType == "VOLT_START" and trifecta[3] == "CAR_START":
            continue
        elif startType == "CAR_START" and trifecta[3] == "VOLT_START":
            continue
        
        if resultType == "winner":
            result = str(trifecta[0])
        elif resultType == "exacta":
            result = str(trifecta[0]) + "," + str(trifecta[1])
        else:
            result = str(trifecta[0]) + "," + str(trifecta[1]) + "," + str(trifecta[2])

        if result in results_dict:
            results_dict[result] += int(toto_results[trifecta])
        else:
            results_dict[result] = int(toto_results[trifecta])
        
    results_dict = sorted(results_dict.items(), key=lambda x: x[1], reverse=True) # Sort results in reversed order by values
    print_results(results_dict)



while stop == 'a':
    print()
    print("Datasta saatavat tulokset: ")
    print("1: Voittaja")
    print("2: Kaksari")
    print("3: Troikka")
    print("4: Voittaja (volttilähtö)")
    print("5: Voittaja (autolähtö)")
    print("6: Kaksari (volttilähtö)")
    print("7: Kaksari (autolähtö)")
    print("8: Troikka (volttilähtö)")
    print("9: Troikka (autolähtö)")
    choice = int(input("Valitse operaatio: "))
    print()
    if choice == 1:
        dict_maker(toto_results, "winner", "")
    elif choice == 2:
        dict_maker(toto_results, "exacta", "")
    elif choice == 3:
        dict_maker(toto_results, "trifecta", "")
    elif choice == 4:
        dict_maker(toto_results, "winner", "VOLT_START")
    elif choice == 5:
        dict_maker(toto_results, "winner", "CAR_START")
    elif choice == 6:
        dict_maker(toto_results, "exacta", "VOLT_START")
    elif choice == 7:
        dict_maker(toto_results, "exacta", "CAR_START")
    elif choice == 8:
        dict_maker(toto_results, "trifecta", "VOLT_START")
    elif choice == 9:
        dict_maker(toto_results, "trifecta", "CAR_START")
    stop = input("Syötä 'p' poistuaksesi tai 'a' aloittaaksesi alusta: ")