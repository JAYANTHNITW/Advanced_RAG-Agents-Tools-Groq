# Chatbot with Llama2

## My Learnings:
1. ```from langchain_core.output_parsers import StrOutputParser```

* ```parser = StrOutputParser()``` : Used to extract the relevant information from the raw output of the foundational model to human readable format and provides plain text (string)
***

2. **Envinormental Varibles**:
* In essence, the environment variable provides the API key value, but the code actively checks for its existence and uses it if available.
***
3. ```python-dotenv()```: Used to load the sensitive information present in ```.env()``` file to the current file.
* In summary, **python-dotenv** is a valuable tool for managing environment variables in Python projects, providing a secure and convenient way to store and access sensitive configuration details from a .env file.
***
4.  ```pypdf``` vs ```PyPDFLoader```:
* **pypdf** extracts text, manipulates PDF pages.
* **PyPDFLoader** (built on pypdf) tailors text for Langchain's RAG tasks.
* **PyPDFLoader** might segment text, handle formatting for RAG compatibility.
* Use **pypdf** for basic needs and manual processing.
* Choose **PyPDFLoader** for simplified **RAG** workflow with Langchain.
***
5. ```RecursiveCharacterTextSplitter()```: 
* **Recursion** is a concept where a function or process calls itself within its own definition. 
*  If the text after splitting with delimiters(**order**: Newline characters (\n), Paragraph breaks (\n\n), white space, and so on ) is still larger than the specified chunk_size, the function recursively calls itself on each resulting segment. This process continues until all segments are either smaller than or equal to the chunk_size.
# RAG Pipeline:
![Alt text](rag\RagPipeline.png)
### Step 1: Load the Source Data
1. **Data ingestion:** We import data from different ways like from pdfs,text files, Excel files, Readme file, directories and web. I used the following classes from langchain in this project: ```PyPDFLoader```, ```WebBaseLoader```, ```TextLoader```.
2. **Transform:** The document will be divided into chunks of specified length using ```RecursiveCharacterTextSplitter```
3. **Embed:**
### Step 2: Query Vector Store
* We store the embeded data into vector data bases (Chroma,faiss,lance) so that we can query what we want!
### Step 3: Retrive Most Similar
* Using similarity_search we can retrive Most similar vector.



