from src.ui_component import UI
from src.preprocessing import pre_processing
from src.pipeline import avg_word2vec
import pickle as pkl

ui = UI()

# Load the trained model

with open('models/model.pkl', 'rb') as file:
    model = pkl.load(file)

def predict_spam(email_text):
    # Placeholder for the actual prediction logic
    # Replace this with your actual model and prediction logic
    if model.predict([email_text]):
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