from .observer import Observer


class CustomerNotifier(Observer):
    def __init__(self): self.messages=[]
    def update(self, event):
        order_id, status = event
        self.notify_customer(order_id, status)

    def notify_customer(self, order_id, status):
        self.messages.append(f"{order_id}:{status}")