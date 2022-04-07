def set_annual():
    global annual
    annual = 10000


def print_monthly():
    print("Your monthly payment is " + str(annual / 12) + " USD.")


set_annual()
print_monthly()
