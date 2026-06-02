START SERVER:

cd Documents/GitHub/MarioMaker-Backend/app/;
source venv/bin/activate;
cd ../;
source config/sample.development.env;
cd app/;
python manage.py migrate;
python manage.py runserver;

===================================================================

MODIF DU MODEL:

python manage.py makemigrations mario_maker;
python manage.py migrate;

===================================================================

EN CAS DE TYPE MISSMATCH

python manage.py flush
