# RaiD ML Model

Raid ML Model for backend deployment

## Deploying to Compute Engine

- Start by running the `start.sh` script to install some dependencies and clone the repo

- Switch to the backend directory `cd raid_ml_model`

- Create a virtual environment `python3 -m venv venv` and activate it `. venv/bin/activate`

- Install dependencies `pip install -r requirements.txt`

- Create a `.env` file and add the required environment variables from `.env_example`

  - `touch .env`

  - `cp .env_example .env`

  - `nano .env` to edit the values

  - `source .env` to add them to the session

- Download the ML model from Google Drive `gdown --id <file-id> --output best.pt`

- Start the server `python main.py`

Note: THIS MUST BE DONE IN A DIFFERENT TERMINAL SESSION WITH THE SAME SUDO USER

- A dummy request

```bash
curl -X POST http://localhost:5000/ -H 'Content-Type: application/json' -d '{"images": ["https://radiologykey.com/wp-content/uploa
ds/2019/03/f003-016-9781455774838.jpg"]}
```
