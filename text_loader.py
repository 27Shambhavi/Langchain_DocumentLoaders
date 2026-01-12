from langchain_community.document_loaders import TextLoader
from regex import template
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
loader=TextLoader("cricket.txt",encoding="utf-8")

model=ChatOpenAI()
prompt=PromptTemplate(
    template=["Write a summary of the following text:\n\n{text}\n\nSummary:"],
    input_variables=["text"]
)

parser=StrOutputParser()

documents=loader.load()
print(type(documents))
print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)

chain=prompt|model|parser
chain.invoke({"text":documents[0].page_content})