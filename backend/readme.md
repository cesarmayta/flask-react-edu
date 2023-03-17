#pasos para despliegue

1 - python -m venv venv
2 - source venv/Scripts/activate
3 - pip install -r requirements.txt
4 - export FLASK_APP=run.py
    export FLASK_DEBUG=1
5 - flask run
