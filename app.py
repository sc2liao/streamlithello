import streamlit as st
import sqlite3
import pandas as pd
import io  # <--- New library needed

st.title("picture viewer")

# Connect to the BLOB database
conn = sqlite3.connect('picture.db')
c = conn.cursor()

c.execute("SELECT name, image_data FROM tools")
rows = c.fetchall()

if not rows:
    st.write("No items found.")
else:
    for row in rows:
        name = row[0]
        image_data = row[1]  # This is raw binary data (bytes)

        with st.container():
            col1, col2 = st.columns([1, 2])
            
            with col1:
                if image_data:
                    # Convert bytes to an image stream
                    image_stream = io.BytesIO(image_data)
                    st.image(image_stream, width=100)
                else:
                    st.write("No Image")
            
            with col2:
                st.subheader(name)
            
            st.divider()

conn.close()
