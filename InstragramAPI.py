import sys
import requests
import pandas as pd

BASE_URL = 'https://api.instagram.com/v1/'
ACCESS_TOKEN = 'XX - COLAR AQUI O TOKEN FORNECIDO PELA API DO INSTAGRAM'


def getOwnPost():
    request_url = 'https://api.instagram.com/v1/users/self/?access_token=%s' % ACCESS_TOKEN
    print('Request: %s' % request_url)

    request_post = requests.get(request_url).json()
    print(request_post)

def getMediaComments():
    #requests
    return False



def getRecentMedia(ACCESS_TOKEN=''):
    request_url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token=%s' % ACCESS_TOKEN
    request_post = requests.get(request_url).json()
    #print(request_url)

    photoID = []
    countLikes = []
    createTime = []
    images = []
    df = {'photoId': photoID, 'countLikes': countLikes, 'createdTime': createTime, 'images': images}

    if request_post['meta']['code'] == 200:

        if len(request_post['data']) > 0:
            for obj in request_post['data']:

                photoID.append(obj['id'])
                countLikes.append(obj['likes']['count'])
                createTime.append(obj['created_time'])
                images.append(obj['images']['standard_resolution']['url'])

                #print('Foto id: %s' % obj['id'])
                #print('Foto: %s' % obj['images']['standard_resolution']['url'])
                #print('Qtde de likes: %s' % obj['likes']['count'])
                #print('Data do post: %s' % obj['created_time'])

        else:
            print('No post to show')

        df = pd.DataFrame(df)
        #print(df.sort_values('countLikes', ascending=False).head(10))
        #print(df.describe())
        print(request_post)

    else:
        print('Error')

    return df


if __name__ == '__main__':

    # Versão para teste - gabrielmlg account
    df = getRecentMedia()

    # Versão de produção.
    #df = getRecentMedia(sys.argv[1])

    # Raking de fotos por likes:
    print(df.sort_values('countLikes', ascending=False)[['photoId']].head(10))
    count = 0

    for x in df['images']:
        count = count + 1
        ran = count
        print('%s - %s' % (str(ran), x))

    #df = df[['countLikes', 'photoId']].groupby(['photoId']).sum().sort_values(by='countLikes', ascending=False)

