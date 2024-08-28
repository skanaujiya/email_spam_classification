import streamlit as st

class UI:
    def __init__(self):
        pass

    def page_config(self):
        st.set_page_config(
            page_title="Email Spam Classifier",
            page_icon="📧",
            layout="centered",
            initial_sidebar_state="expanded"
        )
    def set_page_title(self, title):
        st.title(title)
        st.write(
            """
            This application uses a machine learning model to classify emails as **Spam** or **Not Spam**.
            Simply enter the email text below and click on **Classify** to get the prediction.
            """
        )
        
    def input_text(self, label, placeholder)->str:
        st.subheader(label)
        return st.text_area(placeholder)
    
    def button(self, label:str, email_text:str, function):
        if st.button(label=label):
            if email_text:
                # Get prediction
                result = function(email_text)
                # Display result with colorful markdown
                st.markdown(f"### Prediction: {'🟢 **Not Spam**' if result == 'Not Spam' else '🔴 **Spam**'}")
            else:
                st.warning("Please enter the email text to classify.")


    def sidebar(self):
        st.image("https://images.unsplash.com/photo-1516245821404-177349d5d7f3", use_column_width=True)
        st.sidebar.title("Email Spam Classifier")
        st.sidebar.markdown("Use this app to classify emails as **Spam** or **Not Spam** based on their content.")
    
    def set_sidebar_info(self):
        st.sidebar.subheader("About")
        st.sidebar.info(
            """
            This app is powered by a machine learning model trained to identify spam emails.
            It leverages natural language processing (NLP) techniques to analyze the content of the email.
            """
        )
        st.sidebar.subheader("Instructions")
        st.sidebar.info(
            """
            - **Enter** the email text in the input box.
            - **Click** the **Classify** button to see the result.
            """
        )

    
    def footer(self):
        st.markdown(
            """ 
            ---
            Created with ❤️ by [Shubham Kanaujiya](https://www.linkedin.com/in/shubham-kanaujiya-7367511a5/)
            """
        )