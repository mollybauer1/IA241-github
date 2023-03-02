"""
lab 7
"""
#3.1
i = 0
while (i<6):
    if i!=3:
        print(i)
    i+=1

#3.2
i = 1
result = 1
while i<=5:
    result = result*i
    i+=1
print(result)

#3.3
i = 1
result = 0
while i<= 5:
    result+= i
    i+=1
print(result)

#3.4
i = 3 
result = 1
while i<=8:
    result*=i
    i+=1
print(result)

#3.5
i = 8-3
result = 1
while i<= 8:
    result*=i
    i+=1
print(result)

#3.6
i = 0
num_list = [12,32,43,35]
while i < len(num_list):
    del num_list[i]
print(num_list)
