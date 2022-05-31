# f = open("Code", "r")
# print(*f)
# array[row.strip() for row in f]
# f.close()
from array import *
dictionary = {0:[" "],1:['.',',', '!',"?",';'], 2:["A","B","C"], 3:["D","E",'F'] , 4:['G','H',"I"], 5:['J','K','L','J'],6:['M','N','O'],7:['P','Q','R','S'],8:['T',"U",'V'],9:[
    'W','X','Y','Z']}

########################
with open("Code") as file:
    array = [row.strip() for row in file]
##########################
f2 = open("Code2","w")
print(dictionary, file = f2)
##########################
s = input()
s = s.upper()
print(s)
########################
for i in range(len(s)):
    for j in range(10):
        # print(s[i])
        # print("j"+ str(j))
        if array[j].find(s[i]) != -1:
            # print("НАшел")
            print(str(j) * (array[j].find(s[i]) + 1), end="")
        elif s[i] == " ":
            print(0, end="")
            break
#############################
print("\nMethod 2")
for i in range(len(s)):
    for j in range(len(dictionary)):
        if(s[i] in dictionary[j]):
            for y in range(dictionary[j].index(s[i])+1):
                print(j, end="")
                print(j, end="",file=f2)


print('\n' + s)
