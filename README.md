### Scope of Project
Primary experimentation on evalution of multilinngual-RAG systems. 

### Acknowledgment
The RAG pipeline used for experimentation is based on youtube_rag.ipynb. 
+ Video link: https://youtu.be/BrsocJb-fAo?si=-NrAQ5lF1KYDQoHD 
+ Github Repository:  https://github.com/svpino/youtube-rag 

Languages: English, Hindi, Bengali

Components of RAG system: 
+ LLM, Embeddings - OpenAI 
+ Vector Store - Pinecone
+ LangChain
+ Chunk size = 100, chunk overlap = 20

Dataset (for each languag has been generated by Chatgpt 3.5 turbo) 
+ Knowlegde base: 825 words (A story from Mahabharata, an ancient Indian epic)
+ Evaluation dataset: Size = 20 (Categories = question, response, context, ground_truth)

Evaluation Framework: RAGAS (Metrics = faithfulness, answer_correctness)

Doubt
+ What would be the ideal test conditions?

Possible Scope
+ Concluding some results
+ KB is made such that its pre-exposed to ChatGpt Turbo-3 model
+ Make an API for translation 
+ Increasing the number of metrics
+ Increase size of our dataset {10k-KB(single/multiple stories); 500-Eval}
+ Connect with SQL database
+ Making evaluation algorithm in a different file
+ Making a single multilingual RAG system with cross-lingual capabilities
+ More to be added...

Results
+ Fluctuation in answers when a question is asked again 
+ More to be added...