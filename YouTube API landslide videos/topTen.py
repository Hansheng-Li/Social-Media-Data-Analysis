#!/usr/bin/python

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from datetime import datetime, timedelta

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCqrucKRuLJNUjfpXSpAq90A1nywtBufiE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

start_date = datetime.now() - timedelta(hours=21)
start_date = start_date.isoformat("T") + "Z"
end_date = datetime.now()
end_date = end_date.isoformat("T") + "Z"

print start_date, "\t", end_date


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        # order=viewCount,
        maxResults=options.max_results,
        publishedAfter=options.since,
        # order=options.viewCount
    ).execute()

    videos = []
    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.

    for search_result in search_response.get("items", []):

        video_id = search_result["id"]["videoId"]

        view_temp = []
        view_count = youtube.videos().list(
            id=video_id,
            part="statistics",
            # order=viewCount,
        ).execute()

        for view_count_result in view_count.get("items", []):
            view_temp = view_count_result["statistics"]["viewCount"]

        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s\t%s\t%s" %
                          (search_result["id"]["videoId"],
                           search_result["snippet"]["title"],
                           view_temp
                           ))
        # print(videos[0][0])
        # videos = sorted(videos, key=lambda a_entry: a_entry[2])
        # videos[videos[:,2],argsort()]
        # sorted(videos, key=lambda video: video[2])
        # videos.sort()

    print "\n".join(videos)


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="landslide")
    argparser.add_argument("--max-results", help="Max results", default=10)
    argparser.add_argument("--since", help="Published after", default=start_date)
    argparser.add_argument("--order", help="order", default="viewCount")
    args = argparser.parse_args()

    # currentDT = datetime.datetime.now()
    # print(str(currentDT))
    try:
        youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

# Determine the top 10 most viewed YouTube videos *that were posted* in the
#  past 24 hours containing the word "landslide". For each video, print id,
#  title, and view count. Upload the following files as part of your submission:
#
# source code (Python or Java)
# README with instructions how to run the code
# report consisting of 11 lines, where:
# first line is formatted as follows (without <> symbols): <startDate>\t<endDate>\n
# all other lines are formatted as follows (without <> symbols):
# <video_id>\t<title>\t<viewCount>\n
