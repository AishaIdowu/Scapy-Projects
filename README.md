# **Scapy-Projects**
This repository contains hands-on projects built with Scapy for network analysis, penetration testing, and cybersecurity training. Each project includes step-by-step guides for building and understanding its functionality.




## **Requirements**
- Python 3.8 or later
- Scapy library
- Linux OS
- Wireshark (optional, for packet analysis)



## Projects
1. [Packet Sniffer](Project1_PacketSniffer/README.md)



## **Getting Started**
1. Clone the repository:
   ```bash
   git clone https://github.com/AishaIdowu/Scapy-Projects.git
   cd scapy-projects

2. Install dependencies:
```bash
sudo apt install python3-scapy
```
- Navigate to any project folder.
- Read the README file of the project to understand the code.
- Run the script.


    

## **Scapy Commands**
Here’s a list of commonly used **Scapy commands** for Linux. These commands cover various aspects of Scapy, including packet crafting, sniffing, sending, and analyzing.

---

### **1. General Commands**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `scapy`                             | Launch the Scapy interactive shell.                                      |
| `ls()`                              | List all available Scapy layers.                                         |
| `ls(LayerName)`                     | List all fields in a specific layer (e.g., `ls(IP)`).                    |
| `lsc()`                             | List commonly used Scapy commands.                                       |
| `conf`                              | View and modify Scapy’s configuration.                                   |
| `conf.route`                        | Display the system's routing table.                                      |
| `conf.iface`                        | Get or set the default network interface.                                |

---

### **2. Packet Crafting**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `Ether()`                           | Create an Ethernet frame.                                                |
| `IP()`                              | Create an IP layer.                                                      |
| `TCP()`                             | Create a TCP layer.                                                      |
| `UDP()`                             | Create a UDP layer.                                                      |
| `ICMP()`                            | Create an ICMP layer.                                                    |
| `Raw(load="payload")`               | Add raw data (custom payload) to the packet.                             |
| `packet = IP(dst="8.8.8.8")/TCP()`  | Combine layers to craft a custom packet.                                 |
| `packet.show()`                     | Display the details of the packet.                                       |
| `packet.summary()`                  | Print a one-line summary of the packet.                                  |
| `hexdump(packet)`                   | Show the packet in hexadecimal format.                                   |

---

### **3. Sending Packets**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `send(packet)`                      | Send a packet at the IP layer.                                           |
| `sendp(packet)`                     | Send a packet at the Ethernet layer.                                     |
| `sr(packet)`                        | Send a packet and receive its response.                                  |
| `sr1(packet)`                       | Send a packet and return only the first response.                        |
| `send(packet, count=10)`            | Send a packet multiple times (10 times in this example).                 |
| `sendpfast(packet, iface="eth0")`   | Send packets quickly using the specified interface (e.g., `eth0`).       |

---

### **4. Packet Sniffing**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `sniff(count=10)`                   | Capture 10 packets from the default interface.                           |
| `sniff(iface="eth0", count=5)`      | Sniff 5 packets from the `eth0` interface.                               |
| `sniff(filter="tcp", count=5)`      | Sniff 5 TCP packets.                                                     |
| `sniff(prn=lambda x: x.summary())`  | Print a summary of sniffed packets in real-time.                         |
| `wrpcap("file.pcap", packets)`      | Save captured packets to a `.pcap` file.                                 |
| `rdpcap("file.pcap")`               | Read packets from a `.pcap` file.                                        |

---

### **5. Analyzing Packets**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `packet[IP]`                        | Extract the IP layer from a packet.                                      |
| `packet[IP].src`                    | Get the source IP address.                                               |
| `packet[IP].dst`                    | Get the destination IP address.                                          |
| `packet[TCP].sport`                 | Get the source port from the TCP layer.                                  |
| `packet.haslayer(ICMP)`             | Check if a packet contains an ICMP layer.                                |
| `packet.summary()`                  | Print a summary of the packet.                                           |
| `packet.show()`                     | Display detailed information about the packet.                           |

---

### **6. Advanced Operations**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `Traceroute("8.8.8.8")`             | Perform a traceroute to `8.8.8.8`.                                       |
| `ARP()`                             | Create an ARP request/reply packet.                                      |
| `ARP(op=1, pdst="192.168.1.1")`     | Create an ARP request targeting `192.168.1.1`.                           |
| `Ether()/IP()/TCP()`                | Combine Ethernet, IP, and TCP layers into a single packet.               |
| `fuzz(IP())`                        | Generate a packet with randomized fields.                                |

---

### **7. Interacting with Network Interfaces**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `get_if_list()`                     | List all available network interfaces.                                   |
| `get_if_hwaddr("eth0")`             | Get the MAC address of the `eth0` interface.                             |
| `get_working_if()`                  | Get the current working interface.                                       |

---

### **8. Debugging and Troubleshooting**
| Command                             | Description                                                              |
|-------------------------------------|--------------------------------------------------------------------------|
| `debug.show_all()`                  | Enable detailed debug information.                                       |
| `hexdump(packet)`                   | Display the hexadecimal representation of the packet.                    |
| `packet.show2()`                    | Display detailed information and resolve fields.                         |

---

