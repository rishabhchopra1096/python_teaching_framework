# ice_cream_display.py
import streamlit as st

# UPDATED: Moved page config to be the first Streamlit command
st.set_page_config(
    page_title="Delightful Ice Cream Shop",
    page_icon="🍦",
    layout="wide"
)

# Import our ice cream logic - students can see how Python files work together
from ice_cream_data import ice_cream_flavors, add_new_flavor

# UPDATED: Enhanced custom styling with more modern and polished look
st.markdown("""
    <style>
    /* UPDATED: Global styles and fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    
    /* UPDATED: Enhanced title styling */
    .stTitle {
        font-family: 'Poppins', sans-serif;
        color: #1a1a1a;
        font-size: 3rem !important;
        font-weight: 600 !important;
        padding-bottom: 1rem;
        text-align: center;
    }
    
    /* UPDATED: Subtitle styling */
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    /* UPDATED: Enhanced card styling */
    .flavor-card {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        border: 1px solid #eee;
    }
    
    .flavor-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* UPDATED: Enhanced flavor title */
    .flavor-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
    }
    
    /* UPDATED: Price tag styling */
    .price-tag {
        background: linear-gradient(135deg, #FF6B6B, #FF8E8E);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 500;
        font-size: 1.1rem;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    /* UPDATED: Description styling */
    .flavor-description {
        color: #666;
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 1rem 0;
    }
    
    /* UPDATED: Ingredients section */
    .ingredient-list {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 15px;
        margin-top: 1rem;
        border: 1px dashed #ddd;
    }
    
    .ingredient-item {
        color: #555;
        margin: 0.3rem 0;
        font-size: 1rem;
    }
    
    /* UPDATED: Form styling */
    .create-flavor-form {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.05);
    }
    
    .form-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    /* UPDATED: Input field styling */
    .stTextInput, .stNumberInput, .stTextArea {
        margin-bottom: 1rem;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        width: 100%;
        transition: transform 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
    }
    
    /* UPDATED: Success/Error messages */
    .success-msg {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    
    .error-msg {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # UPDATED: Enhanced header section
    st.markdown('<h1 class="stTitle">🍦 Delightful Ice Cream Shop</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Discover our amazing selection of handcrafted ice cream flavors!</p>', unsafe_allow_html=True)
    
    # Create two columns with adjusted ratio
    col1, col2 = st.columns([3, 1])
    
    with col1:
        for flavor_name, details in ice_cream_flavors.items():
            st.markdown(f"""
                <div class="flavor-card">
                    <h2 class="flavor-title">{flavor_name}</h2>
                    <span class="price-tag">${details['price']:.2f}</span>
                    <p class="flavor-description">{details['description']}</p>
                    <div class="ingredient-list">
                        <strong>✨ Made with love using:</strong>
                        {''.join(f'<p class="ingredient-item">🔸 {ingredient}</p>' for ingredient in details['ingredients'])}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="create-flavor-form">', unsafe_allow_html=True)
        st.markdown('<h3 class="form-header">🆕 Create New Flavor</h3>', unsafe_allow_html=True)
        with st.form("new_flavor_form"):
            new_flavor = st.text_input("🏷️ Flavor Name")
            new_price = st.number_input("💰 Price", 
                min_value=0.0, 
                value=3.99, 
                step=0.50,
                format="%.2f")
            new_description = st.text_area("📝 Description")
            new_ingredients = st.text_input("🧂 Ingredients (comma-separated)")
            
            submit_button = st.form_submit_button("✨ Add New Flavor")
            if submit_button:
                if new_flavor and new_description and new_ingredients:
                    ingredient_list = [i.strip() for i in new_ingredients.split(',')]
                    add_new_flavor(new_flavor, new_description, new_price, ingredient_list)
                    st.markdown('<div class="success-msg">✅ New flavor added successfully!</div>', unsafe_allow_html=True)
                    st.experimental_rerun()
                else:
                    st.markdown('<div class="error-msg">❌ Please fill in all fields!</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()