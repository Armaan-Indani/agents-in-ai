import pandas as pd
import datetime

schedule_df = pd.read_csv("schedule.csv")


def notify_class(today):
    today_classes = schedule_df[schedule_df["day"] == today.strftime("%A")]
    if not today_classes.empty:
        for index, row in today_classes.iterrows():
            print(
                f"Reminder: You have {row['course']} from {row['start_time']} to {row['end_time']}."
            )


today = datetime.datetime.now()
notify_class(today)
