#acces by key

monthConverions={
    1:"January",
    2:"February",
    3:"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"Octomber",
    "Nov":"November",
    "Dec":"December"
}


print(monthConverions["Dec"])
print(monthConverions.get("Nov"))
print(monthConverions.get("John","Not a valid key"))