import streamlit as st

# This should be the first Streamlit function called
st.set_page_config(page_title='My Streamlit Portfolio', layout="wide")

# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a page:', ['Gallery', 'About Me / Contact Me'])

# Custom CSS to inject into the Streamlit app
custom_css = """
<style>
    /* Main app container */
    .main {
        border: 15px solid #90ee90; 
        border-radius: 12px; 
    }
    .css-1e5imcs {
        border: 2px solid #90ee90; 
        border-radius: 5px; 
    }
</style>
"""

# Inject custom CSS with Markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Gallery Page
if page == 'Gallery':
    st.title('Gallery')

    # GitHub image links
    clipnote_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/clipnote_prev.jpg'
    dublin_bike_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/dublin_bike_prev.jpg'
    hotel_app_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/hotel_prev.jpg'
    sql_app_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/sql_where_clause_prev.jpg'

    # Create rows of columns for the apps
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(sql_app_image, caption='SQL Where Clause Formatter App', use_column_width=True)
        st.markdown('[Go to app](https://cem1000-sql-code-where-items-app-u1x6zr.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/sql_code_where_items)')

    with col2:
        st.image(hotel_app_image, caption='Hotel Discovery Ireland', use_column_width=True)
        st.markdown('[Go to app](https://hoteldiscoveryireland.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/HotelDiscovery)')

    with col3:
        st.image(dublin_bike_image, caption='Dublin Bikes', use_column_width=True)
        st.markdown('[Go to app](https://dublinbikes.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/DublinBikeAvailability)')

    with col4:
        st.image(clipnote_image, caption='Clipnote', use_column_width=True)
        st.markdown('[Go to app](https://clipnote.streamlit.app/)')
        # st.markdown('[Github URL](https://github.com/cem1000/yt_summarizer)')

# About Me / Contact Me Page
elif page == 'About Me / Contact Me':
    st.title('About Me / Contact Me')
    st.markdown("""
        I am a data analyst and I enjoy building streamlit apps. 
        Please reach out to me via [LinkedIn](https://www.linkedin.com/in/cemyilmaz94/).
        
        <!-- Add more contact details or an about me description here -->
    """)
