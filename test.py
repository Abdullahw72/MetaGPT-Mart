import fire

from metagpt.roles.di.data_interpreter import DataInterpreter
from constants import constants

DATA_DIR = "test_df"
# sales_forecast data from https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast/data
REQUIREMENT = f"""do some sentiment analysis over the Claim_Description column, Here is the file path: {DATA_DIR}.csv
You are only allowed to use the following libraries for the code you generate in this task: {constants.libraries}"""


async def main():
    mi = DataInterpreter()
    await mi.run(REQUIREMENT)


if __name__ == "__main__":
    fire.Fire(main)