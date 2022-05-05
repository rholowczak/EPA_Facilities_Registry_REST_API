# EPA Facilities Registry REST API
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
<li> Download and install the swagger client REST API code<br>
   I have uploaded two ZIP files above <tt>frs-preprod-query-python-client-generated.zip</tt> and <tt>frs-preprod-submit-python-client-generated.zip</tt> that contain the Python version of the Swagger client code. However if changes are made to the API, the Swagger Python client should be re-generated from the source.
   <p>
   To generate the Python Client:
   <ul><li>Visit https://editor.swagger.io/ and Clear the editor</li>
   <li> Open the Query Swagger client: https://frsquerypre-api.epa.gov/facilityiptquery/swagger-v1.json</li>
   <li>Copy the contents and paste them into the Swagger editor.  You may be prompted to convert the JSON into YAML. Click OK.</li>
   <li>Pull down the Generate Client menu and choose "Python".   The python-client-generated.zip file will be downloaded.</li>
   <li> Move the python-client-generated.zip file to a suitable directory and unzip.</li>
   <li>Follow the instructions in the README.md file to build and install the client.</li>
   </ul>

<li>Obtain a NAAS username and password from nodehelpdesk@epacdx.net <br>
   In the request indicate the provisioning option to receive from and/or submit data to the FRS the partner system.
   </li>
<li>Save the NAAS user id and password in a file named credentials.py<br>
   <pre>
   user_id = 'Your NAAS username here'
   password = 'Your NAAS password here'
   </pre>
   </li>
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
   <li>Now you should be able to run queries against the FRS test or production system. Also, if you have the permissions, you should be able to contribute data to the FRS. </li>
</ol>
   
