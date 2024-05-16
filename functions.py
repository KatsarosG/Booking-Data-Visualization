#   Declaration of functions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mpldates
from scipy.stats import linregress

def readFile(fileName):
    global csvFile
    global df
    df = pd.read_csv(fileName)
    #Add collumn 'date' with the arrival date in format YYYY/Month/D
    df['date'] = df['arrival_date_year'].astype(str) + '/' + df['arrival_date_month'].astype(str) + '/' + df['arrival_date_day_of_month'].astype(str)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%B/%d')
    #Set 'date' collumn as the index of the dataframe
    df = df.set_index('date')
    #Create dictionary of dataframe
    csvFile = df.to_dict(orient='records')

def calcStayInNightsAvg():
    global resortNightsAvg
    global cityNightsAvg
    resortNightsAvg = 0
    cityNightsAvg = 0
    resortCounter = 0
    cityCounter = 0
    #Count all StayIns for each hotel type
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            resortCounter += 1
        else:
            cityNightsAvg += int(lines['stays_in_weekend_nights']) + int(lines['stays_in_week_nights'])
            cityCounter += 1
    #Calculate Precentage
    resortNightsAvg = round(resortNightsAvg/resortCounter, 2)
    cityNightsAvg = round(cityNightsAvg/cityCounter, 2)

def calcCansellationPrc():
    global resortCancellationPrc
    global cityCancellationPrc
    resortCancellationPrc = 0
    cityCancellationPrc = 0
    resortCounter = 0
    cityCounter = 0
    #Count all cansellations for each hotel type
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortCancellationPrc += int(lines['is_canceled'])
            resortCounter += 1
        else:
            cityCancellationPrc += int(lines['is_canceled'])
            cityCounter += 1
    #Calculate Precentage
    resortCancellationPrc = round(float((resortCancellationPrc / resortCounter) * 100), 2)
    cityCancellationPrc = round(float((cityCancellationPrc / cityCounter) * 100), 2)

def calcBasics():
        calcStayInNightsAvg()
        calcCansellationPrc()
        
        #Create double plot of the above data
        fig = plt.figure()
        axes = fig.subplots(2)
        
        #Create first plot about cancellations 
        axes[0].barh(["Resort", "City"], [resortCancellationPrc, cityCancellationPrc], color=['tab:orange', 'tab:red'])
        axes[0].text(resortCancellationPrc/2, 0, str(resortCancellationPrc) + "%", color = 'white')
        axes[0].text(cityCancellationPrc/2, 1, str(cityCancellationPrc) + "%", color = 'white')
        axes[0].title.set_text("Hotel Cancellation Precentage:")
        
        #Create second plot about Stayins
        axes[1].barh(["Resort", "City"], [resortNightsAvg, cityNightsAvg], color=['tab:orange', 'tab:red'])
        axes[1].text(resortNightsAvg/2, 0, str(resortNightsAvg), color = 'white')
        axes[1].text(cityNightsAvg/2, 1, str(cityNightsAvg), color = 'white')
        axes[1].title.set_text("Hotel Night Stay-Ins Average:")
        
        #Save plot
        fig.tight_layout()
        fig.savefig(".basicStats.png")
        plt.close()

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

    #Count reservations for each month and the total reservations
    for lines in csvFile:
        if lines['hotel'] == "Resort Hotel":
            resortMonthDict[lines['arrival_date_month']] += 1
            totalMonthDict[lines['arrival_date_month']] += 1
        else:
            cityMonthDict[lines['arrival_date_month']] += 1
            totalMonthDict[lines['arrival_date_month']] += 1

    #Create plot
    #Plot total reservations
    plt.plot(list(totalMonthDict.keys()), list(totalMonthDict.values()), marker='.', label = 'Total', color='Blue')
    #Plot Resort Reservations
    plt.plot(list(resortMonthDict.keys()), list(resortMonthDict.values()), marker='.', label = 'Resort Hotels', color='Orange')
    #Plot City reservations
    plt.plot(list(cityMonthDict.keys()), list(cityMonthDict.values()), marker='.', label = 'City Hotels', color='Red')
    #Plot Decorations:
    plt.fill_between(list(totalMonthDict.keys()), list(totalMonthDict.values()), color='blue', alpha=.1)
    plt.fill_between(list(cityMonthDict.keys()), list(cityMonthDict.values()), color='red', alpha=.1)
    plt.fill_between(list(resortMonthDict.keys()), list(resortMonthDict.values()), color='orange', alpha=.1)
    plt.grid()
    plt.legend()
    plt.title("Reservations Per Month:")
    plt.xticks(rotation=30)
    plt.tight_layout()
    #Save plot
    plt.savefig(".monthStats.png")
    plt.close()

def calcSeasonStats():
    totalSeasonDict = {
        "Winter" : 0,
        "Spring" : 0,
        "Summer" : 0,
        "Autumn" : 0
    }
    
    #Calculate reservations for each month
    calcMonthStats()
    
    #Season reservation = The sum of the reservation for each month of this season
    totalSeasonDict['Winter'] = totalMonthDict['December'] + totalMonthDict['January'] + totalMonthDict['February'] 
    totalSeasonDict['Spring'] = totalMonthDict['March'] + totalMonthDict['April'] + totalMonthDict['May'] 
    totalSeasonDict['Summer'] = totalMonthDict['June'] + totalMonthDict['July'] + totalMonthDict['August'] 
    totalSeasonDict['Autumn'] = totalMonthDict['September'] + totalMonthDict['October'] + totalMonthDict['November'] 

    #Pie chart with labels, values, precentages and decorations
    plt.pie(list(totalSeasonDict.values()), startangle=-90, labels=list(totalSeasonDict.keys()), explode=[0,0,0.1,0], shadow=True, autopct='%0.0d%%')
    plt.title("Reservations Per Season:")
    #Save Pie chart
    plt.savefig(".seasonStats.png")
    plt.close()

def calcRoomTypeStats():
    roomTypeDict = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0,
        "H" : 0,
        "L" : 0,
        "P" : 0
    }
    counter = 0
    #Count reservations for each room type:
    for lines in csvFile:
        roomTypeDict[lines['reserved_room_type']] += 1
        counter += 1
    
    #Pie Chart with values, Labels of the top 3 room types and decorations
    plt.tight_layout()
    plt.pie(list(roomTypeDict.values()), startangle=90, labels = ["A", "", "", "D", "E", "", "", "", "", ""], labeldistance=.6)
    # Create labels for the legend with format: label: xx.xx% 
    labels = [f'{l}: {round(s/counter*100, 2)}%' for l, s in zip(list(roomTypeDict.keys()),roomTypeDict.values())]
    plt.legend(shadow=True, labels=labels, bbox_to_anchor=(0.05,0.8), loc='center right')
    plt.title("Room Type Reservations:")
    #save pie chart
    plt.savefig(".roomTypeStats.png")
    plt.close()

def calcVisitorTypeStats():
    visitorTypeDict = {
        "Families" : 0,
        "Couples" : 0,
        "Alone Travelers" : 0
    }
    
    #count reservations for each visitor type
    for lines in csvFile:
        if lines['adults'] == 1 and lines['children'] == 0:
            visitorTypeDict['Alone Travelers'] += 1
        elif lines['adults'] == 2 and lines['children'] == 0:
            visitorTypeDict['Couples'] += 1
        elif lines['adults'] >= 1 and lines['children'] >= 0:
            visitorTypeDict['Families'] += 1

    #Pie chart with labels, number of reservations, precentage and decorations
    plt.tight_layout()
    plt.pie(list(visitorTypeDict.values()),labels=[f'{l}\n{s}' for l, s in zip(list(visitorTypeDict.keys()), visitorTypeDict.values())], autopct='%1.1f%%', shadow=True, explode=([0.1, 0.1, 0.2]))
    plt.title("Type of Visitors:")
    #save pie chart
    plt.savefig(".visitorTypeStats.png")
    plt.close()

def calcTrend():
    #calc total Reservation for each month of each year
    df['reservations'] = 1  #Add a new collumn with the constant 1
    #Make a series with only each month and the total number of reservations for this month = sum of reservations = 1+1+...+1
    resampledDF = df.resample('ME').sum()['reservations']
    #x = [1, 2, ..., 26]
    x = range(26)
    y = resampledDF.tolist()
    
    #Calculate Linear Regression
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    regression_line = slope * x + intercept #Array with values of the trend line for each month
    
    #Make type series to type dataFrame
    resampledDF = resampledDF.to_frame()

    #Add collumn 'Trend' with values of trend line
    resampledDF['Trend'] = regression_line
    #Plot reservations per month AND the trend line
    resampledDF.plot()
    #Plot Decorations
    plt.grid()
    plt.legend()
    plt.title("Trend of Reservations over time:")
    plt.tight_layout()
    #save plot
    plt.savefig(".trend.png")
    plt.close() 
