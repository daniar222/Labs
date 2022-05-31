import numpy as np
a = np.random.randint(0,100,size = (3,4))
b = list(a)
print(a)
minimal_elements = [min(b) for b in b]
print(minimal_elements)
