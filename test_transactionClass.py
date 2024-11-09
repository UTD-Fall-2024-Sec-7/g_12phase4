import unittest
from unittest.mock import patch
import importlib
import io
import json
import sys

# Requests can end up throttled sometimes and break output, reset window if that happens

class TestTransactionClass(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements in each test because of how transactionClass is set up
        self.fake_out = io.StringIO()
        sys.stdout = self.fake_out

    def tearDown(self):
        # Reset stdout and ensure a fresh reload of transactionClass in each test (otherwise code breaks)
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=["", ""])  # Empty ticker and representative
    def test_case_1_empty_ticker_representative(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload to reset (breaks otherwise)
        transactionClass.transactionClass()  
        output = self.fake_out.getvalue().strip() # Capture output to analyze

        print("\n[Test Case 1 - Empty Ticker and Representative] Output received:")
        print(repr(output))

        self.assertGreater(len(output), 2, "Output should not be empty")
        try:
            result = json.loads(output)
            self.assertIsInstance(result, list, "Output should be a list of transactions")
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON format")

    @patch('builtins.input', side_effect=["AMZN", ""])  # Ticker AMZN, empty representative
    def test_case_2_ticker_amzn(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload for fresh start
        transactionClass.transactionClass()  
        output = self.fake_out.getvalue().strip()

        print("\n[Test Case 2 - Ticker AMZN] Output received:")
        print(repr(output))

        if not output:
            self.fail("Output is empty when it should contain JSON data.")
        
        try:
            result = json.loads(output)
            for transaction in result:
                self.assertEqual(transaction["Ticker"], "AMZN", "Ticker search failed")
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON format")

    @patch('builtins.input', side_effect=["", "Josh Gottheimer"])  # Empty ticker, representative as Josh
    def test_case_3_representative_josh(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload
        transactionClass.transactionClass() 
        output = self.fake_out.getvalue().strip()

        print("\n[Test Case 3 - Representative Josh Gottheimer] Output received:")
        print(repr(output))

        if not output:
            self.fail("Output is empty when it should contain JSON data.")
        
        try:
            result = json.loads(output)
            for transaction in result:
                self.assertEqual(transaction["Representative"], "Josh Gottheimer", "Name search failed")
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON format")

    @patch('builtins.input', side_effect=["$$$$$$", ""])  # Invalid ticker $$$$$$, empty representative
    def test_case_4_invalid_ticker(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload for each test
        transactionClass.transactionClass() 
        output = self.fake_out.getvalue().strip()

        print("\n[Test Case 4 - Invalid Ticker $$$$$$] Output received:")
        print(repr(output))

        # Expected outcome: Empty array or error
        self.assertEqual(output, "[]", "Expected empty array for invalid ticker")

    @patch('builtins.input', side_effect=["", "Jo4n D@e?"])  # Empty ticker, representative with special characters
    def test_case_5_invalid_representative(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload for each test
        transactionClass.transactionClass()
        output = self.fake_out.getvalue().strip()

        print("\n[Test Case 5 - Invalid Representative Jo4n D@e?] Output received:")
        print(repr(output))

        # Expected outcome: Empty array or appropriate error response
        self.assertEqual(output, "[]", "Expected empty array for invalid representative")

    @patch('builtins.input', side_effect=["TEL", "Josh Gottheimer"])  # Ticker TEL, representative as Josh
    def test_case_6_ticker_tel_representative_josh(self, mock_input):
        import transactionClass
        importlib.reload(transactionClass)  # Reload for each test
        transactionClass.transactionClass()  
        output = self.fake_out.getvalue().strip()

        print("\n[Test Case 6 - Ticker TEL and Representative Josh Gottheimer] Output received:")
        print(repr(output))

        if not output:
            self.fail("Output is empty when it should contain JSON data.")
        
        try:
            result = json.loads(output)
            for transaction in result:
                self.assertEqual(transaction["Ticker"], "TEL", "Ticker search failed")
                self.assertEqual(transaction["Representative"], "Josh Gottheimer", "Representative search failed")
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON format")

if __name__ == '__main__':
    unittest.main()
