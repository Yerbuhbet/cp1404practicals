HEX_COLOUR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc",
    "AntiqueWhite3": "#cdc0b0",
    "AntiqueWhite4": "#8b8378",
    "Aquamarine1": "#7fffd4",
    "Aquamarine2": "#76eec6",
    "Azure1": "#f0ffff",
    "Azure2": "#e0eeee"
}
def main():
    print("Hex Colour Lookup")
    colour_name = input("Enter a colour name (or leave blank to exit): ")
    while colour_name:
        colour_name = colour_name.capitalize()
        if colour_name in HEX_COLOUR_CODES:
            print(f"The code for {colour_name} is {HEX_COLOUR_CODES[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter another colour name (or leave blank to exit): ")


    main()
