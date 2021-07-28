############################import part
import sys
import random
from copy import deepcopy










################################
print("Hello World")

################################
greeting = "Helllo Worlldd"
print (greeting)

################################
print("-----------------------------------------------------------------------------------------------Type")
print( "23  and its type is ", type(23))
print("3.14 and its type is ", type(3.14))
print("hello str and its type is ", type("hello"))
print("23" +" and its type is ", type("23"))
print("3.14" +" and its type is ", type("3.14"))
print("None and its type is ", type(None))
print("True and its type is ", type(True))
print("False and its type is ", type(False))
print("[] and its type is ", type([]))
print("{} and its type is ", type({}))

################################
#rectangle
print("-----------------------------------------------------------------------------------------------Math")
width = 23
height = 17
area = width * height
print("area of rectangle", area)

################################
#multiple string
widthstr = int("23")
heightstr = int("17")
areastr = widthstr * heightstr
print("area of int convertion of rectangle", areastr)

################################
####Add
Adda = 19
Addb = 23
Addc = Adda + Addb
print("Normal Addition", Addc)
Addstra = "19"
Addstrb = "23"
Addstrc = Addstra + Addstrb
print("Add Str solution ", Addstrc)

###############################
##################Math normal

mathA = 10
mathB = 20
mathaddC = mathA + mathB
mathsubC = mathA - mathB
mathsubC_Reverce = mathB - mathA
mathMultipleC = mathA * mathB
mathDivideC = mathA/mathB
mathDivide_Reverce_C = mathB/mathA
print("exercise add", mathaddC)
print("exercise sub", mathsubC)
print("exercise sub reverse", mathsubC_Reverce)
print("exercise multiple", mathMultipleC)
print("exercise divide", mathDivideC)
print("exercise divide reverse", mathDivide_Reverce_C)

#############################\
print("----------------------------------------------------------------------------------------------Module")
print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2))
print(sys.getsizeof(3))
print(sys.getsizeof(4))
print(sys.getsizeof(5))
print(sys.getsizeof(6))
print(sys.getsizeof(7))
print(sys.getsizeof(8))
print(sys.getsizeof(9))
print(sys.getsizeof(10))

#///////////////////////////////////////////////
#/////////////////////////////Function
print("Function")
def mainfuncone():
    print("Hello")

mainfuncone()


#################################
print("------------------------------------------------------------------------------------Ternary Operator")

TernaryX = 3

ternary_Solution = 'positive' if TernaryX > 0 else 'negative'
print(ternary_Solution)
#a = b if c == d else i if e == f else j
#'Yes' if test1() else 'Maybe' if test2() else 'No'
#a = b if c == d else (i if e == f else j)

#######################################Calculatoe exercise
print("-----------------------------------------------------------------------------calculator exercise")

def calculator():
    CalcA = float(int(input("--->1st number :")))
    CalcB = float(int(input("---> 2nd number :")))
    signOfOperator = input("Enter the METHOD add(+) sub(-) multiple(*) or divide(/) or floor division(//): ")

    calculatorValue = \
    (CalcA + CalcB) if signOfOperator == '+' \
    else (CalcA - CalcB) if signOfOperator == '-' \
    else (CalcA * CalcB) if signOfOperator == '*' \
    else (CalcA / CalcB) if signOfOperator == '/' \
    else (CalcA // CalcB) if signOfOperator == '//' \
    else print("Invalid operator: '{}'".format(signOfOperator))
    print(calculatorValue)
    

##calculator()


###########################

#############################################
#########################Random
print("-----------------------------------------------------------------------------------------Random")

#RandomNumCall = random.random()

#print(RandomNumCall)
print("----------------------------------------------------------------------Random Seed ")
#RandomSeed = random.seed(10)
#print("random seed", RandomSeed)
#print("random.random1()", random.random())
#print("random.random2()", random.random())



#########################################################################
#########Rolling Dice
print("----------------------------------------------------------------------Rolling Dice using random")
print(1 + int(6 * random.random()))

print(random.randrange(1, 7))
print(random.randrange(1, 100))
print("----------------------------------------------------------------------Random choice")
RandomChoice = "qwertyuioplkjhgfdsazxcvbnm"
print("Random choice value in string",random.choice(RandomChoice))
RandomChoiceList = ["a","b","c","d","e","f","g","h","i","j"]
print("Random choice list", random.choice(RandomChoiceList))
RandomChoiceDict = {"key1":"valv1", "key2":"valv2", "key3":"valv3"}
print("list of dict", list(RandomChoiceDict))
print("list of dict keys", list(RandomChoiceDict.keys()))
print("list of dict values", list(RandomChoiceDict.values()))
print("Random choice dict keys", random.choice(list(RandomChoiceDict.keys())))
print("Random choice dict values", random.choice(list(RandomChoiceDict.values())))
print("Random choice dict list", random.choice(list(RandomChoiceDict)))
#####################################################40 page over

print("---------------------------------------------------------------------Exercise number guessing")

hiddenValue = random.randrange(1, 21)
print("the hidden value is ", hiddenValue)

#user_inputForHiddenValue = input("Guess from 1 to 20:")
user_inputForHiddenValue = 5
print("Guessed Value", user_inputForHiddenValue)

guess = int(user_inputForHiddenValue)
if guess == hiddenValue:
    print ("Found")
elif guess > hiddenValue:
    print ("No its high")
else:
    print ("NO its low")

print("-------------------------------------------------- exercise random.salad")

fruitsOfRandom = ["Apple", "Banana", "Peach", "Orange", "Papaya", "Grapes"]
saladOfRandom = random.sample(fruitsOfRandom, 1)
print(saladOfRandom, "Random Salad")
###########################################################


print("----------------------------------------- Boolean Short Circuit")
money = 100000000

def check_money():
    return money > 1000000

def check_salary():
    salary = 1000
    salary += 1
    return salary >= 1000

while True:
    has_good_money = check_money()
    has_good_salary = check_salary()
    if has_good_money or has_good_salary:
        print("I can live well")
    break;    
    #if check_money() or check_salary:
    #    print("I can live well")
    #break;

####################################
#a_in = input("Please type in a string: ")
#b_in = input("Please type in another string: ")
a_in = "Please type in a string: "
b_in = "Please type in another string: "
print("How to compare:")
print("1) ASCII")
print("2) Length")
#how = input()
how = '1'
if how == '1':
    first = a_in > b_in
    print(first)
    print(a_in)
    print(b_in)
    second = a_in < b_in
    print(second)
elif how == '2':
    first = len(a_in) > len(b_in)
    second = len(a_in) < len(b_in)

if first:
    print("First number is bigger")
elif second:
    print("First number is smaller")
else:
    print("They are equal")

###############################################################
print("single quotes and double quotes")

print('printing single quotes string')
print("printing single quotes string")
print("'printing single quotes string' inside double quote value")



#################################################################
print("--------------------------------------------------------------Long lines ")

long_text = "one"\
            "two"\
            "three" 
print("""long line using \ -----> """, long_text)

print("-------------------------------------------------------- triple quotes")
print("""
using
multiple
line
using 
triple
quotes
""")
print("---------------------------------------------length of string")
ForString = "HEllo world"

length_ForString = len(ForString)
print(length_ForString)

print("String repetation and concatination")

nameStr = 2 * 'jar'
print(nameStr)

full_nameStr = nameStr + 'Blinks'
print (full_nameStr)

titleStrValue = "We have a title String"
print("$" * len(titleStrValue))

print("--------------------------------------------A character string in a string")
textStringIndexValue = "Hello World"
print(len(textStringIndexValue))
print(textStringIndexValue[2])
print(textStringIndexValue[5])
print(textStringIndexValue[8])
print(textStringIndexValue[10])

print("----------------------------------------A character slice string in a string")

textStringIndexValueSlice = "Hello World"
print(len(textStringIndexValueSlice))
print(textStringIndexValueSlice[1:])
print(textStringIndexValueSlice[3:])
print(textStringIndexValueSlice[5:])
print(textStringIndexValueSlice[:2])
print(textStringIndexValueSlice[:5])
print(textStringIndexValueSlice[:8])
print(textStringIndexValueSlice[2:6])
print(textStringIndexValueSlice[5:7])
print(textStringIndexValueSlice[1:8])
print(textStringIndexValueSlice[2:6])
print(textStringIndexValueSlice[5:7])
print(textStringIndexValueSlice[1:8])
print(textStringIndexValueSlice[:-1])
print(textStringIndexValueSlice[:-2])
print(textStringIndexValueSlice[5:7])
print(textStringIndexValueSlice[1:8])


print("Index of a words")
print(textStringIndexValueSlice.index("e"))
print(textStringIndexValueSlice.index("l", 2))
print(textStringIndexValueSlice.index("l", 5))
print(textStringIndexValueSlice.index("l", 2))
print(textStringIndexValueSlice.index("l", 1))
print(textStringIndexValueSlice.index("l", 6))
print(textStringIndexValueSlice.index("l", 7))
print(textStringIndexValueSlice.index("l", 8))



#################################################################################################################################################
print("------------------------------------------------------------Loops")
txtForLoop = "Hello World From India <3"
for words, index in enumerate(txtForLoop):
    print(index,"-",words)


for fruit in ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]:
    print(fruit)

for i in range(10, 51):
    print("range btw 10 and 51 ", i)


for i in txtForLoop:
    if i == 'l':
        break
    print(i)
print("----------------------------------------")
for i in txtForLoop:
    if i == 'l':
        continue
    print(i)
print("----------------------------------------")

for i in txtForLoop:
    if i == 'l':
        continue
    print(i)
    if(i == 'a'):
        break
    print(i)

print("---------------------------------------------------")
totalwhile = 0
while (totalwhile < 100000000) and (totalwhile % 17 != 1 ) and (totalwhile ** 2 % 23 != 7):
    print(totalwhile)
    totalwhile += random.randrange(20)
print("done")    


################################################################################################
print("----------------------------------------------------------------------------------------------------fromated printing")

nameStrValue = "Ram"
ageValue = "24"

print("My name is " + nameStrValue + ", My age is " + ageValue)
print( "My name is %s and my age is now %s" %(nameStrValue, ageValue))
print("My name is {} and my age is now {}".format(nameStrValue, ageValue))
print(f"My name is {nameStrValue} and name my age is {ageValue}")


print("----------------------------------------------- loopin formatting")

dataclassesValue = [["Foobar", 42],
                    ["raw", 32],
                    ["Smack down", 22],
                    ["Royal Rumble", 12]]

# for i in dataclassesValue:
#     print("{} {}".format(i[0], i[1]))

for i in dataclassesValue:
    for j in i:
        print("{} {}".format(j, i))

print("------------------------------------- format alignment")
for enty in dataclassesValue:
    print("{:<20} | {:>10}".format(enty[0], enty[1]))

print("-------------------------------------------format string")
xValueStore = "Foo Bar"
print(type("{:s}".format(xValueStore)))
print("{:s}".format(xValueStore))
print(type("{}".format(xValueStore)))
print("{}".format(xValueStore))
print("------------------------------------ number binary..... format")
XvalueNumberStore = 42

print(type("{:b}".format(XvalueNumberStore)))
print("{:b}".format(XvalueNumberStore))
print(type("{:c}".format(XvalueNumberStore)))
print("{:c}".format(XvalueNumberStore))
print(type("{:d}".format(XvalueNumberStore)))
print("{:d}".format(XvalueNumberStore))
print(type("{:o}".format(XvalueNumberStore)))
print("{:o}".format(XvalueNumberStore))
print(type("{:x}".format(XvalueNumberStore)))
print("{:x}".format(XvalueNumberStore))
print(type("{:X}".format(XvalueNumberStore)))
print("{:X}".format(XvalueNumberStore))
print(type("{:n}".format(XvalueNumberStore)))
print("{:n}".format(XvalueNumberStore))


print("----------------------------------- format float value")

XvalueNumberStoreFloat = 42

print(type("{:e}".format(XvalueNumberStoreFloat)))
print("{:e}".format(XvalueNumberStoreFloat))
print(type("{:E}".format(XvalueNumberStoreFloat)))
print("{:E}".format(XvalueNumberStoreFloat))
print(type("{:f}".format(XvalueNumberStoreFloat)))
print("{:f}".format(XvalueNumberStoreFloat))
print(type("{:2f}".format(XvalueNumberStoreFloat)))
print("{:2f}".format(XvalueNumberStoreFloat))
print(type("{:F}".format(XvalueNumberStoreFloat)))
print("{:F}".format(XvalueNumberStoreFloat))
print(type("{:g}".format(XvalueNumberStoreFloat)))
print("{:g}".format(XvalueNumberStoreFloat))
print(type("{:G}".format(XvalueNumberStoreFloat)))
print("{:G}".format(XvalueNumberStoreFloat))
print(type("{:n}".format(XvalueNumberStoreFloat)))
print("{:n}".format(XvalueNumberStoreFloat))


print("-----------------------------------------------------------------------------------------------------------------------Lists")

stuff = [42, 3.14, True, None, "Foo Bar", ['another', 'list'], {'a': 'Dictionary', '\
language': 'Python'}]
print(stuff)

more_stuff = [42, 3.14, True, None, "Foo Bar", ['another', 'list'], {'a': 'Dictionary', 'language': 'Python'}]
print(more_stuff)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(planets)
print(len(planets))
print(planets[0])
print(type(planets[0]))
print(planets[3])
print(planets[0:1])
print(planets[0:2])
print(planets[1:3])
print(planets[2:])
print(planets[:3])
print(planets[:])

lettersValue = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(" syntax  [start:end:step]")
print(lettersValue[::])
print(lettersValue[::1])
print(lettersValue[::2])
print(lettersValue[1::2])
print(lettersValue[2:8:2])





# from copy import deepcopy
###################### imported on top

deepcopyXValue = ['apple', 'banana', 'orange', 'pineapple']
deepcopyYValue = deepcopy(deepcopyXValue)
print("deepcopyXValue", deepcopyXValue)
print("deepcopyYValue", deepcopyYValue)


print("----------------------------------------------------------------------------------Join using Lists")
JoinListsXValue = ['one', 'two and three', 'four', 'five']

togetherJoinsValue = ':'.join(JoinListsXValue)
print("'togetherJoinsValue using JOIN in Lists'", togetherJoinsValue)

togetherJoinsValueAnother = ':?????'.join(JoinListsXValue)
print("'togetherJoinsValue using JOIN in Lists'", togetherJoinsValueAnother)


print("-------------------------------------------------------------- Two different list values")

firstListUsingJoinValueStr = ["0", "a", "z", "9"]
firstListUsingJoinValueNum = [0, "a", "z", 9]

print(":".join(firstListUsingJoinValueStr))

print("if we using number in list we cant use join along with string" 
      " we have to use another method  ")

print(":".join(map(str, firstListUsingJoinValueNum)))
print("Or with list comprehension")

print(":" .join(str(x) for x in firstListUsingJoinValueNum))









    



























































































































































































