class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# --- Interactive Menu ---
def main():
    q = Queue()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Is Empty?")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                item = input("Enter item to enqueue: ")
                q.enqueue(item)
                print(f"Enqueued: {item}")
                print("Queue:", q.items)

            elif choice == "2":
                removed = q.dequeue()
                print(f"Dequeued: {removed}")
                print("Queue:", q.items)

            elif choice == "3":
                print("Front item:", q.peek())

            elif choice == "4":
                print("Queue size:", q.size())

            elif choice == "5":
                print("Is queue empty?", q.is_empty())

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter 1-6.")

        except IndexError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()