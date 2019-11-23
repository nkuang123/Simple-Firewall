# Author: Norman Kuang
# Description: Implementation of a Rule class.


class Rule:
    def __init__(self):
        # Rule details implemented using sets in order to support constant
        # lookup time. IPs separated based on single addresses and address
        # ranges.
        self.directions = set()
        self.protocols = set()
        self.ips_discrete = set()
        self.ips_range = set()

    def add_direction(self, direction):
        self.directions.add(direction)

    def add_protocol(self, protocol):
        self.protocols.add(protocol)

    def add_ips_discrete(self, ip):
        self.ips_discrete.add(ip)

    def add_ips_range(self, ip_range):
        self.ips_range.add(ip_range)

    def contains_direction(self, direction):
        return direction in self.directions

    def contains_protocol(self, protocol):
        return protocol in self.protocols

    def is_within_ip_range(self, ip_addr):

        # Helper function for converting a string IP address to a byte array.
        def ip_to_byte_array(ip):
            ip_split = ip.split(".")
            ip_split = [int(byte) for byte in ip_split]
            return bytes(ip_split)

        if (ip_addr in self.ips_discrete):
            return True

        # ip_addr is not one of the discrete addresses, now we need to iterate
        # every ip range. We'll determine whether an ip_addr lies within an
        # ip range by converting each address to a byte array and comparing
        # the byte arrays.
        for ip_range in self.ips_range:
            low_ip, high_ip = ip_range.split("-")

            low_ip_byte = ip_to_byte_array(low_ip)
            high_ip_byte = ip_to_byte_array(high_ip)
            ip_addr_byte = ip_to_byte_array(ip_addr)

            if low_ip_byte <= ip_addr_byte <= high_ip_byte:
                return True

        # ip_addr is not in ips_discrete or ips_range
        return False
