# Author: Norman Kuang
# Description: Implementation of a Firewall class, whose interface contains two
# items:
#
# 1) Constructor that initializes a firewall instance based on the input CSV.
# 2) accept_packet(arg): determines if there exists a rule in the firewall
# for arg.

from rule import Rule

MAX_PORTS = 65535


class Firewall:
    def __init__(self, csv_file):
        self.port_to_rules = [Rule() for _ in range(MAX_PORTS + 1)]

        with open(csv_file, "r") as f:
            for line in f:
                # Parse each input rule.
                direction, protocol, port, ip = line.split(",")

                # Strip newline character from ip
                ip = ip.rstrip()

                # Check if ports are given in ranges.
                if ("-" in port):
                    low, hi = port.split("-")
                    for i in range(int(low), int(hi) + 1):
                        r = self.port_to_rules[i]
                        r.add_direction(direction)
                        r.add_protocol(protocol)
                        if ("-" in ip):
                            r.add_ips_range(ip)
                        else:
                            r.add_ips_discrete(ip)
                else:
                    r = self.port_to_rules[int(port)]
                    r.add_direction(direction)
                    r.add_protocol(protocol)
                    if ("-" in ip):
                        r.add_ips_range(ip)
                    else:
                        r.add_ips_discrete(ip)

    def accept_packet(self, direction, protocol, port, ip_address):
        rule = self.port_to_rules[port]
        return (rule.contains_direction(direction) and
                rule.contains_protocol(protocol) and
                rule.is_within_ip_range(ip_address))

    def print_firewall_rules(self):
        for i, port in enumerate(self.port_to_rules):
            print("Port {}, {}".format(
                i, port))

