from src.ui_component import UI
import joblib
from src.preprocessing import Preprocess

# Set up joblib memory for caching
memory = joblib.Memory(location='.', verbose=0)

# Cache the pipeline loading
@memory.cache
def load_pipeline():
    # Load your pipeline here
    return joblib.load('models/model.pkl')


pipline = load_pipeline()
ui = UI()



def predict_spam(email_text):
    # Placeholder for the actual prediction logic
    # Replace this with your actual model and prediction logic
    if pipline.predict([email_text]):
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