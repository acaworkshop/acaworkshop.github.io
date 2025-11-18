import pandas as pd
import yaml


def yml_reviewers():
    csv_path = "data/reviewers.csv"
    yml_path = "data/reviewers.yml"
    df = pd.read_csv(csv_path)
    items = df.to_dict(orient="records")
    with open(yml_path, "w") as f:
        yaml.safe_dump(items, f, sort_keys=False, allow_unicode=True)

def get_website_data(sheet_name=""):
    sheet_id = "11ngfJidLjbk_DA-4PUXkb7MPbIMVfAcGDWphDtB4Ppk"  # Replace with your actual Sheet ID
    # sheet_name = "HQPs"  # Optional if targeting a specific sheet
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    df = pd.read_csv(url)

    return df

def get_schedule_data(sheet_name=""):
    sheet_id = "1N0suQGLObEm7rYhse1vBTZ6GDQOothg27u3ZW_0AZxA"  # Replace with your actual Sheet ID
    # sheet_name = "HQPs"  # Optional if targeting a specific sheet
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    df = pd.read_csv(url)

    return df

def dump_data():
    dump_papers()


def dump_papers():
    df = get_website_data("papers")

    df_dict = df.to_dict(orient="records")


    df_oral = df[df["oral"] == True]
    df_oral_dict = df_oral.to_dict(orient="records")

    with open("./data/papers.yml", "w") as file:
        yaml.dump(df_dict, file, default_flow_style=False)

    with open("./data/oral-presentations.yml", "w") as file:
        yaml.dump(df_oral_dict, file, default_flow_style=False)




def dump_schedule():
    df = get_schedule_data("schedule_website")

    # drop unnamed / completely empty columns
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    df = df.dropna(how="all")

    # convert NaN -> None so YAML writes nulls instead of `.nan`
    df = df.where(pd.notnull(df), None)

    records = df.to_dict(orient="records")

    with open("./data/schedule.yml", "w") as f:
        yaml.safe_dump(records, f, sort_keys=False, allow_unicode=True)