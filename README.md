# replicate

*This is not an attempt to replace actual machine learning frameworks*

*This is just a (relatively simple) tool to help improve the experimental process*

*Nothing here is unique to a specific ML framework*


## How to run

- Clone this repo
- Work from within the experiments folder
- When you want to launch a new experiment run ```python experiment.py -i```

In machine learning, production and research the issue of clean replication is something which we have to deal with. We have many frameworks which impliment the mathematically difficult algorithms which we use and design.

But at the level of production runs and experiments we often come up with our own solutions for making sure that we are running "repeatable" and how to achieve this goal.

In science each operation we perform on our data / model should be justified, and clearly indicated. This level of abstraction allows for easy understanding of what happens when you change a particular aspect of your model. When randomness is involved eg random seeds we can easily rerun with different ones to ensure that our results are valid.

In ML production we wish to have ability to compose our data pipline in a clear, repeatable and easily modifiable fashion, to easily spot issues when retraining our models on new data etc.

## Enviroment

What was the enviroment in which the run occured?

- Python enviroment (pip , conda, etc)
- CUDA Libs
- etc


We can simply track the enviroment, however additionaly when we are using a supported tool (like conda). We can actually create and prepare the enviroment before we run.


```
create_env.sh
```


## Code

What code was actually ran?

When working on machine learning as a researcher, you will often alter and run code. Then modify it again, rinse and repeat.

Because we are testing and experimenting with different problems, it is easy to loss track of what modifications we have. Often we don't want to "pollute" our code base with random re runs and code changes, however this actually often detrimental to the research process.

git is something which we can actually take advtange of to achieve these ends.

The code we are working with for a particular experiment will be automatically added as a branch to our repo. Code isn't lost, can easily to be retrieved and the experiment rerun.

## Hyperparams

While we can just view the diff of 2 branches to see what was changed between the 2 runs, this quickly gets out of hand when trying to compare large amounts of runs. The hyper parameters of the run can be abstracted out, for easy reading.

## Results

We also want the results of the run to be tracked in a repeatable fashion, configure the outputs you wish to track and run away!

## Data

The data processing pipeline should be included in every experiment. As this can be expensive the code to process it can be abstracted out (ideally into something like a bash file), and we can check if the exact pre-production steps which we want have been followed by comparing the hash of this script with the hash recorded.

## Multiple-runs

If we wish to perform multiple runs of an experiment, or perhaps do interactive hyper parameter searching this should be done and recorded from the same codebase. To make it easy to perform possible merges of the results of these experiments perhaps from a distributied enviroment each will be tracked in an independent file so no merge conflicts.

## Randomness

We should track the starting seeds of any random number generators that we use in our experiments.

## Collate

We can automatically collect the results from each of the runs from the branches by running.

```
sh ./get_res.sh
```