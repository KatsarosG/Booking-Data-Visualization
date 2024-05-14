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
    totalMonthDict = {
        "Jan" : 0,
        "Feb" : 0,
        "Mar" : 0,
        "Apr" : 0,
        "May" : 0,
        "Jun" : 0,
        "Jul" : 0,
        "Aug" : 0,
        "Sep" : 0,
        "Oct" : 0,
        "Nov" : 0,
        "Dec" : 0

    }

    resortMonthDict = totalMonthDict.copy()
    cityMonthDict = totalMonthDict.copy()
    
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            if lines['arrival_date_month'] == "January":
                resortMonthDict['Jan'] += 1
                totalMonthDict['Jan'] += 1
            elif lines['arrival_date_month'] == "February":
                resortMonthDict['Feb'] += 1
                totalMonthDict['Feb'] += 1
            elif lines['arrival_date_month'] == "March":
                resortMonthDict['Mar'] += 1
                totalMonthDict['Mar'] += 1
            elif lines['arrival_date_month'] == "April":
                resortMonthDict['Apr'] += 1
                totalMonthDict['Apr'] += 1
            elif lines['arrival_date_month'] == "May":
                resortMonthDict['May'] += 1
                totalMonthDict['May'] += 1
            elif lines['arrival_date_month'] == "June":
                resortMonthDict['Jun'] += 1
                totalMonthDict['Jun'] += 1
            elif lines['arrival_date_month'] == "July":
                resortMonthDict['Jul'] += 1
                totalMonthDict['Jul'] += 1
            elif lines['arrival_date_month'] == "August":
                resortMonthDict['Aug'] += 1
                totalMonthDict['Aug'] += 1
            elif lines['arrival_date_month'] == "September":
                resortMonthDict['Sep'] += 1
                totalMonthDict['Sep'] += 1
            elif lines['arrival_date_month'] == "October":
                resortMonthDict['Oct'] += 1
                totalMonthDict['Oct'] += 1
            elif lines['arrival_date_month'] == "November":
                resortMonthDict['Nov'] += 1
                totalMonthDict['Nov'] += 1
            elif lines['arrival_date_month'] == "December":
                resortMonthDict['Dec'] += 1
                totalMonthDict['Dec'] += 1
        elif lines['hotel'] == "City Hotel":
            if lines['arrival_date_month'] == "January":
                cityMonthDict['Jan'] += 1
                totalMonthDict['Jan'] += 1
            elif lines['arrival_date_month'] == "February":
                cityMonthDict['Feb'] += 1
                totalMonthDict['Feb'] += 1
            elif lines['arrival_date_month'] == "March":
                cityMonthDict['Mar'] += 1
                totalMonthDict['Mar'] += 1
            elif lines['arrival_date_month'] == "April":
                cityMonthDict['Apr'] += 1
                totalMonthDict['Apr'] += 1
            elif lines['arrival_date_month'] == "May":
                cityMonthDict['May'] += 1
                totalMonthDict['May'] += 1
            elif lines['arrival_date_month'] == "June":
                cityMonthDict['Jun'] += 1
                totalMonthDict['Jun'] += 1
            elif lines['arrival_date_month'] == "July":
                cityMonthDict['Jul'] += 1
                totalMonthDict['Jul'] += 1
            elif lines['arrival_date_month'] == "August":
                cityMonthDict['Aug'] += 1
                totalMonthDict['Aug'] += 1
            elif lines['arrival_date_month'] == "September":
                cityMonthDict['Sep'] += 1
                totalMonthDict['Sep'] += 1
            elif lines['arrival_date_month'] == "October":
                cityMonthDict['Oct'] += 1
                totalMonthDict['Oct'] += 1
            elif lines['arrival_date_month'] == "November":
                cityMonthDict['Nov'] += 1
                totalMonthDict['Nov'] += 1
            elif lines['arrival_date_month'] == "December":
                cityMonthDict['Dec'] += 1
                totalMonthDict['Dec'] += 1
    plt.plot(list(totalMonthDict.keys()), list(totalMonthDict.values()), marker='.', label = 'Total', color='Blue')
    plt.plot(list(resortMonthDict.keys()), list(resortMonthDict.values()), marker='.', label = 'Resort Hotels', color='Orange')
    plt.plot(list(cityMonthDict.keys()), list(cityMonthDict.values()), marker='.', label = 'City Hotels', color='Red')
    plt.fill_between(list(totalMonthDict.keys()), list(totalMonthDict.values()), color='blue', alpha=.1)
    plt.fill_between(list(cityMonthDict.keys()), list(cityMonthDict.values()), color='red', alpha=.1)
    plt.fill_between(list(resortMonthDict.keys()), list(resortMonthDict.values()), color='orange', alpha=.1)
    plt.grid()
    plt.legend()
    plt.savefig(".monthStats.png")
    plt.cla()
