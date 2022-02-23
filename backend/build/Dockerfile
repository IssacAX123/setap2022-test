FROM python:3.811
WORKDIR /src
COPY ../src/ ./
RUN pip install -r requirements.txt
ENV PORT=5000
EXPOSE 5000
CMD ["python", "app.py"]
