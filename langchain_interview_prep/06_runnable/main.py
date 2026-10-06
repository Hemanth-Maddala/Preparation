"""06 - Runnable: the common interface of models, prompts, chains.

Everything callable in LangChain is a Runnable and supports:
  invoke(input)  -> one answer
  batch(inputs)  -> many answers at once
  stream(input)  -> answer produced as chunks
"""

from langchain_core.runnables import RunnableLambda

# 1. Wrap a plain function in a Runnable with RunnableLambda
def double(x: int) -> int:
    return x * 2


runnable = RunnableLambda(double)

# 2. invoke(): one input -> one output
print("invoke :", runnable.invoke(4))           # 8

# 3. batch(): many inputs -> many outputs
print("batch  :", runnable.batch([1, 2, 3]))    # [2, 4, 6]

# 4. stream(): output delivered as it is produced
print("stream :", list(runnable.stream(4)))     # [8]


# Note: models and chains are Runnables too. This works on every LangChain
# component: model.invoke(...), chain.batch(...), agent.stream(...), etc.
# (See projects 01 and 05 for model + chain versions of these three methods.)
