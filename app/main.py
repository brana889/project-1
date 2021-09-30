"""
  Amaya Branche
  Radical Software, Fall 2021
  Project 1
  Sept 29, 2021
  python3
"""


import tweepy

from authorization_tokens import *
import random


message=""


phrase_list = ["you are so deserving of the love and support you seek.",
"you can change your identity as many times as you want, and it will always be valid",
"daily mental health check-in carrd! :) <3 https://checkpoint.carrd.co/",
"black mental health resources carrd! :) <3 https://blackmentalhealthmatters.carrd.co/#resources",
"general bipoc mental health resources! :) <3 https://axidbipocmentalhealth.carrd.co/",
"bipoc mental health resources! https://bipocmh.carrd.co/",
"the safe place- mental health support carrd! <3 https://thesafeplace.carrd.co/",
"you are so beautiful!!",
"you are an ethereal being. you are capable of doing or being anything your heart yearns for.",
"daily affirmation: “I will no longer cut myself in half to make another feel whole.”- Trinity",
"daily affirmation: I give myself compassion when I make mistakes.",
"daily affirmation: I accept my body as it is right now.",
"daily affirmation: I do not beat myself up for healing slower than I would like."
"daily affirmation: I give myself as much time and space to rest and recharge as I can when I feel drained.",
"setting boundaries does not make you a bad person. It makes you a good companion to yourself.",
"as a queer person of color in this world, simply being who you are is a radical act...please do not be afraid to take breaks when your activist life becomes overwhelming.",
"don’t be afraid to reach out to your loved ones when you need them. you are not a burden, no matter what your mind tells you. :)",
"healing isn’t linear. there is no such thing as backtracking in your mental health journey. it's part of the learning process.",
"even if you haven’t reached your end goal, never minimize your progress. you are doing amazing! <3",
" “The Self Love Fix”, an amazinggg podcast for WOC embarking on their quest for self love and inner peace https://open.spotify.com/show/3WdMpEOWYl8Zx8uzzH8rAn?si=Vsi4uz9WQsiTeqoHotoO0w&dl_branch=1",
" “The Good News Podcast”, 2-10 minute podcasts sharing sweet, wholesome stories from around the world :) https://open.spotify.com/show/2SOpj1RYna4yua8aKZiuME?si=q8U_KH1NTE20hZgFimWr7Q&dl_branch=1",
"we are not here on this planet to impress others, to be judged by others. you do not exist for anyone else but yourself.",
"it is okay to have days where you don’t feel as confident, or days where it feels hard to find compassion for yourself. just feel it. it will pass <3",
"your body is for you, and you only. do not feel pressured to look a certain way to please others.",
"a lofi playlist for when you feel anxious, stressed or overwhelmed ＜3 https://youtu.be/u13BVkpEkDo",
"slowed + reverbed calming playlist ~ <3 https://youtu.be/8JNEdmSAbjY",
"affirmations to recite, meditate on, and brighten your energy :) ~ <3 https://youtu.be/QcPQoOPAPq4",
"chosen family is real family :)",
"rest IS productive. please take care of yourself today :)",
"take care of yourself to the best of ability today <3",
"you are more than your political identity. never forget that you are a human being with complex thoughts and feelings, and you deserve to be regarded as such before anything else.",
"your queerness is beautiful! you make the world a better place. <3",
"i hope today brings you nothing but joy and peace <3",
"you are not broken. there is nothing wrong with you. accept where you are right now, and know that things will get better in time. please be gentle with yourself <3"]

message = random.choice(phrase_list)


auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)

print("Done.")
