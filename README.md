# Research guide service Flask

Flask implementation of the a service that returns research guides for a given catalogue reference. 

## Development machine configuration

Use these steps to get up and running

1. Ensure you have Python 3.7 and pip installed
2. Clone this repository
3. Create a virtual environment with `python3 -m venv venv`
4. From the root directory run `source venv/bin/activate` 
5. Install dependencies with `pip install -r requirements.txt`
6. Start the application with `flask run`
7. See the command line for the URL to visit
8. When finished run `deactivate` from the virtual environment

## Running tests

From the project root run `pytest` (within an activated python environment).