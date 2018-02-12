# -*- coding: utf-8 -*-
#!/usr/bin/python

# Author: Hansheng Li
# Version: Python 2.7 & Windows
# Last date modify: 2-11-2018

#-----------------------------------------------------------------------
# Determine the top 10 most popular (mentioned) hashtags
# within 10 minutes of listening to Twitter public stream
# “GET statuses/sample”. For each hashtag, print hashtag
# and number of tweets containing it. Upload the following
# files as part of your submission:
#
# source code (Python or Java)
# README with instructions how to run the code
# report consisting of 11 lines, where:
# first line is formatted as follows: <startDate>\t<endDate>\n
# all other lines are formatted as follows: <hashtag>\t<tweetCount>\n
#-----------------------------------------------------------------------

import argparse
from twitter import *
from datetime import datetime, timedelta


def main(parser):

    # get end datetime from options or use the current time if no option given
    if parser.start is None:
        start_dt = datetime.now()
    else:
        start_dt = datetime.strptime(parser.end, '%Y-%m-%d')
    end_dt = start_dt + timedelta(minutes=10)

    # create report file name based on start and end datetimes
    report_file_name = 'tweet_'
    report_file_name += start_dt.strftime("%Y%m%d-%H%M%S") + "_to_"
    report_file_name += end_dt.strftime("%Y%m%d-%H%M%S") + ".txt"

    # write report string to file
    report_file = open(report_file_name, "w")

    # print start and end datetime, and add line to reportstring
    print(str(start_dt) + "\t" + str(end_dt))
    report_file.write(str(start_dt) + "\t" + str(end_dt) + "\n")

    # load API credentials
    config = {}
    execfile("config.py", config)

    # create twitter API object
    auth = OAuth(config["access_key"], config["access_secret"],
                 config["consumer_key"], config["consumer_secret"])

    # Start to listening
    stream = TwitterStream(auth=auth, secure=True)
    tweets = stream.statuses.sample()

    # Store all the hashtag
    hashtag_dict = {}

    for tweet in tweets:
        if 'entities' in tweet:
            for hashtag in tweet['entities']['hashtags']:
                if hashtag['text']:
                    if hashtag['text'] not in hashtag_dict:
                        hashtag_dict[hashtag['text']] = 0
                    else:
                        hashtag_dict[hashtag['text']] += 1
        if datetime.now() >= end_dt:
            break

    # Sort it and print the top ten
    sorted_hashtag = sorted(hashtag_dict, key=hashtag_dict.__getitem__, reverse=True)
    i = 0
    for item in sorted_hashtag:
        top_ten = item.ljust(50) + "\t" + str(hashtag_dict[item])
        print top_ten
        report_file.write(top_ten.encode('utf8')+'\n')
        i += 1
        if i > 9:
            break

    report_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        help="Start Date in 'YYYY-MM-DD' format. Example: --start 2012-04-23"
    )

    main(parser.parse_args())



