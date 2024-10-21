FROM python:3.12.6-alpine3.20

WORKDIR /app

COPY . .

RUN python3 -m venv ./.venv

RUN source ./.venv/Scripts/activate

RUN pip install -r requirements.txt

ENV IVY_FILTER_PORT=8000

ENTRYPOINT uvicorn server_full:app --host 0.0.0.0 --port $IVY_FILTER_PORT
