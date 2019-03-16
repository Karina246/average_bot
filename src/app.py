from rtmbot import RtmBot
import os

config = {
    "SLACK_TOKEN": os.environ["SLACK_API_TOKEN"],
    "ACTIVE_PLUGINS": ["average_bot.plugins.average_user_number.AvergaeUserNumberPlugin",
    "average_bot.plugins.average_all_numbers.AvergaeAllNumbersPlugin"]
}


def main():
    """
    Run the bot, (run this function only if you want to run the bot without the web wedpoints)
    """
    bot = RtmBot(config)
    bot.start()

if __name__ == '__main__':
    main()