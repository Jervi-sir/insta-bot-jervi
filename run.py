from pathlib import Path
from log import login, save_object, getLogin
from video import uploadVideo
#---------------------------------#
USER_EMAIL = ""
PASSWORD = ""
#---------------------------------#

#from story import postStory
print('#############################')
print('     Posting bot             ')
print('#############################')
#if there is no credential file
if Path('instagramCredentials.pkl').is_file() == False:
    cl = login(USER_EMAIL, PASSWORD)
    #save instagram login credentials
    save_object(cl, 'instagramCredentials.pkl')
user = getLogin('instagramCredentials.pkl')

print('user logged in')

print('start posting')
uploadVideo(user)
print('posting succeeded')

#postStory(user)
