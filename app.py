""" #how much words
sentence = input("input a sentence: ")
def counting_words(sentence):
    words= sentence.split( )
    return len(words)
print("number of words in sentence:",counting_words(sentence)) """

""" #odd or even
number=7
if number % 2 == 0:
    print("even")
else:
    print("odd") """

""" #tip calculator
bill= float(input("bill: "))
service= input("How's the service: ")
tip_percent=0
if service == ("bad") :
    tip_percent = 0.0
elif service == ("okay") :
    tip_percent = 0.15
elif service == ("good") :
    tip_percent = 0.20
elif service == ("great") :
    tip_percent = 0.25
else: 
    print("invalid") 
tip=bill*tip_percent
total=bill+tip
print(f"Tip amount: $ {tip:.2f}")
print(f"Total: $ {total:.2f}") """

""" #factoring
number = 12
for i in range (1, number +1): 
    if(number % i== 0):
        print(i) """

""" #GCF
number1= 48
number2= 60
factors_of_number1 = []
gcf=1
for i in range (1, number1 +1): 
    if number1 % i== 0:
        factors_of_number1.append(i)

for o in range (1, number2 +1): 
    if number2 % o== 0 and o in factors_of_number1:
       gcf = o
print("GCF is: ", gcf)  """

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