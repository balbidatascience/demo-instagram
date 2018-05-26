# ID do Eduardo? 224127472

from instagram.client import InstagramAPI

access_token = "315156082.25f5d28.2633198fd77246e28e73855d7a020a9a"
client_secret = "1befb051b1c146b28be2f58588172033"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

api.user_follows(user_id='315156082')
