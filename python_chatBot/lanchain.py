from langchain.prompts import PromptTemplate

template = """다음과 같은 맥락을 사용하여 마지막 질문에 대답하십시오.
만약 답을 모르면 모른다고만 말하고 답을 지어내려고 하지 마십시오.
답변은 최대 세 문장으로 하고 가능한 한 간결하게 유지하십시오.
항상 '질문해주셔서 감사합니다!'라고 답변 끝에 말하십시오.
{context}
질문: {question}
도움이 되는 답변:"""
rag_prompt_custom = PromptTemplate.from_template(template)
# GPT-3.5 trurbo를 이용해서 LLM 설정
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_KEY)
# RAG chain 설정
from langchain.schema.runnable import RunnablePassthrough

rag_chain = {"context": retriever, "question": RunnablePassthrough()} | rag_prompt_custom | llm
rag_chain.invoke("물어볼 텍스트")
