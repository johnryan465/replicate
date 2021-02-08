# replicate

*This is not an attempt to replace actual machine learning frameworks*

*This is just a (relatively simple) tool to help improve the experimental process*

*Nothing here is unique to a specific ML framework*

*This is basically automatically doing some git stuff, with some config and data management. I know __you__ could do this this stuff manually, but some mere mortals could use some help*

---

## How to run

- Clone this repo
- Have your repo for tracking results as a submodule
- Set the name of this in config.yml
- When you want to launch a new experiment run ```python experiment.py -i```


--- 

## Objective
In machine learning, production and research the issue of clean replication is something which we have to deal with. We have many frameworks which impliment the mathematically difficult algorithms which we use and design, but we spend much of our time dealing with more of the simple issues.

At the level of production runs and experiments we often come up with our own solutions for making sure that we are running "repeatable" and how to achieve this goal.

In science each operation we perform on our data / model should be justified, and clearly indicated. This level of abstraction allows for easy understanding of what happens when you change a particular aspect of your model. When randomness is involved eg random seeds we can easily rerun with different ones to ensure that our results are valid.

In ML production we wish to have ability to compose our data pipline in a clear, repeatable and easily modifiable fashion, to easily spot issues when retraining our models on new data etc.

**Note: The order of when features will be added is basically when I need them, but if you would like something additional let me know**

--- 

## Features




### Enviroment (Todo)

What was the enviroment in which the run occured?

- Python enviroment (pip , conda, etc)
- CUDA Libs
- etc


We can simply track the enviroment, however additionaly when we are using a supported tool (like conda). We can actually create and prepare the enviroment before we run.


```
create_env.sh
```


### Code (Todo)

What code was actually ran?

When working on machine learning as a researcher, you will often alter and run code. Then modify it again, rinse and repeat.

Because we are testing and experimenting with different problems, it is easy to loss track of what modifications we have made. Often we don't want to "pollute" our code base with random re runs and code changes, however this actually often detrimental to the research process.

git is something which we can actually take advantange of to achieve these ends.

The code we are working with for a particular experiment will be automatically added as a branch to our repo. Code isn't lost, can easily to be retrieved and the experiment rerun.


### Hyperparams (Todo)

While we can just view the diff of 2 branches to see what was changed between the 2 runs, this quickly gets out of hand when trying to compare large amounts of runs. The hyper parameters of the run can be abstracted out, for easy reading.

### Results (Todo)

We also want the results of the run to be tracked in a repeatable fashion, configure the outputs you wish to track and run away!

### Data (Todo)

The data processing pipeline should be included in every experiment. As this can be expensive the code to process it can be abstracted out (ideally into something like a bash file), and we can check if the exact pre-production steps which we want have been followed by comparing the hash of this script with the hash recorded. If they have been, we skip and reuse else restart and run again. Different data is a different experiment.

### Multiple-runs (Todo)

If we wish to perform multiple runs of an experiment, or perhaps do interactive hyper parameter searching this should be done and recorded from the same branch. To make it easy to perform possible merges of the results of these experiments perhaps from a distributied enviroment each will be tracked in an independent file so no merge conflicts.

### Randomness (Todo)

We should track the starting seeds of any random number generators that we use in our experiments.

---

## Use cases

### Collate

We can automatically collect the results from each of the runs from the branches, this is part of the real magic of this. We can easily query our experiments?!?!?!?!? 

- Want to see what experiments reached over 90% accuracy on your problem? No problem
- Did I actually test this thing? Hopefully? Go check
- Fuck what experiments has this bug impacted???? Use the git history to see what experiment branches are impacted. Fix all of them. Rerun the affected experiments. Promise yourself you won't let this happen ever again. And repeat

```
sh ./get_res.sh
```

### Combining Code Bases

This also leads to a reasonable straightforward way of ensuring that when you are trying to combine two distint branches of ML code that something hasn't gone terribly wrong. You have the ability to see how it worked previously and can check that on your new code base, you are getting similar-ish results and if you aren't getting them anymore you can see at what point you diverged.


--- 

