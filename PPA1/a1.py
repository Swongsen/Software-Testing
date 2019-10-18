import sys
import math
import re
import mysql.connector

mydb = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    passwd="my-secret-pw"
)

mycursor = mydb.cursor()

# Create DB if it doesn't exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydb")
mycursor.execute("USE mydb")

# Create tables if they don't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS shortestDistance(x1 FLOAT NOT NULL, y1 FLOAT NOT NULL, x2 FLOAT NOT NULL, y2 FLOAT NOT NULL, distance FLOAT NOT NULL, created_at TEXT NOT NULL)")

# IS NUMERIC INPUT FUNCTION
# Input: potential_number (input that may have special characters like $, %, ., ', ")
# Input: allowed_once
#           - Set of characters that are allowed to appear ONCE in a numeric input
#           - Examples: $10.00, 5.4%, 5'10"...
# Output: True/False (True: numeric input, False: non-numeric input detected)
def isNumericInput(input, allowed_once):

    # Make sure input is string for regex
    input = str(input)

    # Remove all commas
    input = re.sub(',', '', input)

    # Remove characters found in 'allowed_once' a single time
    for char in allowed_once:
        input = input.replace(char, '', 1)

    if input.isnumeric():
        return True
    else:
        return False

# BODY MASS INDEX FUNCTION
# Input: height_input (in feet and inches, ex: 5'10")
# Input: weight_input (in pounds, ex: 180)
# Output: BMI, WeightClassification
def bmi(height_input, weight_input):

    invalidInput = ValueError('\nInvalid input detected. ' +
                            'Please enter a proper height/weight\n')

    # Check for non-int/non-float input
    for input in (height_input, weight_input):
        if not isNumericInput(input, allowed_once = ['\'', '\"', '.']):
            raise invalidInput

    # Check that height has one ' to seperate height and weight
    if height_input.count('\'') != 1:
        raise invalidInput

    # Seperate into feet and inches by splitting the string by the single quote
    ft, inch = height_input.split('\'')

    # Convert to floats (remove " in inches if there is one)
    ft, inch = float(ft), float(re.sub('\"', '', inch))

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

    # Removes valid special characters
    def removeSpecial(string):
        return re.sub('[$%,]', '', string)

    # Check for invalid input (non-int/non-float)
    for input in (current_age, salary, saved_percent, savings_goal):
        if not isNumericInput(input, allowed_once = ['$', '%', '.']):
            raise ValueError('\nIncorrect input detected. ' +
                            'Please enter an integer (1, 2, 3...) or a float (1.0, 2.0, 3.0...)\n')

    # Remove special characters for all inputs, and convert them to numbers
    current_age = int(current_age)
    salary = float(removeSpecial(salary))
    saved_decimal = float(removeSpecial(saved_percent)) / 100
    savings_goal = float(removeSpecial(savings_goal))

    # User can technically be 0-99 (Death at 100)
    if current_age >= 100 or current_age < 0:
        raise ValueError('\nIncorrect input detected. ' +
                        'Users can only be ages 0-99.')

    # User can't save more than 100%, and can't save less than 0%
    if saved_decimal < 0 or saved_decimal > 1:
        raise ValueError('\nIncorrect input detected. ' +
                            'Your savings percent is incorrect.')

    # User can't have negative salary
    if salary < 0:
        raise ValueError('\nIncorrect input detected. ' +
                        'Your salary can\'t be negative')

    # Formula to calculate how many years left
    # Based off (salary*saved_percent*years)+(salary*saved_percent*years*0.35) = savings_goal
    years_to_goal = math.ceil(savings_goal/(salary*saved_decimal*1.35))

    savings_goal_age = years_to_goal + current_age
    return savings_goal_age

# SHORTEST DISTANCE FUNCTION
# Input: x1 (x coordinate of point 1)
# Input: y1 (y coordinate of point 1)
# Input: x2 (x coordinate of point 2)
# Input: y2 (y coordinate of point 2)
# Output: distance (euclidian distance between point 1 and 2)
def shortestDistance(x1, y1, x2, y2):
    # Check for non-int/non-float answers
    for coord in (x1, y1, x2, y2):
        if not isNumericInput(coord, ['.']):
            raise ValueError('\nIncorrect input detected. ' +
                            'Please enter an integer (1, 2, 3...) or a float (1.0, 2.0, 3.0...)\n')

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    x_squared = (x2 - x1) * (x2 - x1)
    y_squared = (y2 - y1) * (y2 - y1)
    squared_distance = x_squared + y_squared
    distance = math.sqrt(squared_distance)

    mycursor.execute("INSERT INTO shortestDistance(x1,y1,x2,y2,distance,created_at) VALUES({},{},{},{},{},NOW())".format(x1,y1,x2,y2,distance))

    return distance

# EMAIL VERIFICATION FUNCTION
# Input: email_string (string which has email to be verified)
# Output: True/False (True if valid, False if invalid)
def isValidEmail(email_string):

    # needs at least one @, but more than one @ is improper formatting
    if email_string.count('@') != 1:
        return False

    # split email into some_string '@' domain
    some_string, domain = email_string.split('@')

    # some_string has to be at least 1 character
    if len(some_string) == 0:
        return False

    # domain has to be at least 3 characters
    # domain needs to be in x.y format (Ex: abc.com, x=abc, y=com)
    # can also possibly be in x.y.z
    if len(domain) < 3 or domain.count('.') == 0:
        return False

    for chars in domain.split('.'):
        if len(chars) == 0:
            return False

    # if there is a space in the some_string
    if ' ' in some_string:
        return False

    if ' ' in domain:
        return False

    # some_string can't start or end with '.'
    if some_string[0] == '.' or some_string[-1] == '.':
        return False

    # no consecutive periods
    if '..' in some_string:
        return False

    # must start with a non-numeric
    if some_string[0].isnumeric():
        return False

    # can't contain "(),:;<>@[\]'
    for char in '\"(),:;<>@[\\]\'':
        if (char in some_string) or (char in domain):
            return False

    # if nothing is wrong, it's valid
    return True

def cliInterface(): #pragma: no cover

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
        print('Input height in feet and inches. (ex. 5\'10\")')
        height_input = input()

        print('Input your weight in pounds')
        weight_input = input()

        try:
            BMI, classification = bmi(height_input, weight_input)
            print('BMI: {}, Weight Classification: {}'.format(BMI, classification))
        except Exception as error:
            print(error)

    elif(function == 2):
        print('Retirement function selected.')
        print('Enter your current age (in years)')
        current_age = input()

        print('Enter your annual salary. (ex. $60,000)')
        salary = input()

        print('Enter percentage saved. (ex. 5%)')
        saved = input()

        print('Enter desired retirement savings goal. (ex. $200,000)')
        savings_goal = input()

        try:
            savings_goal_age = retirement(current_age, salary, saved, savings_goal)
            if(savings_goal_age < 100):
                print('You will reach your savings goal at age', savings_goal_age)
            else:
                print('You will not meet your savings goal, ' +
                    'you would have to live to be', savings_goal_age)
        except Exception as error:
            print(error)

    elif(function == 3):
        print('Shortest Distance function selected.')
        print('\nPrior Entries:')
        mycursor.execute('DESCRIBE shortestDistance')
        cols = []
        for x in mycursor:
            cols.append(x[0])
        print(*cols, sep = "  ,  ")
        mycursor.execute("SELECT * FROM shortestDistance")
        for entry in mycursor:
            print(entry)
        print('\nEND of Prior Entries\n')
        print('Input your 2 points. Format: (x1, y1), (x2, y2)')
        x1 = input("x1: ")
        y1 = input("y1: ")
        x2 = input("x2: ")
        y2 = input("y2: ")

        try:
            distance = shortestDistance(x1, y1, x2, y2)
            print('Distance between', (x1,y1), 'and' , (x2,y2), 'is', distance)

        except Exception as error:
            print(error)

    elif(function == 4):
        print('Email Verifier function selected.')
        print('Enter your email.')
        emailstring = input()

        validity = isValidEmail(emailstring)

        if validity:
            validity = 'valid'
        else:
            validity = 'invalid'

        print('The email you entered is {}'.format(validity))

    elif(function == 5):
        sys.exit(0)

    else:
        print('Invalid input, enter a number 1-5')

if __name__=='__main__':
    while True:
        try:
            cliInterface()
        except Exception as error:
            print('\nInvalid input, enter a number 1-5')
        except KeyboardInterrupt:
            sys.exit(0)
