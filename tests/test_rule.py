# Author: Norman Kuang
# Unit tests for testing Rule implementation

import unittest
from impl.rule import Rule


class TestRuleMethods(unittest.TestCase):

    def test_contains_direction(self):
        r = Rule()
        r.add_direction("inbound")
        self.assertTrue(r.contains_direction("inbound"))
        self.assertFalse(r.contains_direction("outbound"))

    def test_contains_protocol(self):
        r = Rule()
        r.add_protocol("tcp")
        self.assertTrue(r.contains_protocol("tcp"))
        self.assertFalse(r.contains_protocol("udp"))

    def test_is_within_ip_range_discrete(self):
        r = Rule()
        r.add_ips_discrete("255.0.0.1")
        r.add_ips_discrete("1.0.0.1")
        self.assertTrue(r.is_within_ip_range("1.0.0.1"))
        self.assertTrue(r.is_within_ip_range("255.0.0.1"))
        self.assertFalse(r.is_within_ip_range("1.0.0.2"))
        self.assertFalse(r.is_within_ip_range("255.0.0.2"))

    def test_is_within_ip_range_boundary(self):
        r = Rule()
        r.add_ips_range("254.255.255.254-255.0.0.1")
        self.assertTrue(r.is_within_ip_range("255.0.0.0"))
        self.assertTrue(r.is_within_ip_range("254.255.255.255"))
        self.assertFalse(r.is_within_ip_range("254.255.255.253"))
        self.assertFalse(r.is_within_ip_range("255.0.0.2"))


if __name__ == "__main__":
    unittest.main()
