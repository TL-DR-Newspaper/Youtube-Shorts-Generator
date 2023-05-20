
from moviepy.editor import *
from gtts import gTTS

def generate_speech(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("speech.mp3")
    return 'speech.mp3'

article_headline = 'Morgan Stanley CEO James Gorman to Exit Within Year, Successor Race Heats Up with 3 Frontrunners.'
txt_clip = ( TextClip(article_headline, fontsize=20,color='white')
                .set_position('center')
                .set_duration(10) )

#Creating all the clips
intro = ImageClip('mediafiles/intro.png').set_duration(3).fx(vfx.fadein, 2, initial_color=1).fx(vfx.fadeout, 1 )
mask = ImageClip('mediafiles/mask.png').set_duration(10).fx(vfx.fadein, 1, initial_color=0).fx(vfx.fadeout, 1 )
content = ImageClip('mediafiles/content.png').set_duration(10).fx(vfx.fadein, 1, initial_color=0).fx(vfx.fadeout, 1 )
jingle = AudioFileClip('mediafiles/jingle.mp3').set_duration(3)
voiceover= AudioFileClip(generate_speech(article_headline))

#Adding audio to video
content.audio = CompositeAudioClip([voiceover])
intro.audio = CompositeAudioClip([jingle])

#creating the main section of video video
# Adding content + text + mask
video_content = CompositeVideoClip([content, txt_clip, mask]) # Overlay text on video

#Adding content after intro
result = concatenate_videoclips([intro, video_content])
result.write_videofile("leader.mp4",fps=25)