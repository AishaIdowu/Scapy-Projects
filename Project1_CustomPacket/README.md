# **Custom Packet Crafting with Scapy**

This project demonstrates how to craft and send custom network packets using the Scapy library in Python. The script creates a packet with the following layers:

- Ethernet (Layer 2)
- IP (Layer 3)
- TCP (Layer 4)
- Raw payload (Layer 7)
It also provides the ability to save the crafted packet to a .pcap file for further analysis in tools like Wireshark.

## **Prerequisites**
Before running this script, ensure you have the following:

### **System Requirements**
- Python 3.7+
- Linux or macOS (preferred for raw socket support)
- Root or Administrator privileges (required for sending raw packets)
- Wireshark (Optional)

### **Python Libraries**
- Install the Scapy library:
````
pip install scapy
````
## **How It Works**
The script performs the following steps:

1. **Create an IP Layer:**
- Sets the destination IP (8.8.8.8, Google's DNS server).
- Sets the source IP (192.168.144.108, a local or spoofed IP).

2. **Create a TCP Layer:**
- Sets the destination port to 80 (HTTP traffic).
- Sets a random source port (12345).
- Sets the SYN flag to initiate a TCP handshake.

3. **Create an Ethernet Layer:**
- Adds an Ethernet header for Layer 2 communication.

4. **Add a Custom Payload:**
- Includes a Raw payload with the message: Hello, this is a custom payload.

5. **Combine Layers into a Packet:**
- Layers are combined in the order: Ethernet -> IP -> TCP -> Payload.

6. **Send the Packet:**
- Sends the crafted packet using sendp() (for Layer 2).

7. **Save Packet to File:**
- Saves the crafted packet to a .pcap file named custom_packet.pcap for analysis.


## **How to Run**

1. **Execute the Script**
Run the script with root privileges to send raw packets:
````
sudo python3 custom_packet.py
````
2. **Analyze the Packet**
Open the .pcap File in Wireshark:
1. Launch Wireshark.
2. Open the saved file (custom_packet.pcap).
3. Inspect the packet layers and payload.

3. **Expected Packet Structure:**
- Ethernet: Displays the MAC addresses (source/destination).
- IP: Displays source and destination IP addresses.
- TCP: Displays source/destination ports and the SYN flag.
- Raw: Displays the custom payload (Hello, this is a custom payload).

## **Notes**
1. **Root Privileges:**
- Sending raw packets requires elevated privileges.
- Use sudo when running the script.

2. **Local IP Address:**
- Update ip_packet.src to match your local IP address if not spoofing.

3. **Broadcast Warning:**
- If the destination MAC address is unknown, Scapy will send the packet as a broadcast. This is normal unless a specific MAC address is required.

4. **Firewall Rules:**
- Ensure your firewall allows outgoing packets to the destination.



