def calculate_grade(marks):
    """Returns grade and encouraging message based on marks"""
    if 90 <= marks <= 100:
        return "A", "Excellent work! You're a star 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better 😊"
    elif 60 <= marks <= 69:
        return "D", "You passed! Work a little harder 💪"
    else:
        return "F", "Don't give up! Practice makes perfect 🚀"


def get_valid_marks():
    """Keeps asking until user enters valid marks (0–100)"""
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    print("📘 STUDENT GRADE CALCULATOR 📘")
    
    name = input("Enter student name: ").strip().title()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name.upper())
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run the program
main()
