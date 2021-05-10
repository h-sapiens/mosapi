import json


class Config:

    __CONFIG_FILE = "config.json"

    def get_devices(self) -> dict:
        config_file = self.__load_config_file()

        devices = {}

        for device in config_file["devices"]:
            devices[device["name"]] = device["address"]

        return devices

    def get_local_ip_address(self) -> str:
        return str(self.__load_config_file()["localIPAdress"])

    def get_urls(self) -> tuple:
        config_file = self.__load_config_file()

        urls = (
            '/', "Index",
            config_file["urls"]["exit"], "Exit",
            config_file["urls"]["linuxPing"], "Linux_ping",
            config_file["urls"]["linuxReboot"], "Linux_reboot",
            config_file["urls"]["linuxShutdown"], "Linux_shutdown",
            '/(.*)', 'Default'
        )

        return urls

    def __load_config_file(self) -> json:
        with open(Config.__CONFIG_FILE) as conf:
            config_file = json.loads(conf.read().replace('\n', ''))
            conf.close()
        return config_file
