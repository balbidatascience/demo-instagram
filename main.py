import requests

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = '315156082.25f5d28.2633198fd77246e28e73855d7a020a9a'

def getOwnPost():
    request_url = 'https://api.instagram.com/v1/users/self/?access_token=%s' %ACCESS_TOKEN
    print('Request: %s' %request_url)

    request_post = requests.get(request_url).json()
    print(request_post)

def getRecentMedia():
    request_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=%s' %ACCESS_TOKEN

    request_post = requests.get(request_url).json()
    #print(request_post)

    if request_post['meta']['code'] == 200:

        if(len(request_post['data']) > 0):
             print(request_post['data'][0]['id'])
             print(request_post['data'][0]['user']['full_name'])
             print(request_post['data'][0]['user']['username'])
        else:
            print('No post to show')

        #print(request_post)
    else:
        print('Error ')



#getOwnPost()
getRecentMedia()
