#codebreak

limit=10
code=6392
while True:
      inputcode=int(input("비번을 입력하세요 : "))
      if inputcode == code:
         print("\n문이 열렸습니다\n")
         break
      else:
         print("\n비번이 틀렸습니다\n")
         limit=limit-1
         print("남은기회 : %s번\n" %limit) 
      if limit == 0:
      	 print("="*40)
      	 print("{0:^20}".format("문이 영원히 잠깁니다"))
      	 print("="*40)
      	 break
