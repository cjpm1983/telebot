from flask import Flask, request
import telepot
import urllib3
import time
import atexit
#from flask_crontab import Crontab 

#estoes para el cron
#from apscheduler.schedulers.background import BackgroundScheduler



proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "777"
bot = telepot.Bot('1054318788:AAGh2wD25PEmbo9-9My2QnZHb_cQ1c_9gB4')
bot.setWebhook("https://cjpm1983.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

# para elschedule
#crontab = Crontab(app)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            if text == "Carlos":
                bot.sendMessage(chat_id, "Ese es el mostro, jj y sergio le va a tirar un cabo en este super bot")
            else:
                bot.sendMessage(chat_id, "dijiste '{}'".format(text))
        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"

@app.route('/check')
def check():
    return "Corriendo sin problemas"



#para elcron
#def tarea():
#    #print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#    bot.sendMessage("checkeando intervalo 5 segundos")



#@crontab.job(minute="1", hour="0")
#def my_scheduled_job():
#    tarea()



#scheduler = BackgroundScheduler()
#scheduler.add_job(func=print_date_time, trigger="interval", seconds=5)
#scheduler.start()

# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())
