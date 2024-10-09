class URLs:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"

    @classmethod
    def get_home_url(cls):
        return cls.BASE_URL

    @classmethod
    def get_login_url(cls):
        return f"{cls.BASE_URL}/login"

    @classmethod
    def get_register_url(cls):
        return f"{cls.BASE_URL}/register"
