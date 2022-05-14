def APOD_Random_date(start,end):
# function to return a random date between 2 given dates

    # import required packages
    from random import randrange
    from datetime import timedelta
    from datetime import datetime
    
    # convert to datetime objects
    end_date   = datetime.strptime(end,'%Y-%m-%d')
    start_date = datetime.strptime(start,'%Y-%m-%d')
    
    # calculate delta between datetime objects
    delta = end_date -start_date
    
    # calculate random number in range
    random_day = randrange(delta.days)
    
    # convert to datetime object
    random_date = start_date + timedelta(days = random_day)
    
    # output date
    output_date = random_date.strftime('%Y-%m-%d')
    
    # return random day in range    
    return output_date

#from random import randrange
#from datetime import timedelta

####################################
# test 
####################################

#from datetime import datetime

# # get today's date
#end_date   = datetime.today().strftime('%Y-%m-%d')
#start_date = "1995-06-16"

#end   = datetime.strptime(end_date,'%Y-%m-%d')
#start = datetime.strptime(start_date,'%Y-%m-%d')

# # get start date


# # call function
#date_r = APOD_Random_date(start_date,end_date)

# # print
#print(date_r)
