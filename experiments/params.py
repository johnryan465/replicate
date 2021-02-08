from dataclasses import dataclass

@dataclass
class Params:
    epochs : int = 1

params = Params(epochs = 10)