from fastapi import FastAPI
import pyjokes
app = FastAPI()

@app.get("/")
def joke():
    return pyjokes.get_joke()

@app.get("/{friend}")
def friends_joke(friend: str):
    return friend + " tells his joke: " + pyjokes.get_joke()

@app.get("/multi/{friend}")
def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + " "
    return result
