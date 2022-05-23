#
# Example file for working with timedelta objects
#

from datetime import date, time, datetime, timedelta

# Construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# Print today's date
now = datetime.now()
print('Today is ' + str(now))

# Print today's date one year from now
print('One year from now it will be: ' + str(now + timedelta(days=365)))

# Create a timedelta that uses more than one argument
print(
    'In 2 days and 3 weeks, it will be: '
    + str(now + timedelta(days=2, weeks=3))
)

# Calculate the date 1 week ago, formatted as a string
t = now - timedelta(weeks=1)
s = t.strftime('%A %B %d, %Y')
print('One week ago was:', s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# Use date comparison to see if April Fools' has already gone for this year and
# if it has, use the replace() function to get the date for next year
if afd < today:
    print(
        'April Fool\'s day already went by %d days ago' % ((today - afd).days)
    )
    afd = afd.replace(year=today.year + 1)

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print('It\'s just', time_to_afd.days, 'days until April Fool\'s Day')
