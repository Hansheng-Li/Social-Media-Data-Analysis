# Twitter API: Most Popular Hashtag

## Program Description

### Requirements
Determine the top 10 most popular (mentioned) hashtags within 10 minutes of listening to Twitter public stream “GET statuses/sample”. For each hashtag, print hashtag and number of tweets containing it. Upload the following files as part of your submission:
* source code (Python or Java)
* README with instructions how to run the code
* report consisting of 11 lines, where:
    - first line is formatted as follows: `<startDate>\t<endDate>\n`
    - all other lines are formatted as follows: `<hashtag>\t<tweetCount>\n`

### Command Line Arguments
* `--start`
    - Specifies the start of the 10 minutes period in which the program should search for videos.
    - Format: `YYYY-MM-DD`
    - Example: `--start 2017-09-06`
    - Default: The datetime at runtime of the program. Gotten from `datetime.now()`.



## How to Run the Program
1. Downloaded the zip file, and extract the contents to a location on your computer.
2. From a command line change dictionaries into that location.
2. Install needed packages to your python environment from the requirements.txt file.
    - `pip install -r requirements.txt`
3. Run the following command: `twitter_api_hashtag.py`
    - This command will use the default command line arguments.
    - The program will listen Twitter public stream for 10 mins and get 10 most popular hashtags.
    - The 10 minutes period chosen is at exactly when you run the program until 10 minutes later.
    - The program will print to the console the 10 minutes period used, and the hashtag, and number of each hashtag appear.
    - The program will also output this information to a report file with a file name of `tweet_<start_datetime>_to_<end_datetime>.txt`.

### Examples
Example Call: `python twitter_api_hashtag.py`

Output File: `tweet_20180211-222653_to_20180211-223653.txt`

Output Content:
```
2018-02-11 22:26:53.032000	2018-02-11 22:36:53.032000
iHeartAwards                                      	965
BestFanArmy                                       	768
BTSARMY                                           	423
EXOL                                              	316
BTS                                               	104
페이브_팬캠프_취소해                                  99
BestBoyBand                                       	95
魔女集会で会いましょう                                77
ローソン                                             42
Lチキ                                                42
```
