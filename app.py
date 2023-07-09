import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada", layout="wide")


# --- Funcation to use a get request to pull the Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/contact_form.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
img_tiktok_for_business = Image.open("images/tiktok_for_business.png")
img_diablo4 = Image.open("images/diablo4_pic.png")



# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, I am Tanner West :wave:")
    st.title("I am a Software Engineer from Georgia")
    st.write("I am using this project to make my first website using Python and Streamlit")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Linkedin Information")
        st.write("Here is some of my Linkedin Profile")
        st.write("[Learn More - Linkedin >](https://www.linkedin.com/in/tanner-west-5147b915a/)")
    with right_column:
        st.header("Github Information")
        st.write("Here is some of my Github Profile")
        st.write("[Learn More - Github >](https://github.com/Tanthok/Python-Project-Websites)")
    
# ---- What I Do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Description of my Time at Equifax")
        st.write("##")
        st.write(
            """
            Here are a few thing about me
            -  I worked at Equifax for almost 5 year under Pradeep, and Bala.
            -  I have had a few rolls while being on the team. 
                -  Implimentation Software Engineer (Main Role).
                -  During the begining I help to build out our regression suit for a few of our features.

            """
        )
# Adding animation to the website using https://lottiefiles.com/        
    with right_column:
        st.header("Funny Note:")
        st.write(
            """
                - Add the "Push it to Production MEME"
                - Just to keep it on the fun side
                """)
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/Tanindorf@gmail.com !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/a4466c794b083ebaa25bf88fe6282bee" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()





# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_diablo4)
    with text_column:
    # Change this to your Twitch Stuff        
        st.subheader("Twitch Information")
        st.write(
            """
            I am normally Streaming on Twitch. You can find me playing Diablo 4 and Overwatch 2. Come check out the fun times, with some laughs!
            """
        )
        st.markdown("[Twitch Link...](https://www.twitch.tv/tanthok)")

    # Add your Tic Tok Stuff
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_tiktok_for_business)
        with text_column:
            st.subheader("TicTok Information")
            st.write(
                """
                You can find some of my funny antics on my TikTok, whether it is playing games or seeing my dog.
                """
            )
            st.markdown("[Watch Videos on TicTok...](https://www.tiktok.com/@tanindorf)")

