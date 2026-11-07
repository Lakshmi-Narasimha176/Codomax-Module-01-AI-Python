def main():
    numbers = [10, 20, 30, 40, 50]

    print("===== PYTHON LIST OPERATIONS =====")
    print("Original list:", numbers)

    numbers.append(60)
    print("After adding an element:", numbers)

    numbers.remove(20)
    print("After removing an element:", numbers)

    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
    print("Total elements:", len(numbers))
    print("Sum:", sum(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

    numbers.sort(reverse=True)
    print("Descending order:", numbers)


if __name__ == "__main__":
    main()