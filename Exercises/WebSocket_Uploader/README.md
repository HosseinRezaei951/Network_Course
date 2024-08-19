# WebSocket Uploader Exercise

Welcome to the WebSocket Uploader exercise repository. This repository contains Python programs that illustrate different network communication methods using TCP and UDP protocols. The exercise includes examples of basic server-client communication, file transfer using TCP and UDP, and the effects of network errors using a network simulation tool.

## Purpose

The primary objectives of this exercise are:

- **Understand TCP and UDP Protocols**: Learn the fundamental differences between TCP and UDP protocols in terms of connection establishment, data transfer, and error handling.
- **Implement File Transfer**: Create Python programs to transfer MP3 files between a client and a server using both TCP and UDP protocols.
- **Simulate Network Errors**: Use a network simulation tool to observe the impact of network errors on file transfer and understand the robustness of TCP versus UDP.

## Directory Structure

### TCP and UDP Communication

The `TCP` and `UDP` directories contain simple client-server programs that demonstrate basic communication using TCP and UDP protocols.

- `TCP`:
  - `client.py`: Python script for the TCP client that sends messages to the server.
  - `server.py`: Python script for the TCP server that receives messages from the client and processes them.

- `UDP`:
  - `client.py`: Python script for the UDP client that sends messages to the server.
  - `server.py`: Python script for the UDP server that receives messages from the client and processes them.

### MP3 File Transfer

The `MP3-TCP` and `MP3-UDP` directories contain client-server programs specifically for transferring MP3 files using TCP and UDP protocols.

- `MP3-TCP`:
  - `receiver folder`:
    - `server.py`: Python script for the TCP server that receives an MP3 file from the client and saves it as `received.mp3`.
  - `client.py`: Python script for the TCP client that sends an MP3 file to the server.

- `MP3-UDP`:
  - `receiver folder`:
    - `server.py`: Python script for the UDP server that receives an MP3 file from the client, handling it in chunks, and saves it.
  - `client.py`: Python script for the UDP client that sends an MP3 file to the server in chunks.

## Understanding TCP and UDP

### TCP

- **Connection-Oriented**: TCP establishes a connection between client and server before data transfer begins, ensuring reliable and ordered delivery of data.
- **Data Transmission**: Uses the `socket.SOCK_STREAM` type to create a socket. The server binds to a host and port, listens for incoming connections, accepts them, and receives data using `recv()`.
- **Reliability**: Provides mechanisms for error checking and retransmission of lost or corrupted packets, ensuring data integrity.

### UDP

- **Connectionless**: UDP does not establish a connection before sending data, and it does not guarantee delivery or order of packets.
- **Data Transmission**: Uses the `socket.SOCK_DGRAM` type to create a socket. The server binds to a host and port, receives data using `recvfrom()`, and does not need to listen for connections.
- **Efficiency**: Lower overhead compared to TCP, but lacks reliability and error recovery features.

### Key Differences

- **Connection Establishment**: TCP requires connection setup and teardown, while UDP does not.
- **Data Integrity**: TCP ensures data integrity and order, whereas UDP does not guarantee delivery or order.
- **Error Handling**: TCP includes built-in error handling and retransmission, whereas UDP relies on the application to handle errors if needed.

## Implementation Details

### File Transfer Using TCP

- **Server**: The TCP server (`MP3-TCP/server.py`) waits for a connection, receives an MP3 file from the client, and saves it as `received.mp3`.
- **Client**: The TCP client (`MP3-TCP/client.py`) connects to the server, prompts the user for an MP3 file, and sends it to the server.

### File Transfer Using UDP

- **Server**: The UDP server (`MP3-UDP/server.py`) receives an MP3 file from the client in chunks of 4096 bytes and saves it.
- **Client**: The UDP client (`MP3-UDP/client.py`) sends an MP3 file to the server in chunks of 4096 bytes.

### Network Error Simulation

- **Tool**: Install and use the `clumsy` tool to simulate network errors such as packet loss and corruption.
- **TCP vs. UDP**: Observe the effects of network errors on file transfer. Typically, TCP will handle errors more gracefully, ensuring better file integrity compared to UDP.

## Summary

This exercise provides a practical understanding of network protocols, file transfer techniques, and error handling in network communications. By implementing and testing TCP and UDP communication and file transfer, you will gain insights into the strengths and weaknesses of each protocol and their applications in real-world scenarios.
