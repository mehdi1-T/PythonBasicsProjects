def BubbleSort(LIST):
    for i in range(len(LIST)):
        for j in range(len(LIST)):
            if LIST[i] > LIST[j]:
                LIST[i], LIST[j] = LIST[j], LIST[i]
                return True
            else:
                return False
 


LIST = [1, 0]

result = BubbleSort(LIST)
print(result)
print(LIST)