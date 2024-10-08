FROM python:3.12.6-alpine3.20

WORKDIR /app
COPY . /app



RUN python3 -m venv ./.venv

RUN source ./.venv/Scripts/activate

RUN pip install -r requirements.txt
ENV IVY_FILTER_PORT=8000
ENTRYPOINT uvicorn server_full:app --port $IVY_FILTER_PORT
