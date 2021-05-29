# NLU Inbox Importer

This importer is designed to take items from a comma-separated values (CSV) file and import them into Rasa X.

**NOTE**

This importer will only put statements into the NLU inbox if a model containing NLU entries is present. This is a known [bug](https://github.com/RasaHQ/rasa-x/issues/5146) that has been reported.

**Instructions**

- Make sure the CSV file to import is in the same directory as the script and is named **statements.csv**.
- Modify the script to use the statement column (for example, `row[0]` matches the first value in each row and `row[6]` is the fifth).