# HOSPITAL INFORMATION
Web Application built with Python using Flask Micro Framework

## Introduction
This Application is used for Hospital Information that provide system for Patient that want to make an appointment with a docter

## Admin email and password
* **Email** - admin@admin.com
* **Password** - admin

**Note** 
* You can create your own admin account through this link (localhost) [Create admin account](http://127.0.0.1:5000/admin/register/)
* Or here online app (Deployed) [Create admin account](https://hospital-information.herokuapp.com/admin/register)


## Built with
* [Python Programming Language](https://www.python.org/) - High-level programming language
* [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) - Python web Framework
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - ORM used to modelling Database
* [Heroku - Python](https://devcenter.heroku.com/categories/python-support) - Cloud Deployment

### Installation
To use this application on your system follow the intruction bellow
Create new virtual enviroment

```
python -m venv venv
```

Activate created virtual enviroment

```
source venv/bin/activate
``` 

Install all requirements.txt
```
pip install -r requirements.txt
```

Create your database (run it on your terminal)
```
from hospital import db

db.create_all()
```

That now you can visit this link to use application [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
Here link to deployed app [https://hospital-information.herokuapp.com](https://hospital-information.herokuapp.com)