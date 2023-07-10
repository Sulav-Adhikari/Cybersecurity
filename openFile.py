#assigning the file with allowed ip address to a variable named import_file
import_file = "C:\\Users\\sulav\\Desktop\\google CS\\allow_list.txt"

#Assigning the ip addresses thar need to be removed in a list 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57","192.168.25.60"]

#using with to read import_file as file

with open(import_file, "r") as file:

#saving the content of import_file in a variable called text

    text = file.read().split()
#displaying the content of import_file
print("Inital allowed list\n",text)
print("\n")
#iterating for all ipaddres in remove_list
for ip_adresses in remove_list:

#when ip_adresses in remove_list match the ipaddress in allowlist removing them
    if ip_adresses in text:
        text.remove(ip_adresses)
print("Updated allowed list\n",text)


with open(import_file,"a") as file:

    file.write("\nUpdated list:\n")
    for ip_addresses in text:
        file.write(ip_addresses+"\n")

    





        

    
