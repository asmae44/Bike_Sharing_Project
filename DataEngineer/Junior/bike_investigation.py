import time
import zipfile
import os
import pandas as pd

CITY_DATA = {
    "chicago": "chicago.csv",
    "new york city": "new_york_city.csv",
    "washington": "washington.csv",
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some bikeshare data!")
    city = input("Give me the city (chicago, new york city, washington):\n").lower()
    month = input("Give me the month (all, january, february, ..., june):\n").lower()
    day = input("Give me the day (all, monday, tuesday, ..., sunday):\n").lower()
    print("-" * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Path to the ZIP file
    zip_file_path = 'DataEngineer/Junior/Bike_raw_data.zip'
    
    # Directory where files will be extracted
    extract_to_path = 'DataEngineer/Junior/Bike_raw_data'
    
    # Ensure the destination directory exists
    os.makedirs(extract_to_path, exist_ok=True)
    
    # Open the ZIP file and extract all files
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
    
    # Load data for each city
    df1 = pd.read_csv(os.path.join(extract_to_path, 'chicago.csv'))
    df2 = pd.read_csv(os.path.join(extract_to_path, 'new_york_city.csv'))
    df3 = pd.read_csv(os.path.join(extract_to_path, 'washington.csv'))
    
    # Add city column
    df1['city'] = 'Chicago'
    df2['city'] = 'New York City'
    df3['city'] = 'Washington'
    
    # Concatenate dataframes
    df = pd.concat([df1, df2, df3], axis=0)
    
    # Convert 'Start Time' and 'End Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # Extract month and day name for filtering
    df['month_name'] = df['End Time'].dt.month_name().str.lower()
    df['day_name'] = df['End Time'].dt.day_name().str.lower()
    
    # Apply filters
    if month != 'all':
        df = df[df['month_name'] == month]
    if day != 'all':
        df = df[df['day_name'] == day]
    if city in CITY_DATA:
        df = df[df['city'].str.lower() == city]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()
    
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    most_common_month = df['month'].mode().iloc[0] if not df['month'].mode().empty else 'none'
    
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    most_common_day_of_week = df['day_of_week'].mode().iloc[0] if not df['day_of_week'].mode().empty else 'none'
    
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode().iloc[0] if not df['hour'].mode().empty else 'none'
    
    print(f"The most common month is: {most_common_month}")
    print(f"The most common day of the week is: {most_common_day_of_week}")
    print(f"The most common start hour is: {most_common_start_hour}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return {
        'mostCommonMonth': most_common_month,
        'mostCommonDayOfWeek': most_common_day_of_week,
        'mostCommonStartHour': most_common_start_hour
    }

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()
    
    most_common_start_station = df['Start Station'].mode().iloc[0] if not df['Start Station'].mode().empty else 'none'
    most_common_end_station = df['End Station'].mode().iloc[0] if not df['End Station'].mode().empty else 'none'
    
    df['Start-End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_trip = df['Start-End Combination'].mode().iloc[0] if not df['Start-End Combination'].mode().empty else 'none'
    
    print(f"The most commonly used start station is: {most_common_start_station}")
    print(f"The most commonly used end station is: {most_common_end_station}")
    print(f"The most frequent combination of start and end station is: {most_common_trip}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return {
        'mostCommonStartStation': most_common_start_station,
        'mostCommonEndStation': most_common_end_station,
        'mostCommonTrip': most_common_trip
    }

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()
    
    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    
    print(f"Total travel time: {total_travel_time} seconds")
    print(f"Mean travel time: {mean_travel_time} seconds")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return {
        'totalTravelTime': total_travel_time,
        'meanTravelTime': mean_travel_time
    }

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()
    
    user_type_counts = df['User Type'].value_counts().to_dict()
    
    gender_counts = df['Gender'].value_counts().to_dict() if 'Gender' in df.columns else {}
    
    earliest_year = int(df['Birth Year'].min()) if 'Birth Year' in df.columns else None
    most_recent_year = int(df['Birth Year'].max()) if 'Birth Year' in df.columns else None
    most_common_year = int(df['Birth Year'].mode().iloc[0]) if 'Birth Year' in df.columns and not df['Birth Year'].mode().empty else None
    
    print("Counts of user types:")
    print(user_type_counts)
    
    if gender_counts:
        print("\nCounts of gender:")
        print(gender_counts)
    else:
        print("\nGender data is not available in this dataset.")
    
    if earliest_year is not None:
        print(f"\nEarliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
    else:
        print("\nBirth Year data is not available in this dataset.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-" * 40)
    
    return {
        'userTypeCounts': user_type_counts,
        'genderCounts': gender_counts,
        'earliestYear': earliest_year,
        'mostRecentYear': most_recent_year,
        'mostCommonYear': most_common_year
    }

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("No data available for the given filters.")
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            print(df.head())

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break

if __name__ == "__main__":
    main()
