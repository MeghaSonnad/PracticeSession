
n1= 20

n2 = 50

n3 = 70

          
max= (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))

min= ((n1 if (n1 < n2 and n1 < n3) else
     (n2 if (n2 < n1 and n2 < n3) else n3)))


print('maximum value is' , max)
print('minimun value is' , min)