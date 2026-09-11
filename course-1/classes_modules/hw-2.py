def date_of_birth(ssn):
    y = int(ssn[4:6])
    if ssn[6] == "+": y += 1800
    if ssn[6] == "-": y += 1900
    if ssn[6] == "A": y += 2000
    m = int(ssn[2:4])
    d = int(ssn[:2])
    return (y, m, d)