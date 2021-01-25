Role Apache
=========

This role will configure apache web server on linux systems.

Requirements
------------

No special requirement for this task

Role Variables
--------------
In the vars/main.yml

### vars file for apache

web_port: port number
package: 
     - package1
     - package2

Dependencies
------------
No dependencies as such needed

Example Playbook
----------------
make one playbook put this yml code inside it and just run the play.

    - hosts: servers
      roles:
         -  role: rolename 


Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
