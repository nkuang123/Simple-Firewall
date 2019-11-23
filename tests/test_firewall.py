# Author: Norman Kuang
# Unit tests for testing Firewall implementation

import unittest
from impl.firewall import Firewall


class TestFirewallMethods(unittest.TestCase):

    def test_accept_packet(self):
        # Create firewall using rules/test1.csv
        fw = Firewall("rules/test1.csv")

        # Testing rule #1 (IP Range)
        self.assertTrue(fw.accept_packet(
            "inbound", "tcp", 80, "128.34.51.255"))
        self.assertTrue(fw.accept_packet(
            "inbound", "tcp", 80, "0.0.0.0"))
        self.assertTrue(fw.accept_packet(
            "inbound", "tcp", 80, "255.255.255.254"))
        self.assertFalse(fw.accept_packet(
            "outbound", "tcp", 80, "255.255.255.254"))
        self.assertFalse(fw.accept_packet(
            "inbound", "tcp", 81, "255.255.255.254"))

        # Testing rule #2 (Port Range)
        self.assertTrue(fw.accept_packet(
            "outbound", "tcp", 10000, "192.168.10.11"))
        self.assertTrue(fw.accept_packet(
            "outbound", "tcp", 20000, "192.168.10.11"))
        self.assertTrue(fw.accept_packet(
            "outbound", "tcp", 15000, "192.168.10.11"))
        self.assertFalse(fw.accept_packet(
            "outbound", "tcp", 80, "192.168.10.11"))
        self.assertFalse(fw.accept_packet(
            "inbound", "tcp", 10000, "192.168.10.11"))

        # Testing rule #3 (Port & IP Range)
        self.assertTrue(fw.accept_packet(
            "inbound", "udp", 53, "192.168.1.1"))
        self.assertTrue(fw.accept_packet(
            "inbound", "udp", 56, "192.168.1.255"))
        self.assertTrue(fw.accept_packet(
            "inbound", "udp", 54, "192.168.2.5"))
        self.assertFalse(fw.accept_packet(
            "outbound", "udp", 53, "192.168.1.1"))
        self.assertFalse(fw.accept_packet(
            "inbound", "udp", 54, "192.168.2.6"))


if __name__ == "__main__":
    unittest.main()
