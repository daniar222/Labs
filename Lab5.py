import numpy as np
a = np.random.randint(-100,100,size = (4,3))
b = list(a)
print(a)
def search_pos(a):
    counter = 0
    for i in a:
        for j in i:
            if j > 0:
                counter += 1
    return(counter)
print(search_pos(a))



