# YouTube API: landslide videos


Get the top 10 most viewed YouTube videos \*that were posted\* in the past 24 hours containing the word "landslide" by using python.

### Install
You will need to check and install: Python, pip, virtualenv, 
#Check if python is installed
```
python --version
```
#Check if pip is installed
```
pip --version
```
#Install virtualenv
```
pip install virtualenv
```
#Check if virtualenv is installed correctly
```
virtualenv --version
```
#Install additional libraries
```
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
```
### How to run the code
#create virtual environment for Python 2.7
```
virtualenv -p /usr/bin/python2.7 venv2.7
```
#activate newly created virtual environment
```
source venv2.7/bin/activate
```
Then run it by using command:
```
python topTen.py
```
### Result
You will get output in 11 lines:
- first line is formatted as follows (without <> symbols): <startDate>\t<endDate>\n
- all other lines are formatted as follows (without <> symbols): <video_id>\t<title>\t<viewCount>\n