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

## Trying it out

Once running, you should be able to test this service by visiting `localhost:5000/guides/<catalogue reference>` (replacing `<catalogue reference>` with a catalogue reference Here are a couple of examples:

* [ADM 1/24558](http://localhost:5000/guides/ADM%201/24558)
* [HO](http://localhost:5000/guides/HO)
* [PROB 1/4](http://localhost:5000/guides/PROB%201/4)
