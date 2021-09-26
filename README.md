# NFL Team Stat Cleaner
Python Script to identify missing Home/Away Teams

## Description

The Script will analyze the JSON payloads that are produced by the NodeJS Scraper application to correct missing Home and Away team names.  These are retrieved from the Play-by-Play drive section to identify the home and way team values.

### Executing

The script expects the values to be present in the __src/input__ directory (create it if it is not present) and will output the results into the __src/output__ directory.  You may need to create these directories as they will be ignored by source control.

To run the script, execute the following:

'''bash
python fix-teams.py
'''
