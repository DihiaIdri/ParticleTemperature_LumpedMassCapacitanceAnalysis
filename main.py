import pandas as pa
from BiotAndTemperature import BiotAndTemperature

def particle_temperature():
    # remember that indexing begins at 0
    air_properties = pa.read_excel('/Users/dihiaidrici/Desktop/Big Paper Doc/BiotNumber.xlsx',sheet_name='AirData', header=1)
    air_std = air_properties.iloc[1]
    air_2000K = air_properties.iloc[6]  # Tw initial properties

    Zr_properties = pa.read_excel('/Users/dihiaidrici/Desktop/Big Paper Doc/BiotNumber.xlsx',sheet_name='ZrData', header=1)
    Zr_2000K = Zr_properties.iloc[0]
    # print(air_std)
    # print(air_2000)
    # print(Zr_vacuum)

    Uinf = 1000  # m/s
    D = 10**-6
    Zr_Air2000 = BiotAndTemperature(air_std, air_2000K, Zr_2000K, Uinf, D)
    Nu, h, Bi = Zr_Air2000.Nusselt_number(Uinf)

    t = 10**-6  # seconds
    Tt = Zr_Air2000.temperature_time_dependence(Nu, t)
    print(Nu, h, Bi, Tt)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Air properties at infinity
    particle_temperature()
