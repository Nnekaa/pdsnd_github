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
    print('Hello! Let\'s explore some US bikeshare data!\n')


    while True:
        cities = ['chicago', 'new york city', 'washington']

        city = input("Enter a city name that is either chicago, new york city or washington to explore: ").lower()
        if city not in cities:
            print("You have entered a wrong city name. Try Again")
            continue
        else:
            break

    while True:
        data_filter= input("Will you like to filter this data by month, day or no filter? Please type 'no' if no filter \n type 'month' to filter by month \n type 'day' to filter by day \n type no, month or day: ")
        if data_filter not in ['no', 'month', 'day']:
            print("Wrong input")
        else:
            break

    if data_filter == 'no':
        month = all
        day = all

    # get user input for month (all, january, february, ... , june)
    if data_filter == 'month':
        while True:
            month = input("Which month would you like to filter by: ").lower()
            if month not in ['january', 'february','march', 'april', 'may', 'june']:
                print("Sorry! There is no existing data for that month. select a month between january and june")
                continue
            else:
                break
        day = all

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if data_filter == 'day':
        month = all
        while True:
            day = input("Enter a day of the week between monday and sunday: ").lower()
            if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                print('Wrong day entered. Try Again')
            else:
                break

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

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    if month != all:

        months = ['january', 'february', 'march', 'april', 'may','june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != all:

        df = df[df['day_of_week'] == day.title()]

    if month == all and day == all:
        df

    return df

def raw_data(df):
    """
    Asks user to specify if they wish to view the raw data and the number of rows to view

    Arg:
    df: takes in a dataframe

    prints the raw dataframe
    """

while True:
        user_input = input("Would you like to view raw data ? type 'yes' or 'no' ").lower()
        if user_input == 'yes':
            i = 5
            df1 = df.head(i)
            print(df1)
        else:
           return
        break
    while True:
        more_rows = input("Will you like to see more rows of data? 'yes' or 'no' ").lower()
        if more_rows == 'yes':
            i += 5
            df2 = df.head(i)
            print(df2)
        else:
            return

    if user_input == 'no':
        return


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().head(1).index
    common_month_count = df['month'].value_counts().max()
    months = ['january', 'february', 'march', 'april', 'may','june']
    for month in months:
        if months.index(month) + 1 == common_month:
            print("The most common month is: {} with count {}".format(month, common_month_count))



    # display the most common day of week
    common_day = df['day_of_week'].value_counts().head(1)
    print("The most common day of the week is: {} with count {}".format(common_day.index[0], common_day[0]))


    # display the most common start hour
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['hour'] = df["Start Time"].dt.hour
    common_start_hr = df['hour'].value_counts().head(1)
    print("the most common start hour is {} with count {} \n".format(common_start_hr.index[0], common_start_hr.max()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df["Start Station"].value_counts().head(1)
    print("The most popular start station is {} with count {}".format(start_station.index[0], start_station[0]))


    # display most commonly used end station
    end_station = df["End Station"].value_counts().head(1)
    print("The most popular end station is {} with count {}".format(end_station.index[0], end_station[0]))


    # display most frequent combination of start station and end station trip
    df["start_end station comb"] = df["Start Station"] + "--- " + "TO" + " ---" + df["End Station"]
    start_end_station = df["start_end station comb"].value_counts().head(1)
    print("The most frequent combination of start station and end station trip is: {} with count {} \n".format(start_end_station.index[0], start_end_station[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df["Trip Duration"].sum()
    print("Total travel time is: {}".format(total_trip))

    # display mean travel time
    average_trip = df["Trip Duration"].mean()
    print("Mean travel time is: {} \n".format(average_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    #remove nulls from dataframe

    # Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The user types are {} \n".format(user_types))


    # Display counts of gender
    if "Gender" in df:
        gender = df["Gender"].value_counts()
        print("Gender counts {} \n".format(gender))
    else:
        print("Gender information doesn't exist for this city \n")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest = df["Birth Year"].sort_values().min()
        most_recent = df["Birth Year"].sort_values(ascending = False).max()
        common_year = df["Birth Year"].value_counts().head(1).index[0]

        print("Earliest year of birth: {}".format(earliest))
        print("Most recent year of birth: {}".format(most_recent))
        print("Most common year of birth: {}".format(common_year))

    else:
        print("Birth Year information doesn't exist for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Handle null values
        for i in df:
            if df[i].isnull().sum() != 0:
                df[i] = df[i].fillna(df[i].mode()[0])

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
