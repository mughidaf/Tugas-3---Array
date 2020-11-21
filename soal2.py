skorA=[]
skorB=[]
print("Masukan nama klub yang bertanding : ")
clubA=input("Klub A : ")
clubB=input("Klub B : ")
x= 1
y= 1
i=1
while x >= 0 and y >= 0 :
    print("Pertandingan",i, " : ",end="")
    x, y = [int(x) for x in input().split()]
    i += 1
    skorA.append(x)
    skorB.append(y)
skorA.pop()
skorB.pop()

b=0
for a in range (len(skorA)):
    if skorA[b] < skorB[b] : print("Hasil ",(a+1),":",clubB)
    elif skorA[b] == skorB[b] : print("Hasil",(a+1)," : Draw")
    elif skorA[b] > skorB[b] : print("Hasil ",(a+1),":",clubA)
    b += 1