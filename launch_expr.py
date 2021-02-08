# This is the entry point for launching an experiment

from experiments.params import params
import experiments.main as expr



if __name__ == "__main__":
    # Load params from file specified in the cmd line args
    # Create folder corresponding to hash/name of run
    # If already exists add additional run to folder
    # Should be in runs/{name}/params.yml
    expr.run(params)
