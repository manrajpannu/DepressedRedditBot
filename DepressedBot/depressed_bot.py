import praw
import config
import time
import os

#search_terms = ['broken-hearted', 'bleeding', 'sorrowful', 'heartsore', 'downcast', 'hurting', 'heartsick', 'cast down', 'grim', 'crestfallen', 'in the toilet', 'daunted', 'moody', 'fed up', 'unhappy', 'morose', 'down and out', 'tearful', 'down in the mouth', 'dejected', 'weighed down', 'in the dumps', 'upset', 'discouraged', 'dismal', 'low-down', 'miserable', 'downhearted', 'low', 'disconsolate', 'despondent', 'lugubrious', 'low in spirits', 'sad', 'glum', 'desolate', 'saddened', 'down', 'in the pits', 'crummy', 'oppressed', 'disheartened', 'melancholy', 'gloomy', 'dolorous', 'let down', 'cast-down', 'down in the dumps', 'in pain', 'low-spirited', 'bummed out', 'in a blue funk', 'dragged', 'woebegone', 'ripped', 'heavy-hearted', 'chapfallen', 'dispirited', 'weeping', 'pessimistic']
subreddit = 'uoft'
search_terms = ['depressed']

def bot_login():
	print ('logging in...')
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Deaf comment bot v0.1")
	print ('logged in!')

	return r
	
def run_bot(r, comments_replied_to):
	print ('Obtaining submission...')
	for term in search_terms:
		print('searching for {} in /r/{}'.format(term,subreddit))
		for submission in r.subreddit(subreddit).search(term, limit=None):
			if submission.id not in comments_replied_to and submission.author != r.user.me():
				print(submission)
				#print ("string with \"depressed\" found!\n" +submission.title)
				with open ("comments_replied_to.txt", 'a') as f:
					f.write(submission.id + "\n")
					

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
			comments_replied_to = []
	else:
		with open('comments_replied_to.txt', 'r') as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to


r = bot_login()

while True:
	run_bot(r, get_saved_comments())
	