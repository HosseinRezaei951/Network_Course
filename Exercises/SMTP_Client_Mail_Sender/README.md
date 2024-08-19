# Client Mail Sender with SMTP Exercise

This repository provides two approaches for sending emails using Python: a command-line application using the `smtplib` library and a web-based solution using Flask. The exercise also includes a brief overview of email protocols such as SMTP, IMAP, and POP3.

## Overview

### Part A: Command-Line Email Sender

In this part, a Python script uses the `smtplib`, `ssl`, and `email.mime` libraries to send emails through a Gmail account. The script prompts the user for their email credentials and the recipient’s email address, then sends an email with a subject and message body.

### Part B: Web-Based Email Sender with Flask

This part involves creating a web application using the Flask framework. Users can submit email details through a web form, and Flask handles the sending of the email. This part demonstrates how to integrate Flask with email functionalities and how to create a basic HTML form for user input.

### Part C: Advanced Form Submission

In this part, a registration form is designed with fields for username, phone, email, and password. The form includes validation for these fields and uses AJAX to submit the data to the server. The password is stored in hashed format in the database.

## Directory Structure

### Part A: Command-Line Email Sender

- **`email_sender.py`**: A Python script for sending emails using SMTP. This script prompts the user for their Gmail credentials and email details.

### Part B: Web-Based Email Sender with Flask

The directory for this part includes:

- **`app.py`**: The main Flask application script.
- **`templates/`**: Contains HTML files for the web forms.
  - **`index.html`**: Main form for sending emails.
  - **`index2.html`**: Additional form or result page (if applicable).
  - **`index3.html`**: Another form or result page (if applicable).
- **`static/`**: Contains static files such as JavaScript and CSS.
  - **`jquery.js`**: jQuery library for AJAX operations.
  - **`script.js`**: Custom JavaScript for form handling.
  - **`script2.js`**: Additional JavaScript (if applicable).
  - **`style.css`**: Stylesheet for the HTML pages.

### Part C: Registration Form

- **`app.py`**: The Flask application script that handles form submission, validation, and database interaction.

## How to Run

### Part A: Command-Line Email Sender

1. Ensure Python is installed on your system.
2. Save the script as `email_sender.py`.
3. Run the script: `python email_sender.py`.
4. Follow the prompts to input your email details and send an email.

### Part B: Web-Based Email Sender with Flask

1. Install Flask using pip: `pip install flask`.
2. Navigate to the `HTML SMTP` directory.
3. Run the Flask application: `python app.py`.
4. Open a web browser and navigate to `http://localhost:5000` to access the form and send emails.

### Part C: Registration Form

1. Ensure Python and Flask are installed.
2. Navigate to the directory containing `app.py`.
3. Run the Flask application: `python app.py`.
4. Access the registration form through the provided URL (e.g., `http://localhost:5000`).

## Protocols Overview

### SMTP (Simple Mail Transfer Protocol)

- **SMTP** is used for sending emails. It is a simple protocol that requires only a username and domain to route messages to the recipient.
- SMTP handles the sending of emails but not the retrieval. For receiving emails, protocols like IMAP or POP3 are used.

### IMAP (Internet Message Access Protocol)

- **IMAP** is used for retrieving and managing email messages on a mail server. It operates on port 143 and allows remote access to email stored on the server.

### POP3 (Post Office Protocol version 3)

- **POP3** is used to retrieve email from a server. It is designed for offline email access and typically downloads emails to the client’s device. It operates on port 110.

## Summary

This exercise demonstrates two methods of sending emails using Python: a command-line interface and a web-based approach using Flask. Additionally, it covers essential email protocols and provides a practical implementation of form validation and data handling with AJAX and Flask.
