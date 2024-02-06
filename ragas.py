# import os
# os.environ["OPENAI_API_KEY"] = "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"


# from datasets import load_dataset

# fiqa_eval = load_dataset("explodinggradients/fiqa", "ragas_eval")
# print(fiqa_eval)

# from ragas.metrics import (
#     answer_relevancy,
#     faithfulness,
#     context_recall,
#     context_precision,
# )   

# from ragas import evaluate

# result = evaluate(
#     fiqa_eval["baseline"].select(range(3)), # selecting only 3
#     metrics=[
#         context_precision,
#         faithfulness,
#         answer_relevancy,
#         context_recall,
#     ],
# )

# result

from ragas import evaluate
from datasets import Dataset
import os

#os.environ["OPENAI_API_KEY"] = "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"
os.environ["OPENAI_API_KEY"] = "PUT THE API KEY HERE"

# prepare your huggingface dataset in the format
# Dataset({
#     features: ['question', 'contexts', 'answer', 'ground_truths'],
#     num_rows: 25
# })

dataset: Dataset

results = evaluate(dataset)