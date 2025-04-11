# file = open("data.txt") # mount memory

# print(file.read())

# file.close()
# # Memory Leaks

# with open("data.txt") as file: # using with statement -> otomatis melakukan closing dari file yang sudah berhenti untuk dibuka
#   print(file.read())
#   pass

import pandas as pd
import streamlit as st

st.title("Belajar CSV with Streamlit di Devscale ID")

# panda used when we're working with tabular data
# if the pandas has wiggly yellow line, just run the command below:
# python -m venv .venv
# source ./.venv/Scripts/activate
# pip install pandas

user_id = st.text_input("Employee ID")
name = st.text_input("Name")
job = st.text_input("Job")
salary = st.number_input("Salary", step=100)

add_button = st.button("Add Employee")

with open("data.csv") as file:
  csv = pd.read_csv(file)
  # print(csv)
  st.write("### Data Employee")
  # st.dataframe(csv)
  # change dataframe to data_editor so the data on streamlit is edit-able
  editable_data = st.data_editor(csv)
  # new button to save the edited data
  save_btn = st.button("Save Changes")
  st.write("### Line Bar for Employee")
  # set index will set the X & Y index based on column
  st.bar_chart(csv.set_index("name")["salary"])
  # the line above will display only Name & Salary based on the data
  
  if save_btn:
    editable_data.to_csv("data.csv", index=False)
    st.rerun()

  if add_button:
    # DataFrame is a class to create new row in csv. 
    # 1st argument is the value we want to insert
    # 2nd argument is the positional argument, which is a column to map of all values
    new_data = pd.DataFrame([[
      user_id, name, job, salary
    ]], columns=["id", "name", "job", "salary"])

    # merge old data in csv with new_data
    # ignore_index to make the new data continue the index 
    csv = pd.concat([csv, new_data], ignore_index=True)

    # inser the data to the csv file
    # index to False to prevent creating index on the data.csv file
    csv.to_csv("data.csv", index=False)

    # re-run the display with latest data
    st.rerun()
# to display on streamlit, just install it:
# pip install streamlit