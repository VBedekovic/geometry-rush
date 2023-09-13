def vel_kut45(vel):
    br=(vel*(2**(1/2)))/2
    return br

def vel_kut_pol45(vel):
    a=vel*0.92388   #cos(45/2)
    b=vel*0.38627   #sin(45/2)   
    return a, b

