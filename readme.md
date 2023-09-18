# Live Site 
### https://davidhearl.github.io/scene-control/webpage/index.html

## Running

To run in CMD for testing purposes:

```cd ../../local storage/github/scene-control```

To Run the code:

```py run.py```

```py ../data/data_logging.py```

Terminal command to host the developer environment.

```py -m http.server```

## Create Virtual Environment

``` 
# Create the virtual environment
py -m venv ./venv

# Load the script
source ./venv/scripts/activate

# Check pip location has changed
which pip

# Exit virtual environment
deactivate
```

## Install Dependancies

```
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

```
pip freeze --local > requirements.txt
```

## Known Issues
1. Mobile view will only update when the page is reloaded.
