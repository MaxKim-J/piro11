#과제 1번
words=['mannnn','mannnniac','mannnndatory','mannnnnipulate','mannnnuscript','mannnnchester','mannnnwhosave']
result=set()
for n in range(1,len(min(words,key=len))+1):
    for m in range(len(words)-1):
        if words[m][:n]==words[m+1][:n]:
            result.add(words[m][:n])
        else:
            result.remove(words[m][:n])
            break
print(max(result,key=len))