# Plagiarism Detection Application

This is a simple web application for detecting plagiarism between two PDF files. The application extracts text from the uploaded PDFs, preprocesses the text, and calculates the similarity between the two texts using cosine similarity. The similarity score is displayed to the user, indicating the percentage of similarity between the two documents.

## Features

- Upload two PDF files to compare
- Extract and preprocess text from PDFs
- Calculate cosine similarity between the texts
- Display similarity percentage with a color-coded background

## Technologies Used

- Python
- Streamlit
- scikit-learn
- NLTK (Natural Language Toolkit)
- PyPDF2
- Pandas

## How to Run the Application

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Xerp839/Plagarism.git
   cd Plagarism

2. **Install the Required Packages**

    Make sure you have Python installed. Then, install the required packages using pip:
    
     ```bash
   pip install streamlit scikit-learn nltk PyPDF2 pandas
     
3. **Run the Application**

     ```bash
   streamlit run app.py --server.enableXsrfProtection false

   

4. **Upload PDF Files**

    -Open your web browser and navigate to the URL provided by Streamlit.
    -Upload two PDF files to compare and click the "Submit" button.
    -The similarity percentage will be displayed with a color-coded background (red for high similarity, green for low similarity).


    ## File Structure
    app.py: Main entry point of the application, handles navigation between pages.
    home.py: Home page for the application, handles PDF uploads and similarity calculation.
    contact.py: Contact page (optional, you can customize this as needed).
    style.css: Custom styles for the application.

    ## License

    This project is licensed under the MIT License. See the LICENSE file for more details.
