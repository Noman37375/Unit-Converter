import streamlit as st
import pint

# Initialize the unit registry
ureg = pint.UnitRegistry()

# Set page config
st.set_page_config(
    page_title="Google Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .main {
        padding: 2rem;
    }
    .stSelectbox {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📏 Unit Converter")
st.markdown("---")

# Define unit categories and their corresponding units
UNIT_CATEGORIES = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters"],
    "Mass": ["kilograms", "grams", "pounds", "ounces"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Volume": ["liters", "milliliters", "gallons", "cubic_meters"],
    "Area": ["square_meters", "square_feet", "square_kilometers", "hectares", "acres"],
}

# Create two columns for input and output
col1, col2 = st.columns(2)

with col1:
    st.subheader("From")
    # Unit category selection
    category = st.selectbox("Select Category", list(UNIT_CATEGORIES.keys()), key="from_category")
    
    # Unit selection
    from_unit = st.selectbox("From Unit", UNIT_CATEGORIES[category], key="from_unit")
    
    # Input value
    value = st.number_input("Enter Value", value=1.0, key="input_value")

with col2:
    st.subheader("To")
    # Unit selection
    to_unit = st.selectbox("To Unit", UNIT_CATEGORIES[category], key="to_unit")

# Perform conversion
try:
    # Create quantities with units
    from_value = value * ureg(from_unit)
    
    # Convert to target unit
    to_value = from_value.to(to_unit)
    
    # Display result
    st.markdown("---")
    st.subheader("Result")
    
    # Format the result
    formatted_result = f"{value:,.4g} {from_unit} = {to_value.magnitude:,.4g} {to_unit}"
    st.success(formatted_result)
    
except pint.errors.DimensionalityError:
    st.error("Cannot convert between these units. Please check your selection.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")

# Add information footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        This unit converter supports various measurement categories including length, mass, temperature, time, volume, and area.
    </div>
""", unsafe_allow_html=True) 