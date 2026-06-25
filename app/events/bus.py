from collections import defaultdict
from typing import Callable


class EventBus:

    def __init__(self):
        self._listeners = defaultdict(list)

    def subscribe(self, event_name: str, handler: Callable):

        self._listeners[event_name].append(handler)

    def publish(self, event_name: str, payload):

        handlers = self._listeners.get(event_name, [])

        for handler in handlers:
            handler(payload)


event_bus = EventBus()
