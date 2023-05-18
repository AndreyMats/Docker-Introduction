FROM python:latest
RUN pip install clickhouse-driver && pip install pandas
WORKDIR /home/andrey
COPY ./hand_db.py ./hand_db.py
ENTRYPOINT ["python3" , "./hand_db.py"]
