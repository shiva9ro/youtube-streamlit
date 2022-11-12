import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import time

st.title("Streamlit 超入門")
st.write("Display Image")
st.write("プログレスバーの表示")
"Start!!"
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
time.sleep(0.1)

left_column,right_cloumn = st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_cloumn.write("ここは右カラム")
expander=st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")
# option = st.text_input(
#     "あなたの趣味を教えてください")
# "あなたの趣味は",option,"です"
# condition=st.slider("あなたの今の調子は？",0,100,50)
# "コンディション",condition

# if st.checkbox("Show Image"):
#     img=Image.open(r"C:\Users\ribra\Desktop\駿、咲乃、颯\sotaro.jpg")
#     st.image(img,caption="sotaro",use_column_width=True)
# df=pd.DataFrame(
#     np.random.rand(100,2)/(50,50)+(35.69,139.70),columns=["lat","lon"])
# st.map(df)