\# AI-Powered Language Translation Tool



A simple and user-friendly language translation application developed as part of the \*\*CodeAlpha Artificial Intelligence Internship – Task 1\*\*.



The application allows users to enter text, select a source language and target language, and translate the text using a \*\*local LibreTranslate API\*\*.



\## Features



\- 🌐 Translate text between multiple languages

\- 📝 Simple text input interface

\- 🔤 Source language selection

\- 🌍 Target language selection

\- ⚡ Fast translation using a local translation API

\- 📋 Copy translated text with one click

\- 🎨 Clean and user-friendly Streamlit interface

\- 🔒 Uses a locally hosted translation server



\## Technologies Used



\- \*\*Python\*\*

\- \*\*Streamlit\*\* – User interface

\- \*\*Requests\*\* – API communication

\- \*\*LibreTranslate\*\* – Translation API

\- \*\*Git \& GitHub\*\* – Version control and project submission



\## Supported Languages



The application currently provides several languages, including:



\- English

\- French

\- German

\- Hindi

\- Italian

\- Japanese

\- Korean

\- Portuguese

\- Russian

\- Spanish

\- Arabic

\- Bengali

\- Chinese

\- Dutch

\- Greek

\- Indonesian

\- Persian

\- Polish

\- Romanian

\- Swedish

\- Thai

\- Turkish

\- Ukrainian

\- Urdu

\- Vietnamese



\## How It Works



1\. Enter the text that you want to translate.

2\. Select the \*\*source language\*\*.

3\. Select the \*\*target language\*\*.

4\. Click the \*\*Translate\*\* button.

5\. The application sends the text to the locally hosted LibreTranslate API.

6\. The translated text is displayed in the result box.

7\. The translated text can be copied using the \*\*Copy\*\* button.



\## Project Structure



```text

CodeAlpha\_LanguageTranslationTool/

│

├── app.py

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/divyasrree/CodeAlpha\_LanguageTranslationTool.git

```



\### 2. Navigate to the project folder



```bash

cd CodeAlpha\_LanguageTranslationTool

```



\### 3. Create and activate a virtual environment



```bash

python -m venv venv

```



Windows:



```bash

venv\\Scripts\\activate

```



\### 4. Install the required packages



```bash

pip install -r requirements.txt

```



\## Running the Application



The project uses a \*\*locally hosted LibreTranslate server\*\*, so the server must be running before starting the Streamlit application.



\### Terminal 1 – Start LibreTranslate



```bash

libretranslate

```



The server should run at:



```text

http://127.0.0.1:5000

```



\### Terminal 2 – Start the Streamlit application



```bash

streamlit run app.py

```



The application will open in your browser.



\## Example



\*\*Input:\*\*



```text

Hello, how are you?

```



\*\*Source Language:\*\* English



\*\*Target Language:\*\* Hindi



\*\*Output:\*\*



```text

नमस्ते, आप कैसे हैं?

```



\## CodeAlpha Internship



This project was developed as \*\*Task 1 – Language Translation Tool\*\* for the \*\*CodeAlpha Artificial Intelligence Internship\*\*.



\### Project Repository



GitHub:  

https://github.com/divyasrree/CodeAlpha\_LanguageTranslationTool



\## Author



\*\*Divya Srree S\*\*



B.Tech – Artificial Intelligence and Data Science  

Sri Sairam Engineering College

