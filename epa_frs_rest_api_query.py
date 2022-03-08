# epa_frs_query.py  EPA Facilities Registry Query Program
# Richard Holowczak 20211213
# This program demonstrates how to use the swagger client REST API
# to query the EPA Facilities Registry System (FRS). General information
# about EPA FRS can be found here at this URL: 
# https://www.epa.gov/frs/facility-registry-service-frs-api
# Technical documentation for the REST Query API can be found at this URL:
#   https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html

# Requirements:
# a) Download and install the swagger client REST API code
# b) Obtain a NAAS username and password from nodehelpdesk@epacdx.net 
#    In the request indicate the provisioning option to receive from and/or 
#    submit data to the FRS the partner system.
# c) Save the NAAS user id and password in a file named credentials.py
#    user_id = 'Your username here'
#    password = 'Your password here'
# d) Some FRS query criteria such as a specific registryid, user_id, state_code
# e) Select the appropriate pre-production (testing) or Production server URL
#    Pre-production:
#    Query: https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html
#    Submit: https://frssubmitpre-api.epa.gov/facilityiptsubmit/swagger-ui/index.html
#    Production:
#    Query: https://frsqueryprd-api.epa.gov/facilityiptqueryprd/swagger-ui/index.html
#    Submit: https://frssubmitprd-api.epa.gov/facilityiptsubmitprd/swagger-ui/index.html
#    Make sure the NAAS account has permissions to use the appropriate server and service.

# Optional: Use Pretty-Print to show JSON documents
from pprint import pprint

# Import the Swagger Client and some specific methods.
import swagger_client
from swagger_client.rest import ApiException
from swagger_client.configuration import Configuration

# Assume the username and password are saved in file credentials.py
# user_id = 'Your NAAS username'
# password = 'Your account password'
import credentials

# Set the query host for either the pre-production or production server
query_host="https://frsquerypre-api.epa.gov/facilityiptquery/v1/FRS"
# query_host="https://frsqueryprd-api.epa.gov/facilityiptqueryprd/v1/FRS"

# Create a Configuration object
configuration = Configuration()

# Set the host property to the appropriate host URI
configuration.host = query_host

# Create an instance of the swagger client API class
api_instance = swagger_client.FRSApi(swagger_client.ApiClient(configuration))

# Set up a few different query parameters.
registry_id = '110040474082'         # A specific FRS registery entry 
state_code = 'NJ'                    # All FRS entries in New Jersey
city_name = 'CARLSTADT'              # All FRS entries in Carlstadt
FacilitySourceSystemProgramCode = 'MERI-FIS'

try:
    # This service is used to query registry data in FRS.
    # api_response = api_instance.query_registry_get(credentials.user_id, credentials.password, registry_id='110040474082')
    # api_response = api_instance.query_registry_get(credentials.user_id, credentials.password, state_code='NJ')
    # api_response = api_instance.query_registry_get(credentials.user_id, credentials.password, city_name='CARLSTADT')
    api_response = api_instance.query_registry_get(credentials.user_id, credentials.password, location_address='118 MOONACHIE AVE')
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FRSApi.query_registry_get: %s\n" % e)
