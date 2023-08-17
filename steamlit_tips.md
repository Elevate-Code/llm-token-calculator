## Using the debugger with PyCharm

In the **Run/Debug Configuration** window, add a new Python configuration with the following settings:
- Confirm that the "Python interpreter" is set to the virtual environment you created and your "Working directory" is correct
- Select `module` from the "Run script or module" dropdown
- Enter `streamlit` in the "Module name" field
- Using the "Modify options" dropdown, select `Add option` > `Parameters`
- Enter `run app.py` in the "Parameters" field

## Using the debugger with VS Code

Add the following configuration to your `launch.json` file:

```json
{
"configurations": [
    {
        "name": "Python:Streamlit",
        "type": "python",
        "request": "launch",
        "module": "streamlit",
        "args": [
            "run",
            "${file}"
        ]
    }
 ]
}
```

# Common Gotchas

`st.button` does not retain state, use caution with what actions are nested inside of it
See here: https://docs.streamlit.io/library/advanced-features/button-behavior-and-examples#when-to-use-if-stbutton