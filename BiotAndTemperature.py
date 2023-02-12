import numpy as np

class BiotAndTemperature:
    def __init__(self, Inf, HotGas, Metal, Uinf, diameter):
        # All properties at the temperature of the gas at infinity
        self.Tinf = Inf.Temp
        self.rho = Inf.rho
        self.cp = Inf.cp
        self.k = Inf.ThermalK
        self.Dv = Inf.Dv
        self.Pr = Inf.Pr
        self.D = diameter

        # properties of the gas at the wall
        self.Tw = HotGas.Temp
        self.DvW = HotGas.Dv

        # Properties of the metal
        self.ks = Metal.ks
        self.rho_s = Metal.rho
        self.cp_s = Metal.cp

    def Nusselt_number(self, Uinf):
        # Whitaker. All properties are evaluated at Tinf, standard state. EXCEPT Dynamic viscosity at the wall
        print(Uinf)
        ReD = self.rho*Uinf*self.D/self.Dv
        Nu = 2 + (0.4*ReD**(0.5) + 0.06*ReD**(2/3))*(self.Pr**0.4)*(self.Dv**0.25/self.DvW**0.25)
        h = self.k*Nu/self.D
        # ks is the thermal conductivity of the metal.
        Bi = Nu*self.k/(6*self.ks)  #ratio of the resistance to conduction in the solid to the resistance to convection in the gas.

        #t = 10*10**-6
        #Tt = BiotAndTemperature.temperature_time_dependence(self, Nu, t)

        return Nu, h, Bi

    def temperature_time_dependence(self, Nu, t):
        A = np.exp(-(6*Nu*self.k)*t/(self.rho_s*self.cp_s*self.D**2))
        Tt = self.Tinf + (self.Tw - self.Tinf)*A

        return Tt
