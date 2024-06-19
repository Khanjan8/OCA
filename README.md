# OCA (Online Chatting Application)

OCA (Online Chatting Application) is a web-based chat application built using Django, HTML, CSS, and JavaScript (with AJAX). It enables users to communicate in real-time through a user-friendly interface, including features such as OTP authentication, user registration, chat functionality, and admin management.

## Constraint

It uses Twilio for OTP authentication. So that you have to register mobile number in twilio And need to change TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER in views.py

## Features

### User-Side Features
- **OTP Authentication**
  - Users can authenticate using OTP (One-Time Password) sent to their registered mobile number.
  - Twilio API is used to send OTP to registered mobile numbers.
  
- **User Registration**
  - Users are required to register their mobile number before sending an OTP for authentication.

- **Chatting Interface**
  - Real-time chat interface where users can send and receive messages.
  - Chat history is displayed with the option to search for specific users.

- **Left Panel**
  - Display of old and new chat users' names for easy navigation and selection.

- **Message Box**
  - Input area for composing and sending messages within the chat interface.

- **Settings and Log Out**
  - User settings include profile updates and the option to log out.

- **Feedback and Customer Service**
  - Users can submit feedback via the application, and there is a customer service feature for addressing user queries.

### Admin-Side Features
- **Admin Login**
  - Admin can log in with a username and password to access admin functionalities.

- **Feedback Management**
  - Admin can view and reply to user feedback submitted through the application.

- **Announcement**
  - Admin can make announcements that are displayed to all users of the application.

## Technologies Used
- **Django**
  - Python-based web framework used for backend development.

- **HTML/CSS/JavaScript**
  - Frontend technologies for user interface design and interactivity.

- **Twilio API**
  - Used for sending OTPs to registered mobile numbers.

- **AJAX**
  - Asynchronous JavaScript and XML for making asynchronous requests to the server.

