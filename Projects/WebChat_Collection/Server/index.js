
var express = require('express');
var app = express();
var path = require('path');
app.use(express.static('assets'))


// viewed at http://localhost:8080
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/../index.html'));
});

// creating variable for userID that starts from 100 
var Counter_UsreID = 100;

// assigning new ID for new user 
app.post('/userID',function(req,res){
    res.send('' + Counter_UsreID);
    Counter_UsreID = Counter_UsreID + 1;
});

app.listen(8080);
// app.listen(8080,'0.0.0.0');

var server = require('ws').Server;
var wss = new server({ port: 5001 });


// create list to hold history of messages
var History_Of_Chat = [];

// creating server on port 5001 localhost 
wss.on('connection', function (ws) 
{

    // loading all messages of history list for new user after login
    History_Of_Chat.forEach(function(data) { ws.send(data); });
    
    //on message event 
    ws.on('message', (data) => {
        console.log(data);
        

        //adding all messages  of clients into chat history list
        History_Of_Chat.push(data);

        //broadcast data to all clients 
        wss.clients.forEach(function e(client) {
            client.send(data);
        })
    });

    ws.on('close', function () {
        console.log('Connection terminated..Closing Client');
    });
})
