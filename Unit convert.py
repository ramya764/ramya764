import tkinter as tk
from tkinter import ttk

def convert():
    unit_type = combo_type.get()
    value = float(entry_value.get())

    if unit_type == "Length":
        convert_length(value)
    elif unit_type == "Mass":
        convert_mass(value)
    elif unit_type == "Temperature":
        convert_temperature(value)
    elif unit_type == "Time":
        convert_time(value)
    elif unit_type == "Speed":
        convert_speed(value)
    elif unit_type == "Energy":
        convert_energy(value)
    elif unit_type == "Pressure":
        convert_pressure(value)
    
    # Add more conditions for other unit types...

def convert_length(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Centimeter to Meter":
        result_label.config(text="{} cm is equal to {} m.".format(value, value / 100))
    elif conv_type == "Meter to Centimeter":
        result_label.config(text="{} m is equal to {} cm.".format(value, value * 100))
    elif conv_type == "Centimeter to INCH":
        result_label.config(text="{} cm is equal to {} inch.".format(value, value / 2.54))
    elif conv_type == "INCH to Centimeter":
        result_label.config(text="{} inch is equal to {} cm.".format(value, value * 2.54))
    elif conv_type == "Centimeter to Km":
        result_label.config(text="{} cm is equal to {} km.".format(value, value / 100000))
    elif conv_type == "KiloMetre to Cm":
        result_label.config(text="{} km is equal to {} cm.".format(value, value * 100000))
    elif conv_type == "Centimeter to Feet":
        result_label.config(text="{} cm is equal to {} feet.".format(value, value / 30.48))
    elif conv_type == "Feet to Centimeter":
        result_label.config(text="{} feet is equal to {} cm.".format(value, value * 30.48))
    elif conv_type == "Kilometre to Mile":
        result_label.config(text="{} KM is equal to {} mile".format(value, value / 1.609))
    elif conv_type == "Mile to Kilometre":
        result_label.config(text="{} mile is equal to {} KM".format(value, value * 1.609))
    elif conv_type == "Sqft to Sqmtrs":
        result_label.config(text="{} sqft is equal to {} sqmtrs".format(value,value * 0.0929))
    elif conv_type == "Sqft to Acres":
        result_label.config(text="{} sqft is equal to {} acres".format(value, value / 43560))

def convert_mass(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Gram to Kilogram":
        result_label.config(text="{} gm is equal to {} kg.".format(value, value / 1000))
    elif conv_type == "Kilogram to Gram":
        result_label.config(text="{} kg is equal to {} gm.".format(value, value * 1000))
    elif conv_type == "Kilogram to Tonne":
        result_label.config(text="{} kg is equal to {} T.".format(value, value / 1000))
    elif conv_type == "Tonne to Kilogram":
        result_label.config(text="{} T is equal to {} kg.".format(value, value * 1000))
    elif conv_type == "Milligram to Kilogram":
        result_label.config(text="{} mg is equal to {} kg.".format(value, value / 1000000))
    elif conv_type == "Kilogram to Milligram":
        result_label.config(text="{} kg is equal to {} mg.".format(value, value * 1000000))
    elif conv_type == "Milligram to Gram":
        result_label.config(text="{} mg is equal to {} gm.".format(value, value / 1000))
    elif conv_type == "Gram to Milligram":
        result_label.config(text="{} gm is equal to {} mg.".format(value, value * 1000))
    elif conv_type == "kilogram to pound":
        result_label.config(text="{} kg is equal to {} pound".format(value, value * 2.20462))
    elif conv_type == "pound to Kilogram":
        result_label.config(text="{} pound is equal to {} kg".format(value, value / 2.20462))
    elif conv_type == "Micrograms to gram":
        result_label.config(text="{} microg is equal to {} gm".format(value, value / 1e+6))
    elif conv_type == "Micrograms to Kg":
        result_label.config(text="{} microg is equal to {} kg".format(value, value / 1e+9))

def convert_temperature(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Celsius to Fahrenheit": 
        result_label.config(text="{} C is equal to {} F.".format(value, (value * 9/5) + 32))
    elif conv_type == "Celsius to Kelvin":
        result_label.config(text="{} C is equal to {} K.".format(value, value + 273.15))
    elif conv_type == "Fahrenheit to Celsius":
        result_label.config(text="{} F is equal to {} C.".format(value, (value - 32) * 5/9))
    elif conv_type == "Fahrenheit to Kelvin":
        result_label.config(text="{} F is equal to {} K.".format(value, (value - 32) * 5/9 + 273.15))
    elif conv_type == "Kelvin to Celsius":
        result_label.config(text="{} K is equal to {} C.".format(value, value - 273.15))
    elif conv_type == "Kelvin to Fahrenheit":
        result_label.config(text="{} K is equal to {} C.".format(value, (value - 273.15) * 95 + 32))

def convert_time(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Second to Minute": 
        result_label.config(text="{} S is equal to {} M.".format(value, value / 60))
    elif conv_type == "Minute to Second":
        result_label.config(text="{} M is equal to {} S.".format(value, value * 60))
    elif conv_type == "Second to Hour":
        result_label.config(text="{} S is equal to {} H.".format(value, value / 3600))
    elif conv_type == "Minute to Hour":
        result_label.config(text="{} M is equal to {} H.".format(value, value / 60))
    elif conv_type == "Hour to Minute":
        result_label.config(text="{} H is equal to {} M.".format(value, value * 60))
    elif conv_type == "Day to Hour":
        result_label.config(text="{} day is equal to {} H.".format(value, value * 24))
    elif conv_type == "Hour to Day":
        result_label.config(text="{} H is equal to {} day.".format(value, value / 24))

def convert_speed(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Mile/hour to Km/hour": 
        result_label.config(text="{} Ml is equal to {} Km.".format(value, value * 1.609))
    elif conv_type == "Km/hour to Mile/hour":
        result_label.config(text="{} Km is equal to {} Ml.".format(value, value / 1.609))
    elif conv_type == "Mile/hour to Meter/Sec":
        result_label.config(text="{} Ml is equal to {} M.".format(value, value / 2.237))
    elif conv_type == "Meter/Sec to Mile/hour":
        result_label.config(text="{} M is equal to {} Ml.".format(value, value * 2.237))
    elif conv_type == "Km/hour to Meter/Sec":
        result_label.config(text="{} Km is equal to {} M.".format(value, value / 3.6))
    elif conv_type == "Meter/Sec to Km/hour":
        result_label.config(text="{} M is equal to {} Km.".format(value, value * 3.6))
    

def convert_energy(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Joule to Kilojoule": 
        result_label.config(text="{} J is equal to {} Kj.".format(value, value / 1000))
    elif conv_type == "Kilojoule to Joule":
        result_label.config(text="{} Kj is equal to {} J.".format(value, value * 1000))
    elif conv_type == "Joule to Kilocalorie":
        result_label.config(text="{} J is equal to {} Kc.".format(value, value / 4184))
    elif conv_type == "Kilocalorie to Joule":
        result_label.config(text="{} MKc is equal to {} J.".format(value, value * 4184))
    elif conv_type == "Kilojoule to Kilocalorie":
        result_label.config(text="{} Kj is equal to {} Kc.".format(value, value / 4.184))
    elif conv_type == "Kilocalorie to Kilojoule":
        result_label.config(text="{} Kc is equal to {} Kj.".format(value, value * 4.184))

def convert_pressure(value):
    conv_type = combo_conversion_type.get()

    if conv_type == "Bar to Pascal": 
        result_label.config(text="{} Bar is equal to {} P.".format(value, value * 100000))
    elif conv_type == "Bar to Std atmosphere":
        result_label.config(text="{} Bar is equal to {} atm.".format(value, value / 1.013))
    elif conv_type == "Pascal to Bar":
        result_label.config(text="{} P is equal to {} Bar.".format(value, value / 100000))
    elif conv_type == "Pascal to Std atmosphere":
        result_label.config(text="{} P is equal to {} atm.".format(value, value / 101300))
    elif conv_type == "Std atmosphere to Pascal":
        result_label.config(text="{} atm is equal to {} P.".format(value, value * 101300))
    elif conv_type == "Std atmosphere to Bar":
        result_label.config(text="{} atm is equal to {} Bar.".format(value, value * 1.013))
    
# GUI setup
root = tk.Tk()
root.title("Unit Converter")

# Type of conversion dropdown
label_type = ttk.Label(root, text="Select Type:")
label_type.grid(row=0, column=0, padx=10, pady=10, sticky="w")

types = ["Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure"]
combo_type = ttk.Combobox(root, values=types)
combo_type.grid(row=0, column=1, padx=10, pady=10)

# Conversion type dropdown
label_conversion_type = ttk.Label(root, text="Conversion Type:")
label_conversion_type.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# The options in the second ComboBox will be updated based on the selection in the first ComboBox
conversion_type_options = {
    "Length": ["Centimeter to Meter", "Meter to Centimeter", "Centimeter to INCH", "INCH to Centimeter","Centimeter to Km","KiloMetre to Cm","Centimeter to Feet","Feet to Centimeter","Kilometre to Mile","Mile to Kilometre","Sqft to Sqmtrs","Sqft to Acres"],
    "Mass": ["Gram to Kilogram", "Kilogram to Gram", "Kilogram to Tonne", "Tonne to Kilogram","Milligram to Kilogram","Kilogram to Milligram","Milligram to Gram","Gram to Milligram","kilogram to pound","pound to Kilogram","Micrograms to gram","Micrograms to Kg"],
    "Temperature": ["Celsius to Fahrenheit","Celsius to Kelvin","Fahrenheit to Celsius","Fahrenheit to Kelvin","Kelvin to Celsius","Kelvin to Fahrenheit"],
    "Time" : ["Second to Minute","Minute to Second","Second to Hour","Minute to Hour","Hour to Minute","Day to Hour","Hour to Day"],
    "Speed" : ["Mile/hour to Km/hour","Km/hour to Mile/hour","Mile/hour to Meter/Sec","Meter/Sec to Mile/hour","Km/hour to Meter/Sec","Meter/Sec to Km/hour"],
    "Energy" : ["Joule to Kilojoule","Kilojoule to Joule","Joule to Kilocalorie","Kilocalorie to Joule","Kilojoule to Kilocalorie","Kilocalorie to Kilojoule"],
    "Pressure" : ["Bar to Pascal","Bar to Std atmosphere","Pascal to Bar","Pascal to Std atmosphere","Std atmosphere to Pascal","Std atmosphere to Bar"]
    # Add more conversion types for other unit types...
}

combo_conversion_type = ttk.Combobox(root)
combo_conversion_type.grid(row=1, column=1, padx=10, pady=10)

# Value entry
label_value = ttk.Label(root, text="Enter Value:")
label_value.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_value = ttk.Entry(root)
entry_value.grid(row=2, column=1, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

def update_conversion_types(event):
    selected_type = combo_type.get()
    combo_conversion_type['values'] = conversion_type_options.get(selected_type, [])

# Bind the update_conversion_types function to the <<ComboboxSelected>> event
combo_type.bind("<<ComboboxSelected>>", update_conversion_types)

root.mainloop()

