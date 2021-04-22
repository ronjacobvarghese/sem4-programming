import array

arr = array.array("i", [1, 2, 3])
arr.insert(0, 21)
arr.insert(2, 7)
arr.append(5)

for i in range(0, 6):
    print(arr[i], end=" ")
arr.pop(2)
arr.pop()
arr.remove(21)
print()

for i in range(0, 3):
    print(arr[i], end=" ")
n = int(input("\nEnter the number to search : "))
for i in range(0, 3):
    if arr[i] == n:
        print("Element found at: " + str(arr.index(n)))
