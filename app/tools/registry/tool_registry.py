from app.tools.adapters.httpx import HttpxAdapter


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "httpx": HttpxAdapter(),
        }

    def get(self, name):

        return self.tools.get(name)
