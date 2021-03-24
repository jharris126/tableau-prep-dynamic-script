# tableau-prep-dynamic-script

## Summary
Tableau Prep does not currently have a Web Data Connector feauture, however, script steps can be used to pull data from APIs where then can then be further manipulated with the Tableau Prep UI. This demo uses the well-known SWAPI API to query the People endpoint and dynamically generate a result for Tableau Prep based on data received from the API.

## How do I test it out?
If you're familiar with Git, you can just pull the repo, open up the .tfl file, and map the dependencies to the file paths each reside in your environment.

If you aren't familiar with Git, you can open up the .csv, .tfl, and .py files individually and click the "Download" button on the top-right of the bottom pane. Then, similarly open up the .tfl file and map each dependency to the location you downloaded them in your local environment.

## To-Do
Work with the Tableau Prep/Analytics Extensions teams to brainstorm a way to make get_output_schema() wait until the function named in the script step finishes before executing (or vice versa). This would allow the use of python's built in functools lru_cache to cache the result so API calls don't have to be made twice.
