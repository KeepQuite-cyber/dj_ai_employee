from orders.models import Order , RefundRequest
from datetime import timezone


def get_order_details(order_id):
    try:
        order = Order.objects.get(id=order_id)
        return {
            "order_id" : order.id,
            "product_name" : order.product_name,
            "amount" : order.amount,
            "status" : order.status,
            "carrier" : order.carrier,
            "tracking_number" : order.tracking_number,
            "delivery_address" : order.delivery,
            "ordered_on" : order.created_at.strftime("%d %b %Y"),
            "days_since_order" : (timezone.now() - order.created_at).days,
        }
    except Order.DoesNotExist:
        return {"error" : f"Order #{order_id} not found"}
    
def get_refund_history(user_id):
    refunds = RefundRequest.objects.filter(user_id=user_id).order_by("-created_at") # - -> it will give the result in dictionary
    history = []
    for refund in refunds:
        history.append({
            "order_id" : refund.order.id,
            "product" : refund.order.product_name,
            "reason" : refund.reason,
            "status" : refund.status,
            "request_on" : refund.created_at.strftime("%d %b %Y"),
        })
            
    return {
        "total_refund_requested" : len(history),
        "history" : history,
    }
        