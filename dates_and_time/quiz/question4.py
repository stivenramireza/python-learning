from datetime import date

today = date.today()
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print('Tomorrow will be ' + days[(today.weekday() + 1) % 7])
