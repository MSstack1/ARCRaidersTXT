import sys
from .state import GameState
from .terminals import process_command
from .utils import type_out

class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.running = True
        
    def run(self):
        self.print_header()
        
        while self.running:
            cmd = input(">> ").strip()
            
            if cmd.lower() in ("exit", "quit"):
                type_out("Shutting down ARC Command Terminal...", delay=0.02)
                self.running = False
                continue
            
            output = process_command(cmd, self.state)
            print(output)
            
    def print_header(self):
        print("=== ARC UPLINK TERMINAL ===")
        print("Type 'help' for commands.")
        print("----------------------------")