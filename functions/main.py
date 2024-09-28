import flask
from firebase_functions import https_fn
from wa.client import get_wa_client

app = flask.Flask(__name__)

#PATCH method is an admin manual made request only to register the webhook and perform the challange once
def handle_patch_method_as_register_webhook():
    get_wa_client(app, f"https://{flask.request.headers.get('host')}") #register webhook
    return https_fn.Response(status=201, response='Webhook registration request was sent successfully')

# Expose Flask app as a single Cloud Function:
@https_fn.on_request()
def handle_whatsapp_request(req: https_fn.Request) -> https_fn.Response:
    if req.method == 'PATCH':
        return handle_patch_method_as_register_webhook()
        
    #initialize client on cold start
    #needs to be invoked before the request is handled so pywa can register the inbound messages Flask route
    get_wa_client(app)
    
    with app.request_context(req.environ):
        return app.full_dispatch_request()
