import psutil
from netmiko import ConnectHandler
#netmiko used to interact with network devices requires hostname and authentication method and also need to specify the device type .
from threading import Thread

class Router_Packet_details:

    @staticmethod
    def get_packet_details():
        router = {
                "device_type":"cisco_ios",
                "ip":"sandbox-iosxe-latest-1.cisco.com",
                "username":"developer",
                "password":"C1sco12345"
                }
        net_connect = ConnectHandler(**router)#connecting to router by using ssh protocol
        network_stats = psutil.net_io_counters(pernic = False)
        #when pernic =true it return iface as keys and net statistics as values)
        #when pernic=false it returns named tuple
        print(network_stats)

        bytes_sent = getattr(network_stats, 'bytes_sent','NA')
        bytes_recv = getattr(network_stats,'bytes_recv')

        print("Bytes Sent = {0} | Bytes Received = {1}".format(bytes_sent,bytes_recv))
        net_connect.disconnect()
Route_details = Router_Packet_details
#Route_details.get_packet_details()
Thread1 = Thread(target = Route_details.get_packet_details())
Thread2 = Thread(target = Route_details.get_packet_details())
Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()