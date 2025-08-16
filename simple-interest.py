"""Program to calculate simple interest."""

def simple_interest(principal,time=2,rate=5):
    """
    This funcion accepts principal, time, and rate and calculates
    simple interest

    Note: enter rate as percent without the percent(%) sign
    Note: enter time as years, ie, give 6 months as 0.5 and so on
    """

    rate /= 100
    interest = principal*time*rate

    return interest


amt = float(input("Enter the amount you deposited: "))
time = float(input("Enter for how many years you have deposited: "))
roi = float(input("Enter the rate of interest (without the '%' sign): \
"))
print(f"Your interest for {amt} is", simple_interest(amt,time,roi))

