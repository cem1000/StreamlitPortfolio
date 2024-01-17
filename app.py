import streamlit as st


st.title('My Streamlit Portfolio')

# creating cols

col1, col2, col3 = st.columns(3)

# App 1 - SQL Code Where Items App
with col1:
    st.subheader('SQL Code Where Items App')
    st.write('Streamlines SQL query building with efficient multi-value integration for where clause. If you are in a hurry and no time to format that long list of values in excel, dump them in here!')
    st.markdown('[Go to app](https://cem1000-sql-code-where-items-app-u1x6zr.streamlit.app/)')
    st.markdown('[Github URL](https://github.com/cem1000/sql_code_where_items)')


# App 2 - Hotel Discovery Ireland
with col2:
    st.subheader('Hotel Discovery Ireland')
    st.write('Utilizes haversine formula and Folium maps for exploring nearby hotels. Demonstrates folium map package usage and creation of programming requiring functions in backend connected to a dashboard.')
    st.markdown('[Go to app](https://hoteldiscoveryireland.streamlit.app/)')
    st.markdown('[Github URL](https://github.com/cem1000/HotelDiscovery)')

# App 3 - Dublin Bikes
with col3:
    st.subheader('Dublin Bikes')
    st.write('Enables Dublin bike users to efficiently plan their bike journey ahead of time using historical data. Data is derived from smart Dublin API providers.')
    st.markdown('[Go to app](https://dublinbikes.streamlit.app/)')
    st.markdown('[Github URL](https://github.com/cem1000/DublinBikeAvailability)')

# About Me section
st.header('About Me')
st.write('I like building streamlit apps :)')
