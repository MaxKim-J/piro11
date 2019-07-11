#과제 3번

sub=[]
height=[20,7,23,19,10,15,25,8,13]

for i in range(0,8):
    sub.append(height[i])
    for m in range(i+1,9):
        sub.append(height[m])
        if sum(height)-sum(sub)==100:
            result=[i for i in height if i not in sub]
            result.sort()
            for i in result:
                print(i)
        else:
            sub.remove(height[m])
            continue
    sub = []