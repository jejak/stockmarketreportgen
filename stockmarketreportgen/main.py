# -*- coding: utf-8 -*-

"""
 Implementation of Stock Market Report Generator proto-software

 It is a program which does the following:

 Fetch the JSON market data from marketdata.json via a HTTP request
 Print a list of stock tickers, the ISIN (the id field in the marketdata.json) and their price in JSON format (see below).
 Implement tests and documentation as you see fit, especially around any design decisions you make.

 For example:

 $ ./stockmarketreportgen http://ws.jenojakab.com/files/marketdata001.json
 [
   {
     "ticker": "ABC",
     "price": 10.50,
     "isin": "US1234567890"
   },
   {
     "ticker": "BBB",
     "price": 400.0,
     "isin": "US0987654321"
   },
   ...
 ]

"""

import sys
import requests
import json

def main():
    if(len(sys.argv) < 2):
        print("Insufficient number of arguments ...", file = sys.stderr)
        printUsage(out=sys.stderr)
    elif((sys.argv[1] == "-help") or (sys.argv[1] == "--help")):
        printUsage(True)
    else:
        stockMarketDataUrl = sys.argv[1]
        try:
            jsonReport = generateStockMarketReport(stockMarketDataUrl)
            print(jsonReport)
        except:
            print('marketDataUrl: {0}'.format(stockMarketDataUrl), file = sys.stderr)
            print("Cannot access remote file ...", file = sys.stderr)


def printUsage(descOn=False, out=sys.stdout):
    """Print program usage"""

    # Print Description
    if(descOn):
        print("""
Program fetches the JSON market data from marketdata.json via a HTTP request.
Print a list of stock tickers, the ISIN (the id field in the marketdata.json) and their price in JSON format


        """)
    # Print Usage
    print("""
Usage: marketreport <url-of-marketdata-json>
       marketreport http://alert-generation-question.rockall-laser.com/ffc9c8e9-f929-46db-ac5c-7c483c647568/marketdata.json

Options:
    --help        Prints this help



    """, file=out)

def retrieveStockMarketData(marketDataUrl):
    r = requests.get(marketDataUrl)
    if(r.status_code != 200):
        r.raise_for_status()
    return r.json()

def generateStockMarketReport(stockMarketDataUrl):
    stockMarketData = retrieveStockMarketData(stockMarketDataUrl)
    report = [
        {
            'ticker': item['ticker'],
            'price': item['price'],
            'isin' : item['id']
        }
        for item in stockMarketData if(('ticker' in item) and ('price' in item) and ('id' in item))
    ]
    jsonReport = json.dumps(report)
    return jsonReport
