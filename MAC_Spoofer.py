import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Cambiando Dirección MAC para " + interface + " to " + new_mac)

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help=" Interfaz para cambiar dirección MAC")
parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva dirección MAC")

parser.parse_args()

interface = input("interface > ")
new_mac = input("nuevo MAC > ") 


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether" , new_mac])
subprocess.call(["ifconfig", interface, "up"])
