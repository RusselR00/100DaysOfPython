#  Considerthesoftwarethatrunsonaself-checkoutmachine.Onetaskthatitmustbe
#  abletoperformistodeterminehowmuchchangetoprovidewhentheshopperpays
#  forapurchasewithcash.
#  Writeaprogramthatbeginsbyreadinganumberofcentsfromtheuserasan
#  integer.Thenyourprogramshouldcomputeanddisplaythedenominationsof the
#  coinsthatshouldbeusedtogivethatamountofchangetotheshopper.Thechange
#  shouldbegivenusingasfewcoinsaspossible.Assumethatthemachineisloaded
#  withpennies,nickels,dimes,quarters,looniesandtoonies
#  Aonedollarcoinwas introducedinCanada in1987. It is referredtoasa
#  looniebecauseonesideofthecoinhasaloon(atypeofbird)onit.Thetwo
#  dollarcoin,referredtoasatoonie,wasintroduced9yearslater.It’snameis
#  derivedfromthecombinationofthenumbertwoandthenameoftheloonie

def calculate_change(cents):
    
    coin_values = {
        "Toonies (2 dollars)": 200,
        "Loonies (1 dollar)": 100,
        "Quarters (25 cents)": 25,
        "Dimes (10 cents)": 10,
        "Nickels (5 cents)": 5,
        "Pennies (1 cent)": 1
    }


    change = {}


    for coin, value in coin_values.items():
        count = cents // value
        if count > 0:
            change[coin] = count
        cents %= value

    return change



cents = int(input("Enter the amount of change in cents: "))
change = calculate_change(cents)

print("\nChange can be given as:")
for coin, count in change.items():
    print(f"{count} x {coin}")