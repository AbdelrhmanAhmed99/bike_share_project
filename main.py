import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'data/chicago.csv',
             'new york city': 'data/new_york_city.csv',
             'washington': 'data/washington.csv'}
MONTH = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


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

    while True:
        try:
            city = input("plz enter your city to city : 1- new york city 2 - chicago 3 - washington \n").lower()
            if city not in CITY_DATA.keys():
                print("please enter valid city")
                continue
            break
        except:
            print("please enter valid city")
    while True:
        try:

            day = input("plz enter your day or just type all \n").lower()
            if day not in DAY:
                print("please enter valid day")
                continue
            break
        except:
            print("please enter valid day")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:

            month = input("plz enter your month from jaunuary to june or just type all \n").lower()
            if month not in MONTH:
                print("please enter valid month")
                continue
            break
        except:
            print("please enter valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-' * 40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if day != 'all':
        df = df[df['day_of_week'] == day]

    if month != 'all':
        Months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = Months.index(month) + 1
        df = df[df['month'] == month]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()

    print("Most Popular Month is :{}".format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()
    print("most common day is : {}".format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()

    print('Most Common Start Hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print("the most common start station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()

    print("\nThe most commonly used end station:{}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'from' + df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
    common_trip = df['trip'].mode()
    print("the most common trips taken are : {}".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_time = df['Trip Duration'].sum()
    minute, sec = divmod(total_duration_time, 60)
    hour, minute = divmod(minute, 60)
    print("the total trip duration is {} hours , {} minutes and {} secounds".format(hour, minute, sec))

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    minute, sec = divmod(average_duration, 60)
    hour, minute = divmod(minute, 60)
    print("the average trip duration is {} hours , {} minutes and {} secounds".format(hour, minute, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print("user types count : {} ".format(user_type))
    # TO DO: Display counts of gender

    if city == 'washington':

        print("washington data doesn't have gender column")
    else:
        gender_counts = df['Gender'].value_counts()
        print("the count of genders are : {}".format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print("washington data doesn't have birth column")
    else:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("the earliest , recent and common year are : {} , {} and {}".format(earliest, recent, common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
