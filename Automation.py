
import os
import getpass
import pyfiglet
os.system("clear")
os.system('tput blink')
os.system('tput setaf 2')
print(pyfiglet.figlet_format("FSOCIETY"))
os.system('tput sgr0')
os.system('tput setaf 7')
print("Please Enter Fsociety Pass \n")
pas = getpass.getpass()
if(pas == "123"):
    while True :

        print('''\n --------Friday Automation manager--------
        c:clear e:Exit the Program
        1.LVM
        2.Docker
        3.Linux Basic
        ''')
        print("Enter Your option : ",end="")
        command = input()
        if(command == "1"):
            while True :

                print('''\n --------LVM manager--------
                c:clear e:Back to main menu
                1.Show avialble devices/HDD
                2.create Physical Volumes(PV)
                3.Create Volume Group (VG)
                4.Extend Volume Group
                5.Create Logical Volume (LV)
                6.Extend LV
                7.Show physical volumes
                8.Show volume groups
                9.show LVM
                10.List of HDD blocks
                11.Mount LVM's
                ''')
                print("Enter Your option : ",end="")
                command = input()
            
                if(command == "1"):
                    os.system("fdisk -l")
                elif(command == "c"):
                    os.system("clear")
                elif(command == "2"):
                    print("Enter device name :",end="")
                    pv = input()
                    os.system("pvcreate "+pv)
            
                elif(command == "3"):
                    print("Enter volume group name : ",end="")
                    name =input()
                    print("Enter device name you want in LVM : ",end="")
                    dev1 = input()
                    os.system("vgcreate {} {} ".format(name,dev1))
                elif(command == "4"):
                    print("Enter your new HDD name : ",end="")
                    hdd = input()
                    print("Enter your VG name : ",end="")
                    vgname = input()
                    os.system("vgextend {} {}".format(vgname,hdd))
            
                elif(command == "5"):
                    print("How much size do you want[Ex.5G] : ",end="")
                    size = input()
                    print("Enter your Volume group name : ",end="")
                    vgname =input()
                    print("Enter name for LVM : ",end="")
                    lvmname = input()
                    os.system("lvcreate -L {} -n {} {}".format(size,lvmname,vgname))
            
                elif(command =="6"):
                    print("Enter How much size do you wan to increase in GB [ex.5] : ",end="")
                    size=input()
                    print("Enter LVM device name : ",end="")
                    lvm = input()
                    os.system("lvextend --size +{}G {}".format(size,lvm))
                    os.system("resize2fs {}".format(lvm))

                elif(command == "7"):
                    os.system("pvdisplay")
            
                elif(command =="8"):
                    os.system("vgdisplay")

                elif(command == "9"):
                    os.system("lvs")

                elif(command == "10"):
                    os.system("lsblk")
            
                elif(command == "11"):
                    print("Enter device name that will mount : ",end="")
                    mountname = input()
                    print("Enetr mount point : ",end="")
                    point = input()
                    os.system("mount {} {}".format(mountname,point))
                elif(command =="e"):
                    os.system("clear")
                    break
        elif(command == "c"):
            os.system("clear")
        elif(command == "e"):
            break
        elif(command == "2"):
             while True :

                print('''\n --------Docker manager--------
                c:clear e:Back to main menu
                install docker : to install docker
                
                1.Display Images
                2.Pull images
                3.Display Container's
                4.Launch Container
                5.Start Container
                6.attach container
                7.stop Container
                8.Remove Container
                9.Remove Image
                
                start: To start docker service
                ''')
                print("Enter Your option : ",end="")
                command = input()
                if(command == "1"):
                    os.system("docker images")
                elif(command == "install docker"):
                    os.system("yum install docker-ce --nobest")
                elif(command == "c"):
                    os.system("clear")
                elif(command == "e"):
                    os.system("clear")
                    break
                elif(command == "2"):
                    print("Enter image you want to Download : ",end="")
                    image=input()
                    os.system("docker pull {}".format(image))
                elif(command == "3"):
                    os.system("docker ps -a")
                elif(command == "4"):
                    print("Enter any Container name : ",end="")
                    name = input()
                    print("Enter image name for launch : ",end="")
                    laun = input()
                    os.system("docker run -dit --name {} {}".format(name,laun))
                elif(command == "5"):
                    print("Enter container name to start : ",end="")
                    container = input()
                    os.system("docker start {}".format(container))
                elif(command == "6"):
                    print("Enter Container name to attach : ",end="")
                    cname = input()
                    os.system("docker attach {}".format(cname))
                elif(command == "7"):
                    print("Enter Container name to stop : ",end="")
                    ename = input()
                    os.system("docker stop {}".format(ename))
                elif(command =="8"):
                    print("Enter Container name to remove : ",end="")
                    rname = input()
                    os.system("docker rm {}".format(rname))
                elif(command =="9"):
                    print("Enter image name to remove : ",end="")
                    iname = input()
                    os.system("docker image rm {}".format(iname))
                elif(command == "start"):
                    os.system("systemctl start docker")
        elif(command == "3"):
            while True :

                print('''\n --------Linux Manager--------
                c:clear e:Back to main menu
                
                1.date
                2.list all things
                3.working Directory
                4.change directory
                5.show memory
                6.cpu info
                7.show mounted volumes
                ''')
                print("Enter Your option : ",end="")
                command = input()
                if(command == "1"):
                    os.system("date")
                elif(command == "c"):
                    os.system("clear")   
                elif(command == "e"):
                    os.system("clear")
                    break
                elif(command == "2"):
                    os.system("ls")
                elif(command == "3"):
                    os.system("pwd")
                elif(command == "4"):
                    print("Enter path to chnage directory : ",end="")
                    path = input()
                    os.system("cd {}".format(path))
                elif(command == "5"):
                    os.system("free -h")
                elif(command == "6"):
                    os.system("lscpu")
                elif(command == "7"):
                    os.system("df -h")




