import sys
import math

while True:
    print("____________________")
    print("  Select a function\n")

    print("1. Body Mass Index")
    print("2. Retirement")
    print("3. Shortest Distance")
    print("4. Email Verifier")
    print("5. Exit Program")
    print("____________________")

    function = int(input())
    if(function == 1):
        print("Body Mass Index function selected.")
        print("Input height in feet and inches. (ex. 5'10)")
        heightinput = input()

        ft = int(heightinput[0])
        # If height is say, 5'9 for example.
        if(len(heightinput) == 3):
            inch = int(heightinput[2])
        # If height is say, 5'10 for example.
        elif(len(heightinput) == 4):
            # Concatenates the last two characters in the input and converts to an int
            concat = heightinput[2] + heightinput[3]
            inch = int(concat)

        # Turns the height into inches
        height = ft*12 + inch
        #print("ur height: ", height)

        print("Input your weight in pounds")
        weightinput = input()

        # Get the weight into kilograms
        convweight = int(weightinput) * 0.45
        # Get the height into meters
        convheight = height * 0.025
        squared = convheight * convheight
        BMI = convweight / squared

        # Checking for different BMI ranges
        if(BMI < 18.5):
            print("Your BMI is", format(BMI,'.1f'), "and you are underweight.")
        elif(BMI >= 18.5 and BMI < 25):
            print("Your BMI is", format(BMI,'.1f'), "and you are normal weight.")
        elif(BMI >= 25 and BMI < 30):
            print("Your BMI is", format(BMI,'.1f'), "and you are overweight.")
        elif(BMI >= 30):
            print("Your BMI is", format(BMI,'.1f'), "and you are obese.")

    elif(function == 2):
        print("Retirement function selected.")
        print("Enter your age")
        age = int(input())

        # Converts the annual salary string into a float
        print("Enter your annual salary. (ex. $60,000)")
        salaryinput = input()
        salarystr = ''
        for x in range(1, len(salaryinput)):
            salarystr += salaryinput[x]
        salary = float(salarystr.replace(',',''))
        #print(salary)

        # Converts the saved percentage string into a float.
        print("Enter percentage saved. (ex. 5%)")
        savedinput = input()
        savedstr = ''
        for x in range(0, len(savedinput) - 1):
            savedstr += savedinput[x]
        saved = float(savedstr.replace('.', ''))
        savedpercent = saved / 100

        # Converts the desired savings goal string into a float
        print("Enter desired retirement savings goal. (ex. $200,000)")
        savingsgoalinput = input()
        savingsgoalstr = ''
        for x in range(1, len(savingsgoalinput)):
            savingsgoalstr += savingsgoalinput[x]
        savingsgoal = float(savingsgoalstr.replace(',',''))
        #print(savingsgoal)

        # Calculation for meeting savings goal
        savingsperyear = salary * savedpercent
        employermatch = 0.35 * savingsperyear
        years = 1
        savings = savingsperyear + employermatch

        while savings <= savingsgoal:
            savings += savingsperyear + employermatch
            years += 1

        savingsgoalage = years + age

        if(savingsgoalage < 100):
            print("You will reach your savings goal at age", savingsgoalage)
        else:
            print("You will reach your savings goal after 100 and will not meet it.")

    elif(function == 3):
        print("Shortest Distance function selected.")
        print("Input your 2 points.")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        xsquared = (x2 - x1) * (x2 - x1)
        ysquared = (y2 - y1) * (y2 - y1)
        inside = xsquared + ysquared
        distance = math.sqrt(inside)

        print("Distance between", (x1,y1), "and" , (x2,y2), "is", distance)


    elif(function == 4):
        print("Email Verifier function selected.")
        print("Enter your email.")
        emailstring = input()
        # Checks if the first character of the email is an alphabet
        z = 1
        if(emailstring[0].isalpha() == False):
            z = 0

        # Checks if there is an instance of two periods next to each other
        for x in range(0, len(emailstring) - 1):
            if(emailstring[x] == '.'):
                if(emailstring[x+1] == '.'):
                    z = 0

        # Checks for forbidden characters in the email string
        if('""' in emailstring) or ('(' in emailstring) or (')' in emailstring) or (',' in emailstring) or (':' in emailstring) or (';' in emailstring) or ('<' in emailstring) or ('>' in emailstring) or ('[' in emailstring) or (']' in emailstring) or ('`' in emailstring) or ('\\' in emailstring):
            z = 0
        if(emailstring.count('@') > 1 or emailstring.count('@') == 0):
            z = 0

        # Checks to see if the '@' used in the string is for the @something.com
        if('@' in emailstring):
                # If after the @, there is no domain ( @.com)
                if((len(emailstring) - emailstring.index('@')) == 5):
                    z = 0
                # If after the @, there is an non-alphabetical letter
                if(emailstring[emailstring.index('@') + 1].isalpha() == False):
                    z = 0
                #print(x,"char:", emailstring[x])
                if(emailstring[len(emailstring) - 1] != 'm'):
                    z = 0
                if(emailstring[len(emailstring) - 2] != 'o'):
                    z = 0
                if(emailstring[len(emailstring) - 3] != 'c'):
                    z = 0
                if(emailstring[len(emailstring) - 4] != '.'):
                    z = 0
                # If all the previous tests pass, it checks to make sure the domain are letters
                #if(z == 1):
                #    for x in range(emailstring.index('@')+1, emailstring.index('.')):
                        #print(emailstring[x])
                #        if(emailstring[x].isalpha() == False):
                #            z = 0

        # If all the tests pass, print out valid email
        if(z == 1):
            print("\nCongratulations, you have a valid email address!")
        elif(z == 0):
            print("\nInvalid email.")

    elif(function == 5):
        sys.exit(0)

    else:
        print("Invalid input")

# 25.69 / 2
# 29.96 / 4
# 29.94 / 3
