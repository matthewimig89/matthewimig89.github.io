import json
import os
from jinja2 import Environment, FileSystemLoader

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Create documentation content
documentation_content = """
<h2>Value & Quality Stock Selection Documentation</h2>

<h3>Background</h3>
<p>This dashboard implements a machine learning approach to identify potentially undervalued stocks combining value investing principles with quality metrics. The methodology is inspired by research on machine learning-based stock picking using value investing and quality features, but with important modifications to optimize for practical use. Special thanks to Ronen Priel and Lior Rokach the author of the paper that inspired this work, you can find the paper for free here: https://link.springer.com/article/10.1007/s00521-024-09700-3 .</p>

<p>The system analyzes thousands of US-listed companies on a quarterly basis to identify stocks that exhibit both value characteristics (trading below intrinsic value) and quality characteristics (strong fundamentals), with a focus on predicting significant future returns (20%+) while avoiding severe underperformers.</p>

<h3>Investment Philosophy</h3>
<p>The dashboard is built on three core investment principles:</p>

<ol>
    <li><strong>Value Investing</strong>: Stocks occasionally trade below their intrinsic value due to market inefficiencies, providing opportunities for excess returns. This system uses multiple valuation metrics relative to industry-specific historical norms to identify potentially undervalued securities.</li>
    <li><strong>Quality Assessment</strong>: Not all cheap stocks represent good investments. Quality metrics help distinguish between temporarily undervalued high-quality businesses and structurally challenged companies trading at justifiably low valuations.</li>
    <li><strong>Margin of Safety</strong>: The greater the discount to intrinsic value, the larger the "margin of safety" protecting against valuation errors and providing higher potential returns.</li>
</ol>

<h3>Methodology</h3>

<h4>Data Sources</h4>
<p>The model processes:</p>
<ul>
    <li>Quarterly financial data from US public companies</li>
    <li>Market capitalization and price information</li>
    <li>Industry classifications</li>
    <li>Macroeconomic indicators (GDP, unemployment rate, fed funds rate, yield spread)</li>
</ul>

<h4>Feature Engineering</h4>
<p><strong>Value Features</strong></p>
<p>The system dynamically selects the most appropriate valuation metric for each company based on historical correlations between low valuations and market cap within their industry:</p>
<ul>
    <li>Price/Earnings (P/E)</li>
    <li>Price/Book (P/B)</li>
    <li>Price/Tangible Book (P/TB)</li>
    <li>Price/Free Cash Flow (P/FCF)</li>
    <li>EV/EBIT</li>
    <li>EV/EBITDA</li>
</ul>

<p>For each company, the system:</p>
<ol>
    <li>Calculates the percentile of current valuation multiples within industry-specific historical distributions</li>
    <li>Compares current multiples to historical 25th, 50th, and 75th percentiles</li>
    <li>Assesses valuation "alpha correlations" - measuring how often low valuations coincide with small market caps</li>
    <li>Calculates margin of safety based on the deviation from historical median valuations</li>
</ol>

<p><strong>Quality Features</strong></p>
<p>Quality assessment evaluates:</p>
<ol>
    <li><strong>Profitability</strong>: Return on Equity (ROE), Return on Assets (ROA), Return on Invested Capital (ROIC), Gross profit to total assets</li>
    <li><strong>Financial Health</strong>: Current ratio > 1, Assets exceeding debt, Leverage metrics</li>
    <li><strong>Consistency & Growth</strong>: 5-year earnings consistency, 10-year CAGR for equity, EPS, and revenue, Cash flow generation quality (FCF > Net Income)</li>
    <li><strong>Quality Frameworks</strong>: Piotroski F-Score components, Greenblatt Magic Formula metrics, Graham quality criteria, Grantham quality rank, Mohanram G-Score</li>
    <li><strong>Economic Environment</strong>: Macroeconomic trend indicators, Yield curve analysis, Volatility metrics</li>
</ol>

<h4>Machine Learning Approach</h4>
<p>The system uses two model types:</p>
<ol>
    <li><strong>Investment Grade Prediction</strong>: Predicts stocks likely to achieve 20%+ returns in next 12 months</li>
    <li><strong>Severe Underperform Prediction</strong>: Identifies stocks likely to decline 20%+ in the next 12 months (to be excluded)</li>
</ol>

<p>Each model utilizes:</p>
<ul>
    <li>Gradient Boosting Classifier with L1 and L2 Regularization</li>
    <li>Maximum Tree Depth of 5</li>
    <li>Optimized Tree Depth and Regularization based on Out-of-Time Sample</li>
</ul>

<p>The final stock selection requires:</p>
<ol>
    <li>High probability score from the investment grade model</li>
    <li>Less than 50th percentile probability score from the underperform model</li>
</ol>

<h3>Dashboard Views</h3>

<h4>1. Stock Recommendations</h4>
<p>The primary view presents current stock recommendations with:</p>
<ul>
    <li>Company identifiers and basic information</li>
    <li>Probability scores for significant returns</li>
    <li>Key valuation and quality metrics</li>
    <li>Industry and size categories</li>
</ul>

<h4>2. Feature Analysis</h4>
<p>This view reveals the most influential predictive factors:</p>
<ul>
    <li>Value feature importance</li>
    <li>Quality feature importance</li>
    <li>Feature ranking by SHAP values</li>
    <li>Correlation analysis between features and outcomes</li>
</ul>

<h4>3. Model Performance Metrics</h4>
<p>Track model effectiveness with:</p>
<ul>
    <li>Success rate in identifying 20%+ return stocks</li>
    <li>Average returns of recommended stocks</li>
    <li>Comparison to relevant benchmarks</li>
    <li>Historical precision and recall metrics</li>
</ul>

<h4>4. Market Environment</h4>
<p>Understand broader context with:</p>
<ul>
    <li>Current macroeconomic indicators</li>
    <li>Market cycle positioning</li>
</ul>

<h4>5. Univariate Feature Analysis</h4>
<p>Examine feature distributions with:</p>
<ul>
    <li>List of valuation, quality and economic features sorted then broken out into deciles</li>
    <li>Plot average investment grade (%) vs feature deciles</li>
    <li>Purpose is to observe correlation of predictor with investment grade (%)</li>
</ul>

<h3>Interpretation Guidelines</h3>

<h4>Reading the Recommendations</h4>
<ul>
    <li><strong>High Probability Scores</strong>: Stocks with higher investment grade probability scores have historically shown better performance</li>
    <li><strong>Valuation Metrics</strong>: Lower percentiles indicate more attractive valuations relative to history</li>
    <li><strong>Quality Metrics</strong>: Higher rankings indicate stronger fundamental characteristics</li>
    <li><strong>Combined Metrics</strong>: Focus on stocks showing both value and quality characteristics</li>
</ul>

<h4>Portfolio Development Process</h4>
<ul>
    <li><strong>Diversification</strong>: Model tends to offer a recommendations from a diverse set of industries.</li>
    <li><strong>Position Sizing</strong>: Equal weight position sizing to reduce bias.</li>
    <li><strong>Time Horizon</strong>: Model is optimized for 12 month investment returns. Each quarter purchase top stock recommendations.</li>
    <li><strong>Rebalancing</strong>: Purchase top 30-50 recommendations each quarter, hold for 1 year then sell. Repeat.</li>
</ul>

<h3>Glossary of Key Metrics</h3>

<h4>Value Metrics</h4>
<ul>
    <li><strong>Valuation Multiple Percentile</strong>: Where current valuation stands in historical distribution (lower is better)</li>
    <li><strong>Margin of Safety</strong>: Discount to historical median valuation (higher is better)</li>
    <li><strong>Alpha Correlation</strong>: How often low valuations coincide with small market caps</li>
</ul>

<h4>Quality Metrics</h4>
<ul>
    <li><strong>F-Score</strong>: Piotroski's 9-point framework for financial strength (higher is better)</li>
    <li><strong>ROIC</strong>: Return on Invested Capital, measuring capital allocation efficiency</li>
    <li><strong>Cash Flow Persistence</strong>: Consistency of cash generation relative to earnings</li>
    <li><strong>Growth Consistency</strong>: Stability of growth across equity, earnings, and revenue</li>
</ul>

<h4>Combined Metrics</h4>
<ul>
    <li><strong>Contrarian Sentiment</strong>: Measures disagreement between valuation and quality indicators</li>
    <li><strong>Neglected Stock Indicator</strong>: Identifies overlooked smaller companies with strong fundamentals</li>
    <li><strong>Quality-Value Composite</strong>: Weighted combination of value and quality signals</li>
</ul>
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
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #1565C0;
            --primary-light: #1976D2;
            --primary-dark: #0D47A1;
            --primary-text: #1E293B;
            --secondary-text: #475569;
            --accent-color: #2DD4BF;
            --background-light: #F8FAFC;
            --background-white: #FFFFFF;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
            --border-radius: 8px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            background-color: var(--background-light);
            color: var(--primary-text);
            line-height: 1.5;
        }

        /* HEADER STYLES */
        header {
            background: var(--primary-color);
            background-image: linear-gradient(to right, var(--primary-color), var(--primary-dark));
            color: white;
            padding: 1.25rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-md);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        header h1 {
            font-weight: 600;
            font-size: 1.5rem;
        }

        header img {
            height: 40px;
        }

        /* MAIN CONTAINER */
        .main-container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 0;
            display: flex;
            height: calc(100vh - 73px); /* Subtract header height */
        }

        /* SIDEBAR STYLES */
        .sidebar {
            width: 280px;
            background-color: var(--background-white);
            box-shadow: var(--shadow-sm);
            height: 100%;
            overflow-y: auto;
            transition: all 0.3s;
            flex-shrink: 0;
            border-right: 1px solid rgba(0, 0, 0, 0.1);
            z-index: 5;
        }

        .sidebar-collapsed {
            width: 60px;
        }

        .sidebar-header {
            padding: 1.5rem 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }

        .sidebar-title {
            font-weight: 600;
            font-size: 1.1rem;
            white-space: nowrap;
            overflow: hidden;
        }

        .collapse-btn {
            cursor: pointer;
            color: var(--primary-color);
            background: none;
            border: none;
            font-size: 1.25rem;
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
            padding: 0.75rem 1rem;
            color: var(--secondary-text);
            text-decoration: none;
            transition: all 0.3s;
            border-left: 3px solid transparent;
        }

        .nav-link:hover, .nav-link.active {
            background-color: rgba(21, 101, 192, 0.08);
            color: var(--primary-color);
            border-left: 3px solid var(--primary-color);
        }

        .nav-icon {
            margin-right: 1rem;
            font-size: 1.25rem;
            width: 20px;
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
            height: 100%;
            overflow-y: auto;
            position: relative;
            display: flex;
            flex-direction: column;
        }

        .tab-buttons {
            display: flex;
            gap: 2px;
            background-color: var(--background-white);
            padding: 0.75rem 1rem;
            overflow-x: auto;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }

        .tab-btn {
            padding: 0.75rem 1.25rem;
            border: 2px solid transparent;
            border-radius: var(--border-radius);
            background-color: transparent;
            color: var(--secondary-text);
            font-weight: 500;
            font-size: 0.875rem;
            cursor: pointer;
            min-width: 120px;
            text-align: center;
            transition: all 0.2s;
        }

        .tab-btn:hover {
            background-color: rgba(21, 101, 192, 0.08);
            color: var(--primary-color);
        }

        .tab-btn.active {
            background-color: var(--primary-color);
            color: white;
            border-color: var(--primary-dark);
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
            background-color: var(--background-white);
            box-shadow: var(--shadow-sm);
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        .open-tab-btn {
            display: inline-block;
            margin: 0.5rem 1rem;
            padding: 0.5rem 1rem;
            background-color: var(--primary-color);
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: var(--border-radius);
            font-weight: 500;
            font-size: 0.875rem;
            transition: all 0.2s;
        }

        .open-tab-btn:hover {
            background-color: var(--primary-dark);
        }

        /* DOCUMENTATION STYLES */
        .documentation {
            padding: 2rem;
            max-height: 100%;
            overflow-y: auto;
        }

        .documentation h2 {
            color: var(--primary-color);
            margin-bottom: 1.5rem;
            font-size: 1.75rem;
            font-weight: 600;
            border-bottom: 2px solid var(--primary-light);
            padding-bottom: 0.5rem;
        }

        .documentation h3 {
            color: var(--primary-text);
            margin: 1.5rem 0 1rem;
            font-size: 1.25rem;
            font-weight: 600;
        }

        .documentation h4 {
            color: var(--primary-text);
            margin: 1.25rem 0 0.75rem;
            font-size: 1.1rem;
            font-weight: 600;
        }

        .documentation p {
            margin-bottom: 1rem;
            line-height: 1.6;
            color: var(--secondary-text);
        }

        .documentation ul, .documentation ol {
            margin-bottom: 1.5rem;
            padding-left: 1.5rem;
        }

        .documentation li {
            margin-bottom: 0.5rem;
            color: var(--secondary-text);
        }

        .documentation strong {
            font-weight: 600;
            color: var(--primary-text);
        }

        .feature-cards {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 1.5rem 0;
        }

        .feature-card {
            background-color: var(--background-white);
            border-radius: var(--border-radius);
            box-shadow: var(--shadow-sm);
            padding: 1.5rem;
            transition: all 0.3s;
        }

        .feature-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-3px);
        }

        .feature-card h4 {
            color: var(--primary-color);
            margin-bottom: 0.75rem;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
        }

        .feature-card h4 i {
            margin-right: 0.75rem;
            font-size: 1.25rem;
        }

        /* DARK MODE TOGGLE */
        .dark-mode-toggle {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background-color: var(--primary-color);
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: var(--shadow-md);
            z-index: 1000;
            transition: all 0.3s;
        }

        .dark-mode-toggle:hover {
            background-color: var(--primary-dark);
            transform: scale(1.05);
        }

        /* RESPONSIVE STYLES */
        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
                height: auto;
            }
            
            .sidebar {
                width: 100%;
                height: auto;
                max-height: 300px;
            }
            
            .sidebar-collapsed {
                height: 60px;
                overflow: hidden;
            }
            
            .content-area {
                height: calc(100vh - 373px); /* Header + sidebar */
            }
            
            .feature-cards {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>{{ header_text }}</h1>
        {% if logo_url %}
            <img src="{{ logo_url }}" alt="Dashboard Logo">
        {% endif %}
    </header>
    
    <div class="main-container">
        <div class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-title">Dashboard Navigation</div>
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
                        <i class="fas fa-book nav-icon"></i>
                        <span class="nav-text">Documentation</span>
                    </a>
                </li>
                {% for tab in tabs %}
                <li class="nav-item">
                    <a href="#" class="nav-link" data-tab="tab-{{ loop.index }}">
                        <i class="fas {% if loop.index == 1 %}fa-chart-line{% elif loop.index == 2 %}fa-landmark{% elif loop.index == 3 %}fa-chart-bar{% elif loop.index == 4 %}fa-calculator{% elif loop.index == 5 %}fa-balance-scale{% else %}fa-chart-pie{% endif %} nav-icon"></i>
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
                        <h2>Value & Quality Stock Selection Dashboard</h2>
                        
                        <p>Welcome to the Value & Quality Stock Selection Dashboard, a machine learning-powered tool designed to identify potentially undervalued stocks with strong fundamentals.</p>
                        
                        <div class="feature-cards">
                            <div class="feature-card">
                                <h4><i class="fas fa-balance-scale"></i>Value Investing</h4>
                                <p>Find stocks trading below their intrinsic value with sufficient margin of safety for capital preservation.</p>
                            </div>
                            
                            <div class="feature-card">
                                <h4><i class="fas fa-award"></i>Quality Assessment</h4>
                                <p>Evaluate companies based on profitability, efficiency, consistency, and leverage metrics.</p>
                            </div>
                            
                            <div class="feature-card">
                                <h4><i class="fas fa-brain"></i>Machine Learning</h4>
                                <p>Using advanced algorithms to predict stocks likely to achieve 20%+ returns while avoiding severe underperformers.</p>
                            </div>
                        </div>
                        
                        <p>This dashboard implements a comprehensive approach to identifying valuable investment opportunities. Navigate through the tabs above to explore different aspects of the model and its recommendations.</p>

                        <h3>Similarities to Other Quantitative Value/Quality Strategies</h3>
                        <ol>
                            <li><strong>Combined Value and Quality Framework:</strong> The model follows the established practice of pairing value metrics with quality indicators, similar to many academic and professional approaches that recognize cheap stocks aren't necessarily good investments without quality considerations.</li>
                            <li><strong>Multiple Valuation Metrics:</strong> The model employ multiple valuation metrics (P/E, P/B, P/FCF, EV/EBIT, etc.) rather than relying on a single ratio, which provides a more robust assessment.</li>
                            <li><strong>Machine Learning Implementation:</strong> The use of gradient boosting classifiers with regularization is consistent with modern quantitative approaches that leverage machine learning to identify patterns in financial data.</li>
                            <li><strong>Fundamental Factor Integration:</strong> The model incorporates established fundamental quality metrics like Piotroski F-Score, ROIC, and growth consistency, which are common in many quality-focused strategies.</li>
                        </ol>

                        <h3>What Makes the Model Unique</h3>
                        <ol>
                            <li><strong>Dynamic Valuation Metric Selection:</strong> The  system uniquely selects the most appropriate valuation metric for each company based on historical correlations between low valuations and market cap within their specific industry. This industry-specific, adaptive approach is more sophisticated than models that apply the same metrics uniformly across all companies.</li>
                            <li><strong>Dual-Model Architecture:</strong> The approach of using two separate models—one to predict significant outperformers (20%+ returns) and another to identify severe underperformers to avoid—creates a more nuanced selection process than typical single-model approaches.</li>
                            <li><strong>Alpha Correlation Analysis:</strong> The assessment of "valuation alpha correlations" that measure how often low valuations coincide with small market caps is an innovative feature that helps identify value traps.</li>
                            <li><strong>Industry-Specific Historical Distributions:</strong> Rather than comparing valuations against the broad market, the model contextualizes each company's valuation within its industry-specific historical distribution, creating more relevant comparisons.</li>
                            <li><strong>Comprehensive Quality Framework Integration:</strong> The model uniquely combines multiple established quality frameworks (Piotroski, Greenblatt, Graham, Grantham, Mohanram) rather than relying on just one approach, creating a more robust quality assessment.</li>
                            <li><strong>Macroeconomic Context Integration:</strong> The inclusion of macroeconomic indicators and market cycle positioning provides important contextual awareness that many stock-specific models lack.</li>
                        </ol>                        
                        
                        <h3>Getting Started</h3>
                        <ol>
                            <li>Review the <strong>Documentation</strong> tab to understand the methodology.</li>
                            <li>Explore <strong>Stock Recommendations</strong> for current investment opportunities.</li>
                            <li>Analyze the <strong>Feature Analysis</strong> tab to understand what drives predictions.</li>
                            <li>Check <strong>Performance Metrics</strong> to validate the model's effectiveness.</li>
                            <li>Consider <strong>Market Environment</strong> for broader context.</li>
                        </ol>
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
    <div class="dark-mode-toggle" id="dark-mode-toggle">
        <i class="fas fa-moon"></i>
    </div>
    
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
            const isDarkMode = localStorage.getItem('darkMode') === 'true';
            
            // Apply dark mode if previously enabled
            if (isDarkMode) {
                enableDarkMode();
            }
            
            darkModeToggle.addEventListener('click', function() {
                if (body.classList.contains('dark-mode')) {
                    disableDarkMode();
                } else {
                    enableDarkMode();
                }
            });
            
            function enableDarkMode() {
                body.classList.add('dark-mode');
                darkModeToggle.querySelector('i').classList.remove('fa-moon');
                darkModeToggle.querySelector('i').classList.add('fa-sun');
                localStorage.setItem('darkMode', 'true');
                document.documentElement.style.setProperty('--background-light', '#121212');
                document.documentElement.style.setProperty('--background-white', '#1E1E1E');
                document.documentElement.style.setProperty('--primary-text', '#E1E1E1');
                document.documentElement.style.setProperty('--secondary-text', '#AAAAAA');
            }
            
            function disableDarkMode() {
                body.classList.remove('dark-mode');
                darkModeToggle.querySelector('i').classList.remove('fa-sun');
                darkModeToggle.querySelector('i').classList.add('fa-moon');
                localStorage.setItem('darkMode', 'false');
                document.documentElement.style.setProperty('--background-light', '#F8FAFC');
                document.documentElement.style.setProperty('--background-white', '#FFFFFF');
                document.documentElement.style.setProperty('--primary-text', '#1E293B');
                document.documentElement.style.setProperty('--secondary-text', '#475569');
            }
            
            // Attempt to request storage access on Safari
            try {
                if (document.featurePolicy && document.featurePolicy.allowsFeature('storage-access')) {
                    document.requestStorageAccess().then(
                        () => {
                            console.log('Storage access granted');
                        },
                        () => {
                            console.log('Storage access denied');
                        }
                    );
                }
            } catch (error) {
                console.error("Storage access request failed:", error);
            }
            
            // iFrame height adjustment for mobile
            function adjustIframeHeight() {
                if (window.innerWidth <= 768) {
                    document.querySelectorAll('.dashboard-iframe-wrapper').forEach(wrapper => {
                        wrapper.style.height = (window.innerHeight - 200) + 'px';
                    });
                } else {
                    document.querySelectorAll('.dashboard-iframe-wrapper').forEach(wrapper => {
                        wrapper.style.height = '';
                    });
                }
            }
            
            window.addEventListener('resize', adjustIframeHeight);
            adjustIframeHeight();
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

with open(os.path.join(deploy_dir, 'index.html'), 'w') as f:
    f.write(html_content)

print(f"Dashboard generated in {deploy_dir}/index.html")
print("To view the dashboard locally, open this file in a web browser.")
print("To deploy to GitHub Pages, push this repository with the docs/ folder.")
