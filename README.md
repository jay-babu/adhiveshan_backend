# Adhiveshan Backend

## Conda Startup

1. Download Anaconda or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
    1. Make sure `conda` is in your path
2. `conda create -n adhiveshanAPI`
3. `conda activate adhiveshanAPI`
4. `pip install -r requirements.txt`

## Django Setup

1. Set `DATABASE_URL` and `SECRET_KEY` in Environment Variables
2. `python manage.py runserver 8100`
    1. This runs Django
3. `python manage.py makemigrations`
    1. This will set up any database migrations necessary but not commit them
4. `python manage.py migrate`
    1. This will commit all migrations in database (irreversible)
   
## Learn more about Django

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction