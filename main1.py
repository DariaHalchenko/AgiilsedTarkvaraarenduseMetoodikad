#tasks=[]
#def add_task(task):
#    return tasks.append(task)

# streamlit

# def main():
#    print('1-lisada ülesande \n 2-kustuda ülesande \n 3-ülevaadata ülesanded')
#    userInput=input("Mida sa tahad? ")
#    if userInput=='1':
#        tasks=add_task(input("sisesta ülesande: "))
#    elif userInput =='2':
#        pass 
#    elif userInput =='3':
#        pass 
#    else:
#        print("sa sisestasid midagi vale")

import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Todo list")

def add_task():
    task = st.text_input("Sisesta uus ülesanne:", key="new_task_input")
    if st.button("Lisa"):
        if task.strip():
            st.session_state.tasks.append({"text": task, "done": False})
            st.rerun()
        else:
            st.warning("Sisesta mitte tühi ülesanne")
add_task()

st.subheader("Ülesanne nimikiri")

def show_tasks():
    if not st.session_state.tasks:
        st.info("Ei ole ülesandeid")
        return
    for index, task in enumerate(st.session_state.tasks):
        # Correct column spec (a valid list with positive numbers)
        cols = st.columns([1, 6, 1])  # Three columns with widths 1, 6, and 1 (adjust the ratio if needed)
        
        with cols[0]:
            task["done"] = st.checkbox("", value=task["done"], key=f"done_{index}")
        
        with cols[1]:
            if task["done"]:
                text = f"--------- {task['text']} --------"
            else:
                text = task["text"]
            st.markdown(text)
        
        with cols[2]:
            if st.button("Kustuta", key=f"delete_{index}"):
                st.session_state.tasks.pop(index)
                st.rerun()

show_tasks()