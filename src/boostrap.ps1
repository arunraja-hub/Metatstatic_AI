#Create Vitrual Env
python3 -m venv env
. env/bin/activate

#Django Setup
pip install Django
django-admin startproject app
python3 app/manage.py migrate
python3 app/manage.py runserver

#Frontend 
npm install -g create-react-app
cd app
create-react-app frontend
cd frontend
npm start