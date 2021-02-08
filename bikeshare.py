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
    city_dict = {1: 'chicago', 2: 'new york city', 3: 'washington'}
    month_dict = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'all'}
    day_dict = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday', 8: 'all'}

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_num = int(input('Enter a number corresponding to the desired city: \n1. Chigago \n2. New York City \n3. Washington \nInput: '))
            if city_num in [1, 2, 3]:
                break
            else:
                continue
        except:
            print('That is not a valid entry!')
    print('City number input: ', city_num)
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month_num = int(input('Enter a number corresponding to the desired month: \n1. January \n2. February \n3. March \n4. April \n5. May \n6. June \n7. All Months \nInput: '))
            if month_num in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                continue
        except:
            print('That is not a valid entry!')
    print('Month number input: ', month_num)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day_num = int(input('Enter a number corresponding to the desired day of week: \n1. Monday \n2. Tuesday \n3. Wednesday \n4. Thursday \n5. Friday \n6. Saturday \n7. Sunday \n8. All Days \nInput: '))
            if day_num in [1, 2, 3, 4, 5, 6, 7, 8]:
                break
            else:
                continue
        except:
            print('That is not a valid entry!')
    print('Day of week number input: ', day_num)
    
    city = city_dict[city_num]
    month = month_dict[month_num]
    day = day_dict[day_num]
    
    print()
    print('City selection: ', city)
    print('Month selection: ', month)
    print('Day of week selection: ', day)

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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    month_dict = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The monst common month is: ', month_dict[df['month'].mode()[0]].title())

    # TO DO: display the most common day of week
    print('The monst common day of the week is: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    if df['hour'].mode()[0] < 12:
        print('The monst common start hour is: ', (df['hour'].mode()[0]),'am')
    else:
        print('The monst common start hour is: ', (df['hour'].mode()[0])-12,'pm')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End Station'] = df[['Start Station', 'End Station']].agg(' with '.join, axis=1)
    print('The most frequent combination of start station and end station is: ', df['Start & End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration Min'] = (df['End Time'] - df['Start Time'])/np.timedelta64(1,'m')
    df['Trip Duration Hour'] = (df['End Time'] - df['Start Time'])/np.timedelta64(1,'h')
    print('Total travel time was ', df['Trip Duration Min'].sum(), ' minutes, or ', df['Trip Duration Hour'].sum(), ' hours')

    # TO DO: display mean travel time
    print('Average travel time was ', df['Trip Duration Min'].mean(), ' minutes, or ', df['Trip Duration Hour'].mean(), ' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types: \n', df['User Type'].value_counts())
    print()

    # TO DO: Display counts of gender
    print('Counts of user gender: \n', df['Gender'].value_counts())
    print()

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Earleist User year of birth: ', int(df['Birth Year'].min()))
    print('Most recent User year of birth: ', int(df['Birth Year'].max()))
    print('Most common User year of birth: ', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_date(df):
    """Shows 5 lines of raw data at a time until user stops."""
    print('\nDisplaying filtered raw data...\n')
    print()
    
    start_index = 0
    end_index = 5
        
    while True:
        print(df[start_index : end_index])
        start_index += 5
        end_index += 5
        user_choice = input('Would you like to see the next 5 lines of raw data? \nEnter Y or N \nEnter: ')
        if user_choice.lower() != 'y':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_date(df)

        restart = input('\nWould you like to restart? \nEnter Y or N \nEnter: ')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
