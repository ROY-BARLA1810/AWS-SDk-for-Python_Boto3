import boto3

ec2 = boto3.resource('ec2', aws_access_key_id='AKIA4CH3B3CMSLHFL5AP',
                     aws_secret_access_key='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',
                     region_name='us-east-1')

vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
# Assign a name to the VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my_vpc_Boto3"}])
vpc.wait_until_available()
print(vpc.id)

# Create and Attach the Internet Gateway
ig = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print(ig.id)

# Create a route table and a public route to Internet Gateway
route_table = vpc.create_route_table()
route = route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig.id
)
print(route_table.id)

# Create a Subnet
subnet = ec2.create_subnet(CidrBlock='10.0.1.0/24', VpcId=vpc.id)
print(subnet.id)

# associate the route table with the subnet
route_table.associate_with_subnet(SubnetId=subnet.id)