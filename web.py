import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos_local = functions.get_todos()
    todos_local.append(todo)
    functions.write_todos(todos_local)

todos = functions.get_todos()
st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

st.session_state