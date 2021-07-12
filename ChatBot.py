from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses.
pairs = [
    [ r"(.*)my name is (.*)",
      ["Hello %2, How are you today ?",]
     ],
    [ r"(.*)help(.*)",
      ["I can help you ",]
     ],
    [ r"(.*) your name ?",
      ["My name is Ankit, but you can just call me robot and I'm a chatbot. ",]
     ],
    [ r"how are you (.*)",
       ["I'm doing very well", "i am great !"]
     ],
    [ r"sorry (.*)",
      ["Its alright","Its OK, never mind that",]
     ],
    [ r"i'm (.*) (good|well|okay|ok)",
      ["Nice to hear that", "Alright, great !",]
     ],
    [ r"(hi|hey|hello|hola|holla)(.*)",
      ["Hello", "Hey there",]
     ],
    [ r"what (.*) want ?",
      ["Make me an offer I can't refuse",]
     ],
    [ r"(.*)created(.*)",
      ["Ankit Dhakate created me using Python's NLTK library ","top secret ;)",]
     ],
    [ r"(.*) (location|city) ?",
      ["Maharashtra, India",]
     ],
    [ r"(.*)raining in (.*)",
      ["No rain in the paast 4 days here in %2","In %2 their is 50% chance of rain",]
     ],
    [ r"how (.*) health (.*)",
      ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
     ],
    [ r"(.*)(sports|game|sport)(.*)",
      ["I'm a very big fan of Cricket",]
     ],
    [ r"who (.*) (Cricketer|Batsman)?",
      ["MS Dhoni"]
     ],
    [ r"quit",
      ["Bye for now. See you soon :) ", "It was a nice talking to you. See you soon :)"]
     ],
    [ r"(.*)",
      ["That is nice to hear"]
     ],
]


#default message at the start of chat
print("Hi, I'm Ankit and I like to chat\nPlease type lowercase English language to start a conversation. Type quiz to leave")

#Create  Chat Bot
chat = Chat(pairs, reflections)

chat.converse()