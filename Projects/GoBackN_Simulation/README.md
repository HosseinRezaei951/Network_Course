# Go-Back-N Simulation

Welcome to the Go-Back-N project repository. This repository contains a C++ program designed to simulate network communication scenarios using the Go-Back-N protocol, an Automatic Repeat reQuest (ARQ) protocol for reliable data transmission.

## Purpose

The primary objectives of this code are:

- **Simulate Network Communication**: Model the transmission of data between network nodes, implementing the Go-Back-N protocol to manage data flow and error recovery.
- **Illustrate Network Protocols**: Demonstrate the functionality of the Go-Back-N protocol, including its error handling and data retransmission mechanisms.
- **Showcase Concurrency**: Utilize multithreading to manage concurrent tasks such as data transmission and error handling in a network simulation.
- **Implement Error Handling**: Simulate network errors and implement mechanisms to handle them, ensuring reliable communication between nodes.
- **Simulate Realistic Network Traffic**: Generate and manage network traffic to test the performance and robustness of the simulation.

## Key Features

- **Go-Back-N Protocol**: Implements the Go-Back-N sliding window protocol for managing data transmission and error recovery.
- **Concurrency**: Uses multithreading to handle simultaneous data transmissions and network events.
- **Error Handling**: Simulates and manages network errors such as packet loss and corruption.
- **Traffic Simulation**: Generates network traffic to evaluate the performance and behavior of the simulation.
- **Key Methods**: Includes methods to manage the sliding window and data transmission, crucial for understanding the protocol's functionality.

## Understanding Key Concepts

This project aids in understanding the following key concepts in network programming:

- **Network Protocols**: Implementation and management of the Go-Back-N protocol for reliable data transmission.
- **Concurrency and Multithreading**: Using threads to handle multiple network tasks simultaneously.
- **Error Handling in Networks**: Simulating and handling network errors to ensure reliable communication.
- **Traffic Simulation**: Generating and managing network traffic to test network performance.

### Go-Back-N Algorithm

The Go-Back-N (GBN) protocol is a sliding window protocol used for reliable data communication. Key features include:

- **Window Size**: The sender can send multiple frames (up to \( N \)) before needing an acknowledgment for the first frame. The receiver can only accept frames in order, and any missing or erroneous frames result in retransmission of the frame and all subsequent frames.
- **Acknowledgment**: The receiver sends acknowledgments (ACKs) for correctly received frames. If a frame is lost or corrupted, the sender retransmits that frame and all subsequent frames.
- **Error Detection and Retransmission**: Ensures reliable data transmission by retransmitting frames if errors or losses are detected.
- **Flow Control**: Limits the number of unacknowledged frames to avoid overwhelming the receiver.

## Key Methods

The following methods are crucial for understanding and implementing the Go-Back-N protocol:

- **`Sliding_Window()`**: Manages the sliding window for the Go-Back-N protocol. This method adjusts the window size and handles the movement of the window as frames are acknowledged and retransmitted.
- **`Sending_Window()`**: Handles the sending of frames within the current window. It ensures that frames are sent correctly and manages the retransmission of lost or corrupted frames.
- **`Shifting_Window()`**: Manages the shifting of the window as frames are acknowledged. This method updates the window position and ensures that new frames can be sent as older frames are acknowledged.

## Problem Definition

The project simulates a network communication system to understand and analyze the Go-Back-N protocol. The simulation involves:

1. Implementing the Go-Back-N protocol to manage data transmission and error recovery.
2. Handling concurrent data transmissions and network events using multithreading.
3. Simulating network errors and implementing mechanisms for reliable communication.
4. Generating network traffic to evaluate the performance of the Go-Back-N protocol.

## Analysis

Based on the problem definition, the Go-Back-N simulation is implemented in C++ with a focus on:

- **Protocol Implementation**: Handling the Go-Back-N protocol for reliable data transmission.
- **Concurrency**: Using threads to manage simultaneous data transmissions and network events.
- **Error Handling**: Simulating and managing network errors to ensure reliable communication.

### Use of Threads

Threads are utilized in the program to:

- Manage concurrent data transmissions and network events.
- Implement and handle the Go-Back-N protocol's sliding window and retransmission mechanisms.

### Conclusion

The Go-Back-N project provides a comprehensive understanding of network communication, protocols, and concurrency. It helps analyze and test the performance of the Go-Back-N protocol in handling data transmission and error recovery in a simulated network environment.
