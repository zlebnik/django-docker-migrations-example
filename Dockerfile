FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN pip install pipenv

WORKDIR /code
COPY Pipfile* .
RUN pipenv install --system --deploy --ignore-pipfile

COPY . .
CMD python example/manage.py runserver
