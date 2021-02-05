# Objective

> Create an Ansible Playbook which will dynamically 
load the variable file named same as OS_name and just by 
using the variable names we can Configure our target node.
(Note: No need to use when keyword here.)

<br></br>
## Steps to run playbook 

1. Run following command to get all OS name from all node.
   ```
   ansible all -m setup
   ```

2. According to os name create variable file (Case sensitive).
   
   Ex. Ubuntu.yml or RedHat.yml


3. Update all the required variable in variable files.
    
   In my case:
   ```
   pacakge: httpd or apache2
   web_port: 80
   ```
4. Run playbook using following command.
   
   ```
   ansible-playbook Dynamic.yml
   ```
<br></br>
##  Read My Blog On [Medium](https://venkateshpensalwar.medium.com/) to Get More Insight :

https://venkateshpensalwar.medium.com/create-an-ansible-playbook-which-dynamically-loads-variable-file-named-the-same-as-os-name-and-4f2bd4bd7c80