from user import User
from database import Database
from userPersister import UserPersister
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

database = Database(host="localhost",dbname="training",user="postgres",password="Ddbhbnz@1")
userPersister = UserPersister(database)

user_email = input("Enter your e-mail address: ")

user = userPersister.load_from_db_using_email(user_email)

if not user:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    userPersister.save_to_db(user)


tweets = user.twitter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])