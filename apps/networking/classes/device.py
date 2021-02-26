class device():


    def __init__(self):
        self.__hostname=""
        self.__ip=""
    
    def set_hostname(self, hostname):
        self.__hostname = hostname
    

    def set_ip(self, ip):
        self.__ip = ip

    def device_info (self):
        print("Hostname Class: ", self.__hostname, "\nIP Class: ", self.__ip)