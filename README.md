# Stock Market Report Generator

This is a proto software to demonstrate how stock market reports can be generated in a banking environment taking the market data from the internet from an other banking subsidiary.

The program does the following:

   * Fetch the JSON stock market data from marketdata.json via a HTTP request
   * Print a list of stock tickers, the ISIN (the id field in the marketdata.json) and their price in JSON format (see below).

For example:

* > stockmarketreportgen http://ws.jenojakab.com/files/marketdata001.json

````````````````````
[
 {
   "ticker": "CBA",
   "price": 21.51,
   "isin": "US92345678901"
 },
 {
   "ticker": "CBB",
   "price": 401.5,
   "isin": "US10987694321"
 },
 ...
]
````````````````````

  The project also provides:
     * unit tests and
     * documentation

## Design

* the choice of programming language is: python
* use the requests python index package to do http get for retrieve the stock market data from the internet
* the python standard library json package natively support the json format
* used json.loads() and json.dumps() to do conversion between json and python expressions

Call Follow
- get the marketdata url from the command-line arguments
- using 'requests' pypi package to fetch market data through http.get
- process the received json content
- the content is supposed to be an array of market data items (correspond to python dict)
- convert the json to a python array via JSON.loads()
- processing the the stock market data to formulate the report data according to the requirements
- create json from the report via json.dumps()
- output the json to standard via print()

Note: any incomplete market data item which cannot supply a fully completed report item (i.e cannot complete all of the reporting fields from it - are excluded from the report

Unit test
- used python unittest
- created one test case
- it is using the task described reference url to get test data  http://ws.jenojakab.com/files/marketdata001.json
- the test checks if all created reporting entry complete in the output json

## Notation

The folder where the git project has been cloned will be referred as **Code** from now.

## To build the program

### Run setup.py install  

To build the program run the following commands.

````````````````````
> cd Code
> python setup.py install
````````````````````

## To run the Market Data program

### Do the build step

Do the above build step

````````````````````````
Usage: stockmarketreportgen <url-of-marketdata-json>
       stockmarketreportgen http://ws.jenojakab.com/files/marketdata001.json
Options:
--help        This help"
````````````````````````

Commands:
````````````````````````
> cd Code
> stockmarketreportgen <url-of-the-marketdata.json>
````````````````````````

## To Run the unit test

````````````````````````
> cd Code
> python -m unittest tests/test_stockmarketreportgen.py
````````````````````````

The test results would genereted on the console.

(Example result)
````````````````````````
> python -m unittest tests/test_stockmarketreportgen.py
.
----------------------------------------------------------------------
Ran 1 test in 0.335s

OK
````````````````````
