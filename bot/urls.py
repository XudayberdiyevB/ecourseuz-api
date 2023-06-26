from django.urls import path

from bot.views import BotView

urlpatterns = [
    path("set-webhook/", BotView.as_view())
]
