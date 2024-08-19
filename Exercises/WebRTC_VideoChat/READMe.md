# WebRTC Video Chat Exercise

This repository demonstrates a WebRTC-based video chat application, implementing real-time peer-to-peer communication using common web technologies like HTML5, JavaScript, and CSS. The exercise includes both a signaling server and a client-side HTML page to establish direct video communication between users.

## Overview

### Part A: WebRTC Technology

WebRTC (Web Real-Time Communication) is designed to enable real-time peer-to-peer communication directly between web browsers. This technology supports streaming audio, video, and other data between browsers without the need for an intermediary server. 

- **Peer-to-Peer Communication**: WebRTC allows two hosts to exchange video, audio, and other data streams directly. This peer-to-peer model reduces the burden on servers, as data is exchanged directly between clients, unlike traditional client-server models which require servers to handle all data transmission.
- **STUN and TURN Servers**: To facilitate peer-to-peer connections, WebRTC relies on STUN (Session Traversal Utilities for NAT) servers to discover public IP addresses and TURN (Traversal Using Relays around NAT) servers when direct peer-to-peer connections are not possible. STUN servers help nodes determine their public IP addresses, while TURN servers relay data when direct connections fail.

### Part B: Client-Server vs. Peer-to-Peer Communication

#### Client-Server Model

- **Structure**: In the client-server model, one or more servers act as intermediaries for communication between clients. Clients send their data to the server, which then forwards it to the intended recipient.
- **Performance**: This model can become inefficient as the number of clients increases, since the server must handle all incoming and outgoing data, potentially leading to bottlenecks and increased latency.
- **Scalability**: While simpler to implement, client-server architectures require robust servers to handle increasing traffic, which can be costly in terms of processing power and bandwidth.

#### Peer-to-Peer Model

- **Structure**: In the peer-to-peer (P2P) model, each node in the network connects directly to others, allowing for direct data transmission between peers. This model is more scalable since it distributes the communication load across all nodes.
- **Performance**: P2P communication generally offers lower latency and faster data transfer between nodes, especially for streaming applications. However, managing multiple connections and data streams can increase computational and bandwidth requirements.
- **Topologies**: The mesh topology connects each node directly to every other node, which can be inefficient with a large number of nodes. Alternative topologies like star or hybrid models use central nodes or MCU (Multipoint Control Units) to manage data distribution more efficiently.

## Directory Structure

- **`signaling-server.js`**: The signaling server script that manages peer connections, including joining and leaving channels, relaying ICE candidates, and exchanging session descriptions.
- **`client.html`**: The client-side HTML page with embedded JavaScript for connecting to the signaling server, handling media streams, and managing peer-to-peer connections.

## How to Run

### Signaling Server

1. Ensure Node.js is installed on your system.
2. Save the `signaling-server.js` script.
3. Run the server: `node signaling-server.js`.
4. The server will listen on port 8080.

### Client

1. Open the `client.html` file in a web browser.
2. The client will connect to the signaling server and request access to the user's camera and microphone.
3. Join the default channel or specify a different channel in the script.

## Summary

This exercise showcases the use of WebRTC for real-time video communication between web browsers. By implementing both the signaling server and client-side components, it demonstrates the advantages of peer-to-peer communication over traditional client-server models, including reduced server load and improved performance for direct data transmission.

For more details on WebRTC, STUN/TURN servers, and the differences between client-server and peer-to-peer communication, refer to the included documentation.
