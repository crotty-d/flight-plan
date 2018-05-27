Flight Plan
===========

Python package to calculate the best round trip route (cheapest cost) for an itinerary returning to the home airport using each airport once (5 airport solution).

![alt text](https://github.com/crotty-d/dublin-bikes/raw/master/images/flow_diagram1.png)
![alt text](https://github.com/crotty-d/dublin-bikes/raw/master/images/route_graph.png)


Prerequisites
----------------------

The project was created in a Python 3.6 environment. It uses only standard libraries.


Installation and Setup
----------------------

Simply download the project repository.


Running the Program
-------------------

Open terminal.

Navigate to the repository directory, then to the 'flight_plan' directory (i.e. 'flight_plan/flight_plan') and run this command

```sh
python main.py
```

You will be asked asked for the *complete* path to your input intinerary/routes file.

Then the same for the CSV file you would like to output the best routes to. If you don't enter a path for the output (just hit return), it will be saved in the output directory under bestroutes.csv.

The calculation, along with some informative feedback in the terminal, should begin once both have been entered. An output CSV file should also be created.


Running the Tests
------------------

The tests are designed to run via pytest, so you can enter 'pip install pytest' if its's not already installed.

Navigate to the repository directory (top level 'flight_plan', not 'flight_plan/flight_plan'), which contains the 'tests' directory.

Then simply enter:

```sh
pytest
```

Pytest will go through the 'tests' directory files and run all functions prefixed with 'test_' (should be 16).
