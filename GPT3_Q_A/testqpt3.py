import os
import openai
openai.api_key = "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"

openai.Answer.create(
  search_model="ada",
  model="curie",
  question="which puppy is happy?",
  documents=["Puppy A is happy.", "Puppy B is sad."],
  examples_context="In 2017, U.S. life expectancy was 78.6 years.",
  examples=[["What is human life expectancy in the United States?","78 years."]],
  max_tokens=5,
  stop=["\n", "<|endoftext|>"],
)
