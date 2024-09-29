# 🏀 NBA Player Stats Explorer

Welcome to the **NBA Player Stats Explorer**! 🎉 This web application lets you explore and analyze player statistics from the NBA. It features a user-friendly interface for web scraping, filtering, and visualizing player data.

## 🚀 Live Demo
Check out the live app [here](https://nba-player-stats-explorer.streamlit.app/)! 🔗

## 📋 Problem Statement
The NBA Player Stats Explorer is designed to:
- **Web Scraping**: 🌐 Automate the extraction of player statistics from the Basketball Reference website.
- **Data Filtering**: 🔍 Allow users to filter player data by year, team, and position.
- **Data Visualization**: 📊 Provide insights through visualizations, specifically an intercorrelation heatmap of player statistics.
- **Data Downloading**: 💾 Enable users to download the filtered data in CSV format for further analysis.

## 🛠 Tools and Technologies Used
- **Streamlit**: 🖥️ A Python library for quick web app development.
- **Pandas**: 📈 A powerful library for data manipulation and analysis.
- **Matplotlib & Seaborn**: 🎨 Libraries for data visualization, with Seaborn offering enhanced plotting capabilities.
- **NumPy**: 🔢 A library for numerical operations and array manipulations.
- **Base64**: 📦 Used for encoding CSV data to create download links.

## ✨ Features
- **Year Selection**: 📅 Choose the year for which you want to view player statistics.
- **Team and Position Filtering**: 🏆 Filter players by team and position for focused analysis.
- **Intercorrelation Heatmap**: 🔥 Visualize the correlation between various player statistics.
- **CSV Download**: 📥 Download the filtered data for offline analysis.

## 🥳 How to Use
1. **Visit the live demo link**.
2. **Use the sidebar** to select the year, team, and position.
3. **Click on "Intercorrelation Heatmap"** to visualize player statistics.
4. **Download the filtered data** as a CSV file using the provided link.

## 📦 Installation
If you want to run the app locally, follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nba-player-stats-explorer.git
   cd nba-player-stats-explorer
   ```
2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

![Screenshot 2024-09-29 133742](https://github.com/user-attachments/assets/231be541-4ca5-40bf-a32b-9b375aeb22bb)


## 📝 License
This project is licensed under the MIT License.

## 🙏 Acknowledgments
- **Data Source**: 📊 Player statistics are sourced from [Basketball Reference](https://www.basketball-reference.com/).
