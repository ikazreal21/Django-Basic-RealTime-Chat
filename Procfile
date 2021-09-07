# web: gunicorn ChatRoom.wsgi --log-file -

web: daphne ChatRoom.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=ChatRoom.settings -v2
