from gtts import gTTS

#data (txt and lang can be change any time as request fhemty)
#kulshi kitapporta mne google 

txt = "hello world this is a test 1 2 3"
langue = 'en'

#pass data a as settings

res = gTTS(text=txt,lang=langue)

res.save("audio.mp3")