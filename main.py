import numpy as np
import random
import streamlit as st

if st.button("HI", type="primary") :
    rand = random.randint(1, 10)

    st.text(rand)
