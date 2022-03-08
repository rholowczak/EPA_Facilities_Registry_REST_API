# EPA_Facilities_Registry_REST_API
Code examples for interacting with the Environmental Protection Agency (EPA) Facilities Registry System (FRS) using the REST API

Python code examples demonstrate how to use the swagger client REST API
to query the EPA Facilities Registry System (FRS). General information
about EPA FRS can be found here at this URL: 
   https://www.epa.gov/frs/facility-registry-service-frs-api
Technical documentation for the REST Query API can be found at this URL:
  https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html

Requirements:<br>
a) Download and install the swagger client REST API code<br>
b) Obtain a NAAS username and password from nodehelpdesk@epacdx.net 
   In the request indicate the provisioning option to receive from and/or 
   submit data to the FRS the partner system.
c) Save the NAAS user id and password in a file named credentials.py
   user_id = 'Your username here'
   password = 'Your password here'
d) Some FRS query criteria such as a specific registryid, user_id, state_code
e) Select the appropriate pre-production (testing) or Production server URL
   Pre-production:
      Query: https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html
      Submit: https://frssubmitpre-api.epa.gov/facilityiptsubmit/swagger-ui/index.html
   Production:
      Query: https://frsqueryprd-api.epa.gov/facilityiptqueryprd/swagger-ui/index.html
      Submit: https://frssubmitprd-api.epa.gov/facilityiptsubmitprd/swagger-ui/index.html
  Make sure the NAAS account has permissions to use the appropriate server and service.
