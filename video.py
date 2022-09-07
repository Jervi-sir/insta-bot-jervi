"""
    Share Video
"""
import os, random, shutil

#get random video file
def pickRandomFile(folderInput):
    file = random.choice(os.listdir(folderInput)) 
    filePath = folderInput + '/' + file
    return filePath

#move file to Done
def makeFileAsDone(filePath, folderOutput):
    shutil.move(filePath, folderOutput)

#get Caption
def getCaption(text, amountOfTags):
    tags = open("tags.txt", "r")
    array = tags.read().split(" ")
    result = [] 
    for i in array: 
        if i not in result: 
            result.append(i) 
    randomTagsArray = random.choices(result, k=amountOfTags)
    randomTagsText = ", ".join(randomTagsArray)
    caption = text + " " + randomTagsText
    return caption

#------------------------------------#
#Upload video with caption
def uploadVideo(user, caption="", amountOfTags=10, InputPath="zmemes", OutputPath="zdone"):
    filePath = pickRandomFile(InputPath)
    user.video_upload(filePath, getCaption(caption, amountOfTags))
    makeFileAsDone(filePath, OutputPath)
