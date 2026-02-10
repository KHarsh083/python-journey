def call_llm(prompt: str) -> str:
    return f"LLM response for: {prompt}"

print(call_llm("Explain sliding window"))
