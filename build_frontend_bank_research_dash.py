import json
import os
from jinja2 import Environment, FileSystemLoader

# Create config.json template
config = {
    "header_text": "Value & Quality Stock Selection Dashboard",
    "logo_url": "https://via.placeholder.com/200x40?text=Logo",
    "tabs": [
        {
            "label": "Stock Recommendations",
            "url": "https://lookerstudio.google.com/embed/reporting/eb4da8db-96e9-48d6-af5a-300d0dd1e5dc/page/bMsBF"
        },
        {
            "label": "Feature Analysis",
            "url": "https://lookerstudio.google.com/embed/reporting/eb4da8db-96e9-48d6-af5a-300d0dd1e5dc/page/p_yjbdako2qd"
        },
        {
            "label": "Model Performance",
            "url": "https://lookerstudio.google.com/embed/reporting/eb4da8db-96e9-48d6-af5a-300d0dd1e5dc/page/p_n9aakyw2qd"
        },
        {
            "label": "Market Environment",
            "url": "https://lookerstudio.google.com/embed/reporting/eb4da8db-96e9-48d6-af5a-300d0dd1e5dc/page/p_oc9ltgy2qd"
        },
        {
            "label": "Univariate Feature Analysis",
            "url": "https://lookerstudio.google.com/reporting/eb4da8db-96e9-48d6-af5a-300d0dd1e5dc/page/p5"
        }
    ]
}

# Save config.json
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)

# Create HTML template
html_template = """<!DOCTYPE html>
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
                        <i class="fas {% if loop.index == 1 %}fa-chart-line{% elif loop.index == 2 %}fa-microscope{% elif loop.index == 3 %}fa-chart-bar{% elif loop.index == 4 %}fa-globe{% else %}fa-percentage{% endif %} nav-icon"></i>
                        <span class="nav-text">{{ tab.label }}</span>
                    </a>
                </li>
                {% endfor %}
            </ul>
        </div>
        
        <div class="content-area">
            <div class="tab-buttons" role="tablist">
                <button id="tab-btn-home" class="tab-btn active" data-tab="home">Overview</button>
                <button id="tab-btn-documentation" class="tab-btn" data-tab="documentation">Documentation</button>
                {% for tab in tabs %}
                <button id="tab-btn-{{ loop.index }}" class="tab-btn" data-tab="tab-{{ loop.index }}">{{ tab.label }}</button>
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
                        <!-- Documentation content goes here -->
                        <h2>Value & Quality Stock Selection Documentation</h2>
                        
                        <!-- Copy the content from the documentation artifact here -->
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
                const selectedTabBtn = document.querySelector(`[data-tab="${tabId}"]`);
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

# Create documentation.md file with value investing documentation
documentation_content = """# Value & Quality Stock Selection Documentation

## Background

This dashboard implements a machine learning approach to identify potentially undervalued stocks combining value investing principles with quality metrics. The methodology is inspired by research on machine learning-based stock picking using value investing and quality features, but with important modifications to optimize for practical use.

The system analyzes thousands of US-listed companies on a weekly basis to identify stocks that exhibit both value characteristics (trading below intrinsic value) and quality characteristics (strong fundamentals), with a focus on predicting significant future returns (20%+) while avoiding severe underperformers.

## Investment Philosophy

The dashboard is built on three core investment principles:

1. **Value Investing**: Stocks occasionally trade below their intrinsic value due to market inefficiencies, providing opportunities for excess returns. This system uses multiple valuation metrics relative to industry-specific historical norms to identify potentially undervalued securities.

2. **Quality Assessment**: Not all cheap stocks represent good investments. Quality metrics help distinguish between temporarily undervalued high-quality businesses and structurally challenged companies trading at justifiably low valuations.

3. **Margin of Safety**: The greater the discount to intrinsic value, the larger the "margin of safety" protecting against valuation errors and providing higher potential returns.

## Methodology

### Data Sources

The model processes:
- Quarterly financial data from US public companies
- Market capitalization and price information
- Industry classifications
- Macroeconomic indicators (GDP, unemployment rate, fed funds rate, yield spread)

### Feature Engineering

#### Value Features
The system dynamically selects the most appropriate valuation metric for each company based on historical correlations between low valuations and market cap within their industry:

- Price/Earnings (P/E)
- Price/Book (P/B)
- Price/Tangible Book (P/TB)
- Price/Free Cash Flow (P/FCF)
- EV/EBIT
- EV/EBITDA

For each company, the system:
1. Calculates the percentile of current valuation multiples within industry-specific historical distributions
2. Compares current multiples to historical 25th, 50th, and 75th percentiles
3. Assesses valuation "alpha correlations" - measuring how often low valuations coincide with small market caps
4. Calculates margin of safety based on the deviation from historical median valuations

#### Quality Features

Quality assessment evaluates:

1. **Profitability**: 
   - Return on Equity (ROE)
   - Return on Assets (ROA)
   - Return on Invested Capital (ROIC)
   - Gross profit to total assets

2. **Financial Health**:
   - Current ratio > 1
   - Assets exceeding debt
   - Leverage metrics

3. **Consistency & Growth**:
   - 5-year earnings consistency
   - 10-year CAGR for equity, EPS, and revenue
   - Cash flow generation quality (FCF > Net Income)

4. **Quality Frameworks**:
   - Piotroski F-Score components
   - Greenblatt Magic Formula metrics
   - Graham quality criteria
   - Grantham quality rank
   - Mohanram G-Score

5. **Economic Environment**:
   - Macroeconomic trend indicators
   - Yield curve analysis
   - Volatility metrics

### Machine Learning Approach

The system uses two model types:
1. **Investment Grade Prediction**: Predicts stocks likely to achieve 20%+ returns
2. **Severe Underperform Prediction**: Identifies stocks likely to decline 20%+ to be excluded

Each model utilizes:
- Random Forest and Gradient Boosting ensembles
- Multiple tree depths and configurations
- Precision-optimized classification thresholds

The final stock selection requires:
1. High probability score from the investment grade model
2. Low probability score from the underperform model
3. Sufficient valuation discount (margin of safety)

## Dashboard Views

### 1. Stock Recommendations
The primary view presents current stock recommendations with:
- Company identifiers and basic information
- Probability scores for significant returns
- Key valuation and quality metrics
- Industry and size categories

### 2. Feature Analysis
This view reveals the most influential predictive factors:
- Value feature importance (80-85% of model decisions)
- Quality feature importance (15-20% of model decisions)
- Feature ranking by SHAP values
- Correlation analysis between features and outcomes

### 3. Performance Metrics
Track model effectiveness with:
- Success rate in identifying 20%+ return stocks
- Average returns of recommended stocks
- Comparison to relevant benchmarks
- Historical precision and recall metrics

### 4. Market Environment
Understand broader context with:
- Current macroeconomic indicators
- Industry valuation metrics
- Market cycle positioning
- Recommendation frequency relative to market conditions

### 5. Percentile Analysis
Examine feature distributions with:
- Valuation metric percentiles
- Quality metric percentiles
- Combined score percentiles
- Industry-relative rankings

## Interpretation Guidelines

### Reading the Recommendations
- **High Probability Scores**: Stocks with higher investment grade probability scores have historically shown better performance
- **Valuation Metrics**: Lower percentiles indicate more attractive valuations relative to history
- **Quality Metrics**: Higher rankings indicate stronger fundamental characteristics
- **Combined Metrics**: Focus on stocks showing both value and quality characteristics

### Portfolio Considerations
- **Diversification**: Consider spreading investments across industries and size categories
- **Position Sizing**: Higher probability scores may warrant larger allocations
- **Time Horizon**: Model is optimized for 1-3 year investment horizons
- **Rebalancing**: Consider refreshing positions when stocks reach intrinsic value or quality deteriorates

## Glossary of Key Metrics

### Value Metrics
- **Valuation Multiple Percentile**: Where current valuation stands in historical distribution (lower is better)
- **Margin of Safety**: Discount to historical median valuation (higher is better)
- **Alpha Correlation**: How often low valuations coincide with small market caps

### Quality Metrics
- **F-Score**: Piotroski's 9-point framework for financial strength (higher is better)
- **ROIC**: Return on Invested Capital, measuring capital allocation efficiency
- **Cash Flow Persistence**: Consistency of cash generation relative to earnings
- **Growth Consistency**: Stability of growth across equity, earnings, and revenue

### Combined Metrics
- **Contrarian Sentiment**: Measures disagreement between valuation and quality indicators
- **Neglected Stock Indicator**: Identifies overlooked smaller companies with strong fundamentals
- **Quality-Value Composite**: Weighted combination of value and quality signals
"""

with open('documentation.md', 'w') as f:
    f.write(documentation_content)

# Create the template with Jinja2
template_file = 'dashboard_template.html'
with open(template_file, 'w') as f:
    f.write(html_template)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(template_file)

# Create a directory for GitHub Pages deployment
deploy_dir = 'docs'
if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

# Parse the documentation file and insert it into the template
with open('documentation.md', 'r') as f:
    doc_content = f.read()

# Create HTML documentation from markdown
# In a real-world scenario, you'd use a proper Markdown to HTML converter
doc_html = doc_content.replace('# ', '<h2>').replace('## ', '<h3>').replace('### ', '<h4>')
doc_html = doc_html.replace('\n\n', '</p><p>')
doc_html = f'<p>{doc_html}</p>'

# Render the template with the documentation
html_content = template.render(
    header_text=config['header_text'],
    logo_url=config.get('logo_url', ''),
    tabs=config['tabs'],
    documentation_content=doc_html
)

# Write the final index.html
with open(os.path.join(deploy_dir, 'index.html'), 'w') as f:
    f.write(html_content)

print(f"Dashboard generated in {deploy_dir}/index.html")
print("To view the dashboard locally, open this file in a web browser.")
print("To deploy to GitHub Pages, push this repository with the docs/ folder.")
