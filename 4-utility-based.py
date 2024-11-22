import pandas as pd
import datetime

schedule_df = pd.read_csv("schedule.csv")


def notify_class_utility_based(today):
    today_classes = schedule_df[schedule_df["day"] == today.strftime("%A")]
    if not today_classes.empty:
        for index, row in today_classes.iterrows():
            course = row["course"]
            topic = row["topic"]
            start_time = row["start_time"]
            end_time = row["end_time"]
            importance = row["importance"]
            if importance > 7:
                print(
                    f"Critical: Do not miss {course} on '{topic}', very important! From {start_time} to {end_time}."
                )
            else:
                print(
                    f"Reminder: You have {course} covering '{topic}' from {start_time} to {end_time} today. Importance level: {importance}"
                )


today = datetime.datetime.now()
notify_class_utility_based(today)
