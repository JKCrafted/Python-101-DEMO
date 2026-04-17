
def to_years(years, weeks, days, hours, minutes, seconds, milliseconds):
    years += (weeks*7)/365
    years += days/365
    years += hours/(365*24)
    years += minutes/(365*24*60)
    years += seconds/(365*24*60*60)
    years += milliseconds/(365*24*60*60*1000)
    return years


def to_weeks(years, weeks, days, hours, minutes, seconds, milliseconds):
    weeks += (years*365)/7
    weeks += days/7
    weeks += hours/(7*24)
    weeks += minutes/(7*24*60)
    weeks += seconds/(7*24*60*60)
    weeks += milliseconds/(7*24*60*60*1000)
    return weeks

def to_days(years, weeks, days, hours, minutes, seconds, milliseconds):
    days += years*365
    days += weeks*7
    days += hours/24
    days += minutes/(24*60)
    days += seconds/(24*60*60)
    days += milliseconds/(24*60*60*1000)
    return days

def to_hours(years, weeks, days, hours, minutes, seconds, milliseconds):
    hours += years*365*24
    hours += weeks*7*24
    hours += days*24
    hours += minutes/60
    hours += seconds/(60*60)
    hours += milliseconds/(60*60*1000)
    return hours
    
def to_minutes(years, weeks, days, hours, minutes, seconds, milliseconds):
    minutes += years*365*24*60
    minutes += weeks*7*24*60
    minutes += days*24*60
    minutes += hours*60
    minutes += seconds/60
    minutes += milliseconds/(60*1000)
    return minutes
    
def to_seconds(years, weeks, days, hours, minutes, seconds, milliseconds):
    seconds += years*365*24*60*60
    seconds += weeks*7*24*60*60
    seconds += days*24*60*60
    seconds += hours*60*60
    seconds += minutes*60
    seconds += milliseconds/1000
    return seconds
    
def to_milliseconds(years, weeks, days, hours, minutes, seconds, milliseconds):
    milliseconds += years*365*24*60*60*1000
    milliseconds += weeks*7*24*60*60*1000
    milliseconds += days*24*60*60*1000
    milliseconds += hours*60*60*1000
    milliseconds += minutes*60*1000
    milliseconds += seconds*1000
    return milliseconds
    
    
    
    
    
    
input_years = int(input("Years: "))
input_weeks = int(input("Weeks: "))
input_days = int(input("Days: "))
input_hours= int(input("Hours: "))
input_minutes = int(input("Minutes: "))
input_seconds = int(input("Seconds: "))
input_milliseconds = int(input("Milliseconds: "))
    
#input_weeks = 42
#input_weeks = 17
#input_days = 4
#input_hours = 14
#input_minutes = 47
#input_seconds = 32
#input_milliseconds = 4789

print("Total years: "+str(to_years(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total weeks: "+str(to_weeks(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total days: "+str(to_days(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total hours: "+str(to_hours(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total minutes: "+str(to_minutes(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total seconds: "+str(to_seconds(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))
print("Total milliseconds: "+str(to_milliseconds(input_years, input_weeks, input_days, input_hours, input_minutes, input_seconds, input_milliseconds)))