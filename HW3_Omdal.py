#Author: Megan Omdal
#Date 10-16-2022
#Description: This program uses modular design to process refunds
#             for salespeople by calculating their meals, miles traveled,
#             gas cost, and lodging only if over 450 miles roundtrip.
#############################################################################
#
#----------------------------------------------------------------------------
def getFirstName():
    firstName = " "
    firstName = input("Enter salesperson's first name: ")
    return firstName
#end getFirstname
#----------------------------------------------------------------------------
def getLastName():
    lastName = " "
    lastName = input("Enter salesperson's last name: ")
    return lastName
#end getLastName
#----------------------------------------------------------------------------
def getMealsCost():
    mealsCost = 0.0
    mealsCost = eval(input("Enter the total cost of meals: "))
    return mealsCost
#end getMealsCost
#----------------------------------------------------------------------------
def getMilesTraveled():
    milesTraveled = 0.0
    milesTraveled = eval(input("Enter the total miles traveled: "))
    return milesTraveled
#end getMilesTraveled
#----------------------------------------------------------------------------
def getGasCost():
    gasCost = 0.0
    gasCost = eval(input("Enter the total gas cost: "))
    return gasCost
#end getGasCost
#----------------------------------------------------------------------------
def getLodgingCost():
    lodgingCost = 0.0
    lodgingCost = eval(input("Enter the total cost of lodging: "))
    return lodgingCost
#end getLodgingCost
#----------------------------------------------------------------------------
def calcMilesRefund(milesTraveled):
    milesRefund = 0.0 #this calc will decide the refund amount for miles traveled.
    milesRefund = milesTraveled * .50
    return milesRefund
#end calcMilesRefund
#-----------------------------------------------------------------------------------------
def calcTotalRefund(mealsCost, gasCost, milesTraveled, milesRefund, lodgingCost):
    totalRefund = 0.0
    if milesTraveled < 450:
        totalRefund = mealsCost + gasCost + milesRefund
    else:
        milesTraveled >= 450
        totalRefund = mealsCost + gasCost + milesRefund + lodgingCost
    return totalRefund
#end calcTotalRefund
#-----------------------------------------------------------------------------------------------
def displayReport(firstName, lastName, mealsCost, milesTraveled, gasCost, milesRefund, lodgingCost, totalRefund):
    print("The following is the refund amount for " , firstName,"", lastName, ":")
    print(      "Meals Cost     : $", mealsCost, "\n",     \
                "Miles Traveled : ", milesTraveled, "\n",   \
                "Miles Refund   : $", milesRefund, "\n",     \
                "Lodging Cost   : $", lodgingCost, "\n",     \
                "Gas Cost       : $", gasCost, "\n",          \
                "Total Refund   : $", totalRefund)
    
#-------------------------------------------------------------------------------------------------   
#
#
def main():
    #Declaration:
    firstName = " "
    lastName = " "
    mealsCost = 0.0
    milesTraveled = 0
    gasCost = 0.0
    lodgingCost = 0.0
    milesRefund = 0.0
    totalRefund = 0.0
    start = 0
    answer = 1
    #Processes:
    start = eval(input("This program calculates Acme Inc's salesperson's refund for travel. "  \
                       "Would you like to start? Press 1 for yes or 0 for no. "))
    if start == 0:
        print("Thank you for visiting!")
    else: #start == 1 user wants to continue
        while answer == 1:
            #input:
            firstName     = getFirstName()
            lastName      = getLastName()
            mealsCost     = getMealsCost()
            milesTraveled = getMilesTraveled()
            gasCost       = getGasCost()
            lodgingCost   = getLodgingCost()
            #calculate the refund cost for miles traveled:
            milesRefund   = calcMilesRefund(milesTraveled)
            #calculate the total refund:
            totalRefund   = calcTotalRefund(mealsCost, gasCost, milesTraveled, milesRefund, lodgingCost)
            #display the report
            displayReport(firstName, lastName, mealsCost, milesTraveled, gasCost, milesRefund, lodgingCost, totalRefund)
            #process another salesperson?
            answer = eval(input("Process another salesperson? Press 1 for yes or 0 for no."))
        #end while answer == 1
        print("Thank you for using this program!")
    print("Goodbye!")
#end main
main()
            
