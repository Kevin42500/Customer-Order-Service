# Customer-Order-Service

This is a customer order service built with Flask, Flask OIDC, and Africa's Talking SMS API. It allows you to create customers and place orders, sending an SMS alert to the customer upon successful order placement.

## Table of Contents
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Unit Tests](#unit-tests)
- [CI/CD Pipeline](#cicd-pipeline)

## Dependencies
- Python
- Flask
- Flask OIDC
- Africa's Talking SDK

## Configuration
Before running the application, you need to set up the following configurations:

1. Create a `client_secrets.json` file with your OIDC client secrets. Follow the guidelines provided by your OIDC provider (e.g., Auth0, Okta) to obtain the necessary client secrets.


## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Kevin42500/Customer-Order-Service.git
   cd Customer-Order-Service