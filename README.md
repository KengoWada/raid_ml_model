# RaiD ML Model

Raid ML Model for backend deployment

## Deploying to Compute Engine

- Clone the repo

- Install Python dependencies `apt-get install python3.8-venv python3-opencv`

- Create a virtual environment `python3 -m venv venv` and activate it `. venv/bin/activate`

- Install all dependencies `pip install -r requirements.txt`

- Download the ML model from Google Drive `gdown --id <file-id> --output best.pt`

- Create a `.env` file and add all the required environment variables then source them `source .env`

- Create `xray_uploads` and `xray_uploads_results` directories

- Start the server `python main.py`

- A dummy request

```bash
curl -X POST http://localhost:5000/ -H 'Content-Type: application/json' -d '{"images": ["https://radiologykey.com/wp-content/uploa
ds/2019/03/f003-016-9781455774838.jpg"]}
```
