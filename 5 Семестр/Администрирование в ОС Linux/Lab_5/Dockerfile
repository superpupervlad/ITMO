FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
SHELL ["/bin/bash", "-c"] 

RUN mkdir django-tutorial
RUN git clone https://github.com/mdn/django-locallibrary-tutorial django-tutorial
WORKDIR django-tutorial

RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic
RUN echo $(python3 manage.py test)
RUN python3 manage.py createsuperuser
CMD gunicorn locallibrary.wsgi:application --bind 0.0.0.0:8000
