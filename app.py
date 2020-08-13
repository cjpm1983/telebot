from flask import Flask, request
import telepot
import urllib3
import time
import atexit
import asyncio
#from flask_crontab import Crontab
import requests

#estoes para el cron
#from apscheduler.schedulers.background import BackgroundScheduler



proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "777"
bot = telepot.Bot('1296963854:AAHI3t3T4h54_qgrjOsMoo-zeaT4q8pZOlg')
bot.setWebhook("https://cjpm1983.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

# para elschedule
#crontab = Crontab(app)

chat_id = ""


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        #content_type, chat_type, chat_id = telepot.glance(update)
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]

            if text == "/masivo" or text == "/masivo@Gigante_de_hierro_bot":
                bot.sendMessage(-1001422441689, "Desde el bot privado tu id es {}".format(update))
                #bot.sendMessage(chat_id, " tu mensaje {}".format(update["message"]))
                #bot.sendMessage("@Gigante_de_hierro", "Desde el bot al canal dime algo")
                #bot.forwardMessage(chat_id,from_chat_id=chat_id,message_id=msg['text'])

            elif text == "/start" or text == "/start@Gigante_de_hierro_bot":
                bot.sendMessage(chat_id, "presionaste inicio")

            elif text == "Denis":
                bot.sendMessage(chat_id, "ese es el mostro, el terror de los AP ladrones")
            elif text == "Angelina":
                bot.sendMessage(chat_id, "Angelina va a ser informatica, jjj")
            elif text == "/cron":
                #cron()
                bot.sendMessage(chat_id, "se sincronizo {}".format(cron()))

            else:
                bot.sendMessage(chat_id, "dijiste '{}' y no se que quiciste decir. Lo siento, culpa de Sergio ;)".format(text))
        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"

@app.route('/check')
def check():
    return "Corriendo sin problemas"

@app.route('/cron')
def cron():
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    #asyncio.run(main())
    #main()
    #bot.sendMessage("@Gigante_de_hierro", "antes del await")

    url = "https://www.google.com"
    sess = requests.session()
    html = sess.get(url)
    contenido = html.content

    payload = {'depPid': '55'}
    url = "http://www.tuenvio.cu/villaclara/Products"
    response = requests.get(url, params=payload)
    contenido = response.content


    #bot.sendMessage("@Gigante_de_hierro", "Cargando Google.com devuelve {}".format("fff"))
    return "Corriendo sin problemas{}".format(contenido)



async def main():
    bot.sendMessage("@Gigante_de_hierro", "antes del await")
    #await asyncio.sleep(3)
    #time.sleep(3)
    bot.sendMessage("@Gigante_de_hierro", "despues del await de 30 segundos")

#async def sub():
#    bot.sendMessage("Gigante_de_hierro", "antes de main")
#    await main()
#    bot.sendMessage("Gigante_de_hierro","despues de main")




#para elcron
def tarea():
    #print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    #self.sender.sendMessage('Beep beep, time to wake up!')
    bot.sendMessage(792294355, "prueba de cron")


#@crontab.job(minute="1", hour="0")
#def my_scheduled_job():
#    tarea()
    #bot.sendMessage(chat_id, "prueba de cron")
    #self.sender.sendMessage('Beep beep, time to wake up!')



#scheduler = BackgroundScheduler()
#scheduler.add_job(func=print_date_time, trigger="interval", seconds=5)
#scheduler.start()

# Shut down the scheduler when exiting the app
#atexit.register(lambda: scheduler.shutdown())
