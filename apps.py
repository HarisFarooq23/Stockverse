import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# ------------------ Page Configurations ------------------
st.set_page_config(
    page_title="StockVerse",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------ Theme Toggle ------------------
mode = st.sidebar.radio("Theme (Coming Soon🌍)", ["Light Mode", "Dark Mode"] , index=1)
if mode == "Dark Mode":
    st.markdown(
        """
        <style>
        body, .reportview-container, .sidebar .sidebar-content {
            background-color: #0e1117;
            color: white;
        }
        .stDataFrame, .stTable {
            background-color: #1e222a;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ------------------ Sidebar Navigation ------------------
st.sidebar.title("📊 StockVerse")
st.sidebar.markdown("#### 🚀 Navigation")
page = st.sidebar.selectbox("Go to", [
    "🏠 Home", 
    "💼 Famous Portfolios", 
    "🔎 Compare Investors", 
    "👤 Your Profile", 
    "ℹ️ About"
])
st.sidebar.markdown("---")
st.sidebar.write("Made by Haris and Fatima")

# ------------------ Dummy Data ------------------

# Trending Stocks Dummy Data
trending_stocks = pd.DataFrame({
    "Stock": ["Apple", "Tesla", "Amazon", "Microsoft", "NVIDIA", "Google", "Meta", "Netflix"],
    "Price": [172.5, 195.4, 130.7, 310.8, 875.6, 285.7, 234.5, 387.4],
    "Market Cap (B$)": [2850, 900, 1350, 2700, 1200, 1750, 900, 500],
    "Change %": [+1.5, -0.5, +2.1, +0.8, -1.2, +0.6, +1.3, -0.7]
})

# Famous Investors' Portfolios + Bios
investors_portfolios = {
    "Warren Buffett": {
        "bio": "CEO of Berkshire Hathaway and one of the most successful investors in history, known for value investing.",
        "portfolio": {
            "Stock": ["Apple", "Coca Cola", "Bank of America", "Chevron"],
            "Shares": [100000, 400000, 80000, 60000],
            "Value": [15000000, 10000000, 5000000, 3000000]
        }
    },
    "Ray Dalio": {
        "bio": "Founder of Bridgewater Associates, pioneer of risk-parity and diversified investing strategies.",
        "portfolio": {
            "Stock": ["Procter & Gamble", "Johnson & Johnson", "Coca Cola", "PepsiCo"],
            "Shares": [90000, 70000, 60000, 80000],
            "Value": [12000000, 9500000, 7000000, 8000000]
        }
    },
    "Cathie Wood": {
        "bio": "CEO of ARK Invest, known for high-growth tech and innovation-driven investment philosophy.",
        "portfolio": {
            "Stock": ["Tesla", "Roku", "Coinbase", "Zoom"],
            "Shares": [30000, 40000, 25000, 35000],
            "Value": [6000000, 4500000, 3200000, 2800000]
        }
    },
    "Peter Lynch": {
        "bio": "Former manager of the Magellan Fund at Fidelity, known for the 'invest in what you know' strategy.",
        "portfolio": {
            "Stock": ["Ford", "General Electric", "McDonald's", "Walmart"],
            "Shares": [20000, 15000, 25000, 30000],
            "Value": [1500000, 1200000, 1800000, 2400000]
        }
    },
    "George Soros": {
        "bio": "Hedge fund manager and philanthropist, famous for 'breaking the Bank of England' in 1992.",
        "portfolio": {
            "Stock": ["Amazon", "Alphabet", "PayPal", "Salesforce"],
            "Shares": [17000, 19000, 14000, 10000],
            "Value": [2200000, 2500000, 1800000, 1300000]
        }
    },
    "Benjamin Graham": {
        "bio": "Father of value investing and mentor to Warren Buffett. Authored 'The Intelligent Investor'.",
        "portfolio": {
            "Stock": ["GE", "IBM", "Xerox", "3M"],
            "Shares": [10000, 8000, 12000, 9000],
            "Value": [1100000, 950000, 980000, 1020000]
        }
    },
    "Charlie Munger": {
        "bio": "Vice chairman of Berkshire Hathaway and Buffett's long-time investing partner and strategist.",
        "portfolio": {
            "Stock": ["Costco", "Berkshire Hathaway", "Wells Fargo", "Bank of America"],
            "Shares": [5000, 10000, 15000, 20000],
            "Value": [1000000, 2500000, 1100000, 1900000]
        }
    },
    "John Templeton": {
        "bio": "A pioneer in global investing, known for finding undervalued stocks worldwide.",
        "portfolio": {
            "Stock": ["Nestle", "Toyota", "HSBC", "Unilever"],
            "Shares": [7000, 8000, 6000, 9000],
            "Value": [1000000, 1200000, 900000, 950000]
        }
    },
    "Jesse Livermore": {
        "bio": "Legendary early 20th century trader known for short-selling and market speculation.",
        "portfolio": {
            "Stock": ["Dow Inc.", "GM", "Citigroup", "AIG"],
            "Shares": [3000, 4000, 3500, 5000],
            "Value": [500000, 600000, 450000, 480000]
        }
    },
    "Michael Burry": {
        "bio": "Famous for predicting the 2008 housing crisis, portrayed in 'The Big Short'.",
        "portfolio": {
            "Stock": ["Meta", "Alibaba", "GameStop", "Amazon"],
            "Shares": [7000, 6000, 9000, 5000],
            "Value": [1300000, 1100000, 900000, 1400000]
        }
    }
}

# ------------------ Page Rendering ------------------

if page == "🏠 Home":
    st.title("📊 Welcome to StockVerse")
    st.markdown("### Trending Stocks Today")
    st.dataframe(trending_stocks.style.format({
        "Price": "${:,.2f}",
        "Market Cap (B$)": "{:,.0f}B",
        "Change %": "{:+.2f}%"
    }).background_gradient(cmap="PuBu"))

    if trending_stocks['Change %'].mean() > 0:
        st.success("📈 Overall market trend is Positive today!")
    else:
        st.error("📉 Overall market trend is Negative today.")

    st.markdown("---")
    st.subheader("🔥 Market Capitalization Comparison")
    cap_chart = px.bar(
        trending_stocks,
        x="Stock",
        y="Market Cap (B$)",
        color="Stock",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    st.plotly_chart(cap_chart, use_container_width=True)

elif page == "💼 Famous Portfolios":
    st.title("💼 StockVerse: Famous Investors' Portfolios")
    selected_investor = st.selectbox("Select an Investor", list(investors_portfolios.keys()))
    bio = investors_portfolios[selected_investor]["bio"]
    data = pd.DataFrame(investors_portfolios[selected_investor]["portfolio"])

    st.markdown(f"#### 🧠 About {selected_investor}")
    st.info(bio)

    st.markdown(f"### 📄 Portfolio of {selected_investor}")
    st.dataframe(data.style.format({"Value": "${:,.2f}"}).background_gradient(cmap="Greens"))

    st.markdown("---")
    st.subheader("📊 Portfolio Distribution")
    pie_chart = px.pie(
        data,
        names="Stock",
        values="Value",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(pie_chart, use_container_width=True)

elif page == "🔎 Compare Investors":
    st.title("🔎 Compare Investors | StockVerse")
    selected_investors = st.multiselect("Select Investors to Compare", list(investors_portfolios.keys()), default=["Warren Buffett", "Ray Dalio"])

    if not selected_investors:
        st.warning("⚠️ Please select at least one investor to compare.")
    else:
        combined_data = pd.DataFrame()
        for investor in selected_investors:
            df = pd.DataFrame(investors_portfolios[investor]["portfolio"])
            df["Investor"] = investor
            combined_data = pd.concat([combined_data, df], ignore_index=True)

        st.markdown("### Value Comparison Among Investors")
        compare_chart = px.bar(
            combined_data,
            x="Stock",
            y="Value",
            color="Investor",
            barmode="group",
            color_discrete_sequence=px.colors.qualitative.Vivid
        )
        st.plotly_chart(compare_chart, use_container_width=True)

elif page == "👤 Your Profile":
    st.title("👤 Your Portfolio | StockVerse")

    investor_name = st.text_input("What's your name? (For Portfolio Identification)", "")
    uploaded_csv = st.file_uploader("📁 Upload Your Portfolio (CSV)", type=["csv"])

    if uploaded_csv:
        try:
            haris_portfolio = pd.read_csv(uploaded_csv)

            # Basic validation
            if not {'Stock', 'Value', 'Sector'}.issubset(haris_portfolio.columns):
                st.error("❌ CSV must contain 'Stock', 'Value', and 'Sector' columns.")
            else:
                if investor_name:
                    st.markdown(f"### {investor_name}'s Portfolio Overview")
                else:
                    st.markdown("### Your Portfolio Overview")

                st.dataframe(haris_portfolio.style.format({"Value": "${:,.2f}"}).background_gradient(cmap="YlGnBu"))

                total_value = haris_portfolio['Value'].sum()
                avg_value = haris_portfolio['Value'].mean()
                max_stock = haris_portfolio.loc[haris_portfolio['Value'].idxmax()]['Stock']

                if total_value > 30000:
                    st.success(f"🎉 Congratulations! Your portfolio is growing strong (${total_value:,.2f})")
                else:
                    st.info(f"Keep investing wisely! Current portfolio value: ${total_value:,.2f}")

                st.markdown("---")
                st.subheader("📊 Investment Distribution by Stock")
                pie_chart_haris = px.pie(
                    haris_portfolio,
                    names="Stock",
                    values="Value",
                    hole=0.3,
                    color_discrete_sequence=px.colors.qualitative.Set2
                )
                st.plotly_chart(pie_chart_haris, use_container_width=True)

                st.markdown("### 🏢 Sector Allocation")
                pie_sector = px.pie(
                    haris_portfolio,
                    names="Sector",
                    values="Value",
                    hole=0.35,
                    color_discrete_sequence=px.colors.qualitative.Bold
                )
                st.plotly_chart(pie_sector, use_container_width=True)

                st.markdown("---")
                st.markdown("### 📌 Quick Stats")
                st.metric(label="Total Portfolio Value", value=f"${total_value:,.2f}")
                st.metric(label="Average Stock Value", value=f"${avg_value:,.2f}")
                st.metric(label="Top Performing Stock", value=max_stock)

                # ------------------ Risk Prediction Model Setup ------------------
                st.subheader("🚨 Sector Risk Analysis")

                # Create dummy model (for example purposes)
                known_sectors = haris_portfolio['Sector'].unique().tolist()
                np.random.seed(42)
                synthetic_data = pd.DataFrame({
                    "MarketCap": np.random.uniform(10, 100, size=100),
                    "Volatility": np.random.uniform(0.1, 0.5, size=100),
                    "Sector": np.random.choice(known_sectors, size=100)
                })
                synthetic_data = pd.get_dummies(synthetic_data, columns=["Sector"])
                synthetic_data["Risk"] = (synthetic_data["MarketCap"] * 0.1 + synthetic_data["Volatility"] * 30 +
                                          np.random.normal(0, 5, size=100))

                feature_columns = [col for col in synthetic_data.columns if col != "Risk"]
                risk_model = RandomForestRegressor(n_estimators=100, random_state=42)
                risk_model.fit(synthetic_data[feature_columns], synthetic_data["Risk"])

                def predict_risk(sector):
                    dummy_input = pd.DataFrame({
                        'MarketCap': [50],
                        'Volatility': [0.3],
                        **{f"Sector_{s}": [1 if s == sector else 0] for s in known_sectors}
                    })
                    for col in feature_columns:
                        if col not in dummy_input.columns:
                            dummy_input[col] = 0
                    return risk_model.predict(dummy_input[feature_columns])[0]

                haris_portfolio["Predicted Risk (%)"] = haris_portfolio["Sector"].apply(predict_risk)

                risk_summary = haris_portfolio.groupby("Sector")["Predicted Risk (%)"].mean().reset_index()
                st.dataframe(risk_summary.style.format({"Predicted Risk (%)": "{:.2f}"}))

                risk_bar = px.bar(
                    risk_summary,
                    x="Sector",
                    y="Predicted Risk (%)",
                    color="Sector",
                    color_discrete_sequence=px.colors.sequential.OrRd
                )
                st.plotly_chart(risk_bar, use_container_width=True)

        except Exception as e:
            st.error(f"⚠️ Error loading file: {e}")
    else:
        st.warning("⚠️ Please upload your portfolio CSV file to view your profile.")


elif page == "ℹ️ About":
    st.title("ℹ️ About StockVerse")
    st.markdown("""
    ### 📊 StockVerse  
    A powerful platform to:

    - 🔥 Track trending stocks and market insights  
    - 💼 Explore portfolios of legendary investors  
    - 📊 Visualize and manage your personal investments

    **Tech Stack:**  
    - Streamlit  
    - Pandas  
    - Plotly
    - Numpy
    - Scikit 

    **Version:** 1.1 (2025)

    ---
    Made with 💻 by **Haris Farooq and Fatima Ameer**
    """)
    st.info("ℹ️ This project is constantly evolving. Stay tuned for live stock integration and more features!")
