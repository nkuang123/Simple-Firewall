# Illumio Challenge - Simple Firewall 

**Goal**:
> Given a set of firewall rules, a network packet will be accepted by the firewall if and only if the
direction, protocol, port, and IP address match at least one of the input rules. If a rule contains
a port range, it will match all packets whose port falls within the range. If a rule contains an IP
address range, it will match all packets whose IP address falls within the range. 

**Design Thoughts**:
+ How do we want to represent the firewall rules?
	- The simplest representation is to build an array of strings, with each
	string representing a firewall rule. There are few problems with this representation. One, looking up a rule takes linear time, with does not scale well with large rulesets. Second, we'd have to do some additional parsing each time we cross-check a packet with the rule set. 
	- Because we desire fast lookups into the ruleset, another idea is to represent the ruleset using hash tables. We can either use the port or the IP address as a key into the hash table, with each key mapping to their respective rules. Ultimately, I chose to use the port number as a key into the ruleset as 65535 possible ports is much less than 2<sup>32</sup>.