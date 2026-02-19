import streamlit as st
import sqlite3
import pandas as pd
import io  # <--- New library needed

st.title("📦 BLOB Inventory Viewer")

# Connect to the BLOB database
conn = sqlite3.connect('inventory_blob.db')
c = conn.cursor()

c.execute("SELECT name, count, image_data FROM tools")
rows = c.fetchall()

if not rows:
    st.write("No items found.")
else:
    for row in rows:
        name = row[0]
        count = row[1]
        image_data = row[2]  # This is raw binary data (bytes)

        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                if image_data:
                    # Convert bytes to an image stream
                    image_stream = io.BytesIO(image_data)
                    st.image(image_stream, width=100)
                else:
                    st.write("No Image")
            
            with col2:
                st.subheader(name)
                st.write(f"Quantity: {count}")
            
            st.divider()

conn.close()