import os
import getpass

def wait():
    os.system("tput setaf 3")
    input("Press Enter to continue.....")
    os.system("tput sgr 0")

def figlet(title,font,color):
    os.system("tput bold")
    os.system("tput setaf {}".format(color))
    os.system("figlet -w 200 -ck -f %s '%s'"%(font,title))
    os.system("tput sgr 0")

def mountpoint(disk_name):
	mount = input("Enter your mount point: ")
	os.system(f"mount /dev/{disk_name} {mount}")
	print("Mounted!!")

def format_type(disk_name):
				os.system("tput bold")
				os.system("tput setaf 2")
				print("""
				Choose The Format Type

				Press 1. For ext2
				Press 2. For ext3
				Press 3. For ext4""")
				format = int(input("Enter your Choice: "))

				if format == 1:
					os.system(f"mkfs.ext2 /dev/{disk_name}1 > /dev/null")
					os.system("sleep 3")
					os.system("clear")
					mountpoint(disk_name)
				if format == 2:
					os.system(f"mkfs.ext3 /dev/{disk_name}1 > /dev/null")
					os.system("sleep 3")
					os.system("clear")
					mountpoint(disk_name)
				if format == 3:
					os.system(f"mkfs.ext4 /dev/{disk_name}1 > /dev/null")
					os.system("sleep 3")
					os.system("clear")
					mountpoint(disk_name)

def create_partition():
	while True:
		os.system("clear")
		os.system("tput bold")
		os.system("tput setaf 2")
		print("""
		Create a New Partition

		Press 1. Create Static Partition
		Press 2. Create LVM Partition
		Press 3. Go To Main Menu
		Press 4. To Exit
		""")
		os.system("tput sgr 0")
		option2_1 = int(input("Enter Your Choice: "))

		if option2_1 == 1:
			os.system("clear")
			os.system("fdisk -l")
			disk_name = input("Enter your disk name(e.g-sda): ")
			os.system(f"fdisk /dev/{disk_name}")
			static_options = input("Have you created the Partion[y/N]: ")
			if static_options == 'N':
				continue
			elif static_options == 'y':
				format_type(disk_name)
			print("Static Partition Created")	
			wait()
		
		elif option2_1 == 2:
			os.system("clear")
			os.system("fdisk -l")
			disk_name = input("Enter your disk name(e.g-sda): ")
			os.system("pvcreate /dev/{disk_name} > /dev/null")
			vg_name = input("Enter name of VG: ")
			os.system("vgcreate {vg_name} {disk_name} > /dev/null")
			lvm_name = input("Enter your LVM name: ")
			lvm_size = input("Enter size of LVM: ")
			os.system(f"lvcreate --size {lvm_size} --name {lvm_name} {vg_name}")
			format_type(disk_name)
			print("LVM Partition Created")	
			wait()
				
		elif option2_1 == 3:
			break
		elif option2_1 == 4:
			exit()
		else:
			print("Wrong Output\nTry again...\n")
			continue

def change_partitions():
	while True:
		os.system("clear")
		os.system("tput bold")
		os.system("tput setaf 2")
		print("""
		Add or Delete Storage in Existing Partition

		Press 1. Add Storage in Static Partition
		Press 2. Increase or Decrease Storage in LVM
		Press 3. Go To Main Menu
		Press 4. Exit
		""")
		os.system("tput sgr 0")
		option3_1 = int(input("Enter Your Choice: "))

		if option3_1 == 1:
			os.system("clear")
			os.system("fdisk -l")
			print("\nPlease Make Sure Not To Remove The Signature")
			disk_name = input("Enter your disk name(e.g-sda): ")
			os.system(f"fdisk /dev/{disk_name}")
			os.system(f"resize2fs /dev/{disk_name} > /dev/null")
			print("Storage added in Static Partition")
			wait()

		elif option3_1 == 2:
			os.system("clear")
			os.system("tput bold")
			os.system("tput setaf 5")
			print("""
			Increase or Decrease Storage in LVM

			Press 1. Increase LVM Partition Size
			Press 2. Decrease LVM Partition Size
			Press 3. Back
			""")
			os.system("tput sgr 0")
			option3_1_2 = int(input("Enter Your Choice: "))

			if option3_1_2 == 1:
				os.system("clear")
				os.system("tput bold")
				os.system("tput setaf 5")
				print("""
				Increase LVM Storage in Linux

				Press 1: Increase VG Size
				Press 2: Increase LV Size
				Press 3: Back
				""")
				os.system("tput sgr 0")
				lvm_options = int(input("Enter Your Choice: "))

				if lvm_options == 1:
					os.system("clear")
					pv = input("Do You Have a PV?(Y or N): ")
						
					if pv == 'Y':
						os.system("clear")
						os.system("pvdisplay")
						pv = input("Enter Your PV Name: ")
						os.system("vgdisplay")	
						vg = input("Enter Your VG Name: ")
						os.system(f"vgextend {vg} {pv}")
						print("VG Size Increased")
						wait()

					elif pv == 'N':
						os.system("clear")
						os.system("fdisk -l")
						disk_name = input("Enter your disk name(e.g-sda): ")
						os.system("pvcreate /dev/{disk_name} > /dev/null")
						os.system("vgdisplay")	
						vg = input("Enter Your VG Name: ")
						os.system(f"vgextend {vg} {disk_name}")
						print("LV Size Increased")
						wait()

					else:
						print("Wrong Output\nTry again...\n")

				elif lvm_options == 2:
					os.system("clear")
					os.system("vgdisplay")
					vg = input("Enter Your VG Name: ")
					os.system("lvdisplay")
					lv = input("Enter Your LV Name: ")
					lvm_size = input("Enter increased size of LVM: ")
					os.system("lvextent -r --size +{lvm_size} /dev/{vg}/{lv}")

				elif lvm_options == 3:
					continue
						
			elif option3_1_2 == 2:
				os.system("clear")
				os.system("tput bold")
				os.system("tput setaf 5")
				print("""
				Decrease LVM Storage in Linux

				Press 1: Decrease VG Size
				Press 2: Decrease LV Size
				Press 3: Back
				""")
				os.system("tput sgr 0")
				lvm_options = int(input("Enter Your Choice: "))

				if lvm_options == 1:
					os.system("clear")
					os.system("tput setaf 1")
					print("Warning: Thats Not a Good Practice Make Sure You First Create a Backup Before Do this")
					os.system("tput setaf 7 ")
					input("Enter To Continue...")
					os.system("clear")
					print(""" Note: There is some points remember before do this 
					1. Make sure you have attached atleast 2 PV in a VG.
					2. One of them is capable to copy all of the data of other.
					""")
					os.system("pvs -o +pv_used")
					vg_name = input("Enter your VG name: ")
					pv_remove = input("Enter your PV name which you want to remove: ")
					os.system("pvmove --alloc anywhere {pv_remove}> /dev/null")
					os.system("vgremove {vg_name} {pv_remove}")
					print("VG  Size Decreased")
					wait()


				elif lvm_options == 2:
					os.system("clear")
					os.system("tput setaf 1")
					print("Warning: Thats Not a Good Practice Make Sure You First Create a Backup Before Do this")
					os.system("tput setaf 7 ")
					input("Enter To Continue...")
					os.system("clear")
					os.system("lvdisplay")
					lv_path = input("Enter Your LV path: ")	
					lv_size = int(input("Enter Your Final Size: "))
					os.system(f"lvreduce -r --size {lv_size} {lv_path}")
					print("LV  Size Decreased")
					wait()
					
				elif lvm_options == 3:
					continue

			elif option3_1_2 == 3:
				continue
							
		elif option3_1 == 3:
			break
		elif option3_1 == 4:
			exit()
		else:
			print("Wrong Output\nTry again...\n")
			continue


def partition():
	while True:
		os.system("clear")
		figlet("Partitions","Banner3-D",3)
		os.system("tput bold")
		os.system("tput setaf 2")
		print("""
		Which Service You Want To Use?

		Press 1. Check about Your Partion Tables
		Press 2. Create a New Partition
		Press 3. Add or Delete Storage in Existing Partition
		Press 4. To See all Mounted Partitions
		Press 5. To Mount a Partition 
		Press 6. Exit
		""")
		os.system("tput sgr 0")
		channel = int(input("Enter Your Choice: "))

		if channel == 1:
			os.system("fdisk -l")
			input("\nPress any key to continue...")
			os.system("clear")
		elif channel == 2:
			create_partition()

		elif channel == 3:
			change_partitions()
				
		elif channel == 4:
			os.system("clear")
			os.system("df -hT")
			wait()

		elif channel == 5:
			os.system("clear")
			disk_name = input("Enter your disk name(e.g-sda1): ")
			mountpoint(disk_name)
			wait()

		elif channel == 6:
			os.system("tput bold")
			os.system("tput setaf 1")
			print("Bye....")
			os.system("tput sgr 0")
			exit()

		else:
			print("Wrong Output\nTry again...\n")



i = 1
while True:
	password = getpass.getpass("Enter the password: ")
	passwd = "project"

	if passwd == password:
		os.system("clear")
		partition()
		break
	elif passwd != password:
		print("The provided password is incorrect")
		i+=1
		if i<=3:
			print("Try again...")
			os.system("sleep 3")
			os.system("clear")
		elif i<=4:
			print("Too many incorrect attempts\nbye")
			exit()