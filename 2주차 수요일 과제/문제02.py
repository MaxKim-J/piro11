#과제 2번
import random

def character_name():
    name1=input("캐릭터 이름을 입력하셈")
    status=[6,7,8]
    power=random.choice(status)
    intel=random.choice(status)

    if power>intel:occup="전사"
    elif power==intel:occup="궁수"
    else:occup="법사"

    print(f"\n캐릭터 이름 : {name1}")
    print(f"힘({power}), 지력({intel})")
    print(f"직업 : {occup}")