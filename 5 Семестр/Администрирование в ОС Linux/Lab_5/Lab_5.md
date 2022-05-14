# Лабораторная работа №5. Docker & Docker-compose

#### Задачи лабораторной работы:

1. Изучить механизм работы Docker

2. Научиться создавать образы и запускать контейнеры на их основе

3. Получить навыки работы с Docker-compose

4. Получить навыки работы с томами Docker volumes

5. Получить навыки работы с DockerHub

6. Научиться настраивать CI/CD для проектов (**опционально**)

#### Отчет

1. Скриншот запуска контейнера hello-world из пункта 1.2
   
   <img title="" src="file:///home/vlad/Images/screenshots/1640523991.png" alt="1640523991.png" data-align="center">

2. Содержимое файла .env
   
   ```bash
   SECRET_KEY=”mayatin”
   DEBUG=True
   ```

3. Скриншот работающего сайта, развернутого локально
   
   <img title="" src="file:///home/vlad/.config/marktext/images/2021-12-26-16-35-58-image.png" alt="" data-align="center">

4. Итоговое содержимое файлов Dockerfile, docker-compose.yml и nginx.conf
   
   `Dockerfile`
   
   ```dockerfile
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
   ```
   
   `docker-compose.yml`
   
   ```yaml
   version: '3.8'
   
   services:
     web:
       image: lab_5_django:latest
       volumes:
         - static_value:/django-tutorial/staticfiles/
         - media_value:/django-tutorial/mediafiles/
       env_file:
         - ./.env
     nginx:
       image: nginx:latest
       ports:
         - 443:443
         - 80:8000
       volumes:
         - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
         - static_value:/var/html/static/
         - media_value:/var/html/media/
       depends_on:
         - web
   
   volumes:
     static_value:
     media_value:
   ```
   
   `nginx/default.conf`
   
   ```nginx
   upstream locallibrary {
       server web:8000;
   }
   
   server {
       listen 8000;
   
       server_name 127.0.0.1;
   
       location /static/ {
           root /var/html/;
       }
   
       location /media/ {
           root /var/html/;
       }
   
       location / {
           proxy_pass http://web:8000;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header Host $host;
           proxy_redirect off;
       }
   
       server_tokens off;
   }
   ```

5. Скриншот работающего сайта, развернутого в docker
   
   <img title="" src="file:///home/vlad/.config/marktext/images/2021-12-26-23-39-26-image.png" alt="" data-align="center">

6. Содержимое .github/workflows/
   
   `docker-image.yml`
   
   ```yaml
   name: Build and push Docker images
   
   on:
     push:
       branches: [ master ]
   
   jobs:
     docker:
       runs-on: ubuntu-latest
       steps:
         -
           name: Set up QEMU
           uses: docker/setup-qemu-action@v1
         -
           name: Set up Docker Buildx
           uses: docker/setup-buildx-action@v1
         -
           name: Login to DockerHub
           uses: docker/login-action@v1 
           with:
             username: ${{ secrets.DOCKERHUB_USERNAME }}
             password: ${{ secrets.DOCKERHUB_TOKEN }}
         -
           name: Build and push
           id: docker_build
           uses: docker/build-push-action@v2
           with:
             push: true
             tags: ${{ secrets.DOCKERHUB_USERNAME }}/linux_adm:latest
   ```
   
   `run-tests.yml`
   
   ```yaml
   name: Run tests
   
   on:
     push:
       branches: [ master ]
   
   jobs:
     docker:
       runs-on: ubuntu-latest
   
       steps:
       - uses: actions/checkout@v2
       - name: Set up Python 
         uses: actions/setup-python@v2
         with:
           python-version: 3.8
   
       - name: Install dependencies
         working-directory: ./django_locallibrary_src/
         run: | 
           pip install -r requirements.txt 
       - name: Test with flake8 and django tests
         working-directory: ./django_locallibrary_src/
         run: |
           python manage.py test
   ```

7. Отчет о прохождении тестировании при операции push в репозитории на github
   
   <img title="" src="file:///home/vlad/.config/marktext/images/2021-12-27-01-27-44-image.png" alt="" data-align="center">
   
   [Autotests · GitHub](https://github.com/superpupervlad/linux_adm/runs/4638024432)

8. Ссылку на форк репозитория в вашем аккаунте на гитхабе с финальной версией проекта
   
   [GitHub - superpupervlad/linux_adm](https://github.com/superpupervlad/linux_adm/)
