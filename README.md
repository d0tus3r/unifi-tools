This simple script downgrades unifi uaps to counter a bug in the latest firmware that intermittently blocks broadcast traffic from non-unifi DHCP servers.

usage:

python3 downgrade.py ipaddress sshpassword


Potential TODO:

-Add support for a local SSH password file to house all site SSH passwords
-include an ip/subnet range for sites to match ipaddresses to site ssh passwords to reduce arguments called on execution.
