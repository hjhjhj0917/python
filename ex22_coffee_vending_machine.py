coffee = 10

while True :
    money = int(input("push the money : "))

    if money == 300 :
        print("give a coffee")
        coffee -= 1
    elif money > 300 :
        print("give a %d money and give a coffee" % (money - 300))
        coffee -= 1
    else :
        print("return money don't dive a coffee")
        print("remain coffee is %d" % coffee)
    if not coffee :
        print("coffee is sold out")
        break