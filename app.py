import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("GenAI Streamlit App")
st.write("Hello Ariba Zafirah")
st.text("Let's start")
name = st.text_input("Enter name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}")
    

# creating charts using pandas and numpy
df = pd.DataFrame(np.random.randn(10,2),columns=['A','B'])

st.line_chart(df)
st.bar_chart(df)


# sidebar, image & video
st.sidebar.title("Navigation")
st.image(r"C:\Users\Admin\Downloads\sea.jpg",caption="Dreams")
st.video("https://www.youtube.com/watch?v=y7anELq6WFs&list=PLoBsNCgt2tGs8MdXg8bp0AeYkqk25OWrd")

# upload csv file
upload_csv = st.file_uploader("Upload a CSV file", type="csv")

if upload_csv:
    df = pd.read_csv(upload_csv)
    st.dataframe(df)


st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("**Bold**, *Italic*, 'Code' [Link](http://streamlit.io)")
st.code ("for i in range(5): print(i)", language="python")

#input components in streamlit
st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0,100)
st.selectbox("Select a fruit",["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings",["Cheese", "tomato", "olives"])
st.radio("Pick one",["option a", "option b"])
st.checkbox("I agree to the items.")


#Matplotlib integration
import matplotlib.pyplot as plt
fig, ax=plt.subplots()
ax.plot([1,2,3],[4,5,6])
st.pyplot(fig)