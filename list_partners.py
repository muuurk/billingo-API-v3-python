from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = '7d48da08-9e3d-11ed-b875-0adb4fd9a356'

# create an instance of the API class
api_instance = swagger_client.PartnerApi(swagger_client.ApiClient(configuration))

try:
    # List all partners
    api_response = api_instance.list_partner()
    print(api_response)
except ApiException as e:
    print("Exception when calling PartnerApi->list_partner: %s\n" % e)
