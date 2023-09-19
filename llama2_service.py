from flask import Flask, request, jsonify

from langchain.llms import LlamaCpp
from langchain import PromptTemplate

app = Flask(__name__)

MODEL_PATH = "./models/llama-2-7b-chat.ggmlv3.q8_0.bin"

template = """
%INSTRUCTIONS:
Please summarize the following piece of text.
Respond in a manner that a 5 year old would understand.

%TEXT:
{text}
"""

# Create a LangChain prompt template that we can insert values to later
prompt = PromptTemplate(
    input_variables=["text"],
    template=template,
)

def load_llama2_7b_model():
    llama2_llm = LlamaCpp(model_path=MODEL_PATH)
    return llama2_llm

def invoke_model(q):
    llm = load_llama2_7b_model()

    return llm(q)

@app.route('/invoke_llm',methods=['POST'])
def invoke_llm():
    input = request.json
    print("!! question is: ",input)

    question = input.get('question')
    final_prompt = prompt.format(text=question)
    answer = invoke_model(final_prompt)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port='4502',debug=True,threaded=True)