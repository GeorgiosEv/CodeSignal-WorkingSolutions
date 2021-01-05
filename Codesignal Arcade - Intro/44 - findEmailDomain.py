def findEmailDomain(address):
    address_spl = address.split("@")
    c = [ i for i in address_spl ]
    if len(address_spl) == 2:
        return c[1]
    if len(address_spl) == 3:
        return c[2]