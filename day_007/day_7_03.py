#  Exercise 43:Faces onMoney

#  (31 Lines)

#  It is common for images of a country’s previous leaders, or other individuals of his

# torical significance, to appear on its money.Theindividualsthatappearonbanknotes

#  in the United States are listed in Table 2.1.

#  Write a program that begins by reading the denomination of a banknote from the

#  user. Thenyourprogramshoulddisplaythenameoftheindividualthatappearsonth

# Individualsthat

#  appearonBanknotes Individual Amount

#  GeorgeWashington $1

#  ThomasJefferson $2

#  AbrahamLincoln $5

#  AlexanderHamilton $10

#  AndrewJackson $20

#  UlyssesS.Grant $50

#  BenjaminFranklin $100

#  banknoteoftheenteredamount.Anappropriateerrormessageshouldbedisplayed

#  ifnosuchnoteexists.

#  WhiletwodollarbanknotesarerarelyseenincirculationintheUnitedStates,

#  theyarelegal tenderthatcanbespent just likeanyotherdenomination.The

#  UnitedStateshasalsoissuedbanknotes indenominationsof$500,$1,000,

#  $5,000,and$10,000forpublicuse.However,highdenominationbanknotes

#  havenotbeenprintedsince1945andwereofficiallydiscontinuedin1969.As

#  aresult,wewillnotconsidertheminthisexercise

denominations = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin",
}

try:
    amount = int(input("Enter the denomination of a banknote: "))

    if amount in denominations:
        print(f"The ${amount} banknote features {denominations[amount]}.")
    else:
        print("There is no such banknote denomination.")

except ValueError:
    print("Invalid input. Please enter a numeric amount.")
