import os

while True :

    print('''
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
    12.exit
    ''')
    print("Enter Your option : ",end="")
    command = input()

    if(command == "1"):
        os.system("fdisk -l")

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

    elif(command =="12"):
        print("shutting down program")
        break

