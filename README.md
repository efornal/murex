# murex
Printer toners administration


### Package Installation
```bash
sudo apt-get install python2.7
sudo apt-get install postgresql-9.4
sudo apt-get install python-psycopg2
sudo apt-get install python-pip=1.5.6-5
sudo apt-get install python-yaml=3.11-2
sudo apt-get install python-ldap=2.4.10-1
sudo apt-get install python-dev=2.7.9-1
sudo apt-get install gettext=0.19.3-2
sudo pip install django-suit==0.2.13
sudo pip install django==1.8
sudo pip install django-extensions==1.5.5
sudo pip install django-bootstrap-themes==3.1.2
```

### Postgres configuration
```bash
createdb murex_db;
createuser murex_owner -P;

/etc/postgresql/9.3/main/pg_hba.conf
hostssl  murex_db     murex_owner        ::1/128                 password

/etc/init.d/postgresql restart
psql -h localhost -U murex_owner -p 5432 -d murex_db
```

### App configuration
```bash
git clone https://github.com/efornal/mollys.git

cd mollys
cp mollys/settings.tpl.py mollys/settings.py

mkdir static_production

habilitar:
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

python manage.py syncdb
python manage.py migrate
python manage.py loaddata estados
django-admin compilemessages

python manage.py collectstatic
```



