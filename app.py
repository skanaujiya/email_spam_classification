from src.ui_component import UI

ui = UI()

def predict_spam(email_text):
    # Placeholder for the actual prediction logic
    # Replace this with your actual model and prediction logic
    if "spam" in email_text.lower():
        return "Spam"
    else:
        return "Not Spam"


ui.page_config()
ui.sidebar()
ui.set_page_title("📧 Email Spam Classifier")
email_text = ui.input_text("Enter the Email Text", "Type or paste the email content here...")

# Button to perform prediction
ui.button("Classify", email_text, predict_spam)
ui.set_sidebar_info()

# Footer
ui.footer()