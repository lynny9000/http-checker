# HTTP Checker

A Python-based HTTP checker that sends requests to a URL and returns status, response time, and server details.

## Features

* Checks HTTP status codes (e.g. 200, 404, 500)
* Displays status meaning (OK, Not Found, etc.)
* Classifies responses (Success, Client Error, Server Error)
* Measures response time
* Displays response headers (server, content type, etc.)
* Handles invalid URLs and connection errors
* Automatically adds `https://` if missing
* Runs continuously until user exits

## How it works

The script uses the `requests` library to send HTTP requests and retrieve responses from web servers.

Key concepts:

* HTTP status codes - indicate result of request (200 OK, 404 Not Found, etc.)
* Response time - measures how long the server takes to respond
* Headers - provide information about the server and response
* Error handling - ensures the script does not crash on invalid input

## Usage

Run:

python http_checker.py

Example:

Enter URL (or type 'exit' to quit): google.com

Output:

--- HTTP Check ---
URL: https://google.com
Status: 200 OK (Success)
Response time: 0.123 seconds

Headers: 
  Date: Tue, 14 Apr 2026 12:40:43 GMT 
  Expires: -1 
  Cache-Control: private, max-age=0 
  Content-Type: text/html; charset=ISO-8859-1 
  P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info." 
  Content-Encoding: gzip 
  Server: gws 
--- 

## Notes

* Uses Python `requests` library for HTTP communication
* Automatically cleans input by adding `https://` if missing
* Not all websites return the same headers
* Response time may vary depending on network conditions
* Handles connection errors and invalid domains safely
