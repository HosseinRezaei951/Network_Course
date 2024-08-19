# webChat-collection

![alt text](https://github.com/HosseinRezaei951/Network_Course/Projects/WebChat_Collection/chat.PNG)

 

Chat with web-socket ('ws') module on nodejs server,

it just for showing how web-sockets work

  

## How to start project

for running application you should install nodemon and then run

```

nodemon Server/index.js

```

  

request to localhost:8080, e.g., simply open browser and go to http://localhost:8080

( Do not open html files directly)

![alt text](https://github.com/HosseinRezaei951/Network_Course/Projects/WebChat_Collection/address.PNG)

  
## Topology:
Our system in this project is  Point-to-multipoin, that we use star graph topology. In an other words, we have a server in the middle that working like access point and any other clients try to connect to it and using it to broadcast messages to every on.
 
### 1) At least 3 users can send messages in one group :
After starting server, we can use any browser in our system to open the web-chat page and if we have 3 (or more) browser we can use them to chat in one group.

### 2) If the user came to the group after the rest of the users, they can receive previous messages :
First, we should make a variable in "Server/index.js" file to list(save) all history of other users.
```
// create list to hold history of messages
var  History_Of_Chat  = [];
```

Second, adding all messages of clients into chat history list in "on message event" part in "Server/index.js", by pushing them into the variable that we made it before .
```
//adding all message of clients into chat history list
History_Of_Chat.push(data);
```

Finally, we should load all messages in our list for new user before "on message event" part in "Server/index.js".
```
// loading all messages of history list for new user after login
History_Of_Chat.forEach(function(data) { ws.send(data); });
```
### 3) Create the perfect method for choosing a unique ID for each user:
First, we should make a variable in "Server/index.js" file as a counter for userIDs.
```
// creating variable for userID that starts from 100
var  Counter_UsreID = 100;
```

Second, using post(or get) method for sending(as response) ID to clients requests that receive to server  in  "Server/index.js" file.
```
// assigning new ID for new user
app.post('/userID',function(req,res){
	res.send('' + Counter_UsreID);
	Counter_UsreID = Counter_UsreID + 1;
});
```

Finally, using  http java request  in client side file "assets/main.js".
```
// generating new id for every user
function  GenerateID(){
	var  xmlHttp  =  new  XMLHttpRequest();
	xmlHttp.open( "POST", 'http://localhost:8080/userID', false ); // false for synchronous request
	xmlHttp.send( null );
	return  xmlHttp.responseText;
}
```

### Extra Point 1) Modify the application to run on a network other than localhost and between two different computers :

First, we should make application listen to "0.0.0.0" IP address in "Server/index.js" file.
* `0.0.0.0` is a non-routable meta-address used to designate an invalid, unknown or non applicable target (a no particular address placeholder). 

```
app.listen(8080,'0.0.0.0');
```
Second, we should create hotspot network on our system and in CMD(on windows) with command `ipconfig` we can see our IP address in our hotspot network that we should set it in url in file "assets/main.js".
Like that :
```
var ws = new WebSocket('ws://192.168.137.1:5001');
```

![alt text](https://github.com/HosseinRezaei951/Network_Course/Projects/WebChat_Collection/cmd.PNG)

Finally, after connecting to hotspot network with any devices and open page "ourID:8080" like `192.168.40.185:8080` we can chat together in other devices.


