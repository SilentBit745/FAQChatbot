IIM Lucknow FAQ Chatbot
A lightweight chatbot for finding answers to common questions about IIM Lucknow.
Instead of searching through long FAQ pages, users can simply type a question in their own words. The chatbot compares the question against a collection of frequently asked questions and returns the most relevant answer.
What it does

Understands questions written in natural language
Matches questions with relevant FAQs using TF-IDF
Uses cosine similarity to rank possible matches
Includes a fallback for questions outside the FAQ dataset
Provides a simple interactive interface through Streamlit
Stores FAQ content separately in JSON for easy updates

Example
User:
What is the admission process for IIM Lucknow?
Chatbot:
Returns the most relevant answer from the FAQ database.
The wording of the question doesn't have to exactly match the stored FAQ. The text-matching layer helps identify similar questions.
How it works
User enters a question
        ↓
Text preprocessing
        ↓
TF-IDF representation
        ↓
Cosine similarity
        ↓
Best matching FAQ
        ↓
Answer

Tech Stack

Python
NLTK
Scikit-learn
Streamlit
JSON

Project Structure
FAQChatbot/
│
├── app.py            # Streamlit interface
├── chatbot.py        # NLP and FAQ matching logic
├── faq_data.json     # FAQ dataset
├── requirements.txt  # Python dependencies
└── README.md

Running Locally
Clone the repository:
git clone https://github.com/SilentBit745/FAQChatbot.git
cd FAQChatbot

Install the dependencies:
pip install -r requirements.txt

Start the application:
streamlit run app.py

The application will then be available through the local Streamlit server.
FAQ Dataset
The chatbot currently works with a curated set of frequently asked questions related to IIM Lucknow.
The FAQ data is kept in faq_data.json, so new questions and answers can be added without changing the core chatbot logic.
Limitations
This is a retrieval-based chatbot rather than a generative AI system. It can answer questions that are reasonably represented by the available FAQ data, but it won't reliably handle topics that aren't covered by the dataset.
Its answers also depend on the quality and coverage of the FAQ collection.
Possible Improvements
Some things that could make the chatbot more useful over time:

Expand and regularly update the FAQ dataset
Improve intent detection
Add better handling for multi-part questions
Add conversation context
Experiment with semantic embeddings instead of traditional TF-IDF matching
Deploy the chatbot for public use

License
This project is open source. See the repository for the applicable license and usage details.
