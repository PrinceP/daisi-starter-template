import streamlit as st
from rembg import remove
from PIL import Image
import requests

def st_ui():
    '''
    Function running the Streamlit UI.
    Doesn't return anything.
    '''
    
    st.set_page_config(layout = "wide")
    st.title("Remove background")

    user_image = st.sidebar.file_uploader("Load your own image")
    if user_image is not None:
        input = Image.open(user_image)
        
    
    else:
        url = "https://raw.githubusercontent.com/danielgatis/rembg/master/examples/girl-3.jpg"
        input = Image.open(requests.get(url, stream=True).raw)
        

    st.header("Original image")
    st.image(input)

    output = remove(input)
    
    st.header("Output image")
    st.image(output)


if __name__ == "__main__":
    st_ui()


#def hello(name="Daisi"):
#  return f"Hello {name}!"
