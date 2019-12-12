FROM python:3.7-alpine
WORKDIR /
COPY requirements.txt .
COPY setup.py .
RUN pip install -r requirements.txt
COPY entry_point.sh .
CMD ["./entry_point.sh"]