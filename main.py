import streamlit as st
import pandas as pd
import urllib.request
from PIL import Image, UnidentifiedImageError

st.set_page_config(layout="centered",
                   page_icon="🕹", page_title="GIF DJ")

page_bg_img = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stAppViewContainer"] {
background-image: url("https://i.ibb.co/GsQBHHq/theatre-img.png");
background-size: contain;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
[data-testid="stToolbar"] {
right: 2rem;
}
[data-testid="column"] {
background: rgba(255,255,255, 0.5);
border: 25 25 round;
}
[data-testid="column"] img:hover {
background: rgba(255,255,255, 0.5);
background-color: white;
border: 25 25 round;
}
.h1 {
color: #ffff;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Add GIFS and DJ!")

headers_style = """
<style>
h1 {
color: #FFF1E6;
}
h2 {
padding-left: 15%;
color: #FFF1E6;
}
h3 {
padding-left: 15%;
color: #FFF1E6;
}
</style>
"""

st.markdown(headers_style, unsafe_allow_html=True)

if "video" not in st.session_state:
    st.session_state.video = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmZiZDA2MWYxMTM4NGU2NWQwMzM2NDUwZmY4MjUzMWRkODM0ODk0OSZjdD1n/ASvQ3A2Q7blzq/giphy.gif"
df = pd.DataFrame(
    [
        {"name": "zoom cat",
         "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmZiZDA2MWYxMTM4NGU2NWQwMzM2NDUwZmY4MjUzMWRkODM0ODk0OSZjdD1n/ASvQ3A2Q7blzq/giphy.gif",
         "playlist": True},
        {"name": "sing cat",
         "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTk2OGMyMDBhMWMxODRiZDMwNjRhMjg5OTJmM2RiYmU2N2IyMzIxOCZjdD1n/SS97q1r1JbrUhguCeV/giphy.gif",
         "playlist": False},
        {"name": "cry cat",
         "gif": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWEyNWNmZDE2NmM1Mjc1ZDU4Nzc5OTRkMjI1MzdlNGM5ZmI0NTJjNyZjdD1n/71PLYtZUiPRg4/giphy.gif",
         "playlist": False},
    ]
)

key_variable = 0

edited_df = st.experimental_data_editor(df, num_rows="dynamic", use_container_width=True)

gif_playlist = []
gif_playlist_len = len(gif_playlist)

for i, row in edited_df.iterrows():

    if row["playlist"]:
        if not gif_playlist:
            gif_dict = {"name": row["name"], "gif": row["gif"]}
            gif_playlist.append(gif_dict)
        else:
            for gif in gif_playlist:
                if row["gif"] == gif["gif"]:
                    continue
                # if row["gif"] in gif_playlist:
                #     continue
            else:
                gif_dict = {"name": row["name"], "gif": row["gif"]}
                gif_playlist.append(gif_dict)
    if not row["playlist"]:
        for gif in gif_playlist:
            if row["gif"] == gif["gif"]:
                gif_playlist.remove(gif)
        else:
            continue


n_cols = 6
n_rows = int(1 + len(gif_playlist) / n_cols)
rows = [st.columns(n_cols) for _ in range(n_rows)]
cols = [column for row in rows for column in row]


# st.write(gif_playlist)

def update_video():
    if col_button == True:
        st.session_state.video = gif["gif"]


# @st.cache_data
# def video_buttons_update():
#     if gif_playlist:
#         for col, gif in zip(cols, gif_playlist):
#             try:
#                 urllib.request.urlretrieve(gif["gif"], f"{key_variable}.gif")
#                 im = Image.open(f"{key_variable}.gif")
#                 im.verify()
#             except ValueError:
#                 gif[
#                     "gif"] = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjVjZjEwZjQxNzVjZDg1NTE3MWQ5ZWZiM2ZkNWI4MGQxODBiMzVjNiZjdD1n/f0BaErqmljUd2/giphy.gif"
#             except UnidentifiedImageError:
#                 gif[
#                     "gif"] = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzUzNzk2NzQ1NTg4MjExOTc1MmZkZjg0ZWJhMjkzNmJiMjc1NWM1NyZjdD1n/j9XoexYMmd7LdntEK4/giphy.gif"
#             except:
#                 gif[
#                     "gif"] = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjVjZjEwZjQxNzVjZDg1NTE3MWQ5ZWZiM2ZkNWI4MGQxODBiMzVjNiZjdD1n/f0BaErqmljUd2/giphy.gif"
#
#

if gif_playlist:
    for col, gif in zip(cols, gif_playlist):
        key_variable += 1

        try:
            col_button = col.button(gif["name"], key=key_variable)
        except TypeError:
            col_button = col.button("Unamed GIF", key=key_variable)
        if col_button == True:
            st.session_state.video = gif["gif"]


col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    pass

with col2:
    try:
        image = st.image(st.session_state.video, width=500)

        # st.write(type(image))
    except NameError:
        image = st.image("https://media.giphy.com/media/I4SEHpagUfSpi/giphy.gif", width=500)
        st.warning("You need to add some gifs to the playlist...")

    except:
        image = st.image("https://media.giphy.com/media/I4SEHpagUfSpi/giphy.gif", width=500)
        st.warning("hmmm...")

with col2:
    pass

gif_styling = """
<style>
img[alt='0'] {
border: 5px solid #000000;
border-radius: 15%;
}
</style>
"""

st.markdown(gif_styling, unsafe_allow_html=True)

