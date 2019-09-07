import sys
import math
import re

# BODY MASS INDEX FUNCTION
# Input: heightInput (in feet and inches, ex: 5'10)
# Input: weightInput (in pounds, ex: 180)
# Output: BMI, WeightClassification
def bmi(height_input, weight_input):
    if ('\'' not in height_input):
        print('Incorrect input for height detected.' +
        '\nAs an example, if you are 5 feet and 10 inches tall, enter: 5\'10')
    
    # Seperate into feet and inches by splitting the string by the single quote
    ft, inch = height_input.split('\'')

    # Convert to floats
    ft, inch = float(ft), float(inch)

    # Turns the height into inches
    height = ft*12 + inch

    # BMI implementation from http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
    # Get the weight into kilograms
    conv_weight = float(weight_input) * 0.45
    # Get the height into meters
    conv_height = height * 0.025
    BMI = round(conv_weight / (conv_height * conv_height), 1)

    # Checking for different BMI ranges
    if(BMI < 18.5):
        return BMI, 'Underweight'
    elif(BMI >= 18.5 and BMI < 25):
        return BMI, 'Normal weight'
    elif(BMI >= 25 and BMI < 30):
        return BMI, 'Overweight'
    elif(BMI >= 30):
        return BMI, 'Obese'

# RETIREMENT FUNCTION
# Input: current_age (in years)
# Input: salary (Annual Salary, ex: $60,000)
# Input: saved (Percent of how much is being saved, ex: 5%)
# Input: savings_goal (Savings goal before death, ex: $500,000)
# Output: savings_goal_age (Age at which the savings_goal is achieved)
def retirement(current_age, salary, saved_percent, savings_goal):

    # Removes special characters
    def removeSpecial(string):
        return re.sub('[!@#$%^&*,]', '', string)
    
    # Conversion from string to float
    salary = float(removeSpecial(salary))
    saved_decimal = float(removeSpecial(saved_percent)) / 100
    savings_goal = float(removeSpecial(savings_goal))

    # Formula to calculate how many years left
    # Based off (salary*saved_percent*years)+(salary*saved_percent*years*0.35) = savings_goal
    years_to_goal = math.ceil(savings_goal/(salary*saved_decimal*1.35))

    savings_goal_age = years_to_goal + current_age
    return savings_goal_age

def shortestDistance(x1, y1, x2, y2):
    x_squared = (x2 - x1) * (x2 - x1)
    y_squared = (y2 - y1) * (y2 - y1)
    squared_distance = x_squared + y_squared
    distance = math.sqrt(squared_distance)

    return distance

def email(emailstring):
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
        return('Valid')
    elif(z == 0):
        return('Invalid')

def cliInterface():
    print('____________________')
    print('  Select a function\n')

    print('1. Body Mass Index')
    print('2. Retirement')
    print('3. Shortest Distance')
    print('4. Email Verifier')
    print('5. Exit Program')
    print('____________________')

    function = int(input())

    if(function == 1):
        print('Body Mass Index function selected.')
        print('Input height in feet and inches. (ex. 5\'10)')
        height_input = input()

        print('Input your weight in pounds')
        weight_input = input()

        BMI, classification = bmi(height_input, weight_input)
        print('BMI: {}, Weight Classification: {}'.format(BMI, classification))

    elif(function == 2):
        print('Retirement function selected.')
        print('Enter your current age (in years)')
        current_age = int(input())
        
        print('Enter your annual salary. (ex. $60,000)')
        salary = input()

        print('Enter percentage saved. (ex. 5%)')
        saved = input()

        print('Enter desired retirement savings goal. (ex. $200,000)')
        savings_goal = input()

        savings_goal_age = retirement(current_age, salary, saved, savings_goal)
        
        if(savings_goal_age < 100):
            print('You will reach your savings goal at age', savings_goal_age)
        else:
            print('You will not meet your savings goal, ' +
            'you would have to live to be', savings_goal_age)

    elif(function == 3):
        print('Shortest Distance function selected.')
        print('Input your 2 points. Format: (x1, y1), (x2, y2)')
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        distance = shortestDistance(x1, y1, x2, y2)
        print('Distance between', (x1,y1), 'and' , (x2,y2), 'is', distance)

    elif(function == 4):
        print('Email Verifier function selected.')
        print('Enter your email.')
        emailstring = input()
        
        validity = email(emailstring)
        print('The email you entered is: {}'.format(validity))

    elif(function == 5):
        sys.exit(0)

    else:
        print('Invalid input, enter a number 1-5')

if __name__=='__main__':
    while True:
        cliInterface()