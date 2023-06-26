import time

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from telebot import types

from bot.main import bot


class BotView(APIView):
    def get(self, request, *args, **kwargs):  # noqa
        try:
            bot.remove_webhook()
            time.sleep(0.1)
            webhook_url = request.build_absolute_uri("?")
            if not webhook_url.startswith("https"):
                webhook_url = webhook_url.replace("http", "https")
            bot.set_webhook(url=webhook_url)
        except Exception as e:
            print(str(e))
        return render(request, "bot.html")

    def post(self, request, *args, **kwargs):  # noqa
        if request.META.get("CONTENT_TYPE") == "application/json":
            json_string = request.body.decode("utf-8")
            update = types.Update.de_json(json_string)
            try:
                bot.process_new_updates([update])
            except Exception as e:
                print(str(e))
            return Response(status=200)
        else:
            return Response(status=400)
