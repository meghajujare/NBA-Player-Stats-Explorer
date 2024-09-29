import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NBA Player Stats Explorer')

st.markdown("""
This app performs simple webscraping of NBA player stats data!
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2025))))

# Web scraping of NBA player stats
@st.cache_data
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)  # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

playerstats = load_data(selected_year)

# Strip any potential whitespace from column names
playerstats.columns = playerstats.columns.str.strip()

# Sidebar - Team selection

if 'Team' in playerstats.columns:
    team_column = 'Team'

if team_column:
    # Convert the team column to string to avoid type mismatch during sorting
    playerstats[team_column] = playerstats[team_column].astype(str)
    
    sorted_unique_team = sorted(playerstats[team_column].unique())
    selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
else:
    selected_team = []

# Sidebar - Position selection (if 'Pos' column exists)
if 'Pos' in playerstats.columns:
    unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
    selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)
else:
    selected_pos = []

# Filtering data only if both columns exist
if selected_team and selected_pos:
    df_selected_team = playerstats[(playerstats[team_column].isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

    st.header('Display Player Stats of Selected Team(s)')
    st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
    st.dataframe(df_selected_team)

    # Download NBA player stats data
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
        return href

    st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')

    # Filter only numeric columns for correlation
    numeric_df = df_selected_team.select_dtypes(include=[np.number])
    
    if not numeric_df.empty:
        corr = numeric_df.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True

        with sns.axes_style("white"):
            fig, ax = plt.subplots(figsize=(7, 5))  # Create a figure object
            sns.heatmap(corr, mask=mask, vmax=1, square=True, ax=ax)
        
        st.pyplot(fig)  # Pass the figure to st.pyplot()
    else:
        st.warning("No numerical data available for correlation.")

