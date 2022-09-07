# auto poster
trying to automate some theme pages with this, since m always consumed with coding, I tend to forget about meme posting, and since I use my PC a lot, it's a perfect situation to schedule a python script to automatically post in the page every 1 hour 

the `instagrapi` package is not an api but a simulated `Xiaomi Mi 5s` phone, so technically m just required to input a verification code, and I also save the credentials into a `pickle` file so I won't abuse instagram login requests

<details open>
  <summary >
    <span style="font-size:25px; font-weight:700">
    so made so far
    </span>
  </summary>
  <ol>
    <li>
      <a href="#packages-used">Packages used</a>
    </li>
    <li>
      <a href="#login-functions">Login fnctions</a>
      <ul>
        <li><a href="#login-to-instagram">login to Instagram</a></li>
        <li><a href="#save-login">save login credentials in a file</a></li>
        <li><a href="#reuse-login">reused saved credentials</a></li>
      </ul>
    </li>
    <li>
      <a href="#video-upload-functions">Video Upload functions</a>
      <ul>
        <li><a href="#pick-random-file">pick random file</a></li>
        <li><a href="#move-file-done">move file as done</a></li>
        <li><a href="#create-caption">create caption</a></li>
        <li><a href="#upload-video">upload video</a></li>
      </ul>
    </li>
    <li>
      <a href="#story-upload-functions">Story Upload functions</a>
      <ul>
        <li><a href="#pick-new-follower">pick randomly a new followers</a></li>
        <li><a href="#save-picked-follower">save picked follower in a file list</a></li>
        <li><a href="#create-story-image">create image with follower mentioned</a></li>
        <li><a href="#upload-story">upload story with a mention</a></li>
      </ul>
    </li>
  </ol>
</details>

# Packages used

* [instagrapi](https://github.com/adw0rd/instagrapi)
* [moviepy](https://zulko.github.io/moviepy/install.html)
* [anaconda](https://www.anaconda.com/products/distribution)
* [vscode Notebook](https://www.youtube.com/watch?v=h1sAzPojKMg&t=57s)


# Login functions
### Login to instagram
<small style="color:#FFA500; opacity:0.6">
Used for direct instagram login, returns a InstagramLogin Object
</small>

```
login(username, password)
```

### Save login
<small style="color:#FFA500; opacity:0.6">
Used for saving Object in a pickle file
</small>

```
save_object(obj, filename)
```

### Reuse login
<small style="color:#FFA500; opacity:0.6">
Open file and turn what contains into an object
</small>

```
getLogin(filePath)
```

# Video upload functions

### Pick random file
<small style="color:#FFA500; opacity:0.6">
returns file path of a random picked file form folderInput
</small>

```
pickRandomFile(folderInput)
```

### Move file done
<small style="color:#FFA500; opacity:0.6">
move file into a folderOutput
</small>

```
makeFileAsDone(filePath, folderOutput)
```

### Create caption
<small style="color:#FFA500; opacity:0.6">
generate caption with random amount of tags
</small>

```
getCaption(text, amountOfTags)
```

### Upload video
<small style="color:#FFA500; opacity:0.6">
upload video with caption
</small>

```
uploadVideo(user, caption="", amountOfTags=10, InputPath="zmemes", OutputPath="zdone")
```



# Story upload functions
### Pick new follower
<small style="color:#FFA500; opacity:0.6">
pick random new follower and save it into a folder automatically ,
with a return of follower username
</small>

```
getRandomNewFollowers(user)
```


### Save picked follower
<small style="color:#FFA500; opacity:0.6">
push username into file
</small>

```
saveChosenFollower(username)
```


### Create story image
<small style="color:#FFA500; opacity:0.6">
create image with username mention, image is orange background and red font
</small>

```
createStoryImage(username)
```


### Upload story
<small style="color:#FFA500; opacity:0.6">
pick random new follower, create image with mention, share the image as a story with mention
</small>

```
postStory(user)
```



