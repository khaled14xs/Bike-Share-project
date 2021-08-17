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
    city = input('Please enter the name of the city that you want to see its data').lower()
    while city not in CITY_DATA :
        print ('You have entered an invalid city name, please choose from chicago , new york,  washington :')
        city = input('please enter the name of the city that you want to see data').lower()
        
    filter = input('would you like to filter by month ,day or by both ').lower()
    while filter not in(['month', 'day', 'both']):
        print('You have entered an invalid item')
        filter = input('would you like to filter by month, day or by both ').lower()
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both' :
        month = input('please chose the month :').lower()
        while month not in months :   
            print ('You have entered an invalid month name ')
            month = input('Please chose the month :')
    else :
        month = 'all'


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if filter == 'day' or filter == 'both':
        day = input('Please chose the day :').lower()
        while day not in days :
            print ('You have entered an invalid day name ')
            day = input('Please chose the day :').lower()
    else :
        day = 'all'

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
    
    df = pd.read_csv(CITY_DATA[city])

# convert the Start Time column to datetime ( from Practice Problem #1 )
    df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column (from Practice Problem #1 ))
    df['hour'] =pd.to_datetime(df['Start Time']).dt.hour

 # extract  day of week  and month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month by using the mode of the months
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('The most common month is: {months[month-1]}')
    # displaying the most common day of week by  using the mode of the days
    day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {day}')
    #  displaying the most common start hour using the mode of the hours
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {most_commonly_used_start_station}')

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {most_commonly_used_end_station}')


    # TO DO: display most frequent combination of start station and end station trip
    most_commonly_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most commonly trip is : from {most_commonly_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
     from datetime import timedelta as td

     #Displays statistics on the total and average trip duration

     print('\nCalculating Trip Duration...\n')
     start_time = time.time()

     # TO DO: display total travel time
     total_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
     days =  total_duration.days
     hours =total_duration.seconds // (60*60)
     minutes = total_duration.seconds % (60*60) // 60
     seconds = total_duration.seconds % (60*60) % 60
     print('the total  time of travel is : {days} days {hours} hours {minutes} minutes {seconds} seconds')

     # TO DO: display mean travel time
     average_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
     days =  average_duration.days
     hours = average_duration.seconds // (60*60)
     minutes = average_duration.seconds % (60*60) // 60
     seconds = average_duration.seconds % (60*60) % 60
     print('the average time of travel is : {days} days {hours} hours {minutes} minutes {seconds} seconds')


     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        
        print(df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print(' the earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most comon birth year is: {year.mode()[0]}')
       



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    
    raw = input(' DO you like to diplay raw data  ? ')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.loc[count: count+4])
            print(df.iloc[count: count+5])
            count += 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
           


if __name__ == "__main__":
	main()
