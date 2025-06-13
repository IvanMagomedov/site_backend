🧑‍💻 Ivan Nikolaevich | Личный сайт разработчика

Добро пожаловать на мой персональный сайт — визитку, сделанную с нуля с помощью HTML, CSS, JavaScript и Django.
На сайте представлены краткая информация обо мне, список навыков, проекты, а также форма обратной связи, данные из которой сохраняются в базу данных.


🔧 Стек технологий
	•	Frontend: HTML5, CSS3, JavaScript
	•	Backend: Python, Django
	•	Базы данных: SQLite (по умолчанию), возможна поддержка PostgreSQL
	•	DevOps: Docker (по желанию), Git


📬 Возможности
	•	Адаптивная верстка (для разных устройств)
	•	Раздел «Обо мне»
	•	Список технических навыков
	•	Карточки проектов
	•	Форма обратной связи с отправкой в админку Django
	•	Админка Django для управления сообщениями


🚀 Как запустить проект локально
	1.	Клонируйте репозиторий:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

	2.	Создайте виртуальное окружение и активируйте его:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

	3.	Установите зависимости:

pip install -r requirements.txt

	4.	Сделайте миграции и примените их:

python manage.py makemigrations
python manage.py migrate

	5.	Создайте суперпользователя:

python manage.py createsuperuser

	6.	Запустите сервер разработки:

python manage.py runserver

	7.	Откройте в браузере:

http://127.0.0.1:8000/




🛠️ TODO / В планах
	•	Подключение почтовой отправки сообщений
	•	Подключение PostgreSQL и деплой на VPS
	•	Добавление секции с сертификатами
	•	Переключение языка (RU/EN)

