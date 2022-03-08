# EPA_Facilities_Registry_REST_API
Code examples for interacting with the Environmental Protection Agency (EPA) Facilities Registry System (FRS) using the REST API

Python code examples demonstrate how to use the swagger client REST API
to query the EPA Facilities Registry System (FRS). General information
about EPA FRS can be found here at this URL: <br>
   https://www.epa.gov/frs/facility-registry-service-frs-api
   <br>
Technical documentation for the REST Query API can be found at this URL:<br>
  https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html
<br>

# Requirements
<ol>
<li> Download and install the swagger client REST API code</li>
<li>Obtain a NAAS username and password from nodehelpdesk@epacdx.net <br>
   In the request indicate the provisioning option to receive from and/or submit data to the FRS the partner system.
   </li>
<li>Save the NAAS user id and password in a file named credentials.py<br>
   <pre>
   user_id = 'Your NAAS username here'
   password = 'Your NAAS password here'
   </pre>
   </li>
<li> Some FRS query criteria such as a specific registryid, user_id, state_code </li>
<li> Select the appropriate pre-production (testing) or Production server URL<br>
     <ul><li> Pre-production:<br>
      Query: https://frsquerypre-api.epa.gov/facilityiptquery/swagger-ui/index.html<br>
      Submit: https://frssubmitpre-api.epa.gov/facilityiptsubmit/swagger-ui/index.html<br>
        </li>
   <li>Production:<br>
      Query: https://frsqueryprd-api.epa.gov/facilityiptqueryprd/swagger-ui/index.html<br>
      Submit: https://frssubmitprd-api.epa.gov/facilityiptsubmitprd/swagger-ui/index.html<br>
        </li>
   </ul>
   </li>
  <li>Make sure the NAAS account has permissions to use the appropriate server and service.</li>
   </ol>
   
