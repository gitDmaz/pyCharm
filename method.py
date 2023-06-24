numbers = [0] * 10
print("Enter number of element in array : ")
size = int(input())
print("Enter " + str(size) + " Elements : ")
for i in range(size):
    print(" Enter" + str(i+1) + " Element")
    numbers[i] = int(input())
print("Insert the position you want to insert value ")
position = int(input())
if position < 0 or position > len(numbers) or position > size:
    print("Wrong position")
else:
    print("Enter your element : ")
    element = int(input())
    for i in range(size, position, -1):
        numbers[i] = numbers[i-1]
    numbers[position-1] = element
print(numbers)