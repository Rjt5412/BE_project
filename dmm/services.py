import tweepy
import requests_oauthlib
import requests
import pytumblr
import pandas as pd
from pytrends.request import TrendReq


def get_twitter_trends():
    consumerKey = "lPFvtvMMoAyDGpuvRVcvO8XrW"
    consumerSecret = "iQ5PMIJgVrRh22nAOMTaSTPJTzo4AkR4dVHdBBC4DXA766dE5W"
    accessToken = "786113501924294656-rpS1oKPiMbOGuR1Ha8ydqxhjsk7HthR"
    accessTokenSecret = "QIpYa9ulI2VkkJA6eXGKmz3EN6LtenCiDaM68hPxI8WJc"

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)
    reply = api.trends_place(23424848)

    response = reply[0]['trends']

    hashtag = []
    url = []

    for i in response:
        hashtag.append(i['name'])
        url.append(i['url'])

    trends = zip(hashtag[:5], url[:5])

    return trends


def get_tumblr_and_gplus_trends():


    pytrends = TrendReq(hl='en-US', tz=360)

    response = pytrends.trending_searches()

    df = pd.DataFrame(response)
    trends = df['title'].tolist()
    urls_tumblr = []
    urls_gplus = []

    for i in range(0,5):
        urls_tumblr.append('https://www.tumblr.com/search/'+trends[i])

    for i in range(6,11):
        urls_gplus.append('https://plus.google.com/s/'+trends[i]+'/posts')

    tumblr_trends = zip(trends[:6],urls_tumblr)
    gplus_trends = zip(trends[6:11],urls_gplus)

    return gplus_trends,tumblr_trends


'''
def get_twitter_data():
    auth = OAuth1('lPFvtvMMoAyDGpuvRVcvO8XrW', 'iQ5PMIJgVrRh22nAOMTaSTPJTzo4AkR4dVHdBBC4DXA766dE5W',
                  '786113501924294656-rpS1oKPiMbOGuR1Ha8ydqxhjsk7HthR',
                  'QIpYa9ulI2VkkJA6eXGKmz3EN6LtenCiDaM68hPxI8WJc')

    r = requests.get('https://api.twitter.com/1.1/search/tweets.json', params=dict(q='#sizzler', count=100), auth=auth)

    result = dict(r.json())

    a = result["statuses"]
    retweet = []
    username = []
    # reply = []   //not available on API
    date = []
    location = []
    for i in a:
     if i['user']['lang'] == 'en':
        retweet.append(i["retweet_count"])
        username.append(i["user"]["name"])
        location.append(i["user"]["location"])
        date.append(i["created_at"])
     else:
        pass

    returned ={}

    for i in range(0, len(username)):
        d = dict({'Username': username[i], 'Location': location[i], 'Date': date[i], 'Retweets': retweet[i]})
        returned.append(d)
    dr = {'data': returned}


def g_plus_data():

    url = 'https://www.googleapis.com/plus/v1/activities'
    params = dict(query = 'cricket', language= 'English', maxResults=100, key='AIzaSyDPIIGBYm-TA9yrhQl5bw0J1CxkmMmQwk4')
    r = requests.get(url, params = params)
    response = dict(r.json())
    a = response["items"]
    title = []
    url = []
    content = []

    for i in a:
        title.append(i['title'])
        url.append(i['url'])
        content.append(i['object']['content'])

def get_tumblr_data():
    
    # Authenticate via API Key
    client = pytumblr.TumblrRestClient('KceYzI17iR8jl5YjJuVUGi8n8XcmY2NbMUOJ69iDekszIGjxE3')

    # Make the request
    response = client.tagged('cricket')
    r = response[:300]

    user_id = []
    likes = []
    summary = []
    x = 0

    for i in r:
        user_id.append(i['blog_name'])
        summary.append(i['summary'])
        likes.append(i['note_count'])
        x = x + 1

    
'''
