# External Reporting System (ERS)

## Scope: Monitors a specified folder for new XML files created from Millennium.  Uses the contents of that XML file to execute
##      custom python scripts to create exported data in the form of Excel, CSV, Text jSON etc.  Each script is customed to 
##      the clients specifications.

Millennium report name: JDM_ExternalReport

Python script named Orchestrator.py runs on a schedule from Windows Task Scheduler and looks in a specified folder for 
new XML files.  It reads them to get the script path and parameters for the script and then executes that script.  It
logs successes and failures in a log file.

XML Parameters:
    Company Number : Millennium company number (required)
    Process Start : Starting payroll process number (required)
    Process End : Ending payroll process number (typically will be the same as start) (required)
    Custom1 : User defined values for custom use (optional)
    Custom2 : User defined values for custom use (optional)
    Custom3 : User defined values for custom use (optional)
    Custom4 : User defined values for custom use (optional)
    Custom5 : User defined values for custom use (optional)


