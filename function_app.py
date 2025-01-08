import azure.functions as func
#import azurefunctions.extensions.bindings.blob as blob
from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential
import datetime
import json
import logging
import os

app = func.FunctionApp()
container="inputcontainer"

@app.blob_trigger(arg_name="myblob", path=container, connection="BlobTriggerStorage") 
def BlobTrigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    
    blob_name = os.path.basename(myblob.name)                                   # Clean name and remove path
    blob_uri = os.getenv("BlobTriggerStorage__blobServiceUri")                  # Stored Uri for Trigger
    client_id = os.getenv("BlobTriggerStorage__clientId")                       # Stored ClientId for User Assigned Identity
    identity = DefaultAzureCredential(managed_identity_client_id=client_id)     # Authenticated User Assigned Identity
    client = BlobClient(account_url=blob_uri, container_name=container, blob_name=blob_name, credential=identity) # Populate Constructor for Client

    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Properties: {client.get_blob_properties()}\n"
        f"Blob content head: {client.download_blob().read(size=1)}"
    )

