# CSV to JSON converter

This is a simple Python script the converts a properly formatted CSV file into a separate JSON file. 

## Requirements

This script requires Python version 3x. 

## Configuration 

In the `csvToJson.py` file, ensure the `.csv` filename matches your actual CSV filename:

```Python
with open('sample.csv'...
```

Also, in the same `.py` file, ensure the `.json` filename matches your intended filename for the outputted JSON file. This name does not have to match the `.csv` filename:

```Python
with open('sample.json'...
```
## Running the script 

Ensure the `.csv` and `.py` files are in the same directory and run:

```ssh
python3 csvToJson.py
```
You should now see your JSON file added to the directory. 

***

### Author

Ryan Wells: [ryanwells.com][website]

### License

Licensed under [MIT][mit]. Enjoy.

[website]: http://ryanwells.com
[mit]: http://www.opensource.org/licenses/mit-license.php