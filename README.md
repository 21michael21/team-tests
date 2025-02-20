# TeamCity API Tests

Это автотесты для проверки API TeamCity, доказывающие что функции создания проектов, управления ролями и другие возможности работают корректно. Используется мокирование (`requests-mock`), чтобы тестировать API без реального сервера, `pytest` и `allure-pytest` для удобного управления и четких отчетов.

## Структура проекта

- `api_client/`: Класс `TeamCityClient` для работы с API.
- `config/`: Конфигурация в `config.yaml`.
- `tests/`: Тесты и фикстуры.
- `utils/`: Генератор данных и мокированные ответы.

## Запуск проекта

### Требования

- Python 3.9+ (рекомендуется 3.10)
- Git

### Установка и запуск

#### **macOS/Linux**

1. Клонируйте репозиторий и перейдите в директорию:
   ```bash
   git clone https://github.com/your-username/teamcity-tests.git && cd teamcity-tests
   ```

2. Создайте виртуальное окружение, активируйте его, установите зависимости:
   ```bash
   python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
   ```

3. Запустите тесты и сгенерируйте отчет Allure:
   ```bash
   pytest tests/ --alluredir=./allure-results -v && allure serve ./allure-results
   ```
---
#### **Windows**

1. Клонируйте репозиторий и перейдите в директорию:
   ```cmd
   git clone https://github.com/your-username/teamcity-tests.git && cd teamcity-tests
   ```

2. Создайте виртуальное окружение, активируйте его, установите зависимости:
   ```cmd
   python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt
   ```

3. Запустите тесты и сгенерируйте отчет Allure:
   ```cmd
   pytest tests/ --alluredir=./allure-results -v && allure serve ./allure-results
   ```

