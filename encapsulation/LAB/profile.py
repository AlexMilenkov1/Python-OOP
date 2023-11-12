class Profile:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if 5 <= len(value) <= 15:
            self.__name = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        if len(value) >= 8 and [x for x in value if x.isdigit()] and [x for x in value if x.isupper()]:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.name}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')