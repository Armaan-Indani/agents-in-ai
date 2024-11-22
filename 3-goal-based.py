import pandas as pd
import datetime

schedule_df = pd.read_csv("schedule.csv")
attendance_df = pd.read_csv("attendance.csv")


def notify_class_goal_based(today):
    today_classes = schedule_df[schedule_df["day"] == today.strftime("%A")]
    if not today_classes.empty:
        for index, row in today_classes.iterrows():
            course = row["course"]
            topic = row["topic"]
            start_time = row["start_time"]
            end_time = row["end_time"]
            course_attendance = attendance_df[attendance_df["course"] == course]
            if (
                not course_attendance.empty
                and course_attendance["percentage"].iloc[0] < 75
            ):
                print(
                    f"Important: Attend {course} from {start_time} to {end_time} to maintain your attendance goal."
                )
            else:
                print(f"Reminder: You have {course} from {start_time} to {end_time}, and attendance is {course_attendance["percentage"].iloc[0]}%")


today = datetime.datetime.now()
notify_class_goal_based(today)
