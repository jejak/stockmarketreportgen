# -*- coding: utf-8 -*-
"""
    Test case file to test marketreport

    To run the this unittest use the below commands
    > cd Code
    > python -m unittest tests/test_stockmarketreportgen.py

"""
import unittest
import json
from stockmarketreportgen.main import generateStockMarketReport

class TestStockMarketReport(unittest.TestCase):

    def test_allkeys_present_in_report(self):
        """
            Check all of the generated report items have all required keys and only those keys.
            The test case uses a sample marketdata.json available on the internet
        """
        url = "http://ws.jenojakab.com/files/marketdata001.json"
        jsonReport = generateStockMarketReport(url)
        report = json.loads(jsonReport)
        for item in report:
            self.assertEqual(3, len(item.keys()))
            self.assertIn('ticker', item)
            self.assertIn('price', item)
            self.assertIn('isin', item)

if __name__ == '__main__':
    unittest.main()
