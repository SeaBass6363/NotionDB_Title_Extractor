# Notion Database Title Extractor Script
## Table of Contents
- [Description](#description)
- [Required Files](#required-files)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

<br><br>

## Description 

When coping directly from a Notion database you get the individual link for each row and a title (or whatever is in the first column of that database). 

This is irritating when wanting to copy the title of the rows in a notion database to use in other applications. 

For now this is just a simple python script that will remove all the fluff and leave you with the data with what is important (to me - the title) all separated by a new line for ease of reading. 

<br>

## Required Files

This project requires the following files:

1. **.env** - This is for environment variables
        This is only used for the file_path (Where you saved the data copied from notion)
2. **config.json** - Config settings for the script
        This is if you want to add your file_path from the config file instead of using the dotenv
        
**Choose one or the Other**

<br>

## Installation
To install the necessary dependencies, run the following:

```bash
pip install -r requirements.txt

```

<br>

## Usage
Once the required files are downloaded, run the script by executing: 
``` bash
python notion_title_extractor.py
```

<br>

## Contributing
If you would like to contribute, fork the repo and submit a pull request 

<br>

## License 
This script is licensed under the [MIT License](LICENSE).
