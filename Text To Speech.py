#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

article.download()
article.parse()

nltk.download('punkt')
article.nlp()

#Get the article text
mytext = article.text

language = 'en' #English

#Now we need to pass the text and language to the engine to 
#convert the text to speech and store it in a variable.
#Mark slow as False to tell the plug-in that the converted
#audio should be at high speed.

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("read_article.mp3")

os.system("start read_article.mp3")