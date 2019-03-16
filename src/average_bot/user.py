from meta_registry import MetaRegistryUsers

class User(object):
    """
    This class implements all the methods for user. 
    User is a slack member that talk to the bot (in private or public channel)
    The class also stores the instances of the user (see MetaRegistryUsers),
    I assume that saving the average and the count for all the numbers is secure enough
    (if not I can save them to db or read the history and parse it many times)
    """
    
    __metaclass__ = MetaRegistryUsers
    this_average_written = False

    def __init__(self, member_id):
        super(User, self).__init__()
        self.member_id = member_id
        self.average = 0.0
        self.count = 0

    def get_average_str(self):
        """
        Get the average number of the user.
        """
        return str(round(self.average,2))

    def add_new_number(self, number):
        """
        Calculate the average number when a new number is added.
        (I assume that number is int but the average can be float)
        """
        self.average = (self.average * self.count + int(number))/(self.count + 1)
        self.count += 1
        User.this_average_written = False

    @classmethod
    def get_average_users(cls):
        """
        Get the average number of all the users, 
        if no user writes any numbers, the function return 0

        """
        if len(cls.users) != 0:
            sum_averages = 0
            for user in cls.users.itervalues():
                sum_averages += user.average
            return str(round(sum_averages/len(cls.users),2))
        return '0'

    @staticmethod
    def _get_member_id_by_username(slack_client, username):
        """
        Get member id by username, 
        if member id dosen't exist return 0
        """
        users = slack_client.api_call("users.list")['members']
        current_user = filter(lambda user: user['real_name'] == username, users)
        if current_user:
            return current_user[0]['id']
        return 0

    @classmethod
    def get_average_user_by_name(cls, slack_client, username):
        """
        Get the average number of user by name.
        """
        member_id = cls._get_member_id_by_username(slack_client, username)
        if member_id:
            if member_id in cls.users:
                return str(cls.users[member_id].average)
            return "No average number for this user!"
        return "No such user!"
