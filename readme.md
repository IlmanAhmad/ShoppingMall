# Prerequisite
- Python(Any version 3+)
- Postgres db(if you want to setup your database in postgres)


# Installation

`pip install -r requirements.txt`

# Database
`db sqlite3` - No changes required

`postgresql - Perform below steps in setting.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_database_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'as_per_your config',
        'PORT': 'as_per_your config',
    }
}
```

# For Window
```shell script
python manage.py migrate
python manage.py runserver
```

# Super User Creation
```shell script
python manage.py createsuperuser
Username : your_user
email : your_email
Password : your_pass
```
# Demo
[Click here](https://github.com/IlmanAhmad/ShoppingMall/blob/main/Demo.md "Demo")