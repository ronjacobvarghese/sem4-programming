queue = []


def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(queue)


def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop()
        print("removed element:", e)
        print(queue)


while True:
    print("Select the operation 1.push 2.pop 3.quit 4.show")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    elif choice == 4:
        print(queue)
    else:
        print("Enter the correct option")
