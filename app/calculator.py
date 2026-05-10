"""
Модуль для обчислення середньої оцінки студента.
"""

from statistics import mean

# import sentry_sdk

# sentry_sdk.init(
#     dsn="YOUR_SENTRY_DSN",
#     traces_sample_rate=1.0,
# )


def calculate_average(grades: list[float]) -> float:
    """
    Обчислює середню оцінку студента.

    Args:
        grades: список оцінок

    Returns:
        float: середнє значення

    Raises:
        ValueError: якщо список порожній

    Examples:
        >>> calculate_average([90, 80, 100])
        90
        >>> calculate_average([5, 5, 5])
        5
    """

    if not grades:
        raise ValueError("Список оцінок порожній")

    return mean(grades)
