import os
import sys

class Experiment4():
    def __init__(self,user) -> None:
        self.user = user
        sys.path.insert(0, f'/home/{user}/BenchLex/benchlex/')
        from experiment import experiment

    def run(self):
        print("Running Experiment4...")