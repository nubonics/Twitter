# Twitter
API driven comment and like extractor for all followees from a starting profile

## Distribution compatibility

 - Windows 7
 -  Windows 10
 Other operating systems have not been tested for compatibility.

## Requirements
A twitter app is required to use this program.
For more details, please see: https://developer.twitter.com/en/apps

## Initial setup
After you have created your own Twitter App...
Fill in the credentials.json file with your twitter app credentials
Next, install the required dependencies via pip

    pip install -r requirements.txt

## Modifying main.py
If you wish this program to scrape tweets that are less than 8 days old, run the program as is.
Otherwise, please edit tweet_dumperv1.py Line 55 Column 44 and replace the 8 with a 31

## Usage:

    python twitter_main.py --screen_name="nubonics"
