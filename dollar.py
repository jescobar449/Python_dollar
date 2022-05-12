#Name: Jose Melquiades Escobar

#turn magic number into named constants 
dollar = 1
moveDecimalPlaceByTwo = 100
quarter = 25
dime = 10
nickel = 5
penny = 1



userMoney = -dollar
#ask the user to input an amount of money 
while userMoney < 0:
    userMoney = float ( input ('Enter a money amount: ') )
    if userMoney < 0:
        print ('Error: Invalid money amount entered')
        print ('')



#Convert total amounts to pennies - Also Find number of one dollars 
userMoneyOnlyDollars = int (userMoney / dollar)  #used to get the amount of dollars 
userMoneyOnlyPennies = int ( float ( format ( ( userMoney - userMoneyOnlyDollars) * moveDecimalPlaceByTwo, ',.2f' ) ) )  #get pennies left over
userMoneyTotalAmountPennies = (userMoneyOnlyDollars * moveDecimalPlaceByTwo) + userMoneyOnlyPennies  #used to get the total amount with pennies only

#Find number of quarters in the remaining amount
userMoneyQuarters = userMoneyOnlyPennies // quarter  # used to find the number of quarters

#Find number of dimes in the remaining amount
userMoneyMinusQuarters = userMoneyOnlyPennies - ( quarter * userMoneyQuarters)  #subtracts total quarters from left over amount
userMoneyDimes = userMoneyMinusQuarters // dime  #used to get the amount of dimes 

#Find number of nickels in the remaining amount
userMoneyMinusDimes = userMoneyMinusQuarters - ( dime * userMoneyDimes) #subtract total dimes from left over amount
userMoneyNickels = userMoneyMinusDimes // nickel  #used to get the amount of nickels

#Find number of pennies in the remaining amount
userMoneyMinusNickels = userMoneyMinusDimes - ( nickel * userMoneyNickels) #subtracts total nickels from left over amount
userMoneyPennies = userMoneyMinusNickels // penny  #used to get the amount of pennies 

#Display results
print ('Your amount', userMoney, 'consists of' )  #displays the first statement 
print (userMoneyOnlyDollars, 'dollars' )          #displays dollars amount 
print (userMoneyQuarters, 'quarters' )            #displays quarters amount
print (userMoneyDimes, 'dimes' )                  #displays dimes amount
print (userMoneyNickels, 'nickles' )              #displays nickels amount
print (userMoneyPennies, 'pennies' )              #displays pennies amount 


