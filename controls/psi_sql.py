from sqlalchemy import create_engine, text
import pandas as pd

def run_mssql_query(query: str, server: str, database: str, driver: str = "ODBC Driver 17 for SQL Server"):
    """
    Docstring for run_mssql_query
    
    :param query: Description
    :type query: str
    :param server: Description
    :type server: str
    :param database: Description
    :type database: str
    :param driver: Description
    :type driver: str

    Executes a SQL query on a MS SQL Server database using a trusted authentication and returns
    a pandas DataFrame.
    """

    # Trusted connection string
    connection_string = (
        f"mssql+pyodbc://@{server}/{database}"
        f"?driver={driver.replace(' ','+')}"
        f"&trusted_connection=yes"
        f"&TrusServerCertificate=yes"
    )

    # Create SQLAlchemy engine
    engine = create_engine(connection_string)

    # Execute query and return DataFrame
    with engine.connect() as conn:
        df = pd.read_sql(text(query),conn)

    return df 