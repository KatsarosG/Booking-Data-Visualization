import pandas as pd
import matplotlib.pyplot as plt

def readFile(fileName):
    global csvFile
    df = pd.read_csv(fileName)
    csvFile = df.to_dict(orient='records')

def calcStayInNightsAvg():
    global resortNightsAvg
    global cityNightsAvg
    resortNightsAvg = 0
    cityNightsAvg = 0
    resortCounter = 0
    cityCounter = 0
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            resortCounter += 1
        else:
            cityNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            cityCounter += 1
    resortNightsAvg = round(resortNightsAvg/resortCounter, 2)
    cityNightsAvg = round(cityNightsAvg/cityCounter, 2)

def calcCansellationPrc():
    global resortCancellationPrc
    global cityCancellationPrc
    resortCancellationPrc = 0
    cityCancellationPrc = 0
    resortCounter = 0
    cityCounter = 0
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortCancellationPrc += int(lines['is_canceled'])
            resortCounter += 1
        else:
            cityCancellationPrc += int(lines['is_canceled'])
            cityCounter += 1
    resortCancellationPrc = round(float((resortCancellationPrc / resortCounter) * 100), 2)
    cityCancellationPrc = round(float((cityCancellationPrc / cityCounter) * 100), 2)

def calcBasics():
        calcStayInNightsAvg()
        calcCansellationPrc()

        fig = plt.figure()
        axes = fig.subplots(2)
        axes[0].barh(["Resort", "City"], [resortCancellationPrc, cityCancellationPrc], color=['tab:orange', 'tab:red'])
        axes[0].text(resortCancellationPrc/2, 0, str(resortCancellationPrc) + "%", color = 'white')
        axes[0].text(cityCancellationPrc/2, 1, str(cityCancellationPrc) + "%", color = 'white')
        axes[0].title.set_text("Hotel Cancellation Precentage:")

        axes[1].barh(["Resort", "City"], [resortNightsAvg, cityNightsAvg], color=['tab:orange', 'tab:red'])
        axes[1].text(resortNightsAvg/2, 0, str(resortNightsAvg), color = 'white')
        axes[1].text(cityNightsAvg/2, 1, str(cityNightsAvg), color = 'white')
        axes[1].title.set_text("Hotel Night Stay-Ins Average:")
        fig.tight_layout()
        fig.savefig(".basicStats.png")
        plt.clf()

def calcMonthStats():
    global totalMonthDict
    totalMonthDict = {
        "January" : 0,
        "February" : 0,
        "March" : 0,
        "April" : 0,
        "May" : 0,
        "June" : 0,
        "July" : 0,
        "August" : 0,
        "September" : 0,
        "October" : 0,
        "November" : 0,
        "December" : 0

    }

    resortMonthDict = totalMonthDict.copy()
    cityMonthDict = totalMonthDict.copy()
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortMonthDict[lines['arrival_date_month']] += 1
            totalMonthDict[lines['arrival_date_month']] += 1
        else:
            cityMonthDict[lines['arrival_date_month']] += 1
            totalMonthDict[lines['arrival_date_month']] += 1

    plt.plot(list(totalMonthDict.keys()), list(totalMonthDict.values()), marker='.', label = 'Total', color='Blue')
    plt.plot(list(resortMonthDict.keys()), list(resortMonthDict.values()), marker='.', label = 'Resort Hotels', color='Orange')
    plt.plot(list(cityMonthDict.keys()), list(cityMonthDict.values()), marker='.', label = 'City Hotels', color='Red')
    plt.fill_between(list(totalMonthDict.keys()), list(totalMonthDict.values()), color='blue', alpha=.1)
    plt.fill_between(list(cityMonthDict.keys()), list(cityMonthDict.values()), color='red', alpha=.1)
    plt.fill_between(list(resortMonthDict.keys()), list(resortMonthDict.values()), color='orange', alpha=.1)
    plt.grid()
    plt.legend()
    plt.title("Reservations Per Month:")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(".monthStats.png")
    plt.cla()

def calcSeasonStats():
    totalSeasonDict = {
        "Winter" : 0,
        "Spring" : 0,
        "Summer" : 0,
        "Autumn" : 0
    }

    calcMonthStats()

    totalSeasonDict['Winter'] = totalMonthDict['December'] + totalMonthDict['January'] + totalMonthDict['February'] 
    totalSeasonDict['Spring'] = totalMonthDict['March'] + totalMonthDict['April'] + totalMonthDict['May'] 
    totalSeasonDict['Summer'] = totalMonthDict['June'] + totalMonthDict['July'] + totalMonthDict['August'] 
    totalSeasonDict['Autumn'] = totalMonthDict['September'] + totalMonthDict['October'] + totalMonthDict['November'] 

    plt.plot(list(totalSeasonDict.keys()), list(totalSeasonDict.values()), marker='.', color='Blue')
    plt.fill_between(list(totalSeasonDict.keys()), list(totalSeasonDict.values()), color='blue', alpha=.1)
    plt.grid()
    plt.title("Reservations Per Season:")
    plt.savefig(".seasonStats.png")
    plt.cla()

def calcRoomTypeStats():
    roomTypeDict = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0
    }
