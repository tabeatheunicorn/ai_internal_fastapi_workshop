# ai_internal_fastapi_workshop
GitHubRepo created for a FastAPI Workshop. Probably each branch is very differnt

## Get started
1. Clone the repo and create your own branch
1. Create a virtual environment for your Python3 version (sth like python3 -m venv env, env being the name of your virtual environment. env is automatically not comitted)
1. Activate your environment (sth like source env/bin/activate or env/Scripts/activate)
1. Install requirements.txt (sth like pip install -r requirements.txt)

## Starting the uvicorn server
''' uvicorn path.to.main:<app-name> --reload '''

If main.py is in your root directory and the application object of fastapi is called app, the command looks like this:
''' uvicorn main:app --reload '''
See  https://fastapi.tiangolo.com/tutorial/first-steps/
