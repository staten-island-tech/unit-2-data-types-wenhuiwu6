""" sentence = input("input a sentence: ")
def counting_words(sentence):
    words= sentence.split( )
    return len(words)
print("number of words in sentence:",counting_words(sentence)) """

""" number=7
if number % 2 == 0:
    print("even")
else:
    print("odd")  """

""" bill= input("bill: ")
service= input("How's the service: ")
tip_percent=0
if service == ("bad") :
    tip_percent == 0.0
elif service == ("okay") :
    tip_percent == 0.15
elif service == ("good") :
    tip_percent == 0.20
elif service == ("great") :
    print("0.25")  
else: 
    print("invalid")  """

""" number = 12
for i in range (1, number +1): 
    if(number % i== 0):
        print(i) """

number1= 12
factors_of_number1 = []
for i in range (1, number1 +1): 
    if number1 % i== 0:
        factors_of_number1.append(i)
number2= 60
factors_of_number2 = []
for o in range (1, number2 +1): 
    if number2 % o== 0:
        factors_of_number2.append(o)

common_factors= list(set(factors_of_number1) & set(factors_of_number2))
gcf = max(common_factors)
print("The GCF is:", gcf)

"""def GCF(x,y):
    if y==0:
        return (x)
    else: 
        return GCF(y, x % y)

print (GCF(9,3)) """

""" # similiar to the quiz 
def skins(money, age, cost, isAvailable):
    if money < 10 or age <18 or isAvailable ==False:
        return ("cannot buy")
def skins(money, age, cost, isAvailable):
    if isAvailable == True:
        if money >10 or cost == 0:
            print ("can purcahse")
        else: 
            print ("Lucas Broke Boy")
    else: 
        print("not available ")

def skins(money, age, cost, isAvailable):
    if isAvailable and money >= cost: 
        print ("can purcahse") """