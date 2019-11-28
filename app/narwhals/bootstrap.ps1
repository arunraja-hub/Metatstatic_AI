#Setup Virtual Env
python3 -m venv env
. env/bin/activate

#Django Backend Install
pip install Django
django-admin startproject app
python3 app/manage.py migrate
python3 app/manage.py runserver

#ReactJS Frontend
npm install -g create-react-app
cd app
create-react-app frontend
cd frontend
npm start