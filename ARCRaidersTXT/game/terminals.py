from .puzzles import get_puzzle
from .utils import type_out

def process_command(cmd, state):
    if cmd == "help":
        return (
            "Commands:\n"
            "  status      Show shift info\n"
            "  task        Start a new communication task\n"
            "  solve       Attempt to solve current puzzle\n"
            "  clear       Clear screen (kinda)\n"
        )

    if cmd == "status":
        return (
            f"Sector: {state.active_sector}\n"
            f"Time: {state.resources['time']}\n"
            f"Power: {state.resources['power']}\n"
            f"Keys: {state.resources['keys']}"
        )

    if cmd == "task":
        state.current_task = get_puzzle(state.active_sector)
        type_out(f"[COMMS] Incoming Raider transmission:\n{state.current_task['prompt']}", delay=0.02)

    if cmd.startswith("solve"):
        if not state.current_task:
            return "No active task."

        attempt = cmd.replace("solve", "").strip()
        if attempt == state.current_task["answer"]:
            state.current_task = None
            type_out("[COMMS] Correct. Raider extracted safely.", delay=0.02)
        else:
            type_out("[COMMS] Incorrect. Raider still trapped.", delay=0.02)

    if cmd == "clear":
        return "\n" * 50

    return "Unknown command."
