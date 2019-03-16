class MetaRegistryUsers(type):
    """
    Metaclass provides an instance registry. 
    This metaclass allows the class to save all its instances.
    Also if instance for member id is already created, we don't create a new instance.
    """

    def __init__(cls, name, bases, attrs):
        super(MetaRegistryUsers, cls).__init__(name, bases, attrs)
        cls.users = {}

    def __call__(cls, member_id):
        if member_id not in cls.users:
            cls.users[member_id] = super(MetaRegistryUsers, cls).__call__(member_id)
        return cls.users[member_id]
