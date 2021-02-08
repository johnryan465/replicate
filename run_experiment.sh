#!/bin/bash

## This is a simple work around to not have to deal with the possibility of python not properly
## reloading the sub repo.
## Just relaunch python after modifying it :/

python create_experiment.py
python enviroment.py
python run_experiment.py