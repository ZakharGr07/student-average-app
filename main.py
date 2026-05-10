import sentry_sdk

sentry_sdk.init(
    dsn="https://d0836fba26455955baff757ef3d2ff98@o4511364644798464.ingest.de.sentry.io/4511364665311312",
    send_default_pii=True,
)
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

