FROM python:latest

COPY main.py .
COPY shape_calculator.py .

RUN pip install test_module

ENTRYPOINT ["python3","main.py"]
