import streamlit as st

def converter(value,unit_type,unit_to):
    
    types = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }
    
    key = f"{unit_type}_{unit_to}"
    
    if key in types:
        conversion = types[key]
        return value * conversion
    else:
        return "Conversion noy supported"
    
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🚀 Unit Converter</h1>", 
    unsafe_allow_html=True
)

value = st.number_input("Enter value:", min_value=1.0, step=1.0)

unit_type = st.selectbox(
    "Convert type:", ["meters", "kilometers", "grams", "kilograms"]
)

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = converter(value, unit_type, unit_to)  # Call the conversion function
    st.write(f"Converted Value: {result}")  # Display the result