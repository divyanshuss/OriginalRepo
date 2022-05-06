// LVM partition //
import os 

os.system("tput setaf 6 ")
print(" \t\t\t Welcome to the partition world ")
pv=[]
vg= " "
lv=" "
 while True :
	os.system("tput setaf 3")
	print(-------------------------------------------------------------)
	print("""
	   Press 1 : To know about the harddisk.
	   Press 2 : To create Physical Volume 
	   
	   Press 3 : To create Volume Group
	   Press 4 : To display vg
           Press 5: to Crerate logical volume
           Press 6 : To display the Logical volume
	   Press 7 : To format and mount the Logical Volume 
	   Press 8 : To extend the logical volume 
           Press 9 : To end the menu !!
               """)
  
	printf("\n")
	c=int(input("Enter the  choice number you wish to execute ")

	if(c==1) :
		os.system("tput setaf 6")
		print(" You entered choice 1 ")
		print(" The Harddisk Information  : ")
		os.system("tput setaf 3 ")
		os.system("fdisk -l")
	elif(c==2):
		os.system("tput setaf 6")
		a=int(input("Enter the number of physical volume you wish to create"))
		for i in range(a):
			printf("Enter physical volume " ; (i+1), ",end=" ")
			b=input()
			os.system("pvcreate{}.format(b))
			pv.append(b)
		os.system("tput setaf 3")
	elif(c==3):
		os.system("tput setaf 6")
                print(" You entered choice 3")
		n=input("Enter any name for your volume group : ")
		vg=n
		hd=" "
		for a in pv :
			hd= hd +" " + a
			print("hd: ",hd)
			os.system("vgcreate{}.format(vg,hd))
	elif(c==4):
		os.system("tput setaf 6")
		print("you entered choice 4")
		print("Volume group information")
		os.system("vgdisplay{} ".format(vg))
	elif(c==5):
		os.system("tput setaf 6")
		print("you entered choice 5")
		n=input("Enter the name of logical volume ")
		s=int(input("Enter the size (in GB) of Logical volume"))
		lv=n
		os.system("lvcreate --size {}G --name {} {}".format(s,lv,vg))
	elif(c==6):
		os.system("tput setaf 6")
		print("You entered choice 6")
		printf(" Logical Volume Information")
		os.system("lvdisplay {} {}".format(lv,vg))
	elif(c==7):
		
		os.system("tput setaf 6")
		print("You entered choice 7")
		os.system("mkfs.ext4  /dev/{}/{}".format(vg ,lv))
		os.system("tput setaf 3")
		print("Successfully formated")
		os.system("tput setaf 3")
		d=input("Enter the directory to mount the lv ")
		os.system("mkdir /{}".format(d))
		os.system(" mount /dev/{}/{} /{}".format(vg,lv,d))
		os.system("tput setaf 3")
		print("Successfully mounted")
	elif(c==8) :
		
		os.system("tput setaf 6")
		print("You entered choice 8")
		printf("The available size of volume group")
		os.system("vgdisplay{}".format(vg))
		size=input("Enter the size you wanna extend the lv")
		os.system("lvextend --size  +{}G /dev/{}/{}".format(size,vg,lv))
		os.system("resize2fs /dev/{}/{}".format(vg,lv))
		os.system("tput setaf 3")
		print(" Successfully Extended")

	elif(c==9)
		os.system("tput setaf 6")
		printf(" The end !! ")
                exit()

		 
	  

	