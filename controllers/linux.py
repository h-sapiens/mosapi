import subprocess

from clases.config import Config


class Linux:

    def ping(self, ping_request: str) -> (int, str):
        address: str

        try:
            if "ip/" in ping_request:
                address = Config().get_local_ip_address() + \
                    str(int(ping_request[3:])) #we make sure it is a number

            else:
                address = Config().get_devices()[ping_request]

        except Exception:
            return self.__handle_error('Invalid argument: %s' % ping_request)

        _, result = self.__execute('ping -c 4 %s' % address)

        if "64 bytes from" in result:
            print(result)
            return 0, "Ping successful!"

        else:
            print(result)
            return 0, "Could not resolve ping"

    def reboot(self) -> (int, str):
        return self.__execute("sudo /sbin/reboot")

    def shutdown(self) -> (int, str):
        return self.__execute("sudo /sbin/shutdown")

    def __execute(self, command: str) -> (int, str):
        try:
            output = subprocess.check_output(command, shell=True)
            return 0, str(output)

        except Exception as error:
            return self.__handle_error(error)

    def __handle_error(self, error) -> (int, str):
        print(error)
        return -1, "Could not resolve request!"
