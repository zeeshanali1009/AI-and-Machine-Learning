import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\Python Libraries\3. Matplotlib\4. Project\netflix_users.csv")

# Clean the data
df = df.dropna(subset=["User_ID", "Name", "Age", "Country", "Subscription_Type", "Watch_Time_Hours", "Favorite_Genre", "Last_Login"])

# 1. Bar chart: Country-wise subscription
country_counts = df["Country"].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(country_counts.index, country_counts.values, color=["orange", "blue"])
plt.title("Country Wise Subscription Type")
plt.xlabel("Country")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig("1_country_wise_subscription_bar.png")
plt.close()

# 2. Pie chart: Watch Time Distribution
watch_time_counts = df["Watch_Time_Hours"].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(
    watch_time_counts,
    labels=watch_time_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=plt.cm.Pastel1.colors
)
plt.title("Percentage of Watch Time Hours")
plt.tight_layout()
plt.savefig("2_watch_time_pie.png")
plt.close()

# 3. Histogram: Watch Time
plt.figure(figsize=(8, 6))
plt.hist(df["Watch_Time_Hours"], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Watch Time Hours")
plt.xlabel("Watch Time (Hours)")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig("3_hist_watch_time_hours.png")
plt.close()

# 4. Scatter Plot: Age vs Watch Time
plt.figure(figsize=(8, 6))
plt.scatter(df["Age"], df["Watch_Time_Hours"], c="green", alpha=0.6, edgecolors="black")
plt.title("Scatter Plot: Age vs Watch Time Hours")
plt.xlabel("Age")
plt.ylabel("Watch Time (Hours)")
plt.grid(True)
plt.tight_layout()
plt.savefig("4_scatter_age_vs_watch_time.png")
plt.close()

# 5. Horizontal Bar Chart: Country-wise
plt.figure(figsize=(10, 6))
plt.barh(country_counts.index, country_counts.values, color="skyblue")
plt.title("Country-wise Subscription Count (Horizontal Bar)")
plt.xlabel("Number of Users")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("5_country_wise_subscription_hbar.png")
plt.close()

# 6. Subplots (Vertical & Horizontal Bar in one image)
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Subplot 1: Vertical Bar Chart
ax[0].bar(country_counts.index, country_counts.values, color="orange")
ax[0].set_title("Country-wise Subscriptions (Vertical)")
ax[0].set_xlabel("Country")
ax[0].set_ylabel("Number of Users")
ax[0].tick_params(axis='x', rotation=45)

# Subplot 2: Horizontal Bar Chart
ax[1].barh(country_counts.index, country_counts.values, color="skyblue")
ax[1].set_title("Country-wise Subscriptions (Horizontal)")
ax[1].set_xlabel("Number of Users")
ax[1].set_ylabel("Country")

plt.tight_layout()
plt.savefig("6_country_subscriptions_subplots.png")
plt.close()
