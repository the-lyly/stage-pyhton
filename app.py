import streamlit as st
import pandas as pd
import plotly.express as px

# Function to load the dataset
@st.cache_data
def load_data():
    return pd.read_excel('graphesdf.xlsx')

df = load_data()

# Calculate the percentage of fraud by Wilaya
fraud_by_wilaya = (df[df['cible'] == 'fraude'].groupby('Wilaya')['cible'].count() /
                   df.groupby('Wilaya')['cible'].count()).reset_index().rename(columns={'cible': 'Fraud Percentage'})

# Calculate the percentage of fraud by Code CNRC
fraud_by_cnrc = (df[df['cible'] == 'fraude'].groupby('Code CNRC')['cible'].count() /
                 df.groupby('Code CNRC')['cible'].count()).reset_index().rename(columns={'cible': 'Fraud Percentage'})

# Streamlit app setup
st.title('Dashboard de detection de fraude')

# Input field for the user to enter the BP
bp_input = st.text_input('Entrez le BP:')

if bp_input:
    try:
        # Search for the BP in the dataset
        result = df[df['BP'] == int(bp_input)]
        if not result.empty:
            st.write(f"Result for BP {bp_input}:")
            st.write(result[['BP', 'cible']].head(1))  # Displaying the target column
        else:
            st.error("aucune donné trouvé avec le BP inseré")
    except ValueError:
        st.error("veuillez entrer un BP valide")

# Display a sorted table of specified columns
st.subheader('données detaillés classées par feature (diff enfte ChAff et TVA annuelle)')
# Sorting the DataFrame by 'featureChT' in descending order
sorted_df = df.sort_values(by='featureChT', ascending=False)
# Displaying specific columns
st.dataframe(sorted_df[['BP', 'Wilaya', 'Code CNRC', 'Code ONS', 'ChAff', 'Total TVA anuelle', 'cible','featureChT']])

# Interactive graph of Fraud Percentage by Wilaya
st.subheader('pourcentage de fraude par Wilaya')
fig_wilaya = px.bar(fraud_by_wilaya, x='Wilaya', y='Fraud Percentage')
st.plotly_chart(fig_wilaya)

# Interactive graph of Fraud Percentage by Code CNRC
st.subheader('pourcentage de fraude par Code CNRC')
fig_cnrc = px.bar(fraud_by_cnrc, x='Code CNRC', y='Fraud Percentage')
st.plotly_chart(fig_cnrc)
