from datetime import date

today = date(2021, 7, 30)
bday = date(today.year, 6, 30)
diff = (bday - today).days

if diff > 0:
    print("Birthday in %d days" % diff)
else:
    print("Birthday in %d days" % (diff + 365))
