import pandas as pd

df = pd.DataFrame([
    ["Max Operating Temperature", 100, "°C", "Maximum continuous temperature the material can withstand"],
    ["Peak Tolerance", 120, "°C", "Short-duration peak temperature limit"],
    ["Density", 2.70, "g/cm^3", "Material density"],
    ["Thermal Conductivity", 167, "W/m·K", "Heat transfer efficiency"],
    ["Tensile Strength", 310, "MPa", "Ultimate tensile strength"],
    ["Yield Strength", 276, "MPa", "Stress at which deformation occurs"],
    ["Application", "Heat shields, casings", "", "Engineering use cases"],
], columns=["Parameter", "Value", "Unit", "Description"])

df.to_csv("parameters.csv", index=False)
