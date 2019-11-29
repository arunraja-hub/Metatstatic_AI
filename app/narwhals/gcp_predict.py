from google.cloud import storage
def implicit():
    # gcp_creditential="C:\\Users\\User\\Documents\\exchange\\csc454\\github\\Narwhals\\app\\narwhals\\metastatic-37388df1c9d5.json"

    

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client.from_service_account_json('metastatic-37388df1c9d5.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

def predict_json(project, model, instances, version=None):
    """Send json data to a deployed model for prediction.

    Args:
        project (str): project where the AI Platform Model is deployed.
        model (str): model name.
        instances ([Mapping[str: Any]]): Keys should be the names of Tensors
            your deployed model expects as inputs. Values should be datatypes
            convertible to Tensors, or (potentially nested) lists of datatypes
            convertible to tensors.
        version: str, version of the model to target.
    Returns:
        Mapping[str: any]: dictionary of prediction results defined by the
            model.
    """
    # Create the AI Platform service object.
    # To authenticate set the environment variable
    # GOOGLE_APPLICATION_CREDENTIALS="C:\\Users\\username\\Downloads\\metastatic-37388df1c9d5.json"
    service = googleapiclient.discovery.build('ml', 'v1')
    name = 'projects/{}/models/{}'.format(metastatic, proto_model)

    if version is not None:
        name += '/versions/{}'.format(version)

    response = service.projects().predict(
        name=name,
        body={'instances': instances}
    ).execute()

    if 'error' in response:
        raise RuntimeError(response['error'])

    return response['predictions']

predict_json(metastatic, proto_model,'C:\Users\User\Documents\exchange\csc454\github\Narwhals\app\narwhals\fffa681f68c58839f9fad90be2ac9cba6ab6f6a5.tif', version=None)
# implicit()