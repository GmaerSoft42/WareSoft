from flask import Flask, request, jsonify
from flask import render_template
import threading
import time
import random
global ended
ended = False

app = Flask(__name__)
def get_word(amount=1000):
    # request code to add in the future
    with open("WORDS.JSON","r") as word:
        words = word.read().strip("[").strip("]").split(",")
        final = []
        for x in range(amount):
            final.append(random.choice(words))
        return final
def timer():
    global ended
    #start timer after a prompt on the website says "And your time starts now!" after loading the words
    time.sleep(60)
    print("Time's Up!")
    ended = True
    return render_template('results.html', score=10, )
    
@app.route("/")
def mainpage():
    return render_template('lantype.html')
@app.route("/keystroke", methods=["POST"])
def get_character():
    return request.get_json("words")["key"][-1]
@app.route("/get-words")
def characters():
    global typed
    typed = []
    for i in range(100):
            word = get_word()[i].replace('"',"").replace(" ","")
            typed.append( word)   
    print(typed)
    return jsonify(message=" ".join(typed))  
def game():
    global correct_words
    global typed
    correct_words = 0
    nextword = 0
    character = ""
    global incorrect
    incorrect = {}
    threading.Thread(target=timer).start()
    while not ended:
            wordstr = ""
            while wordstr != typed[nextword]:
                character = get_character()
                if character in (" "):
                    if wordstr != typed[nextword-1] and wordstr != "":
                        incorrect[typed[nextword-1]] = wordstr
                    elif wordstr != "":
                        correct_words += 1                     
                    break
                else:
                    print(character, end='', flush=True)
                    wordstr += character
                    if wordstr == typed[nextword]:
                        correct_words += 1      
            nextword += 1              
                      


    


