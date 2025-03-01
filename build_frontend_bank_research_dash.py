import json
import os
from jinja2 import Environment, FileSystemLoader

# Load configuration from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ header_text }}</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.4;
        }

        header {
            background: #1976D2;
            color: white;
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .dashboard-container {
            max-width: 1400px;
            margin: 20px auto;
            padding: 0 15px;
        }

        .tab-wrapper {
            margin-bottom: 20px;
        }

        .tab-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 2px;
            background-color: #ddd;
            padding: 4px;
            border-radius: 8px 8px 0 0;
        }

        .tab-btn {
            border: 2px solid #333;
            background-color: #fff;
            color: #000;
            font-weight: bold;
            padding: 12px 24px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 6px;
            min-width: 120px;
            text-align: center;
            outline: none;
        }

        .tab-btn.active {
            background-color: #1976D2;
            color: white;
            border-color: #1565C0;
        }

        .content-container {
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            height: 75vh;
            overflow: hidden;
        }

        .tab-content {
            display: none;
            height: 100%;
        }

        .tab-content.active {
            display: block;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }

        .open-tab-btn {
            display: block;
            margin: 10px 0;
            padding: 10px;
            background-color: #1976D2;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <header>
        <h1>{{ header_text }}</h1>
        {% if logo_url %}
            <img src="{{ logo_url }}" alt="">
        {% endif %}
    </header>
    
    <div class="dashboard-container">
        <div class="tab-wrapper">
            <div class="tab-buttons" role="tablist">
                {% for tab in tabs %}
                    <button 
                        id="tab-btn-{{ loop.index0 }}" 
                        class="tab-btn {% if loop.first %}active{% endif %}" 
                        role="tab" 
                        aria-selected="{% if loop.first %}true{% else %}false{% endif %}" 
                        data-tab-id="{{ loop.index0 }}">
                        {{ tab.label|default('Tab ' ~ loop.index) }}
                    </button>
                {% endfor %}
            </div>
        </div>
        
        <div class="content-container">
            {% for tab in tabs %}
                <div 
                    id="content-{{ loop.index0 }}" 
                    class="tab-content {% if loop.first %}active{% endif %}" 
                    role="tabpanel" 
                    aria-labelledby="tab-btn-{{ loop.index0 }}">
                    
                    <!-- Open in New Tab Button -->
                    <a href="{{ tab.url }}" target="_blank" class="open-tab-btn">Open in New Tab</a>

                    <!-- Embedded iFrame -->
                    <iframe 
                        src="{{ tab.url }}" 
                        title="{{ tab.label|default('Tab ' ~ loop.index) }}" 
                        loading="lazy"
                        sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-storage-access-by-user-activation"
                        allow="fullscreen; clipboard-write; encrypted-media;">
                    </iframe>
                </div>
            {% endfor %}
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');

            if (tabButtons.length === 0 || tabContents.length === 0) {
                console.error("No tabs or content sections found!");
                return;
            }

            // Ensure first tab is active on page load
            tabButtons[0].classList.add('active');
            tabContents[0].classList.add('active');

            tabButtons.forEach(button => {
                button.addEventListener('click', function(event) {
                    event.preventDefault();
                    const tabId = this.getAttribute('data-tab-id');

                    if (!tabId) {
                        console.error("Tab ID missing!");
                        return;
                    }

                    // Remove active states
                    tabButtons.forEach(btn => {
                        btn.classList.remove('active');
                        btn.setAttribute('aria-selected', 'false');
                    });

                    tabContents.forEach(content => {
                        content.classList.remove('active');
                    });

                    // Activate selected tab
                    this.classList.add('active');
                    this.setAttribute('aria-selected', 'true');

                    const targetContent = document.querySelector(`#content-${tabId}`);
                    if (targetContent) {
                        targetContent.classList.add('active');
                    } else {
                        console.error(`Tab content #content-${tabId} not found`);
                    }
                });
            });

            // Attempt to request storage access on Safari
            document.addEventListener('DOMContentLoaded', async function() {
                try {
                    if (document.featurePolicy.allowsFeature('storage-access')) {
                        await document.requestStorageAccess();
                    }
                } catch (error) {
                    console.error("Storage access request failed:", error);
                }
            });
        });
    </script>
</body>
</html>
"""

# Create a directory for GitHub Pages deployment
deploy_dir = 'docs'
if not os.path.exists(deploy_dir):
    os.makedirs(deploy_dir)

# Render the template and write to docs/index.html
template = env.from_string(template_string)
html_content = template.render(
    header_text=config['header_text'],
    logo_url=config.get('logo_url', ''),
    tabs=config['tabs']
)

with open(os.path.join(deploy_dir, 'index.html'), 'w') as f:
    f.write(html_content)
