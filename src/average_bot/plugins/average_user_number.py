from rtmbot.core import Plugin
from ..user import User
import re

class AvergaeUserNumberPlugin(Plugin):
    """
    Whenever a user writes a number and the bot sees it, this plugin sends
    back the average of the numbers the user wrote.
    """

    def process_message(self, data):
        current_user = User(data['user'])
        numbers_in_message = re.findall(r'\d+', data['text'])
        if numbers_in_message:
            for number in numbers_in_message:
                current_user.add_new_number(number)
            average_number = current_user.get_average_str()
            self.outputs.append([data['channel'], "the average of user {} is {}".format(data['user'], average_number)])
