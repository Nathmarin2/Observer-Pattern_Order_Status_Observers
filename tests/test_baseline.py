from order_status.customer_notifier import CustomerNotifier
from order_status.audit_observer import AuditObserver
from order_status.order_status import OrderStatus
from order_status.analytics_observer import AnalyticsObserver

def test_direct_calls():
    c=CustomerNotifier(); a=AuditObserver(); o=OrderStatus("A-100",c,a)
    o.set_status("SHIPPED")
    assert c.messages==["A-100:SHIPPED"]
    assert a.entries==[("A-100","SHIPPED")]

def test_analytics_observer_can_subscribe_and_unsubscribe():
    customer = CustomerNotifier()
    audit = AuditObserver()
    analytics = AnalyticsObserver()

    order = OrderStatus("ORD-123", customer, audit)

    order.attach(analytics)
    order.set_status("SHIPPED")

    assert analytics.events == [("ORD-123", "SHIPPED")]

    order.detach(analytics)
    order.set_status("DELIVERED")

    assert analytics.events == [("ORD-123", "SHIPPED")]

    assert customer.messages == [
        "ORD-123:SHIPPED",
        "ORD-123:DELIVERED"
    ]

    assert audit.entries == [
        ("ORD-123", "SHIPPED"),
        ("ORD-123", "DELIVERED")
    ]