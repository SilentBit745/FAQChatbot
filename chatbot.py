import json
import re

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download stopwords if needed
try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")


class FAQChatbot:

    def __init__(self, faq_file="faq_data.json"):

        # Load FAQ data
        with open(faq_file, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        # English stopwords
        self.stop_words = set(stopwords.words("english"))

        # FAQ questions
        self.questions = [
            faq["question"] for faq in self.faqs
        ]

        # Words related to IIM Lucknow
        self.iim_keywords = {
            "iim",
            "admission",
            "pgp",
            "mba",
            "cat",
            "program",
            "programme",
            "course",
            "campus",
            "hostel",
            "library",
            "scholarship",
            "placement",
            "placements",
            "student",
            "students",
            "faculty",
            "fees",
            "fee",
            "eligibility",
            "ipmx",
            "doctoral",
            "phd",
            "bs",
            "exchange",
            "international",
            "sports",
            "gym",
            "facilities",
            "application",
            "exam",
            "entrance"
        }

        # TF-IDF
        self.vectorizer = TfidfVectorizer(
            preprocessor=self.preprocess_text
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def preprocess_text(self, text):

        # Lowercase
        text = text.lower()

        # Remove punctuation
        text = re.sub(
            r"[^a-zA-Z0-9\s]",
            "",
            text
        )

        # Split words
        words = text.split()

        # Remove stopwords
        words = [
            word
            for word in words
            if word not in self.stop_words
        ]

        return " ".join(words)

    def is_iim_related(self, question):

        # Clean question
        cleaned = self.preprocess_text(question)

        # Get words
        words = set(cleaned.split())

        # Check for IIM-related words
        return bool(words.intersection(self.iim_keywords))

    def get_response(self, user_question):

        # Empty question
        if not user_question.strip():

            return (
                "Please enter a question.",
                0.0
            )

        # Reject clearly unrelated questions
        if not self.is_iim_related(user_question):

            return (
                "Sorry, I can only answer questions "
                "related to IIM Lucknow.",
                0.0
            )

        # Convert question to TF-IDF
        user_vector = self.vectorizer.transform(
            [user_question]
        )

        # Calculate similarity
        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        # Find best match
        best_match_index = similarities.argmax()

        best_score = similarities[
            0
        ][best_match_index]

        # Similarity threshold
        threshold = 0.35

        # If no good match
        if best_score < threshold:

            return (
                "Sorry, I couldn't find a relevant "
                "answer about IIM Lucknow. "
                "Please try asking another question.",
                best_score
            )

        # Return answer
        answer = self.faqs[
            best_match_index
        ]["answer"]

        return answer, best_score