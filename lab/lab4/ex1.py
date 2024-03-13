import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def convert_date(date_str):
    if 'BCE' in date_str:
        year = -1 * int(date_str.replace(' BCE', ''))
    elif 'CE' in date_str:
        year = int(date_str.replace(' CE', ''))
    else:
        year = pd.NaT  # 对于"Unknown"的情况，我们将其设为pandas的NaT（Not a Time）
    return pd.to_datetime(year, format='%Y', errors='coerce')

# Load the data
landslide = pd.read_csv('landslide_catalog.csv')
volcano = pd.read_csv('volcano_database.csv')

# Convert the date column to datetime format
landslide['date'] = pd.to_datetime(landslide['date'])
volcano['Last Known Eruption'] = volcano['Last Known Eruption'].apply(convert_date)

# Extract the day and week of day for landslide
landslide['day'] = landslide['date'].dt.day
landslide['week_of_day'] = landslide['date'].dt.dayofweek

# Extract the year for volcano
volcano['year'] = volcano['Last Known Eruption'].dt.year

# Plot the data
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

sns.distplot(landslide['day'], bins=30, color='blue', ax=axs[0, 0])
axs[0, 0].set_title('Landslide Day Plot')
sns.distplot(landslide['week_of_day'], bins=7, color='blue', ax=axs[0, 1])
axs[0, 1].set_title('Landslide Week-of-Day Plot')

sns.histplot(volcano['year'].dropna(), bins=30, color='red', ax=axs[1, 0])
axs[1, 0].set_title('Volcano Year Distribution')

plt.tight_layout()
plt.show()