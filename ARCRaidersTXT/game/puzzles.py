import random
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "sectors.json")

with open(DATA_PATH, "r") as f:
    SECTORS = json.load(f)

def get_puzzle(sector):
    puzzles = SECTORS[sector]["puzzles"]
    return random.choice(puzzles)