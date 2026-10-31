from .observer import Observer

class AuditObserver(Observer):
    def __init__(self): self.entries=[]
    def record(self,order_id,status): self.entries.append((order_id,status))
    def update(self, event): order_id, status = event; self.record(order_id, status)
    
