import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Crime alert in D.C.')

query_dt=st.date_input("When do you want to know?")
print(query_dt)

# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))
# st.table(dataframe)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4, 5, 6, 7],
#     })

# option = st.selectbox(
#     'Which day of the week you want to hangout in Washington D.C.?',
#      df['first column'])

# 'You selected: ', option
# question = st.text_input("What do you want to know?")

# if question is not None and question != "":
#     st.write("Hightlight:\n", question)
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#display a map
# fig, ax1=plt.subplots()
# ax1.plot(df['first column'])
# st.pyplot(fig)
# plt.close()