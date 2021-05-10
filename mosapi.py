#!/usr/bin/python3
import web

from controllers.linux import Linux
from clases.config import Config


class Default:
    def GET(self, path):
        return "Not Here!"


class Exit:
    def GET(self)
        exit()


class Index:
    def GET(self):
        return "What's up?!"


class Linux_ping:
    def GET(self, device):
        _, result = Linux().ping(device)
        print(result)
        return result


class Linux_reboot:
    def GET(self):
        _, result = Linux().reboot()
        print(result)
        return result


class Linux_shutdown:
    def GET(self):
        _, result = Linux().shutdown()
        print(result)
        return result


if __name__ == "__main__":
    app = web.application(Config().get_urls(), globals())
    app.run()
