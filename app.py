import streamlit as st

# Correct GitHub image links
clipnote_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/clipnote_prev.jpg'
dublin_bike_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/dublin_bike_prev.jpg'
hotel_app_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/hotel_proximity_app.jpg'
sql_app_image = 'https://raw.githubusercontent.com/cem1000/StreamlitPortfolio/main/sql_where_clause_prev.jpg'




def gallery_page():
    st.title('Portfolio')

    # Create rows of columns for the apps
    col1, col2, col3 = st.columns(3)
    
    # App 1 
    
    with col1:
        st.subheader('Dublin Bikes')
        st.image(dublin_bike_image, caption='SQL Where Clause Formatter App', use_column_width=True)
        st.write('Enables Dublin bike users to efficiently plan their bike journey ahead of time using historical data. Data is derived from smart Dublin API providers.')
        st.markdown('[Go to app](https://dublinbikes.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/DublinBikeAvailability)')
    
    
    # App 2 
    with col2:
        st.subheader('SQL Code Where Items App')
        st.image(sql_app_image, caption='SQL Where Clause Formatter App', use_column_width=True)
        st.write('Streamlines SQL query building with efficient multi-value integration for where clause. If you are in a hurry and no time to format that long list of values in excel, dump them in here!')
        st.markdown('[Go to app](https://cem1000-sql-code-where-items-app-u1x6zr.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/sql_code_where_items)')
    
    # App 3
    with col3:
        st.subheader('Hotel Discovery Ireland')
        st.image(hotel_app_image, caption='SQL Where Clause Formatter App', use_column_width=True)
        st.write('Demonstrates folium map package usage and utilisation of latitude and longitude distance calculations. Grabs hotel information from https://app.hotelbeds.com/.')
        st.markdown('[Go to app](https://hoteldiscoveryireland.streamlit.app/)')
        st.markdown('[Github URL](https://github.com/cem1000/HotelDiscovery)')
    
    # Start a new row for the next set of apps
    col4, col5, col6 = st.columns(3)
    
    # App 4 
    with col4:
        st.subheader('Clipnote')
        st.image(clipnote_image, caption='SQL Where Clause Formatter App', use_column_width=True)
        st.write('An app for summarizing YouTube videos. It allows users to understand the content of long videos quickly by providing concise summaries.')
        st.markdown('[Go to app](https://clipnote.streamlit.app/)')
        # st.markdown('[Github URL](https://github.com/cem1000/yt_summarizer)')


def about_me_page():
    st.title('About Me / Contact Me')
    # About Me section
    st.header('About Me')
    st.markdown('Hey, my name is Cem and I am a data analyst. I enjoy building streamlit apps :) Please reach out to via [LinkedIn](https://www.linkedin.com/in/cemyilmaz94/).')
    


# Set page config
st.set_page_config(page_title='My Streamlit Portfolio', layout="wide")

# Sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Select a page:', ['Portfolio', 'About Me / Contact Me'])


# Custom CSS to inject into the Streamlit app
custom_css = """
<style>
    .css-18e3th9 {
        border: 10px solid #005fcc; /* Light green color */
        border-radius: 12px;
    }
</style>
"""

# Inject custom CSS with Markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Page routing
if page == 'Portfolio':
    gallery_page()
elif page == 'About Me / Contact Me':
    about_me_page()

