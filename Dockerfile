FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements-reviewer.txt requirements.lock ./
RUN python -m pip install --no-cache-dir -c requirements.lock -r requirements-reviewer.txt
COPY app.py ./
USER 10001:10001
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "app", "run", "--host", "0.0.0.0"]
