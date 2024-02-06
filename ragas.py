import os
os.environ["OPENAI_API_KEY"] = "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"


from datasets import load_dataset

fiqa_eval = load_dataset("explodinggradients/fiqa", "ragas_eval")
print(fiqa_eval)

from ragas.metrics import (
    answer_relevancy,
    faithfulness,
    context_recall,
    context_precision,
)   

from ragas import evaluate

result = evaluate(
    fiqa_eval["baseline"].select(range(3)), # selecting only 3
    metrics=[
        context_precision,
        faithfulness,
        answer_relevancy,
        context_recall,
    ],
)

result