# SquadMakers challenge    
## Prerequisites
- Install Google Chrome
- Install [Python 3.x.x](https://docs.python.org/3/using/index.html)
- Install [pip](https://pip.pypa.io/en/latest/getting-started/)
- Make sure you have [venv](https://docs.python.org/3/library/venv.html#module-venv) installed (not `virtualenv`). In my case I needed to run `sudo apt install python3.10-venv` even though it was supposed to be included with the standard Python library.
-  If you're using windows, replace every `python3` with a `py` to execute the commands.

## How to run
### Create a new virtual environment  
Open the `terminal` and `cd` into the project directory, then run 
>python3 -m venv env
### Activate the virtual environment
For Unix/macOS
> source env/bin/activate

For Windows
>.\env\Scripts\activate
### Install the requirements
> pip install -r requirements.txt
### Run the tests with Behave
> behave

### More notes
- All the tests documentation written with Gherkin can be found in the `features` folder.









