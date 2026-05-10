# student-average-app


Додаток для обчислення середньої оцінки студента.

## Можливості

- Обчислення середнього значення
- Обробка помилки порожнього списку
- Unit тести
- Doctests
- CI/CD
- Перевірка форматування
- Перевірка вразливостей
- Sentry observability

## Встановлення

```bash
pip install -r requirements.txt
```

## Запуск

```bash
make run
```

## Тести

```bash
make test
```

## Doctests

```bash
make doctest
```

## Форматування

```bash
make format
```

## Перевірка форматування

```bash
make check-format
```

## Перевірка безпеки

```bash
make security
```

## Git hooks

```bash
cp hooks/pre-commit .git/hooks/pre-commit
```

## CI

GitHub Actions автоматично запускає:

- unit tests
- doctests
- formatting check
- security check