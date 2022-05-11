import scapy.all as scapy
from scapy.compat import raw
from scapy.layers import http
from termcolor import colored

choice = int(input("Please select from the below options:"
                   "\n 1. Raw - The raw packet will be displayed on the terminal that are sent to the host"
                   "\n 2. Summary The summary of the packet will be displayed on the terminal that are sent over the "
                   "host."
                   "\n 3. Target - The Host will be displayed on the terminal where the packets are sent"
                   "\n 4. Bytes - The bytes of the packets will be displayed on the terminal that are sent to the "
                   "host."
                   "\n Please enter the selected option: "))


def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=parameter_packet, filter='tcp')


def parameter_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if choice == 1:
            print(colored(str(raw(packet)), "green"))
        elif choice == 2:
            print(colored(packet.summary(), "green"))
        elif choice == 3:
            print(colored(packet.Host, "green"))
        elif choice == 4:
            print(colored(str(bytes(packet)), "green"))
            print("\n")
        else:
            print(colored("Please enter valid number", "red"))
            return choice


sniffing('wlp2s0')
