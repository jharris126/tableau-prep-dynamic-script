# tableau-prep-dynamic-script

## SUMMARY

Tableau Prep does not currently have a Web Data Connector feauture, however, script tasts can be used to pull data from APIs then further manipulated in tableau prep. This demo uses the well-known SWAPI API to query the People endpoint and dynamically generate a result for Tableau Prep based on the data received from the API.


## To-Do
Work with a Tableau Prep team to brainstorm a way to make get_output_schema() wait until the function named in the script component finishes before executing (or vice versa). This would allow the use of python's built in functools lru_cache to cache the result so API calls don't have to be made twice.
