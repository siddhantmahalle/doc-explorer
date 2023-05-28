from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


class QueryDoc:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.qa_chain = load_qa_chain(llm=self.llm, chain_type="stuff")

    def query(self, query: str, search_docs: str):
        answer = self.qa_chain.run(input_documents=search_docs, question=query)
        return answer
