## 🚨 Delete this top section after cloning 🚨

To get started with this template, follow all these steps:

1. On this GitHub repo page, in the top right corner above files, click the **Use this template** > **Create a new repo** button.
2. OR use `git clone https://github.com/Ecom-Analytics-Co/streamlit-projectstarter.git yourprojectname` to clone this repo to your local machine.
3. Edit the `requirements.txt` file to match the dependencies you need for your project.
4. Delete the `/pages` folder if you are only building a single page app.
5. Check out the [streamlit_tips.md](streamlit_tips.md) file for how to use the debugger with VS Code or PyCharm and other tips.
6. Run the `start_project.py` script to create necessary files, then delete the script file as it is no longer needed.
7. ⚠️ Remove this entire section from your README.md file once you've cloned the repository and are ready to proceed with your project.

---

## Running & Developing the Project Locally

### .env file
Duplicate and rename the `.env.example` file to `.env` adding your own values.

### Initial Setup
Requires Python 3.8 or higher
- Create a virtual environment using `python -m venv venv`
- Run `venv\Scripts\activate` to activate the virtual environment
- Run `pip install -r requirements.txt` to install all dependencies
- Run `streamlit run app.py` to start the server

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