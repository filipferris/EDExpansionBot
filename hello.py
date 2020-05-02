from flask import Flask
# import testBot
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello Flask"

@myapp.route("/")
def run():
    # await testBot.run()
    return "Bot is running" 