## PyFriend

PyFriend is a CLI tool for python developers.

This App will list all standard modules(libraries) that python has already built in.

This App can print to terminal the manual page of every standard module that you select.

This App will open the official python3 docs in HTML form for easy use.

PyFriend is a very handy tool that any python developer should have.

# Dependencies

To install dependencies: ```pip3 install -r requirements.txt```

# Usage

- First, you need to change 'configuration.ini'.

- Path option is the application path. Update this with folder path. Exemple: /home/user/Desktop/Py-Friend

- Python_url option is from the python3 official website. The url is found in 'download python3 docs' on website.

- You can leave python_url as default for python3.7.3 html docs.

For Help: ```python3 pyfriend.py -h```

For listing all standatd modules: ```python3 pyfriend.py -l```

For printing a manual page of a module from list: ```python3 pyfriend.py -m [NAME OF MODULE]```

Exemple: ```python3 pyfriend.py -m csv```

For opening docs in HTML form: ```python3 pyfriend.py -d```

For removing and downloading new HTML docs from website: ```python3 pyfriend.py -r```





