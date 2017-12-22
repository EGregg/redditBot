import configMaker, praw, time

configMaker.configPresent()

import config

bot = praw.Reddit(user_agent='MySimpleBot',
                  client_id=config.client_id,
                  client_secret=config.client_secret)

subreddit = bot.subreddit('space')

comments = subreddit.stream.comments()

#this will make the script run for 5 seconds
start_time = time.time()
end_time = start_time + 5
time_running = time.time() - start_time

while time.time() - start_time < 1:
	for comment in comments:
		text = comment.body # Fetch body
		author = comment.author # Fetch author
		print (time.time() - start_time)
		if 'mars' in text.lower():
			# Generate a message
			message = "Why no love for Titan, u/{0} ?".format(author)

			print (message)
			print("--- %s seconds ---" % (time.time() - start_time))

			#comment.reply(message) # Send message

