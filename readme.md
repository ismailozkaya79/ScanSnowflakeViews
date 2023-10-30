I have been working on a BI project that requires connection to Snowflake environment 
and frequent checking any substantial changes in views. For monitoring purposes I have 
searched for a quick solution as a query in SQL if we can check the number of rows 
for every views under a schema, but couldn't find any practical solution that works. 
Yes it is easy to check number of rows for each tables but not views. 
So I come up with a Python script that just works on [Snowsight](https://app.snowflake.com/). 
If you think that would be practical for your projects, I hope it will help. 
