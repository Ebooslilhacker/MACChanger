import subprocess

def change_mac(interface, new_mac):
    print("[+] Cambiando Dirección MAC para " + interface + " to " + new_mac)
    

interface = input("interface > ")
new_mac = input("nuevo MAC > ") 


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether" , new_mac])
subprocess.call(["ifconfig", interface, "up"])
