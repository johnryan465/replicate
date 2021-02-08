# This is the entry point for creating an experiment

from git import Repo
import yaml
import os

# subdir = Repo(self.rorepo.working_tree_dir)


if __name__ == "__main__":
    dir = ""
    with open("config.yml", 'r') as stream:
        try:
            dir = yaml.safe_load(stream)["config"]["directory"]
        except yaml.YAMLError as exc:
            print(exc)

    subdir = Repo(os.getcwd() + "/" + dir)
    new_branch = subdir.create_head('feature')
    print(subdir.heads)
    subdir.git.checkout(new_branch)
