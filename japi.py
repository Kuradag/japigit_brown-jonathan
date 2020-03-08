'''
AUTHOR: Jonathan Brown
###########################################################################
DATE: 03/6/2020
###########################################################################
COURSE: IFT 458
###########################################################################
DESCRIPTION: Project Deliverable 5 japi.py for the sake of practicing
API and JSON, following the instructions of 
"Project Deliverable 5 - Git-API.docx"
API KEY: X3O0W6QJKJVZAT9M
'''
#!/usr/bin/python3.7

import urllib.request

def getStockData(stockSymbol):
    '''Had to change the function due to the one in the instructions being removed from
    the API. The one on the course discussions gave too much data. So GLOBAL_QUOTE seemed
    more appropriate.'''
    nasdaqSymbolURL = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=%s&apikey=X3O0W6QJKJVZAT9M' % (stockSymbol)
    connection = urllib.request.urlopen(nasdaqSymbolURL)
    responseString = connection.read().decode()

    return responseString

def main():
    repeat = True
    while repeat:
        stockSymbol = input('Please enter a stock symbol: ')
        stockData = getStockData(stockSymbol)
        print(stockData)
        print("Stock Quotes retrieved successfully!")

        repeatPrompt = input('Another? (y/n): ')
        if repeatPrompt is 'n':
            repeat = False

    return 0

if __name__ == "__main__":
    main()

