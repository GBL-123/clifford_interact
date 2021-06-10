import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(
    {'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]}
    )

fig,ax = plt.subplots(figsize=(6,4))
ax.plot(df["first column"],df["second column"])

option = st.selectbox(
    'Which number do you like best?',
     df['first column'],
     format_func=lambda x:"{:.2%}".format(x),
     help="help")

st.write('You selected: ', option)

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option

left_column, right_column = st.beta_columns([1,3])
pressed = left_column.button('Press me?')
if pressed:
    right_column.pyplot(fig)
