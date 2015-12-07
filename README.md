# Heroku2FA
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

# Introduction
Develop a Heroku app to provide the Two Factor Authentication (2FA) service using Nexmo Messaging APIs. The app should be integrated easily with any platform such as C#, Java, PHP and etc.
 
# Features

- Simple integration with any Application.
- Less configuration required.
- Phone number verification using the SMS.
- Dynamic security key generate.

# Steps to deploy Heroku 2FA

- Use the following URL in your application to send the verification code.
  - Request URL : ```http://<heroku-app-url>/verify?dst=<phone_with_country_code>```
  - dst parameter is destination phone number with country code to send verification code.
  - Verify will return you a request id in JSON format. Extract that request id and send back with code.
- To authenticate send code and request id on following URL.
  - Request URL : ```http://<heroku-app-url</validate?code=<Mobile received code>&req_id=<request_id>```
  - Send request on validate end point with code and request id query string.
  - Returns JSON with message and status.
- To search on Requests status that are terminated or still running.
  - Request URL: ```http://<heroku-app-url>/status?req_id=<request_id>```
  - Send request on status end point with request id query string.
  - Return the JSON of status information.