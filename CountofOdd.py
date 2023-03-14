
Array= [1,2,3,4,5,6,7,8,9,0]
count=0
num=0

while(num < len(Array)):
     if Array[num] % 2 != 0:
         
         count +=1
         
     num += 1
print('Odd number count', count)  

