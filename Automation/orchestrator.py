import os 
import shutil
import subprocess
import logging
import configparser
import xml.etree.ElementTree as ET
from datetime import datetime

""" Load cofiguration """
config = configparser.ConfigParser()
config.read("config.ini")

INCOMING_DIR = config["paths"]["incoming"]
PROCESSED_DIR = config["paths"]["processed"]
ERROR_DIR = config["paths"]["error"]
LOG_FILE = config["paths"]["logfile"]
PYTHON_EXE = config["paths"]["pythonexe"]

""" Logging """
logging.basicConfig(
    filename=LOG_FILE,
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

""" Helpers """
def parse_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    return {
        "company_number": root.findtext("company"),
        "process_start": root.findtext("processStart"),
        "process_end": root.findtext("processEnd"),
        "script_path": root.findtext("scriptPath"),
        "custom1": root.findtext("custom1"),
        "custom2": root.findtext("custom2"),
        "custom3": root.findtext("custom3"),
        "custom4": root.findtext("custom4"),
        "custom5": root.findtext("custom5")
    }

def move_file(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(src, os.path.join(dest_dir, os.path.basename(src)))

def execute_script(
        script_path : str,
        company_number : str,
        process_start : int,
        process_end : int,
        custom1 : str,
        custom2 : str,
        custom3 : str,
        custom4 : str,
        custom5 : str
        ):
    
    cmd = [
        PYTHON_EXE,
        script_path,
        str(company_number),
        str(process_start),
        str(process_end),
        str(custom1),
        str(custom2),
        str(custom3),
        str(custom4),
        str(custom5)
    ]
    
    logging.info(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    
    logging.info(result.stdout)

""" Main processing loop """
def main():
    logging.info("Orchestrator started")

    for filename in os.listdir(INCOMING_DIR):
        if not filename.lower().endswith(".xml"):
            continue

        xml_path = os.path.join(INCOMING_DIR, filename)
        logging.info(f"Processing {filename}")

        try:
            job = parse_xml(xml_path)

            if not all(job.values()):
                raise ValueError("Missing requried XML values")
            
            execute_script(
                job["script_path"],
                job["company_number"],
                job["process_start"],
                job["process_end"],
                job["custom1"],
                job["custom2"],
                job["custom3"],
                job["custom4"],
                job["custom5"]
            )

            #move_file(xml_path, PROCESSED_DIR)
            logging.info(f"{filename} processed successfully")

        except Exception as ex:
            logging.error(f"{filename} failed: {ex}", exc_info=True)
            #move_file(xml_path, ERROR_DIR)

    logging.info("Orchestrator finished")


if __name__ == "__main__":
    main()


