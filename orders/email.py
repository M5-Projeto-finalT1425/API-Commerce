from django.core.mail import send_mail


def send_email_order(order):
    subject = f"Pedido {order.id} atualizado"
    message = f"O status do seu pedido foi atualizado para {order.status}."
    recipient_list = [order.user.email]
    send_mail(subject, message, from_email=None, recipient_list=recipient_list)
