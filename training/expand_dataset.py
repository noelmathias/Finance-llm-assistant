import json 

with open("data/raw/seed_finance_dataset.json", "r") as f:
    seed_data = json.load(f)

templates = [
"What is {}?",
"Explain {}.",
"Describe {}.",
"Define {}.",
"How does {} work?",
"Explain {} in simple terms.",
"Give a brief explanation of {}.",
"What does {} mean?",
"Why is {} important?",
"Provide an overview of {}.",
"Explain the concept of {}.",
"Can you describe {}?",
"How would you explain {}?",
"What should beginners know about {}?",
"Summarize {}.",
"What are the basics of {}?",
"Explain the fundamentals of {}.",
"Give an introduction to {}.",
"What is the purpose of {}?",
"Why do investors care about {}?",
"Explain {} with an example.",
"What is the significance of {} in finance?",
"How do investors use {}?",
"Explain {} for beginners.",
"What role does {} play in financial markets?",
"How would you describe {} to a student?",
"Why is {} important in investing?",
"What should someone understand about {}?",
"Explain {} in the context of economics.",
"How is {} used in real-world finance?"
]

expanded_dataset = []

for item in seed_data:
    instruction = item["instruction"]
    answer = item["output"]

    topic = instruction.replace("Explain", "").replace("What is ", "").replace("Define ","")

    for template in templates:
        new_instruction = template.format(topic)

        expanded_dataset.append({
            "instruction": new_instruction,
            "input":"",
            "output":answer
        })

        expanded_dataset.append({
            "instruction": new_instruction,
            "input":"",
            "output":answer + "This concept is commonly used in finance & economics."
        })

with open("data/processed/dataset_expanded.json", "w") as f:
    json.dump(expanded_dataset, f, indent=2)

print("Dataset Size:", len(expanded_dataset))