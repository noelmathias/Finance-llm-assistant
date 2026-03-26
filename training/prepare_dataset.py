import json
from sklearn.model_selection import train_test_split

with open("data/processed/dataset_expanded.json", "r") as f:
    dataset = json.load(f)
print("Total Dataset size:", len(dataset))
train_data , val_data = train_test_split(dataset, test_size=0.1, random_state=42)

print("Train size:", len(train_data))
print("Validation size:", len(val_data))

with open("data/processed/train_dataset.json", "w") as f:
    json.dump(train_data, f, indent=2)

with open("data/processed/val_dataset.json", "w") as f:
    json.dump(val_data, f, indent=2)