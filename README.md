# WhatsApp Cloud API Integration using PyWa and Firebase Functions

This repository demonstrates how to integrate WhatsApp Cloud API with Firebase Functions (v2) using the [PyWa](https://github.com/david-lev/pywa) module. Firebase Functions serve as the serverless backend for handling WhatsApp messaging events, offering a scalable and efficient solution.

## Getting Started

Follow the steps below to set up and deploy the WhatsApp Cloud API integration:

### 1. Firebase Functions Setup
To get started with Firebase Functions, follow the official Firebase documentation [here](https://firebase.google.com/docs/functions/get-started?gen=2nd). This will guide you through setting up a Firebase project, installing the Firebase CLI, and deploying your first function.

### 2. Deploying and Making the Function Public
After deploying the function, you'll need to make it publicly accessible. Follow these steps:
1. Navigate to your Google Cloud Console.
2. Locate your function, and edit the **Runtime Environment**.
3. Modify the permissions to make the function public by following this [guide](https://cloud.google.com/run/docs/authenticating/public).

### 3. Setting WhatsApp API Credentials
In order to authenticate and connect to WhatsApp's Cloud API, you will need to configure environment variables within your function. Each environment variable corresponds to a parameter used by the `pywa.WhatsApp()` instance.

#### Environment Variables
Set the following environment variables in your Firebase function (Google Cloud Console > Function > Edit > Runtime Environment Variables):

- `WHATSAPP_PHONE_ID`: Your WhatsApp Phone ID.
- `WHATSAPP_TOKEN`: The token to authenticate with the WhatsApp Cloud API.
- `WHATSAPP_BUSINESS_ACCOUNT_ID`: Your WhatsApp Business Account ID.
- `WHATSAPP_VERIFY_TOKEN`: A custom token for verifying webhook requests.
- `WHATSAPP_APP_ID`: Your WhatsApp App ID.
- `WHATSAPP_APP_SECRET`: Your WhatsApp App Secret.

Refer to the [PyWa documentation](https://pywa.readthedocs.io/en/latest/) for more details on these parameters.

### 4. Setting Up the WhatsApp Webhook
To allow WhatsApp to start invoking your Firebase function webhook, you will need to register the webhook by making a `PATCH` request to the endpoint URL generated during deployment. This registration only needs to be done once, or when the endpoint URL changes.

Example using `curl`:
```bash
curl -X PATCH "https://<your-firebase-function-url>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

## License
This project is licensed under the MIT License.

---

Let me know if there are any other tweaks you'd like!