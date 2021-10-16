import numpy as np
## Pathced Conics Model Used

def hohman_dv(mu,r1,r2):
    dv = np.abs(np.sqrt(mu/r1)*(np.sqrt(2*r2/(r1+r2)) - 1) + np.sqrt(mu/r2)*(1-np.sqrt(2*r1/(r1+r2))))
    return dv

mu_mars = 4.28284e13 #m3/s2
mu_sun = 1.32712e20 #m3/s2
r_mars = 249200000e3#229000000e3#206700000e3 #m, lower bound
r_phobos = 9377e3 #m
r_deimos = 23460e3 #m
T = 1.02749*5*24*60*60 #period, in s

v_phobos = np.sqrt(mu_mars/r_phobos)
v_deimos = np.sqrt(mu_mars/r_deimos)

dv_phobos_deimos = hohman_dv(mu_mars,r_phobos,r_deimos)
dv_deimos_phobos = hohman_dv(mu_mars,r_deimos,r_phobos)
print("Delta-V to get from Phobos to Deimos: " + str(dv_phobos_deimos) + " m/s")
print("Delta-V to get from Deimos to Phobos: " + str(dv_deimos_phobos) + " m/s")


n = 2*np.pi/T
a_io = (mu_mars/n**2)**(1/3)
print("Semi Major Axis of Initial Orbit: " + str(a_io/1000) + " km")
SOI_mars = r_mars*(mu_mars/mu_sun)**(2/5)
print("SOI of Mars: " + str(SOI_mars/1000) + " km")

## Assume Circular Orbit for initial EEV position
v_EEV = np.sqrt(mu_mars/a_io)
print("EEV orbit velocity (circular): " + str(v_EEV) + " m/s")
dv_EEV_deimos = hohman_dv(mu_mars,a_io,r_deimos)
print("Delta-V to get from initial orbit to Deimos: " + str(dv_EEV_deimos) + " m/s")
dv_EEV_phobos = hohman_dv(mu_mars,a_io,r_phobos)
print("Delta-V to get from initial orbit to Phobos: " + str(dv_EEV_phobos) + " m/s")

dv_EEV_deimos_phobos_DST = dv_EEV_deimos + dv_deimos_phobos + dv_EEV_phobos
dv_EEV_phobos_deimos_DST = dv_EEV_phobos + dv_phobos_deimos + dv_EEV_deimos
print("Delta-V for first planet of Deimos: " + str(dv_EEV_deimos_phobos_DST) + " m/s")
print("Delta-V for first planet of Phobos: " + str(dv_EEV_phobos_deimos_DST) + " m/s")
