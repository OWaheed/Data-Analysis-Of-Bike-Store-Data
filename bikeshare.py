import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def validate_answer(answer, choices):
    """
    this function is used to check if the  answer provided by the user belongs to possible choices
    and if it don't the function  ask for new valid answer 
    Returns:
    (str) answer if the answer is valid 
    
    """
    while True:
        answer = answer.lower()
        if answer not in choices:
            answer = input("\n please enter one of the following : " + " , ".join(choices) + "\n")
        else:
            return answer


def choose_city():
    """
    This function Asks user for the city he want to filter with 
    Returns:
    (str) The City name which use choosed 
    """
    city = input('\n Which country would  You like to see it\'s data for Chicago ,New York City or Washington ?\n')
    city = validate_answer(city, ["chicago", "new york city", "washington"])
    return city


def choose_filter():
    """ 
    this function asks the user to enter a time filter and call function to validate his answer 
     Returns:
    (str) The Choosen filter by the customer 
    
    """
    Filter = input(
        "\n would you like to filter data with month ,day ,both or no filter ? type none for no time filter \n")
    Filter = validate_answer(Filter, ["month", "day", "both", "none"])
    return Filter


def choose_month():
    """ 
    this function asks the user to choose month to filter the data with it  
     Returns:
    (str) The Choosen month by the customer
    
    """
    month = input("\n Which month would you like to choose January , Febreuary , March , April , May , June\n")
    month = validate_answer(month, ["january", "febreuary", "march", "april", "may", "june"])
    return month


def choose_day():
    """ 
    this function asks the user to choose day to filter the data with it  
     Returns:
    (str) The Choosen day by the customer
    
    """
    day = input(
        "\nWhich day of the week  would you like to choose Sunday , Monday , Tuesday , Wednesday  , Thrusday , Friday or all \n")
    day = validate_answer(day, ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"])
    return day


def most_common_month(df):
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most popular hour
    popular_month = df['month'].mode()[0]
    return popular_month


def most_common_day_of_week(df):
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.day_name()

    # find the most popular day of week
    popular_day = df['day'].mode()[0]
    return popular_day


def most_common_hour_of_day(df):
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    return popular_hour


def most_common_start_station(df):
    popular_start_station = df["Start Station"].mode()[0]
    return popular_start_station


def most_common_end_station(df):
    popular_end_station = df["End Station"].mode()[0]
    return popular_end_station


def most_common_trip(df):
    df["Trip"] = "from " + df["Start Station"] + " to " + df["End Station"]
    popular_trip = df["Trip"].mode()[0]
    return popular_trip


def users_counts(df):
    user_types = df['User Type'].value_counts()
    return user_types


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = choose_city()
    Filter = choose_filter()
    if Filter == "month":
        # TO DO: get user input for month (all, january, february, ... , june)
        month = choose_month()
        day = "all"
    elif Filter == "day":
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = choose_day()
        month = "all"
    elif Filter == "both":
        month = choose_month()
        day = choose_day()
    else:
        month = "all"
        day = "all"

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # df['day_of_week'] = pd.to_datetime(df['Start Time']).weekday_name
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'febreuary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = most_common_month(df)
    print("The most Common Month : " + str(common_month))
    # TO DO: display the most common day of week
    common_day = most_common_day_of_week(df)
    print("The most Common day : " + common_day)
    # TO DO: display the most common start hour
    common_hour = most_common_hour_of_day(df)
    print("The most Common hour : " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station is :\n", most_common_start_station(df))
    # TO DO: display most commonly used end station
    print("\nThe most commonly used end station is :\n", most_common_end_station(df))

    # TO DO: display most frequent combination of start station and end station trip
    print("\nThe most frequent combination of start station and end station trip is :\n", most_common_trip(df))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df["Trip Duration"].sum()
    print("Total  travel time  is : " + str(total))

    # TO DO: display mean travel time
    print("Mean  travel time  is : " + str(total / len(df)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types Count :\n")
    for x, y in user_types.iteritems():
        print("Count of " + x + " is: " + str(y))
    # TO DO: Display counts of gender
    if city == "washington":
        print("Gender Column in not available in washington")
    else:
        user_genders = df["Gender"].value_counts()
        print("\nUsers Genders Count:\n")
        for x, y in user_genders.iteritems():
            print("Count of " + x + " is: " + str(y))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "washington":
        print("earliest, most recent, most common year of birth  in not available in washington")
    else:
        print("Earliest year of birth is : " + str(df["Birth Year"].min()))
        print("Most Recent year of birth is : " + str(df["Birth Year"].max()))
        print("Most Common year of birth is : " + str(df["Birth Year"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def print_data(df):
    counter = 6
    while True:
        answer = input("\n Would you like to see the raw data ? answer with yes or no \n")
        answer = validate_answer(answer, ["yes", "no"])
        if answer == "yes":
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(df[counter - 6:counter])
                counter += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        print_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
