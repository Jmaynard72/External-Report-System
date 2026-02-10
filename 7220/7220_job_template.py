import sys
import logging
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

""" Configuration """
SCRIPT_NAME = Path(__file__).stem
LOG_DIR = Path(r"C:\Users\jmaynard\OneDrive - PAYROLL SOLUTIONS\Projects\External Report System\Automation\logs")

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / f"{SCRIPT_NAME}.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

""" Argument parsing """
def parse_args(argv):
    """
    Expected:
        argv[0] = script name
        argv[1] = company number (required)
        argv[2] = process start (required)
        argv[3] = process end (required)
        argv[4-8] = custom1...custom5 (optional)
    """

    if len(argv) < 4:
        raise ValueError(
            "Usage: script.py <company_number> <process_start> <process_end> "
            "[custom1] [custom2] [custom3] [custom4] [custom5] (optional)"
        )
    
    company_number = argv[1]
    process_start = argv[2]
    process_end = argv[3]

    optional_values = argv[4:9]
    optional_values += [None] * (5 - len(optional_values))

    return{
        "company_number": company_number,
        "process_start": process_start,
        "process_end": process_end,
        "custom1": optional_values[0],
        "custom2": optional_values[1],
        "custom3": optional_values[2],
        "custom4": optional_values[3],
        "custom5": optional_values[4]
    }

""" Business logic entry point """
def run_job(params: dict):
    logging.info("Job started")
    logging.info(f"Parameters: {params}")

    """ Placeholders """
    company_number = params["company_number"]
    process_start = params["process_start"]
    process_end = params["process_end"]

    """ Optional parameters """
    custom1 = params["custom1"]
    custom2 = params["custom2"]
    custom3 = params["custom3"]
    custom4 = params["custom4"]
    custom5 = params["custom5"]

    # TODO: Implement job logic here
    # Create a hidden tkinter window to act as the parent
    root = tk.Tk()
    root.withdraw() # Hides the main window

    # Display a message box (other types available: showwarning, showerror, askquestion, etc.)
    messagebox.showinfo(title="My Message Box", message=f"Company number: {company_number} Process start: {process_start} Process end: {process_end}")

    # Optional: destroy the hidden root window after the message box is closed
    root.destroy()

    logging.info("Job completed successfully")

""" Main """
def main():
    try:
        params = parse_args(sys.argv)
        run_job(params)
    
    except Exception as ex:
        logging.error("Job failed", exc_info=True)
        print(str(ex)) # visable to orchestrator
        sys.exit(1)

if __name__ == "__main__":
    main()
