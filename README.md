# Restaurant-Chat-Bot-Tkinter
# CHATBOT APPLICATION
I have used NLP along with Pythorch to train our chatbot  
JSON file will be used to train our model for chatbot.(Contextual Chatbots with Tensorflow)  
i have used various pattern tags  
The conversation need not be the same words that need to be put as the same  
  
# CONCEPTS  
1.Bag of words-patterns that box sees,ie split our strings- each different pattern is represented using an array containing numbers and using ‘1’ filled to the array like [1,0,0,0,1,0] which is our x vector.All patterns are coded.Each pattern has values like greeting takes value 0 and goodbye takes the value 1 etc..(y vector).
A deep learning feed forward neural net is trained and a softmax function will be used get the probability that a network belongs to a particular class
   
  
# Basics  
1.Tokenization  
Return an array of all the separate words.Because of the spaces the words are separated

2.Stemming   
Chopp off the endings(we might lose the meaning of the word might be lost)
Running,runs-stem:run
   
   
# PIPELINE FOR PREPROCESSING  
  
Sentence  
“Is anyone there?”   
     |   
     |      TOKENIZE  
     \/   
[“Is”,”anyone”,”there”,”?”]   
     |   
     |     STEMMING   
       \/      
[“is”,”anuon”,”there”,”?”]   
     |   
     |     EXCLUDE PUNCTUATION   
       \/   
[“is”,”anyon”,”there”]   
     |   
     |     BAG OF WORDS   
       \/   
X[0,0,1,1,0,1]   
   
For this process we use a NLTK library toolkit   
For training we make use of Pycharm Deep Learning library   

   


