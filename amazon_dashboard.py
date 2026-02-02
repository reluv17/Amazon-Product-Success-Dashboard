import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

# Custom CSS
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
    }}
    .stTabs [aria-selected="true"] {{
        background-color: {COLORS['primary']};
        color: white;
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
        ('Correlation', '0.976', COLORS['primary'])
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
    
    col1, col2 = st.columns(2)
    
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
                IF early_avg_rating &lt; 4.0 AND volatility &gt; 1.0
            </p>
            <p style="font-size: 14px; color: #666;">→ FLAG AS HIGH RISK</p>
            <br>
            <div style="font-size: 14px; color: #666;">
                <div>Precision: <strong>91.2%</strong></div>
                <div>Recall: <strong>95.0%</strong></div>
                <div>Flags: <strong>125 products (26.5%)</strong></div>
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
