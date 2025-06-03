import json
import os
from jinja2 import Environment, FileSystemLoader

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Enhanced institutional-grade documentation content
documentation_content = """
<div class="hero-section">
    <div class="hero-content">
        <h1 class="hero-title">Value & Quality Stock Selection Model</h1>
        <p class="hero-subtitle">Institutional-Grade Quantamental Investment Strategy</p>
        <div class="hero-performance">
            <div class="perf-metric">
                <span class="perf-number">191%</span>
                <span class="perf-label">Peak Return Q1 2020</span>
            </div>
            <div class="perf-metric">
                <span class="perf-number">89%</span>
                <span class="perf-label">Precision Rate</span>
            </div>
            <div class="perf-metric">
                <span class="perf-number">0.71</span>
                <span class="perf-label">ROC AUC</span>
            </div>
        </div>
    </div>
</div>

<div class="doc-section">
    <h2>Technical Documentation</h2>
    
    <div class="section-card">
        <h3><i class="fas fa-chart-line"></i> Background</h3>
        <p>This machine learning system implements a <strong>quantamental approach</strong> to identify potentially undervalued stocks by combining value investing principles with quality metrics. The methodology builds upon academic research in machine learning-based stock selection, with significant enhancements for practical deployment at institutional scale.</p>
        
        <p>The system analyzes thousands of US-listed companies quarterly to identify stocks exhibiting both value characteristics (trading below intrinsic value) and quality characteristics (strong fundamentals), specifically targeting stocks likely to achieve <strong>20%+ returns</strong> while avoiding severe underperformers.</p>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-lightbulb"></i> Investment Philosophy</h3>
        <p>The model is built on three core principles:</p>
        
        <div class="philosophy-grid">
            <div class="philosophy-item">
                <div class="philosophy-icon">
                    <i class="fas fa-search-dollar"></i>
                </div>
                <h4>Dynamic Value Assessment</h4>
                <p>Stocks occasionally trade below intrinsic value due to market inefficiencies. The system uses multiple valuation metrics relative to industry-specific and company-specific historical distributions to identify potentially undervalued securities.</p>
            </div>
            
            <div class="philosophy-item">
                <div class="philosophy-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h4>Quality-Filtered Selection</h4>
                <p>Not all cheap stocks represent good investments. Quality metrics distinguish between temporarily undervalued high-quality businesses and structurally challenged companies trading at justifiably low valuations.</p>
            </div>
            
            <div class="philosophy-item">
                <div class="philosophy-icon">
                    <i class="fas fa-cogs"></i>
                </div>
                <h4>Regime-Aware Factor Weighting</h4>
                <p>The model adapts its factor emphasis based on macroeconomic conditions and market cycles, optimizing performance across different investment environments.</p>
            </div>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-microscope"></i> Advanced Methodology</h3>
        
        <div class="methodology-subsection">
            <h4><i class="fas fa-database"></i> Data Infrastructure</h4>
            <p>The model processes comprehensive datasets including:</p>
            <ul class="enhanced-list">
                <li>Quarterly financial data from US public companies (2000-present)</li>
                <li>Real-time market capitalization and pricing data</li>
                <li>Industry classifications with 29 proprietary sector groupings</li>
                <li>Macroeconomic indicators (GDP, unemployment, fed funds rate, yield spreads)</li>
                <li>Alternative data sources for sentiment and positioning analysis</li>
            </ul>
        </div>

        <div class="methodology-subsection">
            <h4><i class="fas fa-microchip"></i> Sophisticated Feature Engineering</h4>
            
            <div class="feature-category">
                <h5><span class="category-badge valuation">Valuation</span> Dynamic Valuation Features</h5>
                <p>The system implements industry-leading valuation analysis through:</p>
                <ul class="feature-list">
                    <li><strong>Multi-Horizon Valuation Percentiles:</strong> Current valuation metrics compared to 5-year rolling industry distributions and company-specific historical percentile rankings</li>
                    <li><strong>Cross-validation of valuation measures:</strong> P/E, P/B, P/TB, P/FCF, EV/EBIT, EV/EBITDA</li>
                    <li><strong>Alpha Correlation Analysis:</strong> Proprietary "alpha correlation" metrics measuring historical relationships between low valuations and small market capitalizations</li>
                    <li><strong>Dynamic selection:</strong> Optimal valuation metrics based on predictive power within each industry</li>
                    <li><strong>Company-specific correlation analysis:</strong> Enhanced precision through individual company analysis</li>
                </ul>
            </div>

            <div class="feature-category">
                <h5><span class="category-badge quality">Quality</span> Advanced Quality Assessment</h5>
                <p><strong>Comprehensive Quality Framework:</strong></p>
                <ul class="feature-list">
                    <li>Enhanced Piotroski F-Score with additional factors</li>
                    <li>Industry-ranked quality metrics (ROIC, ROE, asset efficiency)</li>
                    <li>Multi-period growth consistency analysis (10-year CAGR assessments)</li>
                    <li>Cash flow persistence scoring with FCF vs. Net Income analysis</li>
                </ul>
                
                <p><strong>Proprietary Composite Scores:</strong></p>
                <ul class="feature-list">
                    <li><strong>Contrarian Sentiment:</strong> Identifies value/quality disconnects</li>
                    <li><strong>Neglected Stock Indicator:</strong> Targets overlooked small/mid-cap opportunities</li>
                    <li><strong>Growth Consistency Score:</strong> Evaluates sustainable growth patterns</li>
                    <li><strong>Quality-Value Composite:</strong> Weighted combination of value and quality signals</li>
                </ul>
            </div>

            <div class="feature-category">
                <h5><span class="category-badge macro">Macro</span> Macroeconomic Integration</h5>
                <ul class="feature-list">
                    <li><strong>Economic Cycle Positioning:</strong> Dynamic regime classification (Early/Mid/Late/Transitional cycle)</li>
                    <li><strong>Interest rate sensitivity analysis:</strong> For valuation multiples</li>
                    <li><strong>Volatility-adjusted macro factor weighting:</strong> Adaptive to market conditions</li>
                </ul>
            </div>
        </div>

        <div class="methodology-subsection">
            <h4><i class="fas fa-brain"></i> Machine Learning Architecture</h4>
            
            <div class="ml-highlight">
                <h5>Ensemble Model Design</h5>
                <p>The system employs a sophisticated <strong>10-model ensemble approach:</strong></p>
                <div class="model-spec">
                    <p><strong>Investment Grade Model:</strong> K-fold cross-validation with temporal splitting, Gradient Boosted Tree Classifiers optimized for ROC-AUC, Hyperparameter tuning with L1/L2 regularization</p>
                </div>
            </div>

            <div class="validation-highlight">
                <h5>Advanced Validation Framework</h5>
                <ul class="validation-list">
                    <li><strong>Out-of-Time Validation:</strong> 6-fold temporal cross-validation (K1-K6)</li>
                    <li><strong>Data allocation:</strong> 16.7% per fold with strict temporal ordering prevents data leakage</li>
                    <li><strong>Conservative ensemble averaging:</strong> Excluding most recent fold</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-chart-bar"></i> Performance Metrics (2020-2023 Out-of-Time Validation)</h3>
        
        <div class="performance-container">
            <div class="performance-image">
                <img src="image.png" alt="Model Performance Chart 2020-2023" class="perf-chart" />
            </div>
            
            <div class="risk-metrics-grid">
                <div class="risk-metric">
                    <span class="metric-label">Average Portfolio Size</span>
                    <span class="metric-value">50 companies</span>
                </div>
                <div class="risk-metric">
                    <span class="metric-label">Selection Rate</span>
                    <span class="metric-value">Top 1-2% quarterly</span>
                </div>
                <div class="risk-metric">
                    <span class="metric-label">Volatility</span>
                    <span class="metric-value">Higher than benchmark</span>
                </div>
                <div class="risk-metric">
                    <span class="metric-label">Compound Alpha</span>
                    <span class="metric-value">Substantial outperformance</span>
                </div>
            </div>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-cog"></i> Implementation Framework</h3>
        
        <div class="implementation-grid">
            <div class="impl-section">
                <h4><i class="fas fa-sync"></i> Quarterly Rebalancing</h4>
                <ul class="impl-list">
                    <li>Model refresh every quarter using latest financial data</li>
                    <li>Top 50 recommendations selected from ensemble rankings</li>
                    <li>Equal-weight position sizing to reduce sector bias</li>
                </ul>
            </div>

            <div class="impl-section">
                <h4><i class="fas fa-shield-check"></i> Risk Management</h4>
                <ul class="impl-list">
                    <li>Exclusion of micro-cap stocks (market cap >$250M minimum)</li>
                    <li>Underperform probability filtering (<50th percentile threshold)</li>
                    <li>Industry diversification monitoring</li>
                </ul>
            </div>

            <div class="impl-section">
                <h4><i class="fas fa-play-circle"></i> Execution Protocol</h4>
                <ul class="impl-list">
                    <li>Purchase recommendations at start of following quarter</li>
                    <li>12-month holding period</li>
                    <li>Systematic rebalancing and position management</li>
                </ul>
            </div>
        </div>

        <div class="screening-criteria">
            <h4><i class="fas fa-filter"></i> Advanced Screening Criteria</h4>
            <p><strong>Final Selection Requirements:</strong></p>
            <ul class="criteria-list">
                <li>High ensemble investment grade probability (top 1-2% universe)</li>
                <li>Low ensemble underperform probability (<50th percentile)</li>
                <li>Minimum market capitalization thresholds</li>
                <li>Adequate trading liquidity</li>
                <li>Quality score minimum thresholds</li>
            </ul>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-star"></i> Key Differentiators</h3>
        
        <div class="differentiators-grid">
            <div class="diff-item">
                <div class="diff-number">1</div>
                <div class="diff-content">
                    <h4>Dynamic Valuation Selection</h4>
                    <p>Proprietary algorithm selects optimal valuation metric per company/industry based on historical alpha correlation</p>
                </div>
            </div>
            
            <div class="diff-item">
                <div class="diff-number">2</div>
                <div class="diff-content">
                    <h4>Ensemble Risk Management</h4>
                    <p>Dual-model approach with investment grade and underperform prediction</p>
                </div>
            </div>
            
            <div class="diff-item">
                <div class="diff-number">3</div>
                <div class="diff-content">
                    <h4>Regime Adaptation</h4>
                    <p>Macroeconomic factor integration with cycle-aware weighting</p>
                </div>
            </div>
            
            <div class="diff-item">
                <div class="diff-number">4</div>
                <div class="diff-content">
                    <h4>Temporal Validation</h4>
                    <p>Strict out-of-time testing preventing data snooping bias</p>
                </div>
            </div>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-crystal-ball"></i> Expected Forward Performance</h3>
        <div class="forward-performance-placeholder">
            <p class="performance-note">Forward performance expectations based on historical validation and market conditions analysis.</p>
        </div>
    </div>

    <div class="section-card">
        <h3><i class="fas fa-book"></i> Glossary of Key Metrics</h3>
        
        <div class="glossary-grid">
            <div class="glossary-section">
                <h4><span class="category-badge valuation">Value Metrics</span></h4>
                <dl class="glossary-list">
                    <dt>Valuation Multiple Percentile</dt>
                    <dd>Where current valuation stands in historical distribution (lower is better)</dd>
                </dl>
            </div>

            <div class="glossary-section">
                <h4><span class="category-badge quality">Quality Metrics</span></h4>
                <dl class="glossary-list">
                    <dt>F-Score</dt>
                    <dd>Piotroski's 9-point framework for financial strength (higher is better)</dd>
                    <dt>ROIC</dt>
                    <dd>Return on Invested Capital, measuring capital allocation efficiency</dd>
                    <dt>Cash Flow Persistence</dt>
                    <dd>Consistency of cash generation relative to earnings</dd>
                    <dt>Growth Consistency</dt>
                    <dd>Stability of growth across equity, earnings, and revenue</dd>
                </dl>
            </div>

            <div class="glossary-section">
                <h4><span class="category-badge combined">Combined Metrics</span></h4>
                <dl class="glossary-list">
                    <dt>Contrarian Sentiment</dt>
                    <dd>Measures disagreement between valuation and quality indicators</dd>
                    <dt>Neglected Stock Indicator</dt>
                    <dd>Identifies overlooked smaller companies with strong fundamentals</dd>
                    <dt>Quality-Value Composite</dt>
                    <dd>Weighted combination of value and quality signals</dd>
                </dl>
            </div>
        </div>
    </div>
</div>
"""

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ header_text }}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-navy: #0F172A;
            --primary-blue: #1E40AF;
            --primary-light: #3B82F6;
            --accent-blue: #60A5FA;
            --accent-cyan: #06B6D4;
            --success-green: #10B981;
            --warning-amber: #F59E0B;
            --danger-red: #EF4444;
            --neutral-50: #F8FAFC;
            --neutral-100: #F1F5F9;
            --neutral-200: #E2E8F0;
            --neutral-300: #CBD5E1;
            --neutral-400: #94A3B8;
            --neutral-500: #64748B;
            --neutral-600: #475569;
            --neutral-700: #334155;
            --neutral-800: #1E293B;
            --neutral-900: #0F172A;
            --gradient-primary: linear-gradient(135deg, var(--primary-navy) 0%, var(--primary-blue) 100%);
            --gradient-accent: linear-gradient(135deg, var(--primary-blue) 0%, var(--accent-blue) 100%);
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
            --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            --border-radius: 8px;
            --border-radius-lg: 12px;
            --border-radius-xl: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--neutral-50);
            color: var(--neutral-900);
            line-height: 1.6;
            font-size: 14px;
            scroll-behavior: smooth;
        }

        /* HEADER STYLES */
        header {
            background: var(--gradient-primary);
            color: white;
            padding: 1.5rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-lg);
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(10px);
        }

        .header-content h1 {
            font-weight: 800;
            font-size: 1.875rem;
            letter-spacing: -0.025em;
            margin-bottom: 0.25rem;
        }

        .header-subtitle {
            font-size: 0.875rem;
            opacity: 0.85;
            font-weight: 400;
        }

        .header-logo {
            height: 50px;
            opacity: 0.9;
        }

        /* MAIN CONTAINER */
        .main-container {
            max-width: 1800px;
            margin: 0 auto;
            display: flex;
            min-height: calc(100vh - 108px);
        }

        /* SIDEBAR STYLES */
        .sidebar {
            width: 320px;
            background: white;
            box-shadow: var(--shadow-md);
            height: calc(100vh - 108px);
            overflow-y: auto;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            flex-shrink: 0;
            border-right: 1px solid var(--neutral-200);
        }

        .sidebar-collapsed {
            width: 80px;
        }

        .sidebar-header {
            padding: 2rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--neutral-200);
            background: var(--neutral-50);
        }

        .sidebar-title {
            font-weight: 600;
            font-size: 1.125rem;
            color: var(--neutral-900);
            white-space: nowrap;
            overflow: hidden;
        }

        .collapse-btn {
            cursor: pointer;
            color: var(--primary-blue);
            background: none;
            border: none;
            font-size: 1.25rem;
            padding: 0.5rem;
            border-radius: var(--border-radius);
            transition: all 0.2s;
        }

        .collapse-btn:hover {
            background-color: var(--neutral-100);
        }

        .nav-menu {
            list-style: none;
            padding: 1rem 0;
        }

        .nav-item {
            margin-bottom: 0.25rem;
        }

        .nav-link {
            display: flex;
            align-items: center;
            padding: 1rem 1.5rem;
            color: var(--neutral-600);
            text-decoration: none;
            transition: all 0.3s;
            border-left: 3px solid transparent;
            font-weight: 500;
        }

        .nav-link:hover,
        .nav-link.active {
            background-color: var(--neutral-100);
            color: var(--primary-blue);
            border-left-color: var(--primary-blue);
        }

        .nav-icon {
            margin-right: 1rem;
            font-size: 1.25rem;
            width: 24px;
            text-align: center;
        }

        .nav-text {
            white-space: nowrap;
            overflow: hidden;
            transition: all 0.3s;
        }

        .sidebar-collapsed .nav-text {
            opacity: 0;
            width: 0;
        }

        /* CONTENT AREA STYLES */
        .content-area {
            flex-grow: 1;
            height: calc(100vh - 108px);
            overflow-y: auto;
            display: flex;
            flex-direction: column;
        }

        .tab-buttons {
            display: flex;
            gap: 4px;
            background: white;
            padding: 1rem 1.5rem;
            overflow-x: auto;
            border-bottom: 1px solid var(--neutral-200);
            box-shadow: var(--shadow-sm);
        }

        .tab-btn {
            padding: 0.75rem 1.5rem;
            border: 2px solid transparent;
            border-radius: var(--border-radius);
            background: var(--neutral-100);
            color: var(--neutral-600);
            font-weight: 500;
            font-size: 0.875rem;
            cursor: pointer;
            min-width: 140px;
            text-align: center;
            transition: all 0.2s;
            white-space: nowrap;
        }

        .tab-btn:hover {
            background: var(--neutral-200);
            color: var(--neutral-700);
        }

        .tab-btn.active {
            background: var(--primary-blue);
            color: white;
            border-color: var(--primary-navy);
            box-shadow: var(--shadow-md);
        }

        .tab-content-container {
            flex-grow: 1;
            position: relative;
            overflow: hidden;
        }

        .tab-content {
            display: none;
            height: 100%;
            overflow: auto;
        }

        .tab-content.active {
            display: flex;
            flex-direction: column;
        }

        .dashboard-iframe-wrapper {
            flex-grow: 1;
            height: 100%;
            background: white;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        .open-tab-btn {
            display: inline-block;
            margin: 1rem 1.5rem;
            padding: 0.75rem 1.25rem;
            background: var(--primary-blue);
            color: white;
            text-decoration: none;
            border-radius: var(--border-radius);
            font-weight: 500;
            font-size: 0.875rem;
            transition: all 0.2s;
            box-shadow: var(--shadow-sm);
        }

        .open-tab-btn:hover {
            background: var(--primary-navy);
            box-shadow: var(--shadow-md);
        }

        /* DOCUMENTATION STYLES */
        .documentation {
            padding: 0;
            max-height: 100%;
            overflow-y: auto;
            background: var(--neutral-50);
        }

        /* Hero Section */
        .hero-section {
            background: var(--gradient-primary);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
        }

        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1rem;
            letter-spacing: -0.025em;
        }

        .hero-subtitle {
            font-size: 1.25rem;
            opacity: 0.9;
            margin-bottom: 3rem;
            font-weight: 400;
        }

        .hero-performance {
            display: flex;
            justify-content: center;
            gap: 4rem;
            flex-wrap: wrap;
        }

        .perf-metric {
            text-align: center;
        }

        .perf-number {
            display: block;
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--accent-cyan);
            margin-bottom: 0.5rem;
        }

        .perf-label {
            font-size: 0.875rem;
            opacity: 0.8;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* Documentation Content */
        .doc-section {
            max-width: 1200px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }

        .doc-section h2 {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--neutral-900);
            margin-bottom: 3rem;
            text-align: center;
        }

        .section-card {
            background: white;
            border-radius: var(--border-radius-xl);
            padding: 3rem;
            margin-bottom: 3rem;
            box-shadow: var(--shadow-lg);
            border: 1px solid var(--neutral-200);
        }

        .section-card h3 {
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--neutral-900);
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .section-card h3 i {
            color: var(--primary-blue);
        }

        .section-card h4 {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--neutral-800);
            margin: 2rem 0 1rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .section-card h5 {
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--neutral-700);
            margin: 1.5rem 0 1rem;
        }

        .section-card p {
            color: var(--neutral-600);
            margin-bottom: 1.5rem;
            line-height: 1.7;
        }

        /* Philosophy Grid */
        .philosophy-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .philosophy-item {
            background: var(--neutral-50);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            text-align: center;
            border: 1px solid var(--neutral-200);
            transition: all 0.3s;
        }

        .philosophy-item:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-lg);
        }

        .philosophy-icon {
            width: 80px;
            height: 80px;
            background: var(--gradient-accent);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
        }

        .philosophy-icon i {
            font-size: 2rem;
            color: white;
        }

        .philosophy-item h4 {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--neutral-900);
            margin-bottom: 1rem;
        }

        .philosophy-item p {
            color: var(--neutral-600);
            line-height: 1.6;
        }

        /* Lists */
        .enhanced-list,
        .feature-list,
        .impl-list,
        .criteria-list,
        .validation-list {
            list-style: none;
            margin: 1.5rem 0;
        }

        .enhanced-list li,
        .feature-list li,
        .impl-list li,
        .criteria-list li,
        .validation-list li {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 0.75rem;
            color: var(--neutral-600);
            line-height: 1.6;
        }

        .enhanced-list li::before,
        .feature-list li::before,
        .impl-list li::before,
        .criteria-list li::before,
        .validation-list li::before {
            content: "▸";
            position: absolute;
            left: 0;
            color: var(--primary-blue);
            font-weight: 600;
        }

        /* Category Badges */
        .category-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-right: 0.75rem;
        }

        .category-badge.valuation {
            background: #EEF2FF;
            color: var(--primary-blue);
        }

        .category-badge.quality {
            background: #ECFDF5;
            color: var(--success-green);
        }

        .category-badge.macro {
            background: #FEF3C7;
            color: var(--warning-amber);
        }

        .category-badge.combined {
            background: #F0F9FF;
            color: var(--accent-cyan);
        }

        /* Feature Categories */
        .feature-category {
            background: var(--neutral-50);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid var(--primary-blue);
        }

        /* ML Architecture */
        .ml-highlight,
        .validation-highlight {
            background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid var(--neutral-200);
        }

        .model-spec {
            background: var(--neutral-900);
            color: white;
            padding: 1.5rem;
            border-radius: var(--border-radius);
            margin: 1rem 0;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.875rem;
        }

        /* Performance Container */
        .performance-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
            margin: 2rem 0;
        }

        .perf-chart {
            width: 100%;
            height: auto;
            border-radius: var(--border-radius-lg);
            box-shadow: var(--shadow-md);
        }

        .risk-metrics-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
        }

        .risk-metric {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem;
            background: var(--neutral-50);
            border-radius: var(--border-radius);
            border: 1px solid var(--neutral-200);
        }

        .metric-label {
            font-weight: 500;
            color: var(--neutral-700);
        }

        .metric-value {
            font-weight: 600;
            color: var(--neutral-900);
        }

        /* Implementation Grid */
        .implementation-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .impl-section {
            background: var(--neutral-50);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            border: 1px solid var(--neutral-200);
        }

        .impl-section h4 {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            color: var(--neutral-900);
        }

        .impl-section i {
            color: var(--primary-blue);
        }

        /* Screening Criteria */
        .screening-criteria {
            background: linear-gradient(135deg, #FEF7FF 0%, #FAF5FF 100%);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid var(--accent-cyan);
        }

        /* Differentiators */
        .differentiators-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .diff-item {
            display: flex;
            align-items: flex-start;
            gap: 1.5rem;
            padding: 2rem;
            background: var(--neutral-50);
            border-radius: var(--border-radius-lg);
            border: 1px solid var(--neutral-200);
            transition: all 0.3s;
        }

        .diff-item:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .diff-number {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            background: var(--gradient-accent);
            color: white;
            border-radius: 50%;
            font-size: 1.25rem;
            font-weight: 700;
            flex-shrink: 0;
        }

        .diff-content h4 {
            font-size: 1.125rem;
            font-weight: 600;
            color: var(--neutral-900);
            margin-bottom: 0.5rem;
        }

        .diff-content p {
            color: var(--neutral-600);
            line-height: 1.6;
        }

        /* Forward Performance */
        .forward-performance-placeholder {
            background: var(--neutral-100);
            border-radius: var(--border-radius-lg);
            padding: 3rem;
            text-align: center;
            border: 2px dashed var(--neutral-300);
        }

        .performance-note {
            color: var(--neutral-500);
            font-style: italic;
        }

        /* Glossary */
        .glossary-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .glossary-section {
            background: var(--neutral-50);
            border-radius: var(--border-radius-lg);
            padding: 2rem;
            border: 1px solid var(--neutral-200);
        }

        .glossary-section h4 {
            display: flex;
            align-items: center;
            margin-bottom: 1.5rem;
            color: var(--neutral-900);
        }

        .glossary-list {
            margin: 0;
        }

        .glossary-list dt {
            font-weight: 600;
            color: var(--neutral-900);
            margin-bottom: 0.5rem;
        }

        .glossary-list dd {
            color: var(--neutral-600);
            margin-bottom: 1rem;
            margin-left: 0;
            line-height: 1.6;
        }

        /* Dark Mode Toggle */
        .dark-mode-toggle {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--primary-blue);
            color: white;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: var(--shadow-xl);
            z-index: 1000;
            transition: all 0.3s;
            border: none;
        }

        .dark-mode-toggle:hover {
            background: var(--primary-navy);
            transform: scale(1.05);
        }

        /* Responsive Design */
        @media (max-width: 1024px) {
            .hero-performance {
                gap: 2rem;
            }
            
            .performance-container {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            
            .hero-title {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
                min-height: auto;
            }
            
            .sidebar {
                width: 100%;
                height: auto;
                max-height: 300px;
            }
            
            .sidebar-collapsed {
                height: 80px;
                overflow: hidden;
            }
            
            .content-area {
                height: calc(100vh - 408px);
            }
            
            .hero-section {
                padding: 2rem 1rem;
            }
            
            .hero-title {
                font-size: 2rem;
            }
            
            .hero-performance {
                flex-direction: column;
                gap: 1.5rem;
            }
            
            .doc-section {
                padding: 2rem 1rem;
            }
            
            .section-card {
                padding: 2rem;
            }
            
            .philosophy-grid,
            .implementation-grid,
            .glossary-grid {
                grid-template-columns: 1fr;
            }
            
            .tab-buttons {
                padding: 1rem;
            }
            
            .tab-btn {
                min-width: 120px;
                padding: 0.75rem 1rem;
            }
        }

        @media (max-width: 480px) {
            .hero-title {
                font-size: 1.75rem;
            }
            
            .section-card {
                padding: 1.5rem;
            }
            
            .doc-section {
                padding: 1.5rem 1rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>{{ header_text }}</h1>
            <div class="header-subtitle">Institutional-Grade Quantamental Strategy</div>
        </div>
        {% if logo_url %}
            <img src="{{ logo_url }}" alt="Dashboard Logo" class="header-logo">
        {% endif %}
    </header>
    
    <div class="main-container">
        <div class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title">Navigation</div>
                <button class="collapse-btn">
                    <i class="fas fa-chevron-left"></i>
                </button>
            </div>
            
            <ul class="nav-menu">
                <li class="nav-item">
                    <a href="#" class="nav-link active" data-tab="home">
                        <i class="fas fa-home nav-icon"></i>
                        <span class="nav-text">Overview</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link" data-tab="documentation">
                        <i class="fas fa-file-alt nav-icon"></i>
                        <span class="nav-text">Documentation</span>
                    </a>
                </li>
                {% for tab in tabs %}
                <li class="nav-item">
                    <a href="#" class="nav-link" data-tab="tab-{{ loop.index }}">
                        <i class="fas {% if loop.index == 1 %}fa-chart-line{% elif loop.index == 2 %}fa-microscope{% elif loop.index == 3 %}fa-chart-bar{% elif loop.index == 4 %}fa-brain{% elif loop.index == 5 %}fa-globe{% else %}fa-chart-pie{% endif %} nav-icon"></i>
                        <span class="nav-text">{{ tab.label }}</span>
                    </a>
                </li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="content-area">
            <div class="tab-buttons" role="tablist">
                <button class="tab-btn active" data-tab="home">Overview</button>
                <button class="tab-btn" data-tab="documentation">Documentation</button>
                {% for tab in tabs %}
                <button class="tab-btn" data-tab="tab-{{ loop.index }}">{{ tab.label }}</button>
                {% endfor %}
            </div>
            
            <div class="tab-content-container">
                <!-- Home Tab -->
                <div id="home" class="tab-content active">
                    <div class="documentation">
                        <div class="hero-section">
                            <div class="hero-content">
                                <h1 class="hero-title">Value & Quality Model</h1>
                                <p class="hero-subtitle">Institutional-Grade Quantamental Investment Strategy</p>
                                <div class="hero-performance">
                                    <div class="perf-metric">
                                        <span class="perf-number">191%</span>
                                        <span class="perf-label">Peak Return Q1 2020</span>
                                    </div>
                                    <div class="perf-metric">
                                        <span class="perf-number">89%</span>
                                        <span class="perf-label">Precision Rate</span>
                                    </div>
                                    <div class="perf-metric">
                                        <span class="perf-number">0.71</span>
                                        <span class="perf-label">ROC AUC</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="doc-section">
                            <div class="section-card">
                                <h3><i class="fas fa-bullseye"></i> Executive Summary</h3>
                                <p>This machine learning system implements a <strong>quantamental approach</strong> to identify potentially undervalued stocks by combining value investing principles with quality metrics. The methodology builds upon academic research with significant enhancements for institutional-scale deployment.</p>
                                
                                <p>Our system analyzes thousands of US-listed companies quarterly, targeting stocks likely to achieve <strong>20%+ returns</strong> while avoiding severe underperformers through sophisticated ensemble modeling and risk management.</p>
                            </div>

                            <div class="section-card">
                                <h3><i class="fas fa-compass"></i> Strategic Advantages</h3>
                                
                                <div class="philosophy-grid">
                                    <div class="philosophy-item">
                                        <div class="philosophy-icon">
                                            <i class="fas fa-search-dollar"></i>
                                        </div>
                                        <h4>Dynamic Valuation</h4>
                                        <p>Proprietary algorithms select optimal valuation metrics per company/industry based on historical alpha correlation analysis.</p>
                                    </div>
                                    
                                    <div class="philosophy-item">
                                        <div class="philosophy-icon">
                                            <i class="fas fa-shield-alt"></i>
                                        </div>
                                        <h4>Quality Filtering</h4>
                                        <p>Advanced quality frameworks distinguish between temporarily undervalued businesses and value traps.</p>
                                    </div>
                                    
                                    <div class="philosophy-item">
                                        <div class="philosophy-icon">
                                            <i class="fas fa-brain"></i>
                                        </div>
                                        <h4>Regime Adaptation</h4>
                                        <p>Macroeconomic cycle awareness adapts factor weights based on market conditions and economic environment.</p>
                                    </div>
                                </div>
                            </div>

                            <div class="section-card">
                                <h3><i class="fas fa-trophy"></i> Key Performance Highlights</h3>
                                
                                <div class="implementation-grid">
                                    <div class="impl-section">
                                        <h4><i class="fas fa-chart-line"></i> Crisis Alpha</h4>
                                        <ul class="impl-list">
                                            <li>191% return during Q1 2020 crisis</li>
                                            <li>Consistent outperformance in volatile markets</li>
                                            <li>Superior downside protection</li>
                                        </ul>
                                    </div>

                                    <div class="impl-section">
                                        <h4><i class="fas fa-target"></i> Precision</h4>
                                        <ul class="impl-list">
                                            <li>89% accuracy in identifying 20%+ returns</li>
                                            <li>Conservative selection approach</li>
                                            <li>Top 1-2% universe quarterly</li>
                                        </ul>
                                    </div>

                                    <div class="impl-section">
                                        <h4><i class="fas fa-cogs"></i> Systematic Process</h4>
                                        <ul class="impl-list">
                                            <li>Quarterly rebalancing protocol</li>
                                            <li>50-company equal-weight portfolios</li>
                                            <li>12-month systematic holding periods</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="section-card">
                                <h3><i class="fas fa-route"></i> Getting Started</h3>
                                <ol class="enhanced-list">
                                    <li>Review the <strong>Documentation</strong> tab for detailed methodology and validation results</li>
                                    <li>Explore <strong>Stock Recommendations</strong> for current investment opportunities with probability scores</li>
                                    <li>Analyze <strong>Feature Analysis</strong> to understand proprietary factors driving predictions</li>
                                    <li>Examine <strong>Model Performance</strong> metrics to validate institutional-grade effectiveness</li>
                                    <li>Consider <strong>Market Environment</strong> for macroeconomic context and regime positioning</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Documentation Tab -->
                <div id="documentation" class="tab-content">
                    <div class="documentation">
                        {{ documentation_content|safe }}
                    </div>
                </div>
                
                <!-- Dynamic Tabs for Dashboards -->
                {% for tab in tabs %}
                <div id="tab-{{ loop.index }}" class="tab-content">
                    <a href="{{ tab.url }}" target="_blank" class="open-tab-btn">
                        <i class="fas fa-external-link-alt"></i> Open in New Tab
                    </a>
                    <div class="dashboard-iframe-wrapper">
                        <iframe 
                            src="{{ tab.url }}" 
                            title="{{ tab.label }}" 
                            loading="lazy"
                            sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-storage-access-by-user-activation"
                            allow="fullscreen; clipboard-write; encrypted-media;">
                        </iframe>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    
    <!-- Dark Mode Toggle Button -->
    <button class="dark-mode-toggle" id="dark-mode-toggle">
        <i class="fas fa-moon"></i>
    </button>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Tab Navigation
            const navLinks = document.querySelectorAll('.nav-link');
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');
            
            function setActiveTab(tabId) {
                // Hide all tab contents
                tabContents.forEach(content => {
                    content.classList.remove('active');
                });
                
                // Deactivate all buttons
                tabButtons.forEach(btn => {
                    btn.classList.remove('active');
                    btn.setAttribute('aria-selected', 'false');
                });
                
                // Deactivate all nav links
                navLinks.forEach(link => {
                    link.classList.remove('active');
                });
                
                // Activate selected tab
                const selectedContent = document.getElementById(tabId);
                const selectedTabBtn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
                const selectedNavLink = document.querySelector(`.nav-link[data-tab="${tabId}"]`);
                
                if (selectedContent) selectedContent.classList.add('active');
                if (selectedTabBtn) {
                    selectedTabBtn.classList.add('active');
                    selectedTabBtn.setAttribute('aria-selected', 'true');
                }
                if (selectedNavLink) selectedNavLink.classList.add('active');
            }
            
            // Add click handlers to nav links
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    const tabId = this.getAttribute('data-tab');
                    setActiveTab(tabId);
                });
            });
            
            // Add click handlers to tab buttons
            tabButtons.forEach(button => {
                button.addEventListener('click', function(e) {
                    e.preventDefault();
                    const tabId = this.getAttribute('data-tab');
                    setActiveTab(tabId);
                });
            });
            
            // Sidebar Collapse
            const collapseBtn = document.querySelector('.collapse-btn');
            const sidebar = document.querySelector('.sidebar');
            
            collapseBtn.addEventListener('click', function() {
                sidebar.classList.toggle('sidebar-collapsed');
                
                // Toggle icon direction
                const icon = this.querySelector('i');
                if (sidebar.classList.contains('sidebar-collapsed')) {
                    icon.classList.remove('fa-chevron-left');
                    icon.classList.add('fa-chevron-right');
                } else {
                    icon.classList.remove('fa-chevron-right');
                    icon.classList.add('fa-chevron-left');
                }
            });
            
            // Dark Mode Toggle
            const darkModeToggle = document.getElementById('dark-mode-toggle');
            const body = document.body;
            
            darkModeToggle.addEventListener('click', function() {
                body.classList.toggle('dark-mode');
                const icon = this.querySelector('i');
                
                if (body.classList.contains('dark-mode')) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                    // Apply dark mode styles
                    document.documentElement.style.setProperty('--neutral-50', '#0F172A');
                    document.documentElement.style.setProperty('--neutral-100', '#1E293B');
                    document.documentElement.style.setProperty('--neutral-900', '#F8FAFC');
                } else {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                    // Restore light mode styles
                    document.documentElement.style.setProperty('--neutral-50', '#F8FAFC');
                    document.documentElement.style.setProperty('--neutral-100', '#F1F5F9');
                    document.documentElement.style.setProperty('--neutral-900', '#0F172A');
                }
            });
        });
    </script>
</body>
</html>
"""

# Create the template with Jinja2
template = env.from_string(template_string)

# Create a directory for GitHub Pages deployment
deploy_dir = 'docs'
if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

# Render the template and write to docs/index.html
html_content = template.render(
    header_text=config['header_text'],
    logo_url=config.get('logo_url', ''),
    tabs=config['tabs'],
    documentation_content=documentation_content
)

with open(os.path.join(deploy_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Institutional-grade dashboard generated in {deploy_dir}/index.html")
print("\nKey enhancements include:")
print("✓ Sophisticated navy/blue color scheme suitable for institutional investors")
print("✓ Professional typography with Inter and JetBrains Mono fonts")
print("✓ Enhanced hero section with key performance metrics")
print("✓ Comprehensive technical documentation integration")
print("✓ Advanced responsive design for all devices")
print("✓ Polished animations and micro-interactions")
print("✓ Institutional-grade information architecture")
print("✓ Professional styling with subtle gradients and shadows")
print("\nTo deploy:")
print("1. Add image.png to the docs/ folder")
print("2. Push to GitHub repository")
print("3. Enable GitHub Pages from docs/ folder")
print("4. Access via GitHub Pages URL")
