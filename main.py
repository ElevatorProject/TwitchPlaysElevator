    #Define the imports
import twitch
import sql_db

t = twitch.Twitch();
db = sql_db.Sql_db();
 
#Enter your twitch username and oauth-key below, and the app connects to twitch with the details.
#Your oauth-key can be generated at http://twitchapps.com/tmi/
username = "dylan44117";
key = "oauth:hj3w82bti7s80yjsggqjeknlypykq5";
t.twitch_connect(username, key);
 
#The main loop
while True:
    #Check for new mesasages
    new_messages = t.twitch_recieve_messages();
 
    if not new_messages:
        #No new messages...
        continue
    else:
        for message in new_messages:
            #Wuhu we got a message. Let's extract some details from it
            msg = message['message'].lower()
            username = message['username'].lower()
            print(username + ": " + msg);
 
            #This is where you change the keys that shall be pressed and listened to.
            #The code below will simulate the key q if "q" is typed into twitch by someone
            #.. the same thing with "w"
            #Change this to make Twitch fit to your game!
            if msg == "q":
                print("q was pressed")
            if msg == "w":
                print("w was pressed")
            if msg == "1":
                print("1 was pressed")
                db.write_to_db('1')
            if msg == "2":
                print("2 was pressed")
                db.write_to_db('2')
            if msg == "3":
                print("3 was pressed")
                db.write_to_db('3')
