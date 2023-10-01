import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def get_city():
        while True:
            city = input('Enter a City (chicago, new york city, washington): ').lower()
            if city in ['chicago','new york city', 'washington']:
                return city
            else:
                print('Invalid Input!. Enter a Valid City')
         
    # TO DO: get user input for month (all, january, february, ... , june)
    def get_month():
        while True:
            month = input('Enter a Month (all, january, february, ... , june): ').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                return month
            else:
                print('Invalid Input!. Enter a Valid Month')
         
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day_of_week():
        while True:
            day_of_week = input('Enter a Day (all, monday, tuesday, ... sunday): ').lower()
            if day_of_week in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',                                'saturday', 'sunday']:
                return day_of_week
            else:
                print('Invalid Input!. Enter a Valid Day.')
         
    city = get_city()
    month = get_month()
    day = get_day_of_week()
    
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+ 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] 
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The Most Common Month is: ", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The Most Common Day of The Week is: ", common_day)

    # TO DO: display the most common start hour
    common_st_hour = df['Start Time'].mode()[0]
    print("The Most Common Start Hour is: ", common_st_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_st_station = df['Start Station'].mode()[0]
    print("The most commonly used Start Station is:", common_st_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used End Station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of Start Station and End Station trip is: ',         common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time is: ', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('The Average Travel Time is: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types are: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The counts of gender are: ', gender_count)
    else:
        print('Gender data is not available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is: {}, \nThe most recent birth year is: {}, \nThe most common birth year is: {}\n'.format(earliest_birth_year, recent_birth_year, common_birth_year))
    else:
        print('Birth year data is not available for this city.')

    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)

def display_data(df):
    """Display 5 rows of raw data from the data base files"""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no:\n').lower()
    start_loc = 0
    while view_data == 'yes':
        rows = df.iloc[start_loc:start_loc+5]
        print('\nThis is the first 5 rows of data:\n', rows)
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    
    print(f"\nThis took {time.time() - start_time} seconds.")
    print('-' * 40)
    
def references(df):
    """Reference list"""
    name = 'Sanni Ibrahim'
    reference = 'Udacity Team - https://learn.udacity.com/ and the udacity bot.'
    
    print('This Code Was Completed and Debugged by: {}, \nWith the help of the:{}'.format(name, reference))
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        references(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
