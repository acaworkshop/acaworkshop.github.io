import pandas as pd
import yaml


def yml_reviewers():
    csv_path = "data/reviewers.csv"
    yml_path = "data/reviewers.yml"
    df = pd.read_csv(csv_path)
    items = df.to_dict(orient="records")
    with open(yml_path, "w") as f:
        yaml.safe_dump(items, f, sort_keys=False, allow_unicode=True)

