import fire

from metagpt.roles.di.data_interpreter import DataInterpreter

DATA_DIR = "test_df"
# sales_forecast data from https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast/data
REQUIREMENT = f"""do some sentiment analysis over the Claim_Description column, Here is the file path: {DATA_DIR}.csv"""


async def main():
    mi = DataInterpreter()
    await mi.run(REQUIREMENT)


if __name__ == "__main__":
    fire.Fire(main)