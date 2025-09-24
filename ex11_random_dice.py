import random

mylist = ["하나", "둘", "셋", "넷", "다섯", "여섯"]

while(True):

    response = input("주사위 던지기를 계속하시겠습니까? (Yes or No) : ");

    if response == "Yes":
        coin = random.choice(mylist)
        print(coin)
    else:
        break