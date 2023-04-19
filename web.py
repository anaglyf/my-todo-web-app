import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    if len(todo) > 0:
        todo = st.session_state["new_todo"] + '\n'
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My To-Do App")
st.subheader("Designed by Alex Macnab")
st.write("This app was designed to increase your quality of life.")

for index, todo in enumerate(todos):
    unique_key = todo + str(index)
    checkbox = st.checkbox(todo, key=unique_key)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[unique_key]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a new to-do item:",
              on_change=add_todo, key='new_todo')
