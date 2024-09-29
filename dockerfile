FROM python:3.11
WORKDIR /routes-app
COPY ./requirements.txt /routes-app/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /routes-app/requirements.txt
RUN apt update && apt upgrade && apt-get install -y cron
RUN chmod +x start.sh
RUN (crontab -l 2>/dev/null; echo "20 04 * * * /usr/local/bin/python3 /routes-app/getAirlinesList.py > /routes-app/logs/searches-daily-update.log 2>&1") | crontab -
COPY ./ /routes-app/
CMD ["./start.sh"]