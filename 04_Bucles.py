#============ FOR ============
number = [1,2,3,4,5,6]

for i in number:
    print("I es igual a ", i+1)


for i in range(3,10):
    print(i)

frutas = ["manzana","pera","uva","naranja","tomate"]
for frut in frutas:
    print(frut)
    if frut == "naranja":
        print("Naranja encontrada.")

#============ while ============
x = 0
while x<5:
    if x == 3:
        break
    print(x)
    x+=1

#============ continue ============
numeros = [1,2,3,4,5,6]
for i in numeros:
    if i == 3:
        continue
    print("I es igual a ", i)