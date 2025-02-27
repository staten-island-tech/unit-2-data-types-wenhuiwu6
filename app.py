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

""" bill= 400
service= "good"
if service == ("bad") :
    print("0.0")
elif service == ("okay") :
    print("0.15")
elif service == ("good") :
    print("0.20")
elif service == ("great") :
    print("0.25")  
else: 
    print("invalid")  """

""" number = 12
for i in range (1, number +1): 
    if(number % i== 0):
        print(i) """

""" def GCF(x,y):
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