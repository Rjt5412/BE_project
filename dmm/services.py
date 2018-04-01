import tweepy
from requests_oauthlib import OAuth1
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



def get_twitter_data(keyword):
    auth = OAuth1('lPFvtvMMoAyDGpuvRVcvO8XrW', 'iQ5PMIJgVrRh22nAOMTaSTPJTzo4AkR4dVHdBBC4DXA766dE5W',
                  '786113501924294656-rpS1oKPiMbOGuR1Ha8ydqxhjsk7HthR',
                  'QIpYa9ulI2VkkJA6eXGKmz3EN6LtenCiDaM68hPxI8WJc')
    r = requests.get('https://api.twitter.com/1.1/search/tweets.json', params=dict(q= keyword, count=100), auth=auth)

    result = dict(r.json())

    a = result["statuses"]
    site = []
    shares = []
    username = []
    # reply = []   //not available on API
    likes = []
    coeff = []
    main_category = []
    sub_category = []
    ml_out = []
    url = []

    for i in a:
     if i['user']['lang'] == 'en':
        shares.append(i["retweet_count"])
        username.append(i["user"]["name"])
        likes.append(i["favorite_count"])
        url.append("https://twitter.com/i/web/status/" + i['id_str'])
        coeff.append('')
        main_category.append('')
        sub_category.append('')
     else:
        pass


    d = dict({'Username': username, 'Shares': shares, 'Likes': likes,
                  'coefficient': coeff, 'Main_Category': main_category,
                  'Sub_Category': sub_category, 'url': url})

    return d


def g_plus_data(keyword):

    url = 'https://www.googleapis.com/plus/v1/activities'
    params = dict(query = keyword, language= 'English', key='AIzaSyDPIIGBYm-TA9yrhQl5bw0J1CxkmMmQwk4')
    r = requests.get(url, params = params)
    response = dict(r.json())
    a = response["items"]
    site = []
    shares = []
    username = []
    likes = []
    coeff = []
    main_category = []
    sub_category = []
    ml_out = []
    url = []

    for i in a:
        site.append('Google Plus')
        username.append(i['actor']['displayName'])
        likes.append(i['object']['plusoners']['totalItems'])
        shares.append(i['object']['resharers']['totalItems'])
        url.append(i['object']['url'])
        coeff.append('')
        main_category.append('')
        sub_category.append('')

    d = dict({'Site': site, 'Username': username, 'Shares': shares, 'Likes': likes,
              'coefficient': coeff, 'Main_Category': main_category,
              'Sub_Category': sub_category, 'url': url})

    return d

def get_tumblr_data(keyword):
    
    # Authenticate via API Key
    client = pytumblr.TumblrRestClient('KceYzI17iR8jl5YjJuVUGi8n8XcmY2NbMUOJ69iDekszIGjxE3')

    # Make the request
    response = client.tagged(keyword)
    r = response[:300]

    site = []
    shares = []
    username = []
    likes = []
    coeff = []
    main_category = []
    sub_category = []
    ml_out = []
    url = []

    x = 0

    for i in r:
        site.append('tumblr')
        username.append(i['blog_name'])
        coeff.append('')
        url.append('post_url')
        main_category.append('')
        sub_category.append('')
        likes.append(i['note_count'])

        x = x + 1

    d = dict({'Site': site, 'Username': username, 'Shares': shares, 'Likes': likes,
              'coefficient': coeff, 'Main_Category': main_category,
              'Sub_Category': sub_category, 'url': url})

    return d

