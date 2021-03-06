# Objective

Use Ansible playbook to Configure Reverse Proxy on AWS so that Haproxy update it's configuration 
file automatically on each time new Managed node (Configured With Apache Webserver) join the inventory.

## Steps to configure HAPROXY

Install Following packages in controller node
- python2 or python3
  
Using pip to install following packages
- boto or boto3
  
  After that, you need user credentials for accessing AWS. As ```ec2.py``` make an API call to AWS for your requirement. so we need to set 2 environment variable in the following file

```
Create one file at  '~/'    with name ".boto"

// add following data in file 

[Credentials]
aws_access_key_id = <your_access_key_here>
aws_secret_access_key = <your_secret_key_here>
```

1. Download both ec2 file.

        Both File should be execuatable
            
            chmod +x file name
        

2. Add ```ec2.py``` as inventory file in Ansible.cfg
3. Use ```EC2.yml``` file to provision instance just change parameter according to you.
4. Use ```SetUp.yml``` to Configure server as HAPROXY and WebServer.
   
## Note: if you wanted to see provisoned EC2 instance Run Following command 
````
./ec2.py
 ````
<br></br>

### Following are the variables used in HAPROXY Role
app: haproxy

LoadBlancer_port: 8080

WebServer_port: 80

<br></br>

### Following are the variables used in apache Role
web_port: 80

package: 
     - httpd
     - php

<br></br>
##  Read My Blog On [Medium](https://venkateshpensalwar.medium.com/) to Get More Insight :

https://venkateshpensalwar.medium.com/haproxy-on-aws-using-ansible-a2e1ec74bc1d

