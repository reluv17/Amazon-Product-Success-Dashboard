import React, { useState } from 'react';
import { BarChart, Bar, LineChart, Line, ScatterChart, Scatter, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { AlertCircle, TrendingUp, Award, Package } from 'lucide-react';

// Amazon color palette
const COLORS = {
  primary: '#FF9900', // Amazon orange
  secondary: '#146EB4', // Amazon blue
  dark: '#232F3E', // Amazon dark
  success: '#067D62',
  warning: '#F0C14B',
  danger: '#B12704',
  light: '#EAEDED'
};

const AmazonDashboard = () => {
  const [activeTab, setActiveTab] = useState('overview');

  // Sample data - replace with your actual data
  const overviewMetrics = [
    { label: 'Total Reviews', value: '1.5M', icon: Package, color: COLORS.primary },
    { label: 'Products Analyzed', value: '471', icon: Package, color: COLORS.secondary },
    { label: 'Model Accuracy', value: '96.8%', icon: Award, color: COLORS.success },
    { label: 'Correlation', value: '0.976', icon: TrendingUp, color: COLORS.primary }
  ];

  const insights = [
    {
      title: 'Early Reviews Highly Predictive',
      stat: 'r = 0.976',
      description: 'First 100 reviews predict 1-year ratings with 97.6% correlation. Models achieve 96-97% accuracy.',
      color: COLORS.success
    },
    {
      title: 'Volatility Critical Warning',
      stat: '25.5%',
      description: 'Rating volatility contributes 25.5% to predictions - nearly as important as rating itself.',
      color: COLORS.warning
    },
    {
      title: 'Beauty = 3X Higher Risk',
      stat: '31.7%',
      description: 'Beauty products fail at 31.7% vs 11-12% for Electronics/Pets.',
      color: COLORS.danger
    }
  ];

  const modelPerformance = [
    { model: 'Logistic Regression', accuracy: 95.8, precision: 95.9, recall: 98.6, f1: 97.2, auc: 99.2 },
    { model: 'Random Forest', accuracy: 96.8, precision: 100, recall: 95.8, f1: 97.8, auc: 99.3 },
    { model: 'Gradient Boosting', accuracy: 95.8, precision: 98.6, recall: 95.8, f1: 97.1, auc: 99.5 }
  ];

  const featureImportance = [
    { feature: 'early_avg_rating', importance: 0.327 },
    { feature: 'early_rating_std', importance: 0.255 },
    { feature: 'early_1star_rate', importance: 0.133 },
    { feature: 'early_5star_rate', importance: 0.125 },
    { feature: 'early_avg_sentiment', importance: 0.046 }
  ];

  const categoryFailureRate = [
    { category: 'Beauty', rate: 31.7, color: COLORS.danger },
    { category: 'Electronics', rate: 11.7, color: COLORS.warning },
    { category: 'Pet_Supplies', rate: 11.4, color: COLORS.success }
  ];

  const alertDistribution = [
    { name: 'RED - High Risk', value: 125, color: COLORS.danger },
    { name: 'YELLOW - Monitor', value: 39, color: COLORS.warning },
    { name: 'GREEN - Safe', value: 307, color: COLORS.success }
  ];

  const clusterData = [
    { name: 'Elite Performers', value: 312, color: COLORS.success },
    { name: 'High Risk', value: 159, color: COLORS.danger }
  ];

  return (
    <div style={{ background: COLORS.light, minHeight: '100vh', fontFamily: 'Arial, sans-serif' }}>
      {/* Header */}
      <div style={{ 
        background: `linear-gradient(135deg, ${COLORS.dark} 0%, ${COLORS.secondary} 100%)`,
        color: 'white',
        padding: '30px',
        textAlign: 'center'
      }}>
        <h1 style={{ fontSize: '36px', marginBottom: '10px', fontWeight: 'bold' }}>
          🛍️ Amazon Product Success Prediction Dashboard
        </h1>
        <p style={{ fontSize: '16px', opacity: 0.9 }}>
          Early Review Analytics for Third-Party Sellers | 1.5M Reviews | 471 Products | 2015-2023
        </p>
      </div>

      {/* Tabs */}
      <div style={{ 
        display: 'flex', 
        gap: '10px', 
        padding: '20px',
        background: 'white',
        borderBottom: `3px solid ${COLORS.primary}`
      }}>
        {['overview', 'insight1', 'insight2', 'insight3'].map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            style={{
              padding: '12px 24px',
              background: activeTab === tab ? COLORS.primary : 'white',
              color: activeTab === tab ? 'white' : COLORS.dark,
              border: `2px solid ${COLORS.primary}`,
              borderRadius: '8px 8px 0 0',
              cursor: 'pointer',
              fontWeight: 'bold',
              fontSize: '14px',
              transition: 'all 0.3s'
            }}
          >
            {tab === 'overview' && 'Overview'}
            {tab === 'insight1' && 'Predictive Power'}
            {tab === 'insight2' && 'Volatility Warning'}
            {tab === 'insight3' && 'Category Risk'}
          </button>
        ))}
      </div>

      {/* Content */}
      <div style={{ padding: '30px' }}>
        {/* OVERVIEW TAB */}
        {activeTab === 'overview' && (
          <div>
            {/* Metric Cards */}
            <div style={{ 
              display: 'grid', 
              gridTemplateColumns: 'repeat(4, 1fr)', 
              gap: '20px',
              marginBottom: '30px'
            }}>
              {overviewMetrics.map((metric, idx) => (
                <div key={idx} style={{
                  background: 'white',
                  padding: '25px',
                  borderRadius: '12px',
                  boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
                  border: `3px solid ${metric.color}`,
                  textAlign: 'center'
                }}>
                  <metric.icon size={36} color={metric.color} style={{ marginBottom: '10px' }} />
                  <div style={{ fontSize: '14px', color: '#666', marginBottom: '8px' }}>
                    {metric.label}
                  </div>
                  <div style={{ fontSize: '32px', fontWeight: 'bold', color: metric.color }}>
                    {metric.value}
                  </div>
                </div>
              ))}
            </div>

            {/* Insights Cards */}
            <div style={{ 
              display: 'grid', 
              gridTemplateColumns: 'repeat(3, 1fr)', 
              gap: '20px',
              marginBottom: '30px'
            }}>
              {insights.map((insight, idx) => (
                <div key={idx} style={{
                  background: 'white',
                  borderLeft: `5px solid ${insight.color}`,
                  padding: '20px',
                  borderRadius: '8px',
                  boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
                }}>
                  <h3 style={{ fontSize: '16px', marginBottom: '10px', color: COLORS.dark }}>
                     {insight.title}
                  </h3>
                  <div style={{ 
                    fontSize: '28px', 
                    fontWeight: 'bold', 
                    color: insight.color,
                    margin: '10px 0'
                  }}>
                    {insight.stat}
                  </div>
                  <p style={{ fontSize: '13px', color: '#666', lineHeight: '1.6' }}>
                    {insight.description}
                  </p>
                </div>
              ))}
            </div>

            {/* Model Performance */}
            <div style={{ background: 'white', padding: '25px', borderRadius: '12px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <h3 style={{ fontSize: '20px', marginBottom: '20px', color: COLORS.dark, borderBottom: `2px solid ${COLORS.primary}`, paddingBottom: '10px' }}>
                 Model Performance Comparison
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={modelPerformance}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="model" />
                  <YAxis domain={[90, 101]} />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="accuracy" fill={COLORS.primary} name="Accuracy (%)" />
                  <Bar dataKey="precision" fill={COLORS.secondary} name="Precision (%)" />
                  <Bar dataKey="recall" fill={COLORS.success} name="Recall (%)" />
                  <Bar dataKey="f1" fill={COLORS.warning} name="F1-Score (%)" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        )}

        {/* INSIGHT 1 TAB */}
        {activeTab === 'insight1' && (
          <div>
            <div style={{ 
              background: `linear-gradient(135deg, ${COLORS.success} 0%, #0d5a4a 100%)`,
              color: 'white',
              padding: '20px',
              borderRadius: '12px',
              marginBottom: '30px'
            }}>
              <h2 style={{ fontSize: '24px', marginBottom: '10px' }}>
                 Insight 1: Early Reviews Highly Predict 1-Year Success
              </h2>
              <p style={{ fontSize: '16px', opacity: 0.9 }}>
                Correlation of 0.976 between early (100 reviews) and 1-year ratings | 96.8% Classification Accuracy
              </p>
            </div>

            {/* Stats Grid */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '20px', marginBottom: '30px' }}>
              <div style={{ background: 'white', padding: '20px', borderRadius: '8px', textAlign: 'center', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <div style={{ fontSize: '14px', color: '#666' }}>Correlation</div>
                <div style={{ fontSize: '36px', fontWeight: 'bold', color: COLORS.success }}>0.976</div>
                <div style={{ fontSize: '12px', color: '#999' }}>Extremely Strong</div>
              </div>
              <div style={{ background: 'white', padding: '20px', borderRadius: '8px', textAlign: 'center', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <div style={{ fontSize: '14px', color: '#666' }}>Products Stable</div>
                <div style={{ fontSize: '36px', fontWeight: 'bold', color: COLORS.primary }}>73.2%</div>
                <div style={{ fontSize: '12px', color: '#999' }}>±0.1 star change</div>
              </div>
              <div style={{ background: 'white', padding: '20px', borderRadius: '8px', textAlign: 'center', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <div style={{ fontSize: '14px', color: '#666' }}>Best Model</div>
                <div style={{ fontSize: '36px', fontWeight: 'bold', color: COLORS.secondary }}>96.8%</div>
                <div style={{ fontSize: '12px', color: '#999' }}>Random Forest</div>
              </div>
            </div>

            {/* Model Performance Table */}
            <div style={{ background: 'white', padding: '25px', borderRadius: '12px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <h3 style={{ fontSize: '18px', marginBottom: '15px', color: COLORS.dark }}>
                Model Performance Metrics
              </h3>
              <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr style={{ background: COLORS.dark, color: 'white' }}>
                    <th style={{ padding: '12px', textAlign: 'left' }}>Model</th>
                    <th style={{ padding: '12px', textAlign: 'center' }}>Accuracy</th>
                    <th style={{ padding: '12px', textAlign: 'center' }}>Precision</th>
                    <th style={{ padding: '12px', textAlign: 'center' }}>Recall</th>
                    <th style={{ padding: '12px', textAlign: 'center' }}>F1-Score</th>
                    <th style={{ padding: '12px', textAlign: 'center' }}>AUC-ROC</th>
                  </tr>
                </thead>
                <tbody>
                  {modelPerformance.map((model, idx) => (
                    <tr key={idx} style={{ borderBottom: '1px solid #ddd', background: idx === 1 ? '#f0f8ff' : 'white' }}>
                      <td style={{ padding: '12px', fontWeight: idx === 1 ? 'bold' : 'normal' }}>{model.model}</td>
                      <td style={{ padding: '12px', textAlign: 'center' }}>{model.accuracy}%</td>
                      <td style={{ padding: '12px', textAlign: 'center', background: model.precision === 100 ? '#d4edda' : 'transparent', fontWeight: model.precision === 100 ? 'bold' : 'normal' }}>{model.precision}%</td>
                      <td style={{ padding: '12px', textAlign: 'center' }}>{model.recall}%</td>
                      <td style={{ padding: '12px', textAlign: 'center' }}>{model.f1}%</td>
                      <td style={{ padding: '12px', textAlign: 'center' }}>{model.auc}%</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}

        {/* INSIGHT 2 TAB */}
        {activeTab === 'insight2' && (
          <div>
            <div style={{ 
              background: `linear-gradient(135deg, ${COLORS.warning} 0%, #c99200 100%)`,
              color: COLORS.dark,
              padding: '20px',
              borderRadius: '12px',
              marginBottom: '30px'
            }}>
              <h2 style={{ fontSize: '24px', marginBottom: '10px' }}>
                 Insight 2: Rating Volatility is Critical Warning Signal
              </h2>
              <p style={{ fontSize: '16px' }}>
                Volatility contributes 25.5% to predictions | Combined Rule: 91.2% Precision, 95% Recall
              </p>
            </div>

            {/* Feature Importance */}
            <div style={{ background: 'white', padding: '25px', borderRadius: '12px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <h3 style={{ fontSize: '18px', marginBottom: '20px', color: COLORS.dark }}>
                 Feature Importance Rankings
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={featureImportance} layout="vertical">
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis type="number" domain={[0, 0.35]} />
                  <YAxis dataKey="feature" type="category" width={150} />
                  <Tooltip />
                  <Bar dataKey="importance" fill={COLORS.secondary}>
                    {featureImportance.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={index === 1 ? COLORS.warning : COLORS.secondary} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Alert System Performance */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
              <div style={{ background: 'white', padding: '25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <h3 style={{ fontSize: '18px', marginBottom: '20px', color: COLORS.dark }}>
                  Alert Distribution
                </h3>
                <ResponsiveContainer width="100%" height={250}>
                  <PieChart>
                    <Pie
                      data={alertDistribution}
                      cx="50%"
                      cy="50%"
                      outerRadius={80}
                      fill="#8884d8"
                      dataKey="value"
                      label={({ name, value }) => `${name}: ${value}`}
                    >
                      {alertDistribution.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
              </div>

              <div style={{ background: 'white', padding: '25px', borderRadius: '12px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
                <h3 style={{ fontSize: '18px', marginBottom: '20px', color: COLORS.dark }}>
                   Recommended Warning Rule
                </h3>
                <div style={{ 
                  background: '#fff3cd', 
                  border: `3px solid ${COLORS.warning}`,
                  borderRadius: '8px',
                  padding: '20px',
                  marginBottom: '15px'
                }}>
                  <p style={{ fontSize: '16px', fontWeight: 'bold', color: COLORS.dark, marginBottom: '10px' }}>
                    IF early_avg_rating &lt; 4.0 AND volatility &gt; 1.0
                  </p>
                  <p style={{ fontSize: '14px', color: '#666' }}>
                    → FLAG AS HIGH RISK
                  </p>
                </div>
                <div style={{ fontSize: '14px', color: '#666' }}>
                  <div> Precision: <strong>91.2%</strong></div>
                  <div> Recall: <strong>95.0%</strong></div>
                  <div> Flags: <strong>125 products (26.5%)</strong></div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* INSIGHT 3 TAB */}
        {activeTab === 'insight3' && (
          <div>
            <div style={{ 
              background: `linear-gradient(135deg, ${COLORS.danger} 0%, #8b1a04 100%)`,
              color: 'white',
              padding: '20px',
              borderRadius: '12px',
              marginBottom: '30px'
            }}>
              <h2 style={{ fontSize: '24px', marginBottom: '10px' }}>
                 Insight 3: Beauty Products Have 3X Higher Failure Risk
              </h2>
              <p style={{ fontSize: '16px', opacity: 0.9 }}>
                Beauty: 31.7% Failure Rate vs Electronics/Pets: ~11%
              </p>
            </div>

            {/* Category Failure Rate */}
            <div style={{ background: 'white', padding: '25px', borderRadius: '12px', marginBottom: '20px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
              <h3 style={{ fontSize: '18px', marginBottom: '20px', color: COLORS.dark }}>
                 Failure Rate by Category
              </h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={categoryFailureRate}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="category" />
                  <YAxis label={{ value: '% Products Ending <4.0', angle: -90, position: 'insideLeft' }} />
                  <Tooltip />
                  <Bar dataKey="rate">
                    {categoryFailureRate.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Bar>
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Category Recommendations */}
            <div style={{ 
              display: 'grid', 
              gridTemplateColumns: 'repeat(3, 1fr)', 
              gap: '20px'
            }}>
              {[
                { cat: 'Beauty', rate: '31.7%', threshold: '<3.86', risk: 'HIGH', color: COLORS.danger },
                { cat: 'Electronics', rate: '11.7%', threshold: '<3.84', risk: 'MEDIUM', color: COLORS.warning },
                { cat: 'Pet Supplies', rate: '11.4%', threshold: 'Monitor', risk: 'LOW', color: COLORS.success }
              ].map((item, idx) => (
                <div key={idx} style={{
                  background: 'white',
                  border: `3px solid ${item.color}`,
                  padding: '20px',
                  borderRadius: '12px',
                  boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
                }}>
                  <h4 style={{ fontSize: '16px', marginBottom: '10px', color: COLORS.dark }}>
                    {item.cat}
                  </h4>
                  <div style={{ fontSize: '28px', fontWeight: 'bold', color: item.color, marginBottom: '10px' }}>
                    {item.rate}
                  </div>
                  <div style={{ fontSize: '13px', color: '#666' }}>
                    <div>Failure Rate</div>
                    <div style={{ marginTop: '10px', fontWeight: 'bold', color: item.color }}>
                      Risk: {item.risk}
                    </div>
                    <div style={{ marginTop: '5px' }}>
                      Threshold: {item.threshold}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Footer */}
      <div style={{ 
        background: COLORS.dark, 
        color: 'white', 
        padding: '20px', 
        textAlign: 'center',
        marginTop: '40px'
      }}>
        <p style={{ fontSize: '14px', opacity: 0.8 }}>
          Amazon Product Success Prediction | Data: 2015-2023 | Analysis: K-means Clustering, Random Forest, Gradient Boosting
        </p>
      </div>
    </div>
  );
};

export default AmazonDashboard;# Amazon-Product-Success-Dashboard
