def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("===== STUDENT GRADE CALCULATOR =====")

    name = input("Enter student name: ")
    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter subject {i} marks (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)

    print("\n===== RESULT =====")
    print("Student:", name)
    print("Total Marks:", sum(marks))
    print("Average:", round(average, 2))
    print("Grade:", grade)


if __name__ == "__main__":
    main()