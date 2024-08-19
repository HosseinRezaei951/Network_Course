# Multithreaded Web Server Exercise

This repository contains a Python implementation of a multithreaded web server exercise. This exercise aims to demonstrate how to create a web server that can handle multiple client connections concurrently using threads. The server is built using Python's `socket` and `threading` modules and is capable of serving HTTP requests and files.

## Purpose

The primary objectives of this exercise are:

- **Learn Multithreading**: Understand how to use Python’s `threading` module to manage multiple simultaneous connections in a web server.
- **Build a Basic Web Server**: Implement a simple HTTP server that processes GET requests and serves files to clients.
- **Explore HTTP and Socket Programming**: Gain hands-on experience with HTTP request handling and socket programming in Python.

## Directory Structure

The repository includes the following files:

- `server.py`: The main script for the multithreaded web server. It sets up the server to listen for incoming TCP connections, creates a new thread for each client connection, and processes HTTP requests to serve files.

## How It Works

### Server Implementation

- **Socket Setup**: The server initializes a TCP socket using `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` and binds it to a specified host and port (default is port 80). It listens for incoming connections.
- **Multithreading**: To handle multiple clients concurrently, the server uses the `threading` module. Each incoming connection spawns a new thread that manages the client’s request and response cycle independently.
- **Request Handling**: Each thread processes the HTTP request received from the client, determines the requested file, and sends the appropriate response. The server supports serving HTML files, CSS files, and JPEG images.
- **File Serving**: The server reads the requested file from the disk and sends it back to the client with the correct MIME type. If the file is not found, it responds with a 404 Not Found error.

### Code Breakdown

- **Threaded Class**: This class inherits from `threading.Thread` and manages client connections in separate threads. The `run` method handles client requests, reads files, and sends responses.
  - **`run()` Method**: Processes incoming requests, manages file reading and sending, and prints debug information about requests and responses.
- **Main Function**: Sets up the server socket, binds it to the host and port, listens for incoming connections, and starts a new `threaded` instance for each client connection.

## How to Use

1. **Setup**:
   - Ensure Python is installed on your system.
   - Update the `HOST` and `PORT` variables in `server.py` as needed. Set `HOST` to your system’s IP address and `PORT` to 80 or another available port.

2. **Run the Server**:
   - Execute the server script: `python server.py`.
   - The server will start listening for connections and handle client requests.

3. **Test the Server**:
   - Open a web browser and navigate to `http://<your-ip-address>` to test the server.
   - Use tools like `telnet` or `curl` to send HTTP requests and observe the responses.

## Additional Notes

### TCP and HTTP Protocols

- **TCP**: This implementation uses TCP for reliable, connection-oriented communication. The server ensures data integrity and handles requests properly.
- **HTTP**: The server handles HTTP GET requests and serves files based on the requested URL. It supports basic MIME types for different file formats.

### Telnet and SSH

- **Telnet**: A network protocol for remote command-line communication over TCP, typically on port 23. It allows connecting to remote servers for command execution.
- **SSH**: SSH (Secure Shell) provides a secure alternative to Telnet, encrypting communications between clients and servers. It is commonly used for secure remote administration and file transfers.

## Conclusion

This multithreaded web server exercise provides a practical introduction to building a web server capable of handling multiple concurrent client connections. It offers experience in socket programming, HTTP handling, and multithreading in Python.
