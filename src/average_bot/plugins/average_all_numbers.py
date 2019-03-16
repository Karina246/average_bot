from rtmbot.core import Plugin, Job
from ..user import User
import random


class AvergaeAllNumbersJob(Job):
    """
    Only if there were any new numberx since the last time,
    the job outputs the average of all numbers people wrote to one
    of the public channels.
    """
    def run(self, slack_client):
        if not User.this_average_written:
            all_public_channels = slack_client.api_call("conversations.list")['channels']
            channels_with_bot = filter(lambda channel: channel['is_member'] == True, all_public_channels)
            random_channel = random.choice(channels_with_bot)['id']
            User.this_average_written = True
            return [[random_channel, "Average all " + User.get_average_users()]]


class AvergaeAllNumbersPlugin(Plugin):
    """
    This plugin scheduale the AvergaeAllNumbersJob to run every 60 seconds.

    """

    def register_jobs(self):
        job = AvergaeAllNumbersJob(60)
        self.jobs.append(job)