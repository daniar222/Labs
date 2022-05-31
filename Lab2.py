s = input()
counter_0 = 0
counter_1 = 0
i = 0
j =0
while s.find("0",i) != -1:
    counter_0 += 1
    i = 1+s.find("0",i)
print("Количество нулей :" + str(counter_0))
while s.find("1",j) != -1:
    counter_1 += 1
    j = 1+s.find("1",j)
print("Количество единиц :" + str(counter_1))