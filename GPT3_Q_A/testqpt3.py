import os
import openai
openai.api_key = "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"


openai.Answer.create(
    search_model="ada",#beta type in openai
    model="curie",
    question="which puppy is happy?",
    file="file-2ksWL61f0Q5c5vCYOLwUuhPk",
    examples_context="In 2017, U.S. life expectancy was 78.6 years.",
    examples=[["What is human life expectancy in the United States?", "78 years."]],
    max_rerank=10,
    max_tokens=5,
    stop=["\n", "<|endoftext|>"]
).answers
