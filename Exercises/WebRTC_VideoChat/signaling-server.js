/**************/
/*** CONFIG ***/
/**************/
var PORT = 8080;
var HOSTNAME = "0.0.0.0";

/*************/
/*** SETUP ***/
/*************/
var express = require('express');
var main = express()
var http = require('http');
var server = http.createServer(main)
server.listen(PORT, HOSTNAME, function() {
    console.log("Listening on port " + PORT);
});

var io  = require('socket.io').listen(server);


main.get('/', function(req, res){ res.sendFile(__dirname + '/client.html'); });


/*************************/
/*** INTERESTING STUFF ***/
/*************************/
var channels = {};
var sockets = {};

/**
 * Users will connect to the signaling server, after which they'll issue a "join"
 * to join a particular channel. The signaling server keeps track of all sockets
 * who are in a channel, and on join will send out 'addPeer' events to each pair
 * of users in a channel. When clients receive the 'addPeer' even they'll begin
 * setting up an RTCPeerConnection with one another. During this process they'll
 * need to relay ICE(interactive connectivity establishment) Candidate information
 * to one another, as well as SessionDescription information. After all of that
 * happens, they'll finally be able to complete the peer connection and will be 
 * streaming audio/video between eachother.
 */

// Changing in connection
io.sockets.on('connection', function (socket) {
    socket.channels = {};
    sockets[socket.id] = socket;
    console.log("["+ socket.id + "] connection accepted");

    // Node disconnected from server
    socket.on('disconnect', function () {
        for (var channel in socket.channels) {
            part(channel);
        }
        console.log("["+ socket.id + "] disconnected");
        delete sockets[socket.id];
    });

    // New Node Join to channel
    socket.on('join', function (config) {
        console.log("["+ socket.id + "] join ", config);
        var channel = config.channel;
        var userdata = config.userdata;

        // Node already joined to channel
        if (channel in socket.channels) {
            console.log("["+ socket.id + "] ERROR: already joined ", channel);
            return;
        }

        // If there is no channel that user want to join it in channels list 
        if (!(channel in channels)) {
            channels[channel] = {};
        }

        // Add new peer in channel
        for (id in channels[channel]) {
            channels[channel][id].emit('addPeer', {'peer_id': socket.id, 'should_create_offer': false});
            socket.emit('addPeer', {'peer_id': id, 'should_create_offer': true});
        }

        channels[channel][socket.id] = socket;
        socket.channels[channel] = channel;
    });

    // Part from channel
    function part(channel) {
        console.log("["+ socket.id + "] part ");

        // If node not in the channel that wants to part from it
        if (!(channel in socket.channels)) {
            console.log("["+ socket.id + "] ERROR: not in ", channel);
            return;
        }

        delete socket.channels[channel];
        delete channels[channel][socket.id];

        // Remove peer from channel
        for (id in channels[channel]) {
            channels[channel][id].emit('removePeer', {'peer_id': socket.id});
            socket.emit('removePeer', {'peer_id': id});
        }
    }
    socket.on('part', part);

    // Relaying ICE Candidate to peer
    socket.on('relayICECandidate', function(config) {
        var peer_id = config.peer_id;
        var ice_candidate = config.ice_candidate;
        console.log("["+ socket.id + "] relaying ICE candidate to [" + peer_id + "] ", ice_candidate);

        // Setting ICE Candidate for peer
        if (peer_id in sockets) {
            sockets[peer_id].emit('iceCandidate', {'peer_id': socket.id, 'ice_candidate': ice_candidate});
        }
    });

    // Relaying Session Description to peer
    socket.on('relaySessionDescription', function(config) {
        var peer_id = config.peer_id;
        var session_description = config.session_description;
        console.log("["+ socket.id + "] relaying session description to [" + peer_id + "] ", session_description);

        // Setting Session Description to peer
        if (peer_id in sockets) {
            sockets[peer_id].emit('sessionDescription', {'peer_id': socket.id, 'session_description': session_description});
        }
    });
});
