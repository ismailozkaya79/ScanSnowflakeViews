# This code scans row counts of every views under a schema

# 👇🏻👇🏻 change only these 👇🏻👇🏻
thedatabase = 'MyDatabaseName'
theschema   = 'MySchemaName'


############ no change needed below #################
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    tableName = thedatabase+'.INFORMATION_SCHEMA.VIEWS' 
    listofviews = session.table(tableName).filter(col("TABLE_SCHEMA")==theschema)

    viewrows = []
    for view in listofviews.collect():
        view_name = view["TABLE_NAME"]
        row_count = session.sql(f"SELECT COUNT(*) AS COUNT FROM {view_name}").collect()[0]["COUNT"]
        viewrows.append((thedatabase, theschema, view_name, row_count))
    
    row_count_df = session.create_dataframe(viewrows, ["Database","Schema","View Name","Row Count"]).sort("View Name")
    
    return row_count_df
