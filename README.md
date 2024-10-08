# Prerequisites

- Python 3.12.6 or similar, 3.11 probably works? (See requirements.txt for specific packages)

- Docker if launching that way

# Launch 

## Commandline
`uvicorn server_full:app --reload`

## Or With Docker
`docker compose up -d `

## Then
Go to `http://localhost:8000/`
or `http://localhost:8000/docs` for the debug view provided with FastAPI

# Known Issues
A good portion of the code in `static/js/main.js` is esoteric, I don't know the intricacies of it at all...

Drag and Drop is not implemented, yet it is stated as such in the `static/html/index.html`

