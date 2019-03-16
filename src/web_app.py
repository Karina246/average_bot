import os
from flask import Flask, redirect, url_for, render_template
from rtmbot import RtmBot
from threading import Thread
from average_bot.user import User

config = {
    "SLACK_TOKEN": os.environ["SLACK_API_TOKEN"],
    "ACTIVE_PLUGINS": ["average_bot.plugins.average_user_number.AvergaeUserNumberPlugin",
    "average_bot.plugins.average_all_numbers.AvergaeAllNumbersPlugin"]
}
 
app = Flask(__name__)
bot = RtmBot(config)
 
@app.route("/")
def index():
    return redirect(url_for('average'))

@app.route("/average/")
def average():
    """
    Get the average for all the users
    """
    return render_template('average_all.html',average=User.get_average_users())
 
@app.route("/average/<string:name>/")
def average_name(name):
    """
    Get the average for user
    """
    average = User.get_average_user_by_name(bot.slack_client, name)
    return render_template('average_user.html',average=average, name=name)
 
def main():
    """
    Run the bot and the web app.
    """
    bot_thread = Thread(target=bot.start)
    bot_thread.start()
    app_thread = Thread(target=app.run, kwargs={'host':'0.0.0.0', 'port':8081})
    app_thread.start()

if __name__ == "__main__":
    main()