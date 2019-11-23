# Illumio Challenge - Simple Firewall 

**Goal**:
> Given a set of firewall rules, a network packet will be accepted by the firewall if and only if the
direction, protocol, port, and IP address match at least one of the input rules. If a rule contains
a port range, it will match all packets whose port falls within the range. If a rule contains an IP
address range, it will match all packets whose IP address falls within the range. 

**Design Thoughts**:
+ How do we want to represent the firewall rules?
	- The simplest representation is to build an array of strings, with each
	string representing a firewall rule. There are few problems with this representation. One, looking up a rule takes linear time, with does not scale well with large rulesets. Second, we'd have to do some additional parsing each time we cross-check a packet with the rule set. Memory also scales linearly with respect to the number of rules in the ruleset. 
	- Because we desire fast lookups into the ruleset, another idea is to represent the ruleset using hash tables which have constant lookup times. We can either use the port or the IP address as a key into the hash table, with each key mapping to their respective rules. 
	- Ultimately, I chose to use the port number as a key into the ruleset as 65535 possible ports is much, much less than 2<sup>32</sup> possible IP addresses, with each port number mapping to a Rule object. Because the data relationship is **integer->Rule**, we can stick to an array and index with the port number. Thus, we'll represent the firewall ruleset with an array with 65536 entries (1 for each port), with each entry containing a Rule object. In the grand scheme of things, an array with 65536 isn't too memory intensive and is fixed (doesn't scale with ruleset size).
+ What information do we need in each rule entry?
	- Each port will map to a Rule object, which will contain 4 sets, promoting fast lookup times into desired information such as supported directions, protocols, and IP addresses. IP addresses will be split into discrete (single address) and ranges (range of addresses). The Rule class will also implement methods to test whether a given direction/protocol/IP address is supported.

**Efficiency**:
+ We can access the rules of a specific port in constant time. Testing if a packet direction/protocol is supported or not also takes constant time since we stored the information in sets. The meat of the algorithm takes place in determine whether an IP address is supported, which in the worst case takes O(*k*), where *k* is number of IP address ranges supported. All in all, it takes O(*k*) to determine whether a packet is accepted by a firewall, which is not too bad. Of course, this all assumes that converting an integer to a byte array takes constant time.

**Areas Of Improvement**: 
+ If memory is not a concern, we could theoretically use a set to represent each IP address in a range of IP addresses. It would take a bit longer to process the CSV and enumerate all IP addresses within a range, but the end result is optimal efficiency of the accept_packet() method, since the IP address lookup will be constant time. This is a classic example of the tradeoff between space & time.

**Testing**: 
+ Testing was done through the `unittest` module supported by Python. First, testing was done on the Rule class to confirm functionality before implementing the Firewall class. Firewall class tests were then written afterwards using "rules/test1.csv" as the ruleset. To test, run the following command in the top-most directory:
```
> python -m unittest discover -v
```

## Teams of Interest ##
+ The teams that interest me the most are the **Platform** and **Data** teams. Specifcally for the Platform team, working directly on the system infrastructure and finding bottlenecks in the caching layer are the most intriguing to me. I'd like to acquire a deeper knowledge on how to design systems around these bottlenecks. On the Data team, I would like to work directly with the core data instructure. This includes the entire process in determining what data to extract, how to extract that data, and making it as efficient as possible. As you may notice from my comments, system design is one of the areas I am most interested in, and it would be an invaluable experience from an engineering perspective if I was given the opportunity to work on Illumio's systems. 