array = [3, 53, 14, 31513, 31, 31]

evencouter = 0
oddcounter = 0
dublicate = []
for i in array:
    if i % 2 == 0:
        evencouter += 1
    else:
        oddcounter += 1

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] == array[j] and array[j] not in dublicate:
            dublicate.append(array[j])


print("average:"+sum(array) / len(array))
print("Min:"+min(array))
print("Max:"+max(array))
print("Evens:"+evencouter)
print("Odd:"+oddcounter)
print("Dublicates:"+dublicate)