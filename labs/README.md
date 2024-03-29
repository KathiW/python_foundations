# Running the labs

## Here's the software stack I use:
* [Python >=3.7](https://www.python.org/downloads/)
* [VS Code](https://code.visualstudio.com/)
* [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Git](https://git-scm.com/downloads)

## Installing

First, make sure you have the repository:
  git clone https://github.com/bathcat/python_foundations
  cd python_foundations/labs

### On Windows
  py -m venv .venv
  .\.venv\Scripts\activate
  py -m pip install -r requirements.txt


### On Linux:
  python3 -m venv .venv
  source ./.venv/bin/activate
  pip install -r requirements.txt

### Test it out:
```
py .\src\A.1.HelloSetup\startingpoint\mood.py
```

## Troubleshooting

You __may__ need to install [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
Here's how I did on Linux:
  `sudo apt-get install python3-pip python3-venv idle3`
Then try activating again.