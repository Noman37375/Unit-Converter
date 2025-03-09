import streamlit as st
import pint
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components

# Initialize the unit registry
ureg = pint.UnitRegistry()

# Set page config
st.set_page_config(
    page_title="Smart Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS with enhanced styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
        font-family: 'Roboto', sans-serif;
    }
    
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    .title-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #4CAF50 0%, #2196F3 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .converter-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox {
        margin-bottom: 1.5rem;
    }
    
    .stNumberInput {
        margin-bottom: 1.5rem;
    }
    
    .result-container {
        background: #e8f5e9;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 2rem;
        text-align: center;
    }
    
    .footer {
        text-align: center;
        padding: 1rem;
        color: #666;
        font-size: 0.9rem;
        margin-top: 2rem;
    }
    
    /* Custom styling for select boxes */
    .stSelectbox > div > div {
        background-color: white;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    /* Custom styling for number input */
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem;
    }
    
    /* Category icons */
    .category-icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title with enhanced design
st.markdown("""
    <div class="title-container">
        <h1>🔄 Smart Unit Converter</h1>
        <p style='font-size: 1.2rem; opacity: 0.9;'>Convert between different units with ease</p>
    </div>
""", unsafe_allow_html=True)

# Define unit categories with icons
UNIT_CATEGORIES = {
    "📏 Length": ["meters", "kilometers", "miles", "feet", "inches", "centimeters"],
    "⚖️ Mass": ["kilograms", "grams", "pounds", "ounces"],
    "🌡️ Temperature": ["celsius", "fahrenheit", "kelvin"],
    "⏱️ Time": ["seconds", "minutes", "hours", "days"],
    "🧊 Volume": ["liters", "milliliters", "gallons", "cubic_meters"],
    "📐 Area": ["square_meters", "square_feet", "square_kilometers", "hectares", "acres"],
}

# Main converter container
st.markdown('<div class="converter-container">', unsafe_allow_html=True)

# Create two columns for input and output with better spacing
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### From")
    # Unit category selection
    category = st.selectbox(
        "Select Category",
        list(UNIT_CATEGORIES.keys()),
        key="from_category",
        help="Choose the category of measurement"
    )
    
    # Unit selection
    from_unit = st.selectbox(
        "From Unit",
        UNIT_CATEGORIES[category.split(" ")[1]],
        key="from_unit",
        help="Choose the unit to convert from"
    )
    
    # Input value with better styling
    value = st.number_input(
        "Enter Value",
        value=1.0,
        key="input_value",
        help="Enter the value to convert"
    )

with col2:
    st.markdown("### To")
    # Unit selection
    to_unit = st.selectbox(
        "To Unit",
        UNIT_CATEGORIES[category.split(" ")[1]],
        key="to_unit",
        help="Choose the unit to convert to"
    )

# Perform conversion
try:
    # Create quantities with units
    from_value = value * ureg(from_unit)
    
    # Convert to target unit
    to_value = from_value.to(to_unit)
    
    # Display result with enhanced styling
    st.markdown('<div class="result-container">', unsafe_allow_html=True)
    st.markdown("### Result")
    
    # Format the result with better presentation
    formatted_result = f"""
    <div style='font-size: 1.5rem; font-weight: 500; color: #2e7d32;'>
        {value:,.4g} {from_unit} = {to_value.magnitude:,.4g} {to_unit}
    </div>
    """
    st.markdown(formatted_result, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
except pint.errors.DimensionalityError:
    st.error("⚠️ Cannot convert between these units. Please check your selection.")
except Exception as e:
    st.error(f"⚠️ An error occurred: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# Enhanced footer with additional information
st.markdown("""
    <div class="footer">
        <p>This unit converter supports various measurement categories:</p>
        <p style='margin-top: 0.5rem;'>
            📏 Length • ⚖️ Mass • 🌡️ Temperature • ⏱️ Time • 🧊 Volume • 📐 Area
        </p>
        <p style='margin-top: 1rem; font-size: 0.8rem; opacity: 0.8;'>
            Built with Streamlit • Powered by Pint
        </p>
    </div>
""", unsafe_allow_html=True) 
