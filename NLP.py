from transformers import CamembertTokenizer, CamembertForSequenceClassification
import torch
import pickle

class Nlp_model:
    """
    classe du model nlp entrainé
    """
    def __init__(self):
        self.tokenizer = CamembertTokenizer.from_pretrained("./orlvoice_intent_model")
        self.model = CamembertForSequenceClassification.from_pretrained("./orlvoice_intent_model")
        with open('label_encoder.pkl', 'rb') as f:
            self.label_encoder = pickle.load(f)

    def predict_intent(self, text):
        """
        predit l'intention a partir d'un texte
        :param text:
        :return: intent
        """
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=32)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits, dim=1).item()

            intent = self.label_encoder.inverse_transform([predicted_class_id])[0]
            return intent
