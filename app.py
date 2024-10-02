import streamlit as st
import toonify

st.title('Toonify!')
st.text("Upload a photo and see what you'd look like in your own toon character.")

uploaded_file = st.file_uploader('upload image')

st.markdown('##') 

if uploaded_file is not None:
    
    image = toonify.to_img(uploaded_file)
    

    col1, col2, col3 = st.columns(3)
    
    with col3:
        st.markdown("<p style='text-align: center;'>parameters</p>", unsafe_allow_html=True)
        TOTAL_COLORS = st.slider("Color",min_value= 1,max_value= 10, value= 1)
        LINE_WIDTH = st.slider("Line", min_value = 3, max_value = 21, value= 3,step = 2)
        BLUR_VALUE = st.slider("Blur", min_value = 1, max_value = 11, value= 1,step = 2)

    
    with col1:
        st.markdown("<p style='text-align: center;'>original image</p>", unsafe_allow_html=True)
        st.image(image, channels="RGB")
    with col2:
        st.markdown("<p style='text-align: center;'>toonify image</p>", unsafe_allow_html=True)
        output_image = toonify.generate(image,TOTAL_COLORS,LINE_WIDTH,BLUR_VALUE)
        st.image(output_image, channels="BGR")
    
    

        