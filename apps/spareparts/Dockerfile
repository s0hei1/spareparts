FROM python:3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /apps/spareparts

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/apps/spareparts

CMD ["uvicorn", "app.main:app", "--host", "192.168.18.169", "--port", "8000", "--reload"]
