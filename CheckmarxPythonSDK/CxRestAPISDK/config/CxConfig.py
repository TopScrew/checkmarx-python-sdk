# encoding: utf-8
"""
Configuration of Checkmarx
"""

import configparser
import pathlib

config_folder = pathlib.Path(__file__).parent.absolute()
# config_file_path = config_folder / "config.ini"
config_file_path = pathlib.Path.home() / ".Checkmarx/config.ini"


class CxConfig(object):
    """
    get configuration information from config.ini
    """
    config = None

    def __init__(self, config_file=config_file_path):
        """
        :param config_file: pathlib.Path
            the absolute path of the file config.ini
        """
        try:
            config_file = config_file.resolve()
        except FileNotFoundError:
            print("config.ini not found under config directory.")

        parser_obj = configparser.ConfigParser(interpolation=configparser.BasicInterpolation())
        parser_obj.read(config_file)
        self.cx_config = parser_obj["checkmarx"]
        CxConfig.config = self

    @property
    def base_url(self):
        """
        get the base url of Checkmarx REST API
        :return:
        str
            The base url of Checkmarx REST API, if not provided in config.ini, fallback to "http://localhost:80".
        """
        return self.cx_config.get("base_url", "http://localhost:80")

    @property
    def username(self):
        """
        get the username of Checkmarx security platform
        :return:
        str
            The user name of Checkmarx security platform, if not provided in config.ini, fallback to "Admin".
        """
        return self.cx_config.get("username", "Admin")

    @property
    def password(self):
        """
        get the password
        :return:
        str
            The password of username, if not provided in config.ini, fallback to "Password01!".
        """
        return self.cx_config.get("password", "Password01!")

    @property
    def grant_type(self):
        """
        get the grant type, used in the request header to get access token
        :return:
        str
            The grant type, if not provided in config.ini, fallback to "password".
        """
        return self.cx_config.get("grant_type", "password")

    @property
    def scope(self):
        """
        get the scope, used in the request header to get access token
        :return:
        str
            the scope, if not provided in config.ini, fallback to "sast_rest_api".
        """
        return self.cx_config.get("scope", "sast_rest_api")

    @property
    def client_id(self):
        """
        get the client id, used in the request header to get access token
        :return:
        str
            the client id, if not provided in config.ini, fallback to "resource_owner_client".
        """
        return self.cx_config.get("client_id", "resource_owner_client")

    @property
    def client_secret(self):
        """
        get the client secret, used in the request header to get access token
        :return:
        str
            the client secret, if not provided in config.ini, fallback to "014DF517-39D1-4453-B7B3-9930C563627C".
        """
        return self.cx_config.get("client_secret", "014DF517-39D1-4453-B7B3-9930C563627C")

    @property
    def url(self):
        """
        get the url of Cx REST API
        :return:
        str
            the url, if not provided in config.ini, fallback to the base url concatenated with "/cxrestapi".
        """
        return self.cx_config.get("url", self.base_url + "/cxrestapi")

    @property
    def scan_preset(self):
        """
        get the scan preset
        :return:
        str
            the scan preset, if not provided in config.ini, fallback to "Checkmarx Default".
        """
        return self.cx_config.get("scan_preset", "Checkmarx Default")

    @property
    def configuration(self):
        """
        get the project configuration
        :return:
        str
            the project configuration, if not provided in config.ini, fallback to "Default Configuration".
        """
        return self.cx_config.get("configuration", "Default Configuration")

    @property
    def team_full_name(self):
        """
        get the team that the user is a member of
        :return:
        str
            the team, if not provided in config.ini, fallback to /CxServer/SP/Company/Users
        """
        return self.cx_config.get("team_full_name", r"/CxServer/SP/Company/Users")

    @property
    def max_try(self):
        """
        number of max try for each HTTP request
        Returns:

        """
        return int(self.cx_config.get("max_try", 3))

    @property
    def verify(self):
        """
        ver
        Returns:

        """
        return self.cx_config.get("verify", False)


# construct an CxConfig object when import this module, so that the file config.ini will only be read once.
# please use CxConfig.config class variable to get configuration data.
CxConfig()
