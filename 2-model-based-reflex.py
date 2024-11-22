import pandas as pd
import datetime

schedule_df = pd.read_csv("schedule.csv")
holidays_df = pd.read_csv("holidays.csv", parse_dates=["date"])


def is_holiday(today):
    today = today.strftime("%Y-%m-%d")
    holiday_today = holidays_df[holidays_df["date"] == today]
    if not holiday_today.empty:
        return holiday_today["occasion"].values[0]
    return None


def notify_class_model_based(today):
    holiday_occasion = is_holiday(today.date())
    if holiday_occasion:
        print(f"Today is a holiday ({holiday_occasion}), no classes!")
    else:
        today_classes = schedule_df[schedule_df["day"] == today.strftime("%A")]
        if not today_classes.empty:
            for index, row in today_classes.iterrows():
                print(
                    f"Reminder: You have {row['course']} covering '{row['topic']}' from {row['start_time']} to {row['end_time']}."
                )


today = datetime.datetime.now()
notify_class_model_based(today)
