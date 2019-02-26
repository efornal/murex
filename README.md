# murex
Printer toners administration


### Package Installation debian stretch
```bash
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install libpq-dev
sudo apt-get install libyaml-dev
sudo apt-get install libldap2-dev
sudo apt-get install libsasl2-dev
sudo apt-get install gettext
sudo apt-get install libjpeg-dev
sudo apt-get install zlib1g-dev
sudo apt-get install python-dnspython # for reidi
sudo apt-get install mariadb-client # for dumpserver
sudo apt-get install pkg-config
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgirepository1.0-dev
```

### Python lib Installation
```bash
pip install -r requieremens.txt
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