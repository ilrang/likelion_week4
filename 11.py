money = int(input("money를 입력하세요"))

def func(money):
    if(money >= 10000):
        print("고기를 먹는다")
    elif (5000<=money):
        print("국밥을 먹는다")
    else:
        print("라면을 먹는다")

func(money) 