from app.calculator import calculate_average


def main():
    try:
        user_input = input("Введіть оцінки через пробіл: ")

        grades = [float(x) for x in user_input.split()]

        average = calculate_average(grades)

        print(f"Середня оцінка: {average}")

    except ValueError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
