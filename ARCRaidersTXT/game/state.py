class GameState:
    def __init__(self):
        self.active_sector = "A1"
        self.resources = {
            "time": 120,
            "power": 5,
            "keys": [],
        }
        
        self.current_task = None