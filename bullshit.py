from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
# Create an AcsClient object.
client = AcsClient(
   "<your-access-key-id>", 
   "<your-access-key-secret>",
   "<your-region-id>"
);
# Create a request and set required parameters.
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
# Initiate the API request and display the returned value.
response = client.do_action_with_exception(request)
print(response)