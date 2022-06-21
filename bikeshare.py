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
    CITY_DATA = ['chicago','new york city','washington']
    months = ['all','january','february','march','april','may','june']
    days = ['all', 'monday' , 'tuesday', 'wednesday',' thursday', 'friday', 'saturday', 'sunday']
    
              
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago,     new york city, washington). HINT: Use a while loop to handle invalid inputs
    city  = input('please enter the city: ').lower().strip()
    while city not in CITY_DATA:
        city = input('value is invalied please enter the city chicago,new york city, washington)  : ').lower().strip()
     

    # TO DO: get user input for month (all, january, february, ... , june)
 
    month = input(' please enter the month: ').lower().strip()
    while month not in months:
        month = input('value is invalied please enter the month: ').lower().strip()
 
     
    day = input(' please enter thy day: ').lower().strip()
       
    while day not in days:
        day = input('value is invalied please enter thy day: ').lower().strip()
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
      
           
   


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

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

   
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\n The most common month : ',df['month'].mode()[0]) 
        
    


    # TO DO: display the most common day of week
    print('\n The most common days of week : ',df['day_of_week'].mode()[0])
  
    

    # TO DO: display the most common start hour
    print('\n The most common start hour : ',df['hour'].mode()[0])
     


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n The Most Popular Stations and Trip : ')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n The Most commonly used start Stations and Trip : ',df['Start Station'].mode()[0])


    
    # TO DO: display most commonly used end station
    print('\n The Most commonly used End Stations and Trip : ',df['End Station'].mode()[0])


    

    # TO DO: display most frequent combination of start station and end station trip
          
    
    print('\n The most frequent combination of start and end station : ',(df['End Station'] +df['Start Station']).mode()[0])
    

    

    print("\nThis took %s seconds." % (time.time() - start_time))
          
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
  
    
    
    
    print('\n Total travel time :  ',df['Trip Duration'].sum())
    
    

    

    # TO DO: display mean travel time
    print('\n Mean travel time : ',df['Trip Duration'].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n Counts of user types :  ',df['User Type'].value_counts())
    


    # TO DO: Display counts of gender
    try:
    
       print('\n Counts of gender :   ',df['Gender'].value_counts())
    

    # TO DO: Display earliest, most recent, and most common year of birth
       print('\n Earliest year  of birth   : ',df['Birth Year'].min())
       print('\n Most recent year of birth :  ',df['Birth Year'].max())
       print('\n Most common year of birth :  ',df['Birth Year'].mode()[0])
    

    except KeyError:
      print('\n No data to display') 
   



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def display_row_data(df):
    
     RowData = input('\n Would you like to view 5 row of individual data trip ? Enter yes or no : ')
        
    
    
     if RowData.lower() == 'yes':
          start_loc = 0  
          
     while True :   
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5      
        
        
        RowData = input('\n Would you like to view 5 row of individual data trip ? Enter yes or no : ')
         
         
     
        if RowData.lower() != 'yes':
      
           break   
                 
            


          
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
