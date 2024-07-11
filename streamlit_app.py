import streamlit as st
from streamlit_option_menu import option_menu
import projects  # Importing the projects module

def main():
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        """,
        unsafe_allow_html=True
    )
    
    with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Home", "Project", "Connect with me"],
            icons=["house", "rocket", "envelope"],
        )

    if selected == "Home":
        st.title("Hi im raj")
        st.write("go to projects there's nothing here")

    elif selected == "Project":
        projects.display_projects()  # Calling the function from projects.py

    elif selected == "Connect with me":
        st.title("Contact Me")
        github_button = st.markdown(
            """
            <style>
            .github-button {
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #24292e;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                text-decoration: none;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .github-button:hover {
                background-color: #444;
            }
            .github-button i {
                margin-right: 10px;
            }
            </style>
            <a href="https://github.com/Hari-Narayana-Rath" class="github-button" target="_blank">
                <i class="fab fa-github"></i> GitHub
            </a>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
