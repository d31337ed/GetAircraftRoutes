FROM python:3.11
WORKDIR /routes-app
COPY ./requirements.txt /routes-app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /routes-app/requirements.txt
RUN apt-get install -y cron
RUN crontab crontab
COPY ./ /routes-app/
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]