from .observer import Observer

class AnalyticsObserver(Observer):

    def __init__(self):
        self.events = []

    def update(self, event):
        self.events.append(event)
