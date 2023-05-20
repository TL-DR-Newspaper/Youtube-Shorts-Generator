# Youtube-Shorts-Generator
Fetches news from the main site and generates shorts which are posted to YouTube

# Generator: 
Youtube shorts have a standard size of 1920px by 1080px and a 9:16 aspect ratio. 
They can be up to 60 seconds in length. 

# Dependancies:
For video generation we rely on moviepy which in turn relies on imagemagick. The latter cannot be easily installed through PIP. So we'll have to build this in some kind of workflow. 