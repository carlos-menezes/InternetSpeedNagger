import tweepy
import speedtest
import threading

# TWITTER AUTH SETUP #

# Enter your details
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# SPEEDTEST SETUP #

speedtester = speedtest.Speedtest()
speedtester.get_best_server()

def getSpeed(down=100, up=100, time=1800):
    #down and up are the expected values for download and upload speed, respectively, in Megabytes.
    threading.Timer(time, getSpeed).start() # Runs the function every 30 minutes (unless you specify another one).

    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()

    # speedtester.download() and speedtester.upload() return a float which represents the internet speed in B/s.
    # I use this to create a very rough approximation to MB/s.

    # Say the download speed is 96540000.423932.
    # First, I make dSpeed a string so that I can split the value.
    # I split the float by the dot, which turns dSpeed into a list.

    #  dSpeed = ['96540000', '423932']

    # To finalize, I concatenate the first two digits of the first index with the first two digits of the second index.

    # dSpeed = dSpeed[0][0:2] + '.' + dSpeed[1][0:2]
    # print(dSpeed)
    # 93.79

    dSpeed = str(speedtester.download())
    dSpeed = dSpeed.split('.')
    dSpeed = dSpeed[0][0:2] + '.' + dSpeed[1][0:2]
    dSpeed = float(dSpeed) # Converting dSpeed from string to float so that I can compare the value later on.

    # Same process for the upload speed.

    uSpeed = str(speedtester.upload())
    uSpeed = uSpeed.split('.')
    uSpeed = uSpeed[0][0:2] + '.' + uSpeed[1][0:2]
    uSpeed = float(uSpeed)


    if dSpeed < down-10: # Compares the download speed from the speedtest with the expected download speed passed as a function argument minus 10. If we have a contract for 100MB/s download, the tweet will be sent if the download speed is below 90MB/s.

        #api.update_status sends a status update.
        api.update_status(f'@MEOpt porque é que a minha velocidade de download está a {dSpeed}MB/s quando tenho um contrato para {down}MB/s? #meo #meofibra') 

        print(f"Mensagem enviada: @MEOpt porque é que a minha velocidade de download está a {dSpeed}MB/s quando tenho um contrato para {down}MB/s? #meo #meofibra")

    elif uSpeed < up-10: # Compares the upload speed from the speedtest with the expected download speed passed as a function argument minus 10. If we have a contract for 100MB/s upload, the tweet will be sent if the upload speed is below 90MB/s.
        api.update_status(f'@MEOpt porque é que a minha velocidade de upload está a {uSpeed}MB/s quando tenho um contrato para {up}MB/s? #meo #meofibra')
        print(f"Mensagem enviada: @MEOpt porque é que a minha velocidade de upload está a {uSpeed}MB/s quando tenho um contrato para {up}MB/s? #meo #meofibra")

    elif dSpeed < down-10 and uSpeed < down-10:
        api.update_status(f'@MEOpt porque é que as minhas velocidades de download e upload estão a {dSpeed}MB/s e {uSpeed}MB/s, respetivamente, quando tenho um contrato para {down}/{up} MB/s? #meo #meofibra')
        print(f"Mensagem enviada: @MEOpt porque é que as minhas velocidades de download e upload estão a {dSpeed}MB/s e {uSpeed}MB/s, respetivamente, quando tenho um contrato para {down}/{up} MB/s? #meo #meofibra")
    else:
        pass
                
getSpeed()
