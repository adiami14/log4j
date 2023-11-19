#!/bin/env python3
from ldap3 import Server, Connection, ALL

# Connect to the LDAP server
server = Server(host='10.1.22.130', port=666, get_info=ALL)
conn = Connection(server, auto_bind=True)

# Search for the entry
base_dn = 'dc=example,dc=com'
query = '(cn=webentry)'
attributes = ['cn', 'sn', 'description', 'url']
conn.search(base_dn, query, attributes=attributes)

# Print the retrieved entry
entry = conn.entries[0]
print("Entry details:")
print(f"CN: {entry.cn}")
print(f"SN: {entry.sn}")
print(f"Description: {entry.description}")
print(f"URL: {entry.url}")

# Disconnect from the server
conn.unbind()
