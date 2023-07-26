import streamlit as st
from Modules import functions

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos) 


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my todo app.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new Todo...", 
              on_change=add_todo, key='new_todo')

print("Hello")