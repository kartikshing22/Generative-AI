from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('attention-is-all-you-need.pdf')
docs = loader.load()

print(type(docs))

print(len(docs))
print(docs[0].page_content,docs[0].metadata)

