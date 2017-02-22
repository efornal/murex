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
sudo pip install django-auth-ldap==1.2.6
```

### App configuration for production
```bash
git clone https://github.com/efornal/murex.git

cd murex
cp murex/settings.tpl.py murex/settings.py

mkdir static_production

configure:
STATIC_URL = '/murex/static_production/'
STATIC_ROOT = os.path.join(PROJECT_DIR, '/srv/murex/murex/static_production')
STATICFILES_DIRS = (
        '/srv/murex/static',
)

python manage.py migrate --database=murex_owner
django-admin compilemessages

the first time:
python manage.py loaddata estados

python manage.py collectstatic
```


### Postgres configuration
```bash
createdb murex_db;
createuser murex_owner -P;
createuser murex_user  -P;

GRANT SELECT,INSERT,DELETE,UPDATE ON ALL TABLES IN SCHEMA public TO murex_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO murex_user;


/etc/postgresql/9.3/main/pg_hba.conf
hostssl  murex_db     murex_owner        ::1/128                 password

/etc/init.d/postgresql restart
psql -h localhost -U murex_owner -p 5432 -d murex_db
```


### Apache configuration
En /etc/apache2/conf.d/django
```bash
 WSGIScriptAlias /murex /srv/murex/murex/wsgi.py
 WSGIPythonPath /srv/murex/

 Alias /murex/static /srv/murex/murex/static_production/
 <Directory /srv/murex/murex>
        <Files wsgi.py>
                 Allow from all
         </Files>
 </Directory>
```