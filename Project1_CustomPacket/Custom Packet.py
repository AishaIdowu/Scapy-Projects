from scapy.all import *

# Create an IP layer
ip_packet = IP()
ip_packet.dst = '8.8.8.8' #Destination IP (Google's DNS)
ip_packet.src = '192.168.144.108'  #Source IP (Spoofed or yur local IP)
ip_packet.show() # Display the IP Packets details

# Create a TCP layer
tcp_layer = TCP()
tcp_layer.dport = 80 # Destination port (HTTP)
tcp_layer.sport = 12345 # Source port (Random)
tcp_layer.flags = "S" # SYN flag for initiating a connection

# Create an Ethernet Layer
EthernetFrame = Ether()

# Create a payload
payload = Raw(load="Hello, this is a custom payload")

# Combine layers together
myPacket = EthernetFrame/ip_packet/tcp_layer/payload

# Display the packet
print('Packet created:')
myPacket.show()

# Send the packet
sendp(myPacket)

#Save Packet to file
wrpcap("custom_packet.pcap", [myPacket])
print("Packet saved to custom_packet")