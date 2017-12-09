#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
sys.path.append(os.path.join(sys.path[0], 'src'))
from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="stoicphysique",
    password="",
    like_per_day=750,
    comments_per_day=50,
    tag_list=["philosophy", "lifemotivation", "stoic", "motivational", "stoicism",
    "lifestyle", "healthylifestyle", "gymmotivation",
    "fitlife",  "socrate", "philosopher", "thinker"],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=250,
    follow_time=30 * 60,
    unfollow_per_day=200,
    unfollow_break_min=0,
    unfollow_break_max=1,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "that"],
                  ["photo", "shot", "post"],
                  ["is", "looks", "feels",],
                  ["great", "super", "wow",
                   "WOW", "cool", "GREAT", "magnificent",
                   "very cool", "stylish", "insane",
                   "so stylish", "insane", "glorious","so glorious"
                   ,"excellent", "amazing"],
                  [". Keep up the good workd! #stoicphysique", "!! Check out my new page. Thx! #stoicphysique", "! Looking forward for more! #stoicphysique"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[],
    unfollow_whitelist=[])

while True:
    mode = 0

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        print "Total following: %d Total followers: %d" % (bot.selfg_following, bot.self_follower)

        check_status(bot)

        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)

        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(10)
                follow_protocol(bot)
                time.sleep(10)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
