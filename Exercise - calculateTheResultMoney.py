def setupinitialMoney():
    money = float(input("Insert the initial balance above 0: "))
    while money<0:
        print ("Please, insert balance above 0")
        money = float(input("Insert the initial balance above 0: "))
    else:
        return(money)
    
def setupPercent():
    percentage = float(input("Insert the percentage without % sign: "))
    return(percentage)

def setupYears():
    years = float(input("Insert value of years between 0 and 20: "))
    while years < 0 or years >20:
        print("Please, insert number between 0 and 20")
        years = float(input("Insert value of years between 0 and 20: "))
    else:
        return(years)
    
def calculateTheResultMoney(initialMoney, percentage):
    i = (percentage/100)+1
    value = initialMoney *i
    return(value)

def main():
    print("Hello user! This app is going to calculate the amount of money you will have in your account according to the data inserted")
    initialMoney = setupinitialMoney()
    percent = setupPercent()
    years = setupYears()
    x = initialMoney
    y = years
    while (years>0):
        result = calculateTheResultMoney(initialMoney, percent)
        years=years-1 
    print ("After", y, "years, your", y, "balance will turn to", result)
    print ("Thank you for using the app!")
main()
