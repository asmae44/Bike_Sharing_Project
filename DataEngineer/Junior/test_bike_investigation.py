import unittest
import pandas as pd
from bike_investigation import time_stats, station_stats, trip_duration_stats, user_stats

class TestBikeShareData(unittest.TestCase):

    def setUp(self):
        """
        Set up the data for the tests.
        """
        # Sample data for testing
        self.data = {
            'Start Time': ['2017-01-01 09:07:57', '2017-01-02 09:07:57', '2017-01-03 00:07:57'],
            'End Time': ['2017-01-01 09:20:53', '2017-01-02 09:20:53', '2017-01-03 00:20:53'],
            'Start Station': ['Station A', 'Station B', 'Station C'],
            'End Station': ['Station B', 'Station C', 'Station A'],
            'Trip Duration': [800, 600, 1000],
            'User Type': ['Subscriber', 'Customer', 'Subscriber'],
            'Gender': ['Male', 'Female', 'Male'],
            'Birth Year': [1985, 1990, 1985]
        }
        self.df = pd.DataFrame(self.data)
        self.df['Start Time'] = pd.to_datetime(self.df['Start Time'])
        self.df['End Time'] = pd.to_datetime(self.df['End Time'])

    def test_time_stats(self):
        """
        Test the time_stats function.
        """
        result = time_stats(self.df)
        self.assertEqual(result['mostCommonMonth'], 'january')
        self.assertEqual(result['mostCommonDayOfWeek'], 'sunday')
        self.assertEqual(result['mostCommonStartHour'], 9)

    def test_station_stats(self):
        """
        Test the station_stats function.
        """
        result = station_stats(self.df)
        self.assertEqual(result['mostCommonStartStation'], 'Station A')
        self.assertEqual(result['mostCommonEndStation'], 'Station A')
        self.assertEqual(result['mostCommonTrip'], 'Station A to Station B')

    def test_trip_duration_stats(self):
        """
        Test the trip_duration_stats function.
        """
        result = trip_duration_stats(self.df)
        self.assertEqual(result['totalTravelTime'], 2400)
        self.assertEqual(result['meanTravelTime'], 800)

    def test_user_stats(self):
        """
        Test the user_stats function.
        """
        result = user_stats(self.df)
        self.assertEqual(result['userTypeCounts']['Subscriber'], 2)
        self.assertEqual(result['userTypeCounts']['Customer'], 1)
        self.assertEqual(result['genderCounts']['Male'], 2)
        self.assertEqual(result['genderCounts']['Female'], 1)
        self.assertEqual(result['earliestYear'], 1985)
        self.assertEqual(result['mostRecentYear'], 1990)
        self.assertEqual(result['mostCommonYear'], 1985)

if __name__ == '__main__':
    unittest.main()
