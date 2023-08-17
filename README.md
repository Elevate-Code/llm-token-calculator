## Running & Developing the Project Locally

### .env file
Duplicate and rename the `.env.example` file to `.env` adding your own values.

### Initial Setup
Requires Python 3.8 or higher
- Create a virtual environment using `python -m venv venv`
- Run `venv\Scripts\activate` to activate the virtual environment
- Run `pip install -r requirements.txt` to install all dependencies
- Run `streamlit run app.py` to start the server

### Subsequent Runs 🚀
- Run `venv\Scripts\activate` to activate the virtual environment
- Run `streamlit run app.py` to start the server
- (optionally) `pip install -r requirements.txt` if you encounter a `ModuleNotFoundError`

## Deploying to Railway.app
- Dashboard > New Project > Deploy from GitHub repo
- If you get a "Invalid service name" error create a blank service and then link the repo under Settings > Source Repo
- If needed, update project name
- Click on the service, under **Variables**:
    - Add `PORT` with value `8501`
- In the service, under **Settings**:
    - Environment > Domains, click `Generate Domain`, this will be the public URL, change if needed
    - Service > Service Name, change to "app" or similar
    - Service > Start Command, enter `streamlit run app.py`
- You should now be able to view the app at the public URL
- For debugging deployment issues, in the service, under **Deployments**:
    - Click on the latest deployment > `View Logs`
    - Check `Build Logs` and `Deploy Logs` for errors