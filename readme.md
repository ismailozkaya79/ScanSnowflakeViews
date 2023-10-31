I have been working on a BI project that requires connection to Snowflake environment and frequently checking any substantial changes in the views under a specific schema. For monitoring purposes I have searched for a quick solution as a query in SQL if we can check the number of rows for every views under a schema, but couldn't find any practical solution that works. Yes it is easy to check number of rows for each tables but not views. 
# Get Row Counts of Snowflake Views 
In Snowsight there are two types of worksheets to begin with: SQL and Python. If I could not solve the problem in SQL, why not using Python? So I come up with a Python script that just works on [Snowsight](https://app.snowflake.com/). If you think that would be practical for your projects, I hope it will help. Just copy the code into a python worksheet, than make the necessary changes and designate the role and the warehouse. 

Steps of running the script:
1. Open a python worksheet
2. Select the role
3. Select the warehouse
4. Copy & paste the code
5. Change two variables in the code: the *database* and the *schema*.
