import pandas as pd

data = pd.read_csv("./drinkWaterApp_data copy.csv", parse_dates=["Date", "Time"])

data["year"] = data["Date"].dt.year
data["month"] = data["Date"].dt.month
data["week"] = data["Date"].dt.isocalendar().week
data["day_of_the_week"] = data["Date"].dt.year
data["hour"] = data["Time"].dt.strftime("%H: %M")
data["day"] = (data["Date"].dt.day).astype("category")

month_names = {11: "November", 12: "December", 1: "January", 2: "February", 3: "March"}
data["month"] = data["month"].map(month_names)

time_bins = [0, 11, 18, 21, 24]
time_labels = ['Morning', 'Noon', 'Evening', 'Night']
data['time_of_day'] = pd.cut(data['hour'].dt.hour, bins=time_bins, labels=time_labels, right=False)

water_data = data.query("year == 2024")
water_data.drop("year", axis=1)


# Format a number to a string eg 8 to 'week 8'
def format_week_num(week_num): 
  return f"Week {week_num}"

data["week"] = data ["week"].apply(format_week_num)

water_data.to_csv ("my_water_intake_data.csv", index=False)
