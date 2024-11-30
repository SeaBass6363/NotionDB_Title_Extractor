# Notion Book Title Extractor

## Table of Contents
- [Description](#description)
- [Required Files](#required-files)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description 

When coping directly from a Notion database you get the individual link for each row and a title (or whatever is in the first column of that database). 

This is irritating when wanting to copy the notion database to use in other applications. 

For now this is just a simple python script that will remove all the fluff and present the data with what is important to me (the title) all separated by a new line for ease of reading. 

## Required Files

This project requires the following files:

1. **.env** - This is for environment variables
2. **config.json** - Config settings for the script

## Installation
To install the necessary dependencies, run the following:

```bash
pip install -r requirements.txt

```
## Usage
Once the required files are downloaded, run the script by executing: 
``` bash
python notion_title_extractor.py
```

## Contributing
If you would like to contribute, fork the repo and submit a pull request 

## License 
This script is licensed under the [MIT License](LICENSE).