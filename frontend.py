import streamlit as st
import streamlit as st
from PIL import Image
from app1 import a1
from app3 import a3


from app5 import a5
from app6 import a6
from app7 import a7
from app8 import a8
from app9 import a9
from app10 import a10
from app11 import a11
from app12 import a12
from app13 import a13
from app14 import a14
from app15 import a15

# Define a function to display the "Start Here" page
def start_here():
    image=Image.open("logo1.png")  # Add this line to display the image
    col1, col2, col3 = st.columns([1, 2, 1])

# Place the image in the center column
    with col1:
        st.write("")

    with col2:
        st.image(image, caption='', use_column_width=True)

    with col3:
        st.write("")
    st.markdown("<p style='text-align: center;'>Click the button below to get started.</p>", unsafe_allow_html=True)
    if st.button('Start Here', key='start_here_button', use_container_width=True):
        st.session_state.page = 'Main Menu'

# Define a function to display the main menu
def main_menu():
    image = Image.open("logo1.png")
    col1, col2, col3 = st.columns([1, 2, 1])

# Place the image in the center column
    with col1:
        st.write("")

    with col2:
        st.image(image, caption='', use_column_width=True)

    with col3:
        st.write("")
    st.text_input("Search Module...")

    # Create columns for the buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('Qualification Questionnaire'):
            st.session_state.page = 'Qualification Questionnaire'

        if st.button('Landscape Detail Questions'):
            st.session_state.page = 'Landscape Detail Questions'

        if st.button('Finance'):
            st.session_state.page = 'Finance'
        
    with col2:
        if st.button('Organization Management'):
            st.session_state.page = 'Quality Management'
        if st.button('Sales and Distribution'):
            st.session_state.page = 'Sales and Distribution'
        if st.button('Human Resources'):
            st.session_state.page = 'Human Resources'

    with col3:
        if st.button('Material Management'):
            st.session_state.page = 'Material Management'
        if st.button('Warehouse Management'):
            st.session_state.page = 'Warehouse Management'
        if st.button('Transportation Management'):
            st.session_state.page = 'Transportation Management'
    
    # Create a new row for the remaining buttons
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button('Production Planning'):
            st.session_state.page = 'Production Planning'

    with col5:
        if st.button('Plant Maintenance'):
            st.session_state.page = 'Plant Maintenance'
        
    with col6:
        if st.button('Controlling, Treasury'):
            st.session_state.page = 'Controlling, Treasury'
    
    col7, col8, col9 = st.columns(3)
    with col7:
        if st.button('Project Systems'):
            st.session_state.page = 'Project Systems'
    with col8:
        if st.button('Quality Management'):
            st.session_state.page = 'Organization Management'

# Check if 'page' is in session state
if 'page' not in st.session_state:
    st.session_state.page = 'Start Here'

# Define the content for each page
if st.session_state.page == 'Start Here':
    start_here()
elif st.session_state.page == 'Qualification Questionnaire':
    a1()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Main Menu':
    main_menu()

elif st.session_state.page == 'Landscape Detail Questions':
    a3()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'
elif st.session_state.page == 'Transportation Management':
    a10()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'
#elif st.session_state.page == 'Organization Management':
    #a4()
    #if st.button("Home"):
        #st.session_state.page = 'Main Menu'
elif st.session_state.page == 'Controlling, Treasury':
    a13()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'
elif st.session_state.page == 'Material Management':
    a5()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Production Planning':
    a6()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Quality Management':
    a7()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Sales and Distribution':
    a9()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Warehouse Management':
    a8()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Plant Maintenance':
    a11()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Finance':
    a12()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

elif st.session_state.page == 'Human Resources':
    a14()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'
elif st.session_state.page == 'Project Systems':
    a15()
    if st.button("Home"):
        st.session_state.page = 'Main Menu'

# Styling the sidebar and buttons
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #f0f0f5;
        }
        .css-1d391kg {
            font-size: 18px;
        }
        div.stButton > button {
            width: 100%;
            height: 50px;
            margin: 10px 0;
            font-size: 16px;
        }
        #start_here_button {
            background-color: yellow;
        }
    </style>
""", unsafe_allow_html=True)
