import os
import getpass	

def mountpoint(disk_name):
	mount = input("Enter your mount point: ")
	os.system(f"mount /dev/{disk_name} {mount}")

def format_type(disk_name):
				print("""Choose The Format Type
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


def partition():
	while True:
		print(""" Which Service You Want To Use?
		Press 1. Check about Your Partion Tables
		Press 2. Create a New Partition
		Press 3. Add or Delete Storage in Existing Partition
		Press 4. To See all Mounted Partitions
		Press 5. To Mount a Partition 
		Press 6. Exit
		""")
		channel = int(input("Enter Your Choice: "))

		if channel == 1:
			os.system("fdisk -l")
			input("\nPress any key to continue...")
			os.system("clear")
		elif channel == 2:
			os.system("clear")
			print("""Create a New Partition
			Press 1. Create Static Partition
			Press 2. Create LVM Partition
			Press 3. Go To Main Menu
			Press 4. To Exit
			""")
			option2_1 = int(input("Enter Your Choice: "))

			while True: 
				if option2_1 == 1:
					os.system("clear")
					os.system("fdisk -l")
					disk_name = input("Enter your disk name(e.g-sda): ")
					os.system(f"fdisk /dev/{disk_name}")
					format_type(disk_name)
		
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
				
				elif option2_1 == 3:
					continue
					os.system("clear")

				elif option2_1 == 4:
					exit()

				else:
					print("Wrong Output\nTry again...\n")

			if option2_1 == 4:
				print("bye")
				exit()


		elif channel == 3:
			os.system("clear")
			print(""" Add or Delete Storage in Existing Partition
			Press 1. Add Storage in Static Partition
			Press 2. Increase or Decrease Storage in LVM
			Press 3. Go To Main Menu
			""")
			option3_1 = int(input("Enter Your Choice: "))

			if option3_1 == 1:
				os.system("clear")
				os.system("fdisk -l")
				print("\nPlease Make Sure Not To Remove The Signature")
				disk_name = input("Enter your disk name(e.g-sda): ")
				os.system(f"fdisk /dev/{disk_name}")
				os.system(f"resize2fs /dev/{disk_name} > /dev/null")

			elif option3_1 == 2:
				os.system("clear")
				print(""" Increase or Decrease Storage in LVM
				Press 1. Increase LVM Partition Size
				Press 2. Decrease LVM Partition Size
				""")
				option3_1_2 = int(input("Enter Your Choice: "))

				if option3_1_2 == 1:
					os.system("clear")
					print(""" Increase LVM Storage in Linux
					Press 1: Increase VG Size
					Press 2: Increase LV Size
					""")
					lvm_options = int(input("Enter Your Choice: "))

					if lvm_options == 1:
						os.system("clear")
						pv = input("Do You Have a PV?(Y or N): ")
						
						if pv == Y:
							os.system("clear")
							os.system("pvdisplay")
							pv = input("Enter Your PV Name: ")
							os.system("vgdisplay")	
							vg = input("Enter Your VG Name: ")
							os.system(f"vgextend {vg} {pv}")

						elif pv == N:
							os.system("clear")
							os.system("fdisk -l")
							disk_name = input("Enter your disk name(e.g-sda): ")
							os.system("pvcreate /dev/{disk_name} > /dev/null")
							os.system("vgdisplay")	
							vg = input("Enter Your VG Name: ")
							os.system(f"vgextend {vg} {disk_name}")

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
						

				elif option3_1_2 == 2:
					if option3_1_2 == 1:
						os.system("clear")
						print(""" Decrease LVM Storage in Linux
						Press 1: Decrease VG Size
						Press 2: Decrease LV Size
						""")
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
							
			elif option3_1 == 3:
				continue
				os.system("clear")	
				
		elif channel == 4:
			os.system("clear")
			os.system("df -hT")

		elif channel == 5:
			os.system("clear")
			disk_name = input("Enter your disk name(e.g-sda1): ")
			mountpoint(disk_name)

		elif channel == 6:
			print("bye")
			exit

		else:
			print("Wrong Output\nTry again...\n")



i = 1
while True:
	password = getpass.getpass("Enter the password: ")
	passwd = "project"

	if passwd == password:
		os.system("clear")
		os.system("figlet -ck Welcome")
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
