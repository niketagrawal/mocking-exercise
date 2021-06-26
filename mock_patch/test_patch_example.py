import datetime
import unittest
from unittest.mock import patch
from mock_patch import patch_example
from requests.exceptions import Timeout


class TestPatchExample(unittest.TestCase):
    def test_timeout(self):
        with patch('mock_patch.patch_example.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                patch_example.get_holidays()
                mock_requests.get.assert_called_once()

    def test_datetime(self):
        tuesday = datetime.datetime(year=2019, month=1, day=1)
        saturday = datetime.datetime(year=2019, month=1, day=5)
        with patch('mock_patch.patch_example.datetime') as mock_datetime:
            mock_datetime.today.return_value = tuesday
            self.assertEqual(patch_example.is_weekday(), True)
            mock_datetime.today.return_value = saturday
            self.assertEqual(patch_example.is_weekday(), False)


if __name__ == '__main__':
    unittest.main()