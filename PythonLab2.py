
def question1():

    print("--------Q1--------")
    length1 = int(input("Enter the Length of Rectangle 1: "))

    width1 = int(input("Enter the Width of Rectangle 1: "))

    length2 = int(input("Enter the Length of Rectangle 2: "))

    width2 = int(input("Enter the Width of Rectangle 2: "))

    sum1 = length1 * width1

    print(sum1)

    sum2 = length2 * width2
    print(sum2)

    if sum1 > sum2:
        print("Rectangle 1 is bigger")

    elif sum1 < sum2:
        print("Rectangle 2 is bigger")

    else:

        print("Both are the same")


def question2():
    print("--------Q2--------")
    yearsExperience = int(input("How many years of experience have you got?"))

    hasCertification = str(input("Do you have a microsoft certification? (y/n) "))

    print(yearsExperience, hasCertification)

    if (yearsExperience < 3):
        print("Sorry, Not Eligible. You need 3 years Experience")

    elif (hasCertification == 'n'):
        print("Sorry, You need a certification")

    else:
        print("Congratulations, You are eligible")


def question3():
    print("--------Q3--------")

    purchasePrice = 99;
    purchased = int(input("How many packages did you purchase?"))
    discountAmount = 0;





    #purchased 1-9 packages, no discount

    if(purchased < 1):

        print("You need to purchase at least one package!")
        exit()


    if(purchased ==1 or purchased <= 9):

        disountAmount = purchasePrice/100*0

        purchasePrice = purchasePrice - discountAmount




    #Purchased 10-19 packages (20%off)

    elif(purchased == 10 or purchased <= 19):

        discountAmount = (purchasePrice / 100) * 20



        purchasePrice = purchasePrice - discountAmount


    #20-49 packages

    elif (purchased == 20 or purchased <= 49):

        discountAmount = (purchasePrice / 100) * 30

        purchasePrice = purchasePrice - discountAmount


    #50-99 packages

    elif (purchased == 50 or purchased <= 99):

        discountAmount = (purchasePrice / 100) * 40

        purchasePrice = purchasePrice - discountAmount


    #otherwise 100+ packages
    else:
        discountAmount = purchasePrice/100 * 50
        purchasePrice = purchasePrice - discountAmount



    print("Discount: ", discountAmount)
    print("Price: ", purchasePrice)






def question3Part1(numEntered, stop):
    print("--------Q3(i)--------")

    counter = 0;
    sum = 0;

    while counter < stop+1:

        sum = numEntered * counter

        print(numEntered, "* ", counter, " = ", sum)



        counter += 1



def printNumTriangle():

    number = int(input("Enter a single number: "))

    for num in range(number+1):
        for i in range(num):
            print(num, end=" ")  # print number

        print("\n")


def question4():
    print("--------Q4--------")


    months = int(input("How many months of data would you like: "))

    if(months<1):
        print("Thats not possible!")
        exit()

    currentRain = 0;
    highestRain = 0;

    for num in range(0,months):


        currentRain = int(input("Enter the rainfall:  "))

        if(currentRain < 0):
            print("That's not possible!!")

            exit()

        if currentRain > highestRain:

            highestRain = currentRain

            print("Highest is: ", highestRain)








#------------------------Function calls---------------------------------#

question1()
question2()
question3()
question3Part1(5, 7)
printNumTriangle()
question4()

