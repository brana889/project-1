import tweepy

from authorization_tokens import *
import random

message=""

# phrase_list = ["hello!",
# "heyy!",
# "chicken noodle soup",
# "chips!",
# ":)"]

# Option 2: A simple madlib

# string_template= "{} is great but {} is way better."
# word_list= ["catching sidewalk bugs", "eating soup", "making your bed", "frying chicken"]
# word1= random.choice(word_list)
# word2= random.choice(word_list)
# message=string_template.format(word1,word2)

#Option 3: a list of possible madlibs

# template_list= ["I love {}.", "{} is so mysterious.", "I forgot to water my {} today"]
# word_list1= ["peaches", "bugs", "kimchi stew"]
# word_list2= ["cats", "plants", "TV"]
# template = random.choice(template_list)
# word1 = random.choice(word_list1)
# word2= random.choice(word_list2)
# message = template.format(word1,word2)

#Option 4: using if statements

# string_template= "The {} is always {} in here!"
#
# word_list1= ["air", "smell"]
# word_list2_a= ["pink", "yellow"]
# word_list2_b= ["waffle-scented", "pungent"]
#
# word1 = random.choice(word_list1)
# if word1 == "air":
#     word2= random.choice(word_list2_a)
# if word1 == "smell":
#     word2 = random.choice(word_list2_b)
# message = string_template.format(word1,word2)

#Option 1 self

phrase_list = ["Get jiggy with it!",
"Did you do it? Did you get jiggy with it?",
"You didn't do it, did you?",
"Yay you did it!",
"You're doing a great job!",
"I love you!",
"You are so loved.",
"Don't forget to drink water today <3",
"poop",
"test, test, onetwothree"]
message = random.choice(phrase_list)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)

print("Done.")
