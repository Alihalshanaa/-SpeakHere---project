from django import template
from SpeakHere_app.models import Notifications

register = template.Library()

@register.inclusion_tag('app/show-all-notifications.html', takes_context=True)
def show_notifications(context):
	request_user = context['request'].user
	notifications = Notifications.objects.filter(to_user=request_user).exclude(user_has_seen=True).order_by('-date_on')
	return {'notifications': notifications}