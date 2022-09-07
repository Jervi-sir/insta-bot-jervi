"""
    Stroy   postStory(user:obj)
"""
import random

## pic latest followers
def getLatestFollowers(user, howMany):
    return user.user_followers(user.account_info().pk, amount=howMany)
## get my Total followers (not used)
def getTotalFollowers(user):
    return user.user_info_by_username(user.account_info().username).follower_count
## primary
def getRandomNewFollowers(user):
    chosen = random.choice(list(getLatestFollowers(user, 5).values()))
    saveChosenFollower(chosen.username)
    return chosen.username

#----- File ---------------------------#
#will open file of latest followers
def getSavedFollowersList():
    f = open("latestFollowers.txt", "r")
    content = f.read()
    f.close()
    return content
#will save new content in file latest followers
def saveFollowersList(username, content):
    f = open("latestFollowers.txt", "w")
    content = username + " " + content
    f.write(content)
#will save new content in file latest followers
def saveChosenFollower(username):
    content = getSavedFollowersList()
    if not(username in content):
        saveFollowersList(username, content)


#----- Image ---------------------------#
from PIL import Image
from PIL import ImageFont, ImageDraw

### Create image for story
def createStoryImage(username):
    img = Image.new('RGB',(720,1280),color="orange")
    I1 = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 50)
    I1.text((20, 600), "@" + username, fill=(255, 0, 0), font=font, align="center")
    img.save("story.jpg")

### share a story
from instagrapi.types import StoryMention, StoryMedia
def postStory(user):
    username = getRandomNewFollowers(user)
    createStoryImage(username)
    user.photo_upload_to_story(
        'story.jpg',
        "@" + username,
        mentions=[StoryMention(user=user.user_info_by_username(username), x=0.4, y=0.5, width=1, height=0.2)],
    )
