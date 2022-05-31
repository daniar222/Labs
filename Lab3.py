import numpy as np
a = np.random.randint(0,100,20)
b = list(a)
print(b)
max_number = max(a)
max_index = b.index(max_number)
print("Максимальный элемент : " + str(max_number))
x = b[0]
b[0] = b[max_index]
b[max_index] = x
print(b)

