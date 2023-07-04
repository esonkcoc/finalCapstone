import math

print("Investment- To calculate the amount of interest you'll earn on your investment.\nBond- To calculate the amount you'll have to pay on a home loan.")
print()
calculator=input("Enter either 'Investment' or 'Bond' to choose which calculator you'd like to use: ")
print()

#The investment calculation
if calculator=="investment"or calculator=="Investment"or calculator=="INVESTMENT":
    deposit=float(input("How much money are you depositing in GBP? "))
    rate=float(input("At what rate of interest, as a percentage? "))
#Logic error fix
    rate=rate/100
    time=float(input("Over how many years? "))
    interest=input("Are you calculating for 'Simple' or 'Compound' interest? ")

#The simple interest calculation
    if interest=="simple"or interest=="Simple"or interest=="SIMPLE":
        amount=deposit*(1+rate*time)
        print()
#rate*100 to give the percentage rate, following logic error fix
        print("The simple "+str(rate*100)+" percent rate of return on your "+str(deposit)+" GBP investment over "+str(time)+" years will be "+str(amount)+" GBP.")

#The compound interest calculation
    elif interest=="compound"or interest=="Compound"or interest=="COMPOUND":
        amount=deposit*math.pow((1+rate),time)
        print()
#rate*100 to give the percentage rate, following logic error fix
        print("The compound "+str(rate*100)+" percent rate of return on your "+str(deposit)+" GBP investment over "+str(time)+" years will be "+str(amount)+" GBP.")

#Error message
    else:
        ("Invalid input. Try again and only enter either 'Simple' or 'Compound'.")

#The bond calculation
elif calculator =="bond"or calculator=="Bond"or calculator=="BOND":
    value=float(input("What is the value of the house in GBP? "))
    rate2=float(input("At what rate of interest, as a percentage? "))
    time2=float(input("Over how many months? "))
    i=float((rate2/100)/12)
    repayment=(i*value)/(1-(1+i)**(-time2))
    print()
    print("The rate of repayment on the value of "+str(value)+" GBP at "+str(rate2)+" percent over "+str(time2)+" months will be "+str(repayment)+" GBP per month.")

#Error message
else:
    print("Invalid input. Try again and only enter either 'Investment' or 'Bond'.")