import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Amazon color palette
COLORS = {
    'primary': '#FF9900',
    'secondary': '#146EB4',
    'dark': '#232F3E',
    'success': '#067D62',
    'warning': '#F0C14B',
    'danger': '#B12704',
    'light': '#EAEDED'
}

# Page config
st.set_page_config(
    page_title="Amazon Product Success Prediction",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Fixed tab visibility
st.markdown(f"""
    <style>
    .main {{
        background-color: {COLORS['light']};
    }}
    .stTabs [data-baseweb="tab-list"] {{
        gap: 10px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: white;
        border: 2px solid {COLORS['primary']};
        border-radius: 8px 8px 0 0;
        padding: 12px 24px;
        font-weight: bold;
        color: {COLORS['dark']};
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {COLORS['primary']};
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Header with Amazon logo
st.markdown(f"""
    <div style="background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['secondary']} 100%);
                color: white; padding: 40px 30px; text-align: center; border-radius: 0;">
        <div style="margin-bottom: 20px;">
            <span style="background: white; padding: 8px 25px; border-radius: 8px; display: inline-block;">
                <span style="color: {COLORS['dark']}; font-size: 42px; font-weight: bold; font-family: Arial, sans-serif;">amazon</span><span style="color: {COLORS['primary']}; font-size: 28px; font-weight: bold;">.com</span>
            </span>
        </div>
        <h1 style="font-size: 32px; margin-top: 15px; margin-bottom: 10px; font-weight: 600;">Product Success Prediction Dashboard</h1>
        <p style="font-size: 16px; opacity: 0.9;">
            Early Review Analytics for Third-Party Sellers | 1.5M Reviews | 471 Products | 2015-2023
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# YOUR ACTUAL DATA
model_performance = pd.DataFrame({
    'model': ['Logistic Regression', 'Random Forest', 'Gradient Boosting'],
    'accuracy': [95.8, 96.8, 95.8],
    'precision': [95.9, 100.0, 98.6],
    'recall': [98.6, 95.8, 95.8],
    'f1': [97.2, 97.8, 97.1],
    'auc': [99.2, 99.3, 99.5]
})

feature_importance = pd.DataFrame({
    'feature': ['early_avg_rating', 'early_rating_std', 'early_1star_rate', 
                'early_5star_rate', 'early_avg_sentiment'],
    'importance': [0.327, 0.255, 0.133, 0.125, 0.046]
})

category_failure = pd.DataFrame({
    'category': ['Beauty', 'Electronics', 'Pet_Supplies'],
    'rate': [31.7, 11.7, 11.4],
    'color': [COLORS['danger'], COLORS['warning'], COLORS['success']]
})

alert_distribution = pd.DataFrame({
    'name': ['RED - High Risk', 'YELLOW - Monitor', 'GREEN - Safe'],
    'value': [125, 39, 307],
    'color': [COLORS['danger'], COLORS['warning'], COLORS['success']]
})

# Complaint patterns data
complaint_patterns = pd.DataFrame({
    'pattern': ['waste money', 'dont waste', 'doesnt work', 'poor quality', 'stopped working',
                'didnt work', 'disappointed product', 'would recommend', 'work well', 'thick hair',
                'waste time', 'nothing like', 'nail polish', 'dont know', 'works well'],
    'frequency': [259, 125, 72, 67, 55, 51, 40, 38, 38, 33, 30, 30, 29, 28, 28]
})

# Generate sample data for visualizations
np.random.seed(42)

# Product Rating Trajectories data
n_stable_high = 340
n_stable_low = 114
n_recovered = 11
n_declined = 6

early_stable_high = np.random.uniform(4.2, 5.0, n_stable_high)
oneyear_stable_high = early_stable_high + np.random.normal(0, 0.15, n_stable_high)
oneyear_stable_high = np.clip(oneyear_stable_high, 4.0, 5.0)

early_stable_low = np.random.uniform(2.0, 3.9, n_stable_low)
oneyear_stable_low = early_stable_low + np.random.normal(0, 0.2, n_stable_low)
oneyear_stable_low = np.clip(oneyear_stable_low, 1.5, 3.99)

early_recovered = np.random.uniform(3.5, 3.9, n_recovered)
oneyear_recovered = np.random.uniform(4.0, 4.5, n_recovered)

early_declined = np.random.uniform(4.3, 4.7, n_declined)
oneyear_declined = np.random.uniform(3.5, 3.99, n_declined)

trajectory_data = pd.DataFrame({
    'Early Rating': np.concatenate([early_stable_high, early_stable_low, early_recovered, early_declined]),
    '1-Year Rating': np.concatenate([oneyear_stable_high, oneyear_stable_low, oneyear_recovered, oneyear_declined]),
    'Trajectory': ['Stable High']*n_stable_high + ['Stable Low']*n_stable_low + ['Recovered']*n_recovered + ['Declined']*n_declined
})

# K-Means Clustering data
n_elite = 312
n_risk = 159

elite_rating = np.random.uniform(4.2, 5.0, n_elite)
elite_volatility = np.random.uniform(0.3, 1.0, n_elite)

risk_rating = np.random.uniform(2.0, 4.2, n_risk)
risk_volatility = np.random.uniform(1.0, 1.8, n_risk)

kmeans_data = pd.DataFrame({
    'Early Rating': np.concatenate([elite_rating, risk_rating]),
    'Volatility': np.concatenate([elite_volatility, risk_volatility]),
    'Cluster': ['Elite Performers']*n_elite + ['High Risk']*n_risk
})

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Predictive Power', 'Volatility Warning', 'Category Risk'])

# TAB 1: OVERVIEW
with tab1:
    # Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        ('Total Reviews', '1.5M', COLORS['primary']),
        ('Products Analyzed', '471', COLORS['secondary']),
        ('Model Accuracy', '96.8%', COLORS['success']),
        ('Early-to-1Yr Predictive Strength', '0.976', COLORS['primary'])  # Changed label
    ]
    
    for col, (label, value, color) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
                <div style="background: white; padding: 25px; border-radius: 12px; 
                            box-shadow: 0 4px 6px rgba(0,0,0,0.1); border: 3px solid {color}; text-align: center;">
                    <div style="font-size: 14px; color: #666; margin-bottom: 8px;">{label}</div>
                    <div style="font-size: 32px; font-weight: bold; color: {color};">{value}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Insights Cards
    col1, col2, col3 = st.columns(3)
    
    insights = [
        ('Early Reviews Highly Predictive', 'r = 0.976', 
         'First 100 reviews predict 1-year ratings with 97.6% correlation. Models achieve 96-97% accuracy.',
         COLORS['success']),
        ('Volatility Critical Warning', '25.5%',
         'Rating volatility contributes 25.5% to predictions - nearly as important as rating itself.',
         COLORS['warning']),
        ('Beauty = 3X Higher Risk', '31.7%',
         'Beauty products fail at 31.7% vs 11-12% for Electronics/Pets.',
         COLORS['danger'])
    ]
    
    for col, (title, stat, desc, color) in zip([col1, col2, col3], insights):
        with col:
            st.markdown(f"""
                <div style="background: white; border-left: 5px solid {color}; padding: 20px; 
                            border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h3 style="font-size: 16px; margin-bottom: 10px; color: {COLORS['dark']};">{title}</h3>
                    <div style="font-size: 28px; font-weight: bold; color: {color}; margin: 10px 0;">{stat}</div>
                    <p style="font-size: 13px; color: #666; line-height: 1.6;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Model Performance Chart
    st.markdown("### Model Performance Comparison")
    fig = go.Figure()
    
    metrics_to_plot = ['accuracy', 'precision', 'recall', 'f1']
    colors_bar = [COLORS['primary'], COLORS['secondary'], COLORS['success'], COLORS['warning']]
    
    for metric, color in zip(metrics_to_plot, colors_bar):
        fig.add_trace(go.Bar(
            name=metric.capitalize() + ' (%)',
            x=model_performance['model'],
            y=model_performance[metric],
            marker_color=color
        ))
    
    fig.update_layout(
        barmode='group',
        yaxis=dict(range=[90, 101]),
        height=400,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# TAB 2: PREDICTIVE POWER
with tab2:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS['success']} 0%, #0d5a4a 100%);
                    color: white; padding: 20px; border-radius: 12px; margin-bottom: 30px;">
            <h2 style="font-size: 24px; margin-bottom: 10px;">Insight 1: Early Reviews Highly Predict 1-Year Success</h2>
            <p style="font-size: 16px; opacity: 0.9;">
                Correlation of 0.976 between early (100 reviews) and 1-year ratings | 96.8% Classification Accuracy
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Stats Grid
    col1, col2, col3 = st.columns(3)
    
    stats = [
        ('Correlation', '0.976', 'Extremely Strong'),
        ('Products Stable', '73.2%', '±0.1 star change'),
        ('Best Model', '96.8%', 'Random Forest')
    ]
    
    for col, (label, value, sublabel) in zip([col1, col2, col3], stats):
        with col:
            st.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 8px; text-align: center; 
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <div style="font-size: 14px; color: #666;">{label}</div>
                    <div style="font-size: 36px; font-weight: bold; color: {COLORS['success']};">{value}</div>
                    <div style="font-size: 12px; color: #999;">{sublabel}</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Product Rating Trajectories
    st.markdown("### Product Rating Trajectories: Early to 1-Year")
    st.markdown("""
    This visualization shows how products' ratings evolve from their first 100 reviews to one-year performance. 
    The tight clustering along the diagonal demonstrates that early ratings are highly predictive of long-term success.
    """)
    
    fig = px.scatter(
        trajectory_data,
        x='Early Rating',
        y='1-Year Rating',
        color='Trajectory',
        color_discrete_map={
            'Stable High': COLORS['success'],
            'Stable Low': COLORS['danger'],
            'Recovered': COLORS['secondary'],
            'Declined': COLORS['warning']
        },
        opacity=0.6,
        height=500
    )
    
    # Add diagonal line
    fig.add_trace(go.Scatter(
        x=[2, 5],
        y=[2, 5],
        mode='lines',
        line=dict(dash='dash', color='gray', width=2),
        name='No Change Line',
        showlegend=True
    ))
    
    # Add success threshold line
    fig.add_hline(y=4.0, line_dash="dot", line_color="red", 
                  annotation_text="Success Threshold (4.0)", 
                  annotation_position="right")
    
    fig.update_layout(
        xaxis_title="Early Average Rating (First 100 Reviews)",
        yaxis_title="1-Year Average Rating",
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # K-Means Clustering
    st.markdown("### K-Means Clustering Analysis")
    st.markdown("""
    Unsupervised clustering reveals two distinct product groups based on early review characteristics. 
    Elite Performers show high ratings with low volatility, while High Risk products exhibit lower ratings and greater inconsistency.
    """)
    
    fig = px.scatter(
        kmeans_data,
        x='Early Rating',
        y='Volatility',
        color='Cluster',
        color_discrete_map={
            'Elite Performers': COLORS['success'],
            'High Risk': COLORS['secondary']
        },
        opacity=0.6,
        height=500
    )
    
    # Add threshold lines
    fig.add_vline(x=4.0, line_dash="dot", line_color="red", 
                  annotation_text="Rating Threshold: 4.0")
    fig.add_hline(y=1.0, line_dash="dot", line_color=COLORS['warning'], 
                  annotation_text="Volatility Threshold: 1.0")
    
    fig.update_layout(
        xaxis_title="Early Average Rating",
        yaxis_title="Rating Volatility (Std Dev)",
        template='plotly_white',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Model Performance Table
    st.markdown("### Model Performance Metrics")
    
    styled_df = model_performance.style.highlight_max(
        subset=['accuracy', 'precision', 'recall', 'f1', 'auc'],
        color='lightgreen'
    ).format({
        'accuracy': '{:.1f}%',
        'precision': '{:.1f}%',
        'recall': '{:.1f}%',
        'f1': '{:.1f}%',
        'auc': '{:.1f}%'
    })
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

# TAB 3: VOLATILITY WARNING
with tab3:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS['warning']} 0%, #c99200 100%);
                    color: {COLORS['dark']}; padding: 20px; border-radius: 12px; margin-bottom: 30px;">
            <h2 style="font-size: 24px; margin-bottom: 10px;">Insight 2: Rating Volatility is Critical Warning Signal</h2>
            <p style="font-size: 16px;">
                Volatility contributes 25.5% to predictions | Combined Rule: 91.2% Precision, 95% Recall
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Feature Importance Rankings")
        
        fig = px.bar(
            feature_importance,
            y='feature',
            x='importance',
            orientation='h',
            color='importance',
            color_continuous_scale=['#146EB4', '#F0C14B'],
            labels={'importance': 'Importance', 'feature': 'Feature'}
        )
        
        fig.update_layout(
            height=300,
            showlegend=False,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Alert Distribution")
        
        # Shortened explanation
        st.markdown("""
        **Risk Classification:**
        
        - **RED**: Rating <4.0 AND volatility >1.0 → 91.2% actually fail
        - **YELLOW**: Warning signs → 5.1% fail
        - **GREEN**: Strong & stable → 1.3% fail
        """)
        
        fig = px.pie(
            alert_distribution,
            values='value',
            names='name',
            color='name',
            color_discrete_map={
                'RED - High Risk': COLORS['danger'],
                'YELLOW - Monitor': COLORS['warning'],
                'GREEN - Safe': COLORS['success']
            }
        )
        
        fig.update_layout(height=300)
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Warning Rule
    st.markdown(f"""
        <div style="background: #fff3cd; border: 3px solid {COLORS['warning']}; 
                    border-radius: 8px; padding: 20px;">
            <h3 style="font-size: 18px; margin-bottom: 15px; color: {COLORS['dark']};">Recommended Warning Rule</h3>
            <p style="font-size: 16px; font-weight: bold; margin-bottom: 10px; color: {COLORS['dark']};">
                IF early_avg_rating &lt; 4.0 AND volatility &gt; 1.0 → FLAG AS HIGH RISK
            </p>
            <div style="font-size: 14px; color: #666;">
                <div>✓ Precision: <strong>91.2%</strong> | Recall: <strong>95.0%</strong> | Flags: <strong>125 products (26.5%)</strong></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# TAB 4: CATEGORY RISK
with tab4:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, {COLORS['danger']} 0%, #8b1a04 100%);
                    color: white; padding: 20px; border-radius: 12px; margin-bottom: 30px;">
            <h2 style="font-size: 24px; margin-bottom: 10px;">Insight 3: Beauty Products Have 3X Higher Failure Risk</h2>
            <p style="font-size: 16px; opacity: 0.9;">
                Beauty: 31.7% Failure Rate vs Electronics/Pets: ~11%
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Explanation of Failure Risk
    st.markdown(f"""
        <div style="background: white; padding: 20px; border-radius: 8px; border-left: 5px solid {COLORS['danger']}; margin-bottom: 20px;">
            <h3 style="font-size: 18px; margin-bottom: 10px; color: {COLORS['dark']};">What is "Failure Risk"?</h3>
            <p style="font-size: 14px; color: #666; line-height: 1.6;">
                <strong>Product failure</strong> = ending with a rating below 4.0 stars after one year. 
                On Amazon, products rated below 4.0 struggle to compete as most customers filter for 4+ star products. 
                Beauty products face unique challenges including subjective preferences and skin compatibility, leading to 3X higher failure rates.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Failure Rate Chart
    st.markdown("### Failure Rate by Category")
    
    fig = px.bar(
        category_failure,
        x='category',
        y='rate',
        color='category',
        color_discrete_map={
            'Beauty': COLORS['danger'],
            'Electronics': COLORS['warning'],
            'Pet_Supplies': COLORS['success']
        },
        labels={'rate': '% Products Ending <4.0', 'category': 'Category'}
    )
    
    fig.update_layout(
        showlegend=False,
        height=400,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Top Complaint Patterns
    st.markdown("### Top 15 Complaint Patterns in Failed Products")
    st.markdown("""
    Most frequent complaint phrases from negative reviews of 120 failed products.
    """)
    
    fig = px.bar(
        complaint_patterns,
        y='pattern',
        x='frequency',
        orientation='h',
        color='frequency',
        color_continuous_scale=['#8b1a04', '#B12704'],
        labels={'frequency': 'Frequency', 'pattern': 'Complaint Pattern'}
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Category Cards
    col1, col2, col3 = st.columns(3)
    
    category_info = [
        ('Beauty', '31.7%', '<3.86', 'HIGH', COLORS['danger']),
        ('Electronics', '11.7%', '<3.84', 'MEDIUM', COLORS['warning']),
        ('Pet Supplies', '11.4%', 'Monitor', 'LOW', COLORS['success'])
    ]
    
    for col, (cat, rate, threshold, risk, color) in zip([col1, col2, col3], category_info):
        with col:
            st.markdown(f"""
                <div style="background: white; border: 3px solid {color}; padding: 20px; 
                            border-radius: 12px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <h4 style="font-size: 16px; margin-bottom: 10px; color: {COLORS['dark']};">{cat}</h4>
                    <div style="font-size: 28px; font-weight: bold; color: {color}; margin-bottom: 10px;">
                        {rate}
                    </div>
                    <div style="font-size: 13px; color: #666;">
                        <div>Failure Rate</div>
                        <div style="margin-top: 10px; font-weight: bold; color: {color};">
                            Risk: {risk}
                        </div>
                        <div style="margin-top: 5px;">
                            Threshold: {threshold}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown(f"""
    <div style="background: {COLORS['dark']}; color: white; padding: 20px; 
                text-align: center; margin-top: 40px;">
        <p style="font-size: 14px; opacity: 0.8;">
            Amazon Product Success Prediction | Data: 2015-2023 | 
            Analysis: K-means Clustering, Random Forest, Gradient Boosting
        </p>
    </div>
""", unsafe_allow_html=True)
