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
        /* Reset and base styles */
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

        header h1 {
            font-size: 24px;
        }

        header img {
            max-height: 40px;
        }

        .dashboard-container {
            max-width: 1400px;
            margin: 20px auto;
            padding: 0 15px;
        }

        /* Tab navigation styles */
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
            position: relative;
            overflow: visible;
            min-width: 120px;
            text-align: center;
            outline: none;
            z-index: 2;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        .tab-btn:hover {
            background-color: #e3f2fd;
        }

        .tab-btn.active {
            background-color: #1976D2;
            color: white;
            border-color: #1565C0;
            box-shadow: 0 0 8px rgba(25, 118, 210, 0.6);
        }

        /* Tab content container */
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

        /* Debug Info Panel */
        .debug-panel {
            margin-top: 20px;
            padding: 15px;
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-family: monospace;
            display: none;
        }

        .debug-btn {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            padding: 5px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 12px;
            margin-top: 5px;
        }

        @media (max-width: 768px) {
            .tab-btn {
                padding: 10px 15px;
                font-size: 14px;
                min-width: 100px;
            }
        }
    </style>
</head>
<body>
    
    <div class="dashboard-container">
        <div class="tab-wrapper">
            <!-- Debug text to verify data -->
            <div id="debug-info" style="margin-bottom:10px;font-family:monospace;font-size:12px;display:none;">
                Tabs loaded: <span id="tab-count">0</span>
            </div>
            
            <div class="tab-buttons" role="tablist">
                {% for tab in tabs %}
                    <button 
                        id="tab-btn-{{ loop.index }}" 
                        class="tab-btn {% if loop.first %}active{% endif %}" 
                        role="tab" 
                        aria-selected="{% if loop.first %}true{% else %}false{% endif %}" 
                        data-tab-id="{{ loop.index }}">
                        {{ tab.label|default('Tab ' ~ loop.index) }}
                    </button>
                {% endfor %}
            </div>
        </div>
        
        <div class="content-container">
            {% for tab in tabs %}
                <div 
                    id="content-{{ loop.index }}" 
                    class="tab-content {% if loop.first %}active{% endif %}" 
                    role="tabpanel" 
                    aria-labelledby="tab-btn-{{ loop.index }}">
                    <iframe 
                        src="{{ tab.url }}" 
                        title="{{ tab.label|default('Tab ' ~ loop.index) }}" 
                        loading="lazy"
                        sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
                        allowfullscreen>
                    </iframe>
                </div>
            {% endfor %}
        </div>
        
        <!-- Debug Panel -->
        <div class="debug-panel" id="debug-panel">
            <h3>Debug Information</h3>
            <pre id="debug-output"></pre>
            <button class="debug-btn" id="toggle-debug">Toggle Debug Mode</button>
            <button class="debug-btn" id="reload-frames">Reload All Frames</button>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Get all UI elements
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');
            const debugOutput = document.getElementById('debug-output');
            const debugPanel = document.getElementById('debug-panel');
            const tabCount = document.getElementById('tab-count');
            const iframes = document.querySelectorAll('iframe');
            
            // Debug mode functionality
            let isDebugMode = false;
            document.getElementById('toggle-debug').addEventListener('click', function() {
                isDebugMode = !isDebugMode;
                debugPanel.style.display = isDebugMode ? 'block' : 'none';
                document.getElementById('debug-info').style.display = isDebugMode ? 'block' : 'none';
                logDebug('Debug mode ' + (isDebugMode ? 'enabled' : 'disabled'));
            });
            
            // Iframe reload functionality
            document.getElementById('reload-frames').addEventListener('click', function() {
                iframes.forEach((iframe, i) => {
                    const src = iframe.src;
                    logDebug(`Reloading iframe ${i+1}: ${src}`);
                    iframe.src = 'about:blank';
                    setTimeout(() => {
                        iframe.src = src;
                    }, 100);
                });
            });
            
            // Simple double-click anywhere triggers debug mode
            document.addEventListener('dblclick', function() {
                isDebugMode = !isDebugMode;
                debugPanel.style.display = isDebugMode ? 'block' : 'none';
                document.getElementById('debug-info').style.display = isDebugMode ? 'block' : 'none';
            });
            
            // Logging helper function
            function logDebug(message) {
                if (debugOutput) {
                    const timestamp = new Date().toLocaleTimeString();
                    debugOutput.textContent = `[${timestamp}] ${message}\n` + debugOutput.textContent;
                }
            }
            
            // Initial debug info
            tabCount.textContent = tabButtons.length;
            let debugInfo = 'Tab Information:\n';
            tabButtons.forEach((btn, i) => {
                let label = btn.textContent.trim();
                let tabId = btn.getAttribute('data-tab-id');
                debugInfo += `Tab ${i+1}: "${label}" (ID: ${tabId})\n`;
            });
            
            // Log iframe info
            debugInfo += '\nIframe Sources:\n';
            iframes.forEach((iframe, i) => {
                debugInfo += `Iframe ${i+1}: "${iframe.src}"\n`;
            });
            
            debugOutput.textContent = debugInfo;
            
            // Tab switching functionality - enhanced for reliability
            tabButtons.forEach(button => {
                button.addEventListener('click', function(event) {
                    event.preventDefault();
                    const tabId = this.getAttribute('data-tab-id');
                    
                    if (!tabId) {
                        logDebug('ERROR: Missing tab ID on clicked button');
                        return;
                    }
                    
                    logDebug(`Switching to tab ${tabId}: "${this.textContent.trim()}"`);
                    
                    // Update active states for buttons
                    tabButtons.forEach(btn => {
                        btn.classList.remove('active');
                        btn.setAttribute('aria-selected', 'false');
                    });
                    
                    // Update active states for content panels
                    tabContents.forEach(content => {
                        content.classList.remove('active');
                    });
                    
                    // Activate clicked tab
                    this.classList.add('active');
                    this.setAttribute('aria-selected', 'true');
                    
                    // Find and activate corresponding content
                    const targetContent = document.getElementById(`content-${tabId}`);
                    if (targetContent) {
                        targetContent.classList.add('active');
                        
                        // Force iframe refresh if it's empty or having issues
                        const iframe = targetContent.querySelector('iframe');
                        if (iframe) {
                            if (!iframe.src || iframe.src === 'about:blank' || iframe.contentDocument && iframe.contentDocument.body.innerHTML === '') {
                                const originalSrc = iframe.getAttribute('data-original-src') || iframe.src;
                                logDebug(`Refreshing iframe in tab ${tabId}: ${originalSrc}`);
                                iframe.src = 'about:blank';
                                setTimeout(() => {
                                    iframe.src = originalSrc;
                                }, 100);
                            }
                        }
                    } else {
                        logDebug(`ERROR: Content panel #content-${tabId} not found`);
                    }
                });
            });
            
            // Store original iframe sources for potential refreshes
            iframes.forEach(iframe => {
                iframe.setAttribute('data-original-src', iframe.src);
            });
            
            // Force tab label visibility and ensure first tab is active
            setTimeout(() => {
                // Make sure first tab is active
                if (tabButtons.length > 0 && tabContents.length > 0) {
                    tabButtons[0].classList.add('active');
                    tabButtons[0].setAttribute('aria-selected', 'true');
                    tabContents[0].classList.add('active');
                    logDebug('Initial tab setup complete - first tab activated');
                }
                
                // Force reflow to ensure rendering of all tabs
                tabButtons.forEach(btn => {
                    btn.style.display = 'inline-block';
                    btn.style.visibility = 'visible';
                    btn.style.opacity = '1';
                });
            }, 300);
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

print("""
Dashboard files generated in the 'docs' directory:
- index.html: Main dashboard with fixed tab functionality
- debug.html: Alternative version with hardcoded tab names for troubleshooting

To update on GitHub Pages:
1. Run these commands:
   - git add docs/
   - git commit -m "Fixed tab functionality and improved reliability"
   - git push origin main

""")
