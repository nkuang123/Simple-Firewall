# Author: Norman Kuang
# Description: Implementation of a Rule class.


class Rule:
    def __init__(self):
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

        def ip_to_byte_array(ip):
            ip_split = ip.split(".")
            ip_split = [int(byte) for byte in ip_split]
            return bytes(ip_split)

        if (ip_addr in self.ips_discrete):
            return True

        for ip_range in self.ips_range:
            low_ip, high_ip = ip_range.split("-")

            low_ip_byte = ip_to_byte_array(low_ip)
            high_ip_byte = ip_to_byte_array(high_ip)
            ip_addr_byte = ip_to_byte_array(ip_addr)

            if low_ip_byte <= ip_addr_byte <= high_ip_byte:
                return True

        return False

    def __repr__(self):
        return "Directions: {}, Protocols: {}, Discrete IPS: {}, Range IPS: {}".format(
            self.directions,
            self.protocols,
            self.ips_discrete,
            self.ips_range)
