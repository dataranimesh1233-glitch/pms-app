import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # FastAPI backend

st.title("Project Management System (PMS)")

menu = ["Users", "Projects", "Tasks"]
choice = st.sidebar.selectbox("Menu", menu)

# USERS
if choice == "Users":
    st.subheader("Create User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["Admin", "Project Manager", "Team Member"])
    if st.button("Add User"):
        response = requests.post(f"{API_URL}/users/", json={"name": name, "email": email, "role": role})
        if response.status_code == 200:
            st.success("User added successfully!")
    
    st.subheader("User List")
    users = requests.get(f"{API_URL}/users/").json()
    st.write(users)

# PROJECTS
elif choice == "Projects":
    st.subheader("Create Project")
    name = st.text_input("Project Name")
    desc = st.text_area("Description")
    if st.button("Add Project"):
        response = requests.post(f"{API_URL}/projects/", json={"name": name, "description": desc})
        if response.status_code == 200:
            st.success("Project added successfully!")
    
    st.subheader("Project List")
    projects = requests.get(f"{API_URL}/projects/").json()
    st.write(projects)

# TASKS
elif choice == "Tasks":
    st.subheader("Create Task")
    title = st.text_input("Task Title")
    desc = st.text_area("Task Description")
    project_id = st.number_input("Project ID", min_value=1)
    if st.button("Add Task"):
        response = requests.post(f"{API_URL}/tasks/", json={"title": title, "description": desc, "project_id": project_id})
        if response.status_code == 200:
            st.success("Task added successfully!")
    
    st.subheader("Task List")
    tasks = requests.get(f"{API_URL}/tasks/").json()
    st.write(tasks)
