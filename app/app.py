import os
import pandas as pd
import streamlit as st
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from dotenv import load_dotenv
import chromadb

load_dotenv()  
# --- 1. Configuration ---
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")


# Define file paths
PDF_DATA_DIR = "data"
STATIC_DIR = "data"
CHROMA_PERSIST_DIR = "chroma_db"
OUTPUT_EXCEL_FILE = "document_dates_report.xlsx"
CHROMA_COLLECTION_NAME = "document_retrieval"
# --- 2. Load Documents ---
def load_documents_from_directory():
    """
    Loads all PDF documents from the specified directory.
    Uses SimpleDirectoryReader to process all files in PDF_DATA_DIR.
    """

    print(f"Loading documents from '{PDF_DATA_DIR}'...")
    # Loading all files from the directory. The reader chooses the best parser.
    reader = SimpleDirectoryReader(PDF_DATA_DIR)
    documents = reader.load_data()
    return documents

# --- 3. Data Extraction using a Query Engine ---
def extract_content_from_documents(documents):
    """
    Iterates through each document, creates a query engine for it,
    and extracts the created and posted dates.
    """
    extracted_data = []

    # Group documents by filename to process one file at a time
    docs_by_filename = {}
    for doc in documents:
        filename = os.path.basename(doc.metadata.get('file_name', 'Unknown File'))
        if filename not in docs_by_filename:
            docs_by_filename[filename] = []
        docs_by_filename[filename].append(doc)

    print(f"\nFound {len(docs_by_filename)} unique documents to process.")

    for filename, doc_list in docs_by_filename.items():
        print(f"\nProcessing '{filename}'...")
        print(doc_list)

        # Create an index specifically for the content of this single document
        # This isolates the context for accurate data extraction per file.
        index = VectorStoreIndex.from_documents(doc_list)

        # Create a query engine to ask questions about this document
        query_engine = index.as_query_engine()

        # --- Programmatically ask questions to extract the information ---
        # Query for the creation date
        created_date_response = query_engine.query(
            "What is the creation date mentioned in this document? "
            "Respond with only the date and nothing else."
        )
        created_date = str(created_date_response).strip()

        # Query for the posted date
        posted_date_response = query_engine.query(
            "What is the posted date mentioned in this document? "
            "Respond with only the date and nothing else."
        )

        # Query for the posted date
        summary_response = query_engine.query(
            "What is the summary in this document? "
            "Respond with only summary from Haedlines as bullet points line by line."
        )
        
        posted_date = str(posted_date_response).strip()

        print(f"  - Extracted Created Date: {created_date}")
        print(f"  - Extracted Posted Date: {posted_date}")
        print(f"  - Extracted Summary: {summary_response}")
        file_url = f"{filename.replace(' ', '%20')}" # Handle spaces in filenames
        # file_url = f"file://{os.path.abspath(os.path.join(PDF_DATA_DIR, filename))}"
        markdown_link = f"{file_url}"
        # Store the extracted data
        extracted_data.append({
            "Source Document": markdown_link,
            "Created Date": created_date,
            "Posted Date": posted_date,
            "Summary": summary_response
        })

    return extracted_data

# --- 4. Export to Excel ---
def export_to_excel(data):
    """
    Converts the list of extracted data into a pandas DataFrame
    and saves it as an Excel file.
    """
    if not data:
        print("No data was extracted. Cannot generate Excel file.")
        return

    print("\nExporting extracted data to Excel...")
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    df.to_excel(OUTPUT_EXCEL_FILE, index=False, engine='openpyxl')
    print(f"Successfully created report: '{OUTPUT_EXCEL_FILE}'")


def export_to_html(data):
    if extracted_data:
        st.subheader("Extraction Results")
        
        # Create a DataFrame from the results
        df = pd.DataFrame(extracted_data)
        
        # Display the DataFrame as a configurable table
        # We configure the 'File' column to be a LinkColumn, using the 'url' column data for the links



        st.data_editor(
            df,
            column_config={
                "Source Document": st.column_config.LinkColumn(
                    "Source Document",
                    help="Click to open the PDF file in a new tab"
                ),
                "url": None  # Hide the raw url column
            },
            hide_index=True,
            use_container_width=True
        )
    else:
        st.warning("Could not extract any data from the uploaded files.")


# --- Main Execution ---
if __name__ == "__main__":
    # Check if the data directory exists
    if not os.path.exists(PDF_DATA_DIR) or not os.listdir(PDF_DATA_DIR):
        print(f"Error: The directory '{PDF_DATA_DIR}' is empty or does not exist.")
        print("Please create it and add your PDF files.")
    else:
        # Step 1: Load all documents from the PDF directory
        documents = load_documents_from_directory()

        # Step 2: Extract the specific dates from each document
        extracted_data = extract_content_from_documents(documents)

        # Step 3: Export the final report to an Excel file
        export_to_excel(extracted_data)

        export_to_html(extracted_data)

        

        
