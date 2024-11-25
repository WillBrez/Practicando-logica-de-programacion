inicial = [0, 1]
for i in range(0, 10):
    inicial.append(inicial[-1] + inicial[-2]) 
print(inicial)
