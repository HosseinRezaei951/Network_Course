# Network Course

Welcome to the Network Course repository. This repository contains coursework, projects, and special exercises related to networking technologies and protocols.

## Directory Structure

### Exercises

The `Exercises` directory includes practical implementations and exercises focused on various networking concepts:

#### Multithreaded_WebServer

- `Multithreaded_WebServer.py`: Python implementation of a multithreaded web server. This server handles multiple client connections concurrently, demonstrating basic principles of multithreading and network communication.
- `README.md`: Documentation explaining the functionality and usage of the multithreaded web server.

#### SMTP_Client_Mail_Sender

- **HTML SMTP**
  - **static**: Contains static files for the SMTP client interface.
    - `jquery.js`: JavaScript library for DOM manipulation and event handling.
    - `script.js`: Custom JavaScript for additional client-side functionality.
    - `script2.js`: Additional JavaScript for extended features.
    - `style.css`: CSS file for styling the client interface.
  - **templates**: HTML templates used for the SMTP client application.
    - `index.html`: Main HTML template.
    - `index2.html`: Alternative HTML template.
    - `index3.html`: Additional HTML template.
  - `app.py`: Python application for sending emails via SMTP, including HTML templates and static files.
  
- **SMTP**
  - `SMTP.py`: Python script for implementing an SMTP client, demonstrating basic email sending functionality.

- `README.md`: Documentation for the SMTP client mail sender, including setup and usage instructions.

#### WebRTC_VideoChat

- `client.html`: HTML file for the client-side of the WebRTC video chat application. It includes JavaScript for managing WebRTC connections and user interactions.
- `package-lock.json`: File that locks the versions of installed npm packages.
- `READMe.md`: Documentation for the WebRTC video chat application, including setup and usage instructions.
- `signaling-server.js`: JavaScript file for the signaling server used to establish WebRTC connections between clients.

#### WebSocket_Uploader

- **MP3-TCP**
  - **receiver folder**
    - `server.py`: Python script for handling MP3 file uploads over TCP.
  - `client.py`: Python script for uploading MP3 files to the server using TCP.
  
- **MP3-UDP**
  - **receiver folder**
    - `server.py`: Python script for handling MP3 file uploads over UDP.
  - `client.py`: Python script for uploading MP3 files to the server using UDP.

- **TCP**
  - `client.py`: Python script for TCP client communication.
  - `server.py`: Python script for TCP server communication.

- **UDP**
  - `client.py`: Python script for UDP client communication.
  - `server.py`: Python script for UDP server communication.

- `README.md`: Documentation for the WebSocket uploader exercise, including details on TCP and UDP implementations.

### Projects

The `Projects` directory contains more extensive implementations and applications:

#### GoBackN_Simulation

- `GoBackN_Simulation.cpp`: C++ implementation of the Go-Back-N ARQ protocol simulation. This project demonstrates how the Go-Back-N protocol manages reliable data transmission over a network.
- `README.md`: Documentation explaining the Go-Back-N protocol and how to run the simulation.

#### WebChat

- **assets**: Contains static assets for the WebChat application.
  - `main.js`: JavaScript file for client-side functionality.
  - `reset.css`: CSS file for resetting browser styles.
  - `style.css`: CSS file for styling the WebChat interface.

- **Server**
  - `index.js`: JavaScript file for the server-side of the WebChat application, handling client connections and messaging.

- `.gitignore`: Git ignore file specifying which files and directories should be excluded from version control.
- `address.PNG`: Screenshot or diagram related to the WebChat project.
- `chat.PNG`: Screenshot or diagram of the WebChat application.
- `cmd.PNG`: Screenshot or diagram of the command-line interface.
- `index.html`: Main HTML file for the WebChat interface.
- `package.json`: npm package configuration file for managing dependencies.
- `README.md`: Documentation for the WebChat project, including setup and usage instructions.
