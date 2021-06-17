'''
In the Testclass make a mocked version of the original function, give it the 
same name. Set the mocked function as a class variable and then use self. 
notation inside the mocked function definition. It is not needed to call the 
original function inside the test for that function when mocking is being used.
Instead, we call the mocked version of that function inside it. The mock 
version for a function fun() needs to be in the same class as a member function
and can be named mock_fun() to avoid confusion. The test function can be named 
in the usual way test_fun()
'''

import datetime
import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

class TestCalendar(unittest.TestCase):
    
    datetime = Mock()
    requests = Mock()

    def mock_is_weekday(self):
        # Save a couple of test days
        today = self.datetime.datetime.today()
        # Python's datetime library treats Monday as 0 and Sunday as 6
        # Mock datetime to control today's date
        return (0 <= today.weekday() < 5)
    
    def test_is_weekday(self):
        tuesday = datetime.datetime(year=2019, month=1, day=1)
        saturday = datetime.datetime(year=2019, month=1, day=5)
        # Mock .today() to return Tuesday
        self.datetime.datetime.today.return_value = tuesday
        # Test Tuesday is a weekday
        assert self.mock_is_weekday()
        # Mock .today() to return Saturday
        self.datetime.datetime.today.return_value = saturday
        # Test Saturday is not a weekday
        assert not self.mock_is_weekday()

    def mock_get_holidays(self):
        r = self.requests.get('http://localhost/api/holidays')
        if r.status_code == 200:
            return r.json()
        return None

    def test_get_holidays_timeout(self):
        # Test a connection timeout
        self.requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            self.mock_get_holidays()

if __name__ == '__main__':
    unittest.main()