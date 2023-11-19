FROM python:latest

COPY main.py .
COPY shape_calculator.py .

ENTRYPOINT ["python3","main.py"]
