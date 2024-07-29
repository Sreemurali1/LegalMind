import streamlit as st
from model import Model

# Initialize the model
model = Model()

# Streamlit application
st.set_page_config(page_title="LegalMind")

# Streamlit interface
st.title("LegalMind⚖️")

st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)


# Add tabs
tab1, tab2 = st.tabs(["About This Project", "Response"])

# About This Project tab
with tab1:
    st.write("""
    **LegalMind** is an AI-powered legal assistant designed to help you with your legal queries. Useful for law students, educators, and anyone interested in gaining legal insights.
    Using advanced natural language processing models, this tool can understand and provide responses to a wide range of legal questions.


    ### How to Use:
    1. Navigate to the 'Query & Response' tab.
    2. Enter your legal question or topic in the provided text area.
    3. Click on 'Get Response' to receive an AI-generated response.
    4. Ensure your question is clear and concise for the best results.

    This project is created by Sreemurali Sekar K. Feel free to connect on [LinkedIn](https://www.linkedin.com/in/sreemurali-sekar-k-84630517a/) or [GitHub](https://github.com/Sreemurali1).
    """)

# Query & Response tab
with tab2:
    user_input = st.text_area("Enter your legal question or topic:")

    if st.button("Get Response"):
        if user_input:
            with st.spinner('Generating Legal answers...'):
                response = model.get_response(user_input)
            st.write(response)
        else:
            st.warning("Please enter a question or topic to get a response.")
