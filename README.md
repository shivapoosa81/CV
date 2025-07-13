llama-index-core
llama-index-utils-workflow
llama-index-readers-file 
llama-index-llms-ollama 
llama-index-embeddings-huggingface
llama-index-vector-stores-chroma
llama-index-llms-openai
llama-index-embeddings-openai
llama-index-program-openai
llama-index-question-gen-openai
llama-index-agent-openai
llama-index-multi-modal-llms-openai
python-dotenv
pandas
pypdf
streamlit
chroma


python -m .venv env
chmod -R 777 env
source env/bin/activate
.\env\Scripts\activate
pip list
pip install -r requirements.txt


from dotenv import load_dotenv
import os



async def main():
    load_dotenv()    
    print(os.getenv('OPENAI_API_KEY'))

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

