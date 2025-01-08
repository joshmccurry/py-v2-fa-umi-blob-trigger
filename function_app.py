import azure.functions as func
import azurefunctions.extensions.bindings.blob as blob
import datetime
import json
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="client", path="inputcontainer", connection="BlobTriggerStorage") 
#def BlobTrigger(myblob: func.InputStream):
def BlobTrigger(client: blob.BlobClient):
    #logging.info(f"Python blob trigger function processed blob"
    #            f"Name: {myblob.name}"
    #            f"Blob Size: {myblob.length} bytes")
    logging.info(
        f"Python blob trigger function processed blob \n"
        f"Properties: {client.get_blob_properties()}\n"
        f"Blob content head: {client.download_blob().read(size=1)}"
    )

