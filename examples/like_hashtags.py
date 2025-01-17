"""
    instabot example

    Workflow:
        Like last images with hashtag.
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
proxy=args.proxy)

tags = [#競艇予想]
wait = 25 * 60 # in seconds => 25 minutes
retry = 5 * 60 * 60 # in hours => 5 hours

while True:
try:
for hashtag in tags:
bot.like_hashtag(hashtag)
sleep(wait)
except:
sleep(retry)
    
    def like_medias(self, medias, check_media=True):
broken_items = []
if not medias:
self.logger.info("Nothing to like.")
return broken_items
self.logger.info("Start Logging")
self.logger.info("Going to like %d medias." % (len(medias)))
start_count = self.total['likes'] 
for media in tqdm(medias):
if not self.like(media, check_media):
self.error_delay()
broken_items.append(media)
self.logger.info("Total Like:" + str(self.total['likes']))
if self.total['likes'] != start_count and self.total['likes'] % 36 == 0: 
break
self.logger.info("DONE: Total liked %d medias." % self.total['likes'])
return broken_items
