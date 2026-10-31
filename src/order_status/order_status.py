from .customer_notifier import CustomerNotifier
from .audit_observer import AuditObserver
from .observer import Observer

class OrderStatus:

    def __init__(self, order_id, customer_notifier: Observer, audit_observer: Observer):
        self.order_id = order_id
        self.status = "NEW"
        self.observers = []

        self.attach(customer_notifier)
        self.attach(audit_observer)

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

    def set_status(self, status):
        self.status = status
        event = (self.order_id, status)
        self.notify(event)

