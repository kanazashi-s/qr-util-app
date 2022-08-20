FROM python:3.9.13
EXPOSE 8080
WORKDIR /workspace

COPY . /workspace

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/workspace/src"

CMD ["streamlit", "run", "src/app.py", "--server.port", "8080"]