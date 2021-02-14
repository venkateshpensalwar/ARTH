# Retrive Container IP
🔰  It is an Ansible playbook that will retrieve new Container IP and update the inventory. So that further Configuration of Web Server could be done inside that Container.
<br></br>

# Quick Refernce

1. <b>ContainerIP.yml:</b> 
   
   This file will launch Container image From `venkatesh14/sshimage` will retrive IP
    and will save container IP using `DockerIP.txt.j2` .

2. <b>DockerIP.txt.j2:</b> 
   
   This is Template file which will used to create inventory of Container IP.

3. <b>DockerTask:</b>
   
   1. ansible.cfg: configuration file for the ansible.
   2. DockerIP.txt: Inventory created from template `DockerIP.txt.j2`.
   3. Docker.yml:  To install and configure `Apache web server` on Container.
   4. index.html:  dummy file to check our web server is properly running or not.
   
# How to use?

1. Run the `ContainerIP.yml` To launch and retrive ip of container.
   
   ```
   ansible-playbook ContainerIP.yml
   ```
2. Now launch `Docker.yml` to configure apache web server on it.
   
   ```
   ansible-playbook Docker.yml
   ```
<br></br>

##  Read My Blog On [Medium](https://venkateshpensalwar.medium.com/) to Get More Insight :

https://venkateshpensalwar.medium.com/retrieve-container-ip-and-update-ansible-inventory-using-ansible-a7eb8b76f8c0