# Automated Rain Alert SMS Notifier

A Python script that monitors the weather forecast for a specific location and sends an SMS alert if rain is predicted in the next 12 hours. This project is a practical example of API integration and task automation.

The script fetches hourly forecast data from the OpenWeatherMap API. If any of the upcoming weather conditions indicate rain, it uses the Twilio API to send a customizable SMS notification to a designated phone number.

## Key Features

-   **Proactive Weather Alerts:** Checks the 12-hour forecast to give you advance warning of rain.
-   **Automated SMS Notifications:** Uses Twilio to send alerts directly to your phone.
-   **Location-Specific:** Easily configurable for any latitude and longitude.
-   **Secure Credential Management:** Instructions provided for using environment variables to keep your API keys and tokens safe.
-   **Cloud-Ready:** Designed for deployment on a cloud service like PythonAnywhere to run automatically every day.

## Project Setup & Configuration

This project requires credentials from two different services. Follow these steps carefully.

### 1. Prerequisites

-   Python 3.x
-   An [OpenWeatherMap](https://openweathermap.org/) account
-   A [Twilio](https://www.twilio.com/) account
-   `pip` (Python package installer)

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/pythonProjectwetheralert.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd pythonProjectwetheralert
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install requests twilio
    ```

### 3. Acquiring Your API Credentials

You will need to gather several secret keys and tokens.

1.  **Get OpenWeatherMap API Key:**
    -   Sign up for a free account on [OpenWeatherMap](https://openweathermap.org/).
    -   Navigate to the "API keys" tab in your account dashboard.
    -   Copy the default API key provided.

2.  **Get Twilio Credentials:**
    -   Sign up for a free trial account on [Twilio](https://www.twilio.com/).
    -   From your account console dashboard, you will need three things:
        1.  **Account SID:** Your unique account identifier.
        2.  **Auth Token:** Your secret authentication token.
        3.  **Twilio Phone Number:** Get a trial phone number from the "Phone Numbers" section. This will be the number that sends the SMS.

### 4. Securing Your Credentials with Environment Variables

**Do not hardcode your secret keys in `main.py`**. The best practice is to use environment variables.

**How to Set Environment Variables:**

-   **On macOS/Linux:**
    ```bash
    export OWM_API_KEY="Your_OpenWeatherMap_API_Key"
    export TWILIO_ACCOUNT_SID="Your_Twilio_Account_SID"
    export TWILIO_AUTH_TOKEN="Your_Twilio_Auth_Token"
    export TWILIO_PHONE_NUMBER="Your_Twilio_Phone_Number"
    export RECIPIENT_PHONE_NUMBER="The_Number_To_Send_Alerts_To"
    ```
-   **On Windows:**
    ```bash
    set OWM_API_KEY="Your_OpenWeatherMap_API_Key"
    set TWILIO_ACCOUNT_SID="Your_Twilio_Account_SID"
    # ... and so on for the other variables
    ```

**Update `main.py` to Use Environment Variables:**
You need to modify your code to read these variables.

```python
import os
import requests
from twilio.rest import Client

# Fetch credentials securely from environment variables
api = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone = os.environ.get("TWILIO_PHONE_NUMBER")
recipient_phone = os.environ.get("RECIPIENT_PHONE_NUMBER")

# ... rest of your code ...

# Inside the 'if will_rain:' block, use the variables
message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂️",
    from_=twilio_phone,
    to=recipient_phone,
)
```

## Deployment to the Cloud (PythonAnywhere)

To automate this script, deploy it to a service like PythonAnywhere.

**Recommended Schedule:** Run the script once a day, early in the morning (e.g., **7:00 AM UTC**), to get a forecast for the day ahead.

**Steps to Deploy:**

1.  **Create a free PythonAnywhere account.**
2.  **Set Environment Variables:**
    -   Go to the "Web" tab and scroll down to the "Environment variables" section.
    -   Add each variable and its value (e.g., `OWM_API_KEY` and `Your_Key`).
3.  **Upload Your Files:**
    -   Go to the "Files" tab and upload your modified `main.py` file.
4.  **Set Up a Scheduled Task:**
    -   Go to the "Tasks" tab.
    -   Create a new "Daily task".
    -   Set the time you want the script to run (e.g., `07:00` UTC).
    -   In the command box, enter: `python3 /home/YourUsername/main.py` (replace `YourUsername` with your PythonAnywhere username).
    -   Click "Create task".

Your script will now run automatically every morning, check the weather, and alert you if it's going to rain.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.
