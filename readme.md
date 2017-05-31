# face analyzer 👱

#### tasks
- [ ] annotate face images 👨‍👨‍👦‍👦
- [ ] train model on faces annotations 🏋️
- [ ] fix web front-end aesthetics 💁
- [ ] get upload to work 🆙
- [x] database structure 🛢

#### running development flask server:
    1. git clone https://github.com/abbirdboy/face_analyzer.git
    2. Download Anaconda 3 (Python3)
    3. Run 'conda env create -f environment.yml' in root directory
    4. Run 'source activate face_analyzer'
    5. 'cd web'
    6. 'mkdir instance'
    7. 'touch instance/config.py'
        a. type 'psql' in command line
        b. run 'CREATE DATABASE face_analyzer;' and then quit by type '\q'
        c. add SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/face_analyzer' to instance/config.py
        d. add SECRET_KEY = [generate a key here]

    8. 'python manage.py db upgrade'
    9  'python manage.py runserver'
    10. Flask Dev Server should be running

#### project Structure:
```text
├── data/
├── environment.yml
├── models/
├── notebooks/
├── readme.txt
└── web
    ├── app
    │   ├── __init__.py
    │   ├── app.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── static
    │   ├── templates
    │   └── views.py
    ├── config/
    ├── info.txt
    ├── manage.py
    ├── migrations/
    └── run.py
```
