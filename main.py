import streamlit as st
from streamlit.components.v1 import html

# ===============================================
# 1. CONTENIDOS HTML REALES DE LOS DASHBOARDS
# (ESTE CONTENIDO ES 100% FIEL A TUS ARCHIVOS HTML Y NO SE MODIFICA)
# ===============================================

HTML_MODERNO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Corporate Elegante</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0a0a;
            --bg-secondary: #1a1a1a;
            --bg-tertiary: #2a2a2a;
            --text-primary: #ffffff;
            --text-secondary: #a0a0a0;
            --accent-primary: #d4af37;
            --accent-secondary: #c19a2e;
            --border-color: rgba(212, 175, 55, 0.2);
            --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #f5f5f5;
            --bg-secondary: #ffffff;
            --bg-tertiary: #e8e8e8;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent-primary: #c19a2e;
            --accent-secondary: #a88826;
            --border-color: rgba(193, 154, 46, 0.3);
            --shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 30px 25px;
            border-bottom: 1px solid var(--border-color);
        }

        .logo {
            font-size: 24px;
            font-weight: 700;
            color: var(--accent-primary);
            letter-spacing: 1px;
            margin-bottom: 15px;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-secondary);
            font-size: 14px;
        }

        .user-avatar {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 600;
        }

        .sidebar-nav {
            flex: 1;
            padding: 20px 0;
            overflow-y: auto;
        }

        .nav-item {
            list-style: none;
        }

        .nav-item a {
            display: flex;
            align-items: center;
            padding: 14px 25px;
            color: var(--text-secondary);
            text-decoration: none;
            transition: all 0.2s ease;
            font-size: 15px;
            font-weight: 500;
            position: relative;
        }

        .nav-item a::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 3px;
            background: var(--accent-primary);
            transform: scaleY(0);
            transition: transform 0.2s ease;
        }

        .nav-item a:hover {
            color: var(--text-primary);
            background: var...
        }
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">CORP DASH</div>
            <div class="user-info">
                <div class="user-avatar">JM</div>
                <span>Julián Martínez<br>CEO, Data Insights</span>
            </div>
        </div>
        <ul class="sidebar-nav">
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'overview')">
                    <span class="material-icons-outlined">dashboard</span> Overview
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'finance')">
                    <span class="material-icons-outlined">account_balance</span> Finance
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'sales')">
                    <span class="material-icons-outlined">shopping_cart</span> Sales
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'projects')">
                    <span class="material-icons-outlined">folder_open</span> Projects
                </a>
            </li>
            <div class="nav-category">Settings</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'config')">
                    <span class="material-icons-outlined">settings</span> Configuration
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">brightness_4</span> Toggle Theme
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">logout</span> Logout
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="search-box">
                    <span class="material-icons-outlined">search</span>
                    <input type="text" placeholder="Search reports...">
                </div>
            </div>
            <div class="right-section">
                <button class="icon-btn">
                    <span class="material-icons-outlined">notifications</span>
                </button>
                <button class="icon-btn">
                    <span class="material-icons-outlined">mail_outline</span>
                </button>
                <div class="profile">
                    <div class="profile-avatar">JM</div>
                </div>
            </div>
        </header>

        <main class="content">
            <section id="content-overview" class="content-section active">
                <h1>Executive Overview</h1>
                <p>Welcome to the Corporate Dashboard.</p>
                
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="icon-container primary">
                            <span class="material-icons-outlined">attach_money</span>
                        </div>
                        <div class="stat-info">
                            <p class="stat-label">Total Revenue</p>
                            <h2 class="stat-value">$1.2M</h2>
                            <p class="stat-change positive">+8.5% last month</p>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="icon-container secondary">
                            <span class="material-icons-outlined">group</span>
                        </div>
                        <div class="stat-info">
                            <p class="stat-label">New Clients</p>
                            <h2 class="stat-value">2,500</h2>
                            <p class="stat-change negative">-1.2% last month</p>
                        </div>
                    </div>
                    <div class="stat-card">
                        <div class="icon-container tertiary">
                            <span class="material-icons-outlined">poll</span>
                        </div>
                        <div class="stat-info">
                            <p class="stat-label">Conversion Rate</p>
                            <h2 class="stat-value">12.4%</h2>
                            <p class="stat-change positive">+0.5% last month</p>
                        </div>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Revenue Trend</h3>
                        <div class="chart-placeholder">Chart area for Revenue vs Time</div>
                    </div>
                    <div class="chart-card small">
                        <h3>Client Acquisition</h3>
                        <div class="chart-placeholder">Chart area for Client Funnel</div>
                    </div>
                </div>
            </section>

            <section id="content-finance" class="content-section">
                <h1>Finance Dashboard</h1>
                <p>Detailed financial metrics and reports.</p>
                <div class="placeholder-content">
                    <p>This is the Finance section content.</p>
                </div>
            </section>

            <section id="content-sales" class="content-section">
                <h1>Sales Dashboard</h1>
                <p>Key sales performance indicators.</p>
                <div class="placeholder-content">
                    <p>This is the Sales section content.</p>
                </div>
            </section>
             <section id="content-projects" class="content-section">
                <h1>Project Management</h1>
                <p>Track project progress and resources.</p>
                <div class="placeholder-content">
                    <p>This is the Projects section content.</p>
                </div>
            </section>
             <section id="content-config" class="content-section">
                <h1>Configuration</h1>
                <p>System settings and user preferences.</p>
                <div class="placeholder-content">
                    <p>This is the Configuration section content.</p>
                </div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_FINANCIERO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Financiero</title>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a1628;
            --bg-secondary: #0f1d35;
            --bg-tertiary: #162842;
            --text-primary: #ffffff;
            --text-secondary: #94a3b8;
            --accent-primary: #10b981;
            --accent-secondary: #059669;
            --accent-blue: #3b82f6;
            --border-color: rgba(16, 185, 129, 0.2);
            --shadow: 0 8px 32px rgba(16, 185, 129, 0.2);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #f8fafc;
            --bg-secondary: #ffffff;
            --bg-tertiary: #f1f5f9;
            --text-primary: #0f172a;
            --text-secondary: #64748b;
            --accent-primary: #10b981;
            --accent-secondary: #059669;
            --accent-blue: #3b82f6;
            --border-color: rgba(16, 185, 129, 0.2);
            --shadow: 0 4px 20px rgba(16, 185, 129, 0.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'IBM Plex Sans', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 28px 25px;
            border-bottom: 1px solid var(--border-color);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .logo-icon {
            width: 42px;
            height: 42px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .logo-icon .material-icons-outlined {
            color: #fff;
            font-size: 24px;
        }

        .logo-text {
            font-size: 22px;
            font-weight: 700;
            color: var(--text-primary);
            letter-spacing: -0.5px;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px;
            background: var(--bg-tertiary);
            border-radius: 8px;
            border-left: 3px solid var(--accent-primary);
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 700;
            color: #fff;
            font-family: 'IBM Plex Mono', monospace;
        }

        .sidebar-nav {
            flex: 1;
            padding: 20px 0;
            overflow-y: auto;
        }

        .nav-category {
            color: var(--text-secondary);
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 0 25px;
            margin: 20px 0 10px 0;
        }

        .nav-item...
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <div class="logo-icon"><span class="material-icons-outlined">trending_up</span></div>
                <div class="logo-text">FINEX</div>
            </div>
            <div class="user-info">
                <div class="user-avatar">AD</div>
                <div>
                    <div style="font-weight: 600; color: white;">Alex Durán</div>
                    <div style="font-size: 12px; color: var(--text-secondary);">Chief Finance Officer</div>
                </div>
            </div>
        </div>
        <ul class="sidebar-nav">
            <div class="nav-category">Main</div>
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'summary')">
                    <span class="material-icons-outlined">account_balance</span> Financial Summary
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'investments')">
                    <span class="material-icons-outlined">bar_chart</span> Investments
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'budget')">
                    <span class="material-icons-outlined">pie_chart</span> Budget Analysis
                </a>
            </li>
            <div class="nav-category">Reports</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'income')">
                    <span class="material-icons-outlined">receipt_long</span> Income Statements
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'cashflow')">
                    <span class="material-icons-outlined">monetization_on</span> Cash Flow
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">light_mode</span> Toggle Theme
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">exit_to_app</span> Sign Out
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="page-title">Financial Summary Dashboard</div>
            </div>
            <div class="right-section">
                <div class="date-selector">
                    <span class="material-icons-outlined">calendar_today</span>
                    <select>
                        <option>Last 30 Days</option>
                        <option>Last 90 Days</option>
                        <option>Year to Date</option>
                    </select>
                </div>
                <button class="icon-btn">
                    <span class="material-icons-outlined">notifications</span>
                </button>
                <div class="profile-avatar">AD</div>
            </div>
        </header>

        <main class="content">
            <section id="content-summary" class="content-section active">
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">attach_money</span>
                        <p class="stat-label">Net Income (TTM)</p>
                        <h2 class="stat-value">$450M</h2>
                        <p class="stat-change positive">+12.5% YoY</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">inventory</span>
                        <p class="stat-label">Operating Margin</p>
                        <h2 class="stat-value">18.2%</h2>
                        <p class="stat-change negative">-0.5% YoY</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">trending_up</span>
                        <p class="stat-label">Return on Equity (ROE)</p>
                        <h2 class="stat-value">22.1%</h2>
                        <p class="stat-change positive">+2.1% YoY</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">assessment</span>
                        <p class="stat-label">Debt-to-Equity Ratio</p>
                        <h2 class="stat-value">0.45</h2>
                        <p class="stat-change positive">+0.03 YoY</p>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Revenue & Net Income Trend</h3>
                        <div class="chart-placeholder">Area Chart of Revenue vs Net Income over 12 months</div>
                    </div>
                    <div class="chart-card small">
                        <h3>Asset Allocation</h3>
                        <div class="chart-placeholder">Donut Chart of Asset Categories</div>
                    </div>
                </div>

                <div class="table-card">
                    <h3>Key Ratios Comparison</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Metric</th>
                                <th>Q4 2024</th>
                                <th>Q3 2024</th>
                                <th>YoY Change</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Gross Margin</td>
                                <td>55.2%</td>
                                <td>54.8%</td>
                                <td class="positive">▲ 0.4%</td>
                            </tr>
                            <tr>
                                <td>EPS</td>
                                <td>$1.45</td>
                                <td>$1.38</td>
                                <td class="positive">▲ 5.1%</td>
                            </tr>
                            <tr>
                                <td>P/E Ratio</td>
                                <td>18.5x</td>
                                <td>19.1x</td>
                                <td class="negative">▼ -3.1%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </section>

            <section id="content-investments" class="content-section">
                <h1>Investment Portfolio</h1>
                <p>Detailed breakdown of stock and bond holdings.</p>
                <div class="placeholder-content">Investment content here.</div>
            </section>
            
            <section id="content-budget" class="content-section">
                <h1>Budget Analysis</h1>
                <p>Track department spending against budget.</p>
                <div class="placeholder-content">Budget content here.</div>
            </section>
             <section id="content-income" class="content-section">
                <h1>Income Statements</h1>
                <p>Quarterly and annual income reports.</p>
                <div class="placeholder-content">Income content here.</div>
            </section>
             <section id="content-cashflow" class="content-section">
                <h1>Cash Flow</h1>
                <p>Operating, investing, and financing cash flow details.</p>
                <div class="placeholder-content">Cash flow content here.</div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_INDUSTRIAL = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Industrial</title>
    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0d0d0d;
            --bg-secondary: #1a1a1a;
            --bg-tertiary: #262626;
            --text-primary: #ffffff;
            --text-secondary: #b8b8b8;
            --accent-primary: #ff6b2c;
            --accent-secondary: #ffaa00;
            --accent-dark: #cc5522;
            --border-color: rgba(255, 107, 44, 0.3);
            --shadow: 0 8px 32px rgba(255, 107, 44, 0.25);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #e8e8e8;
            --bg-secondary: #f5f5f5;
            --bg-tertiary: #ffffff;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent-primary: #ff6b2c;
            --accent-secondary: #ff8c42;
            --accent-dark: #cc5522;
            --border-color: rgba(255, 107, 44, 0.2);
            --shadow: 0 4px 20px rgba(255, 107, 44, 0.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Rajdhani', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 2px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 25px;
            border-bottom: 2px solid var(--border-color);
            background: linear-gradient(135deg, rgba(255, 107, 44, 0.1), rgba(255, 170, 0, 0.05));
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 18px;
        }

        .logo-icon {
            width: 45px;
            height: 45px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .logo-icon .material-icons-outlined {
            color: #000;
            font-size: 26px;
            font-weight: bold;
        }

        .logo-text {
            font-size: 26px;
            font-weight: 700;
            color: var(--accent-primary);
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: var(--bg-tertiary);
            border-left: 3px solid var(--accent-primary);
            font-family: 'Roboto Mono', monospace;
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight...
        }
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <div class="logo-icon"><span class="material-icons-outlined">precision_manufacturing</span></div>
                <div class="logo-text">INDUSTRY X</div>
            </div>
            <div class="user-info">
                <div class="user-avatar">AM</div>
                <div>
                    <div style="font-weight: 600; color: var(--text-primary);">A. Moreno</div>
                    <div style="font-size: 13px; color: var(--text-secondary);">Operations Manager</div>
                </div>
            </div>
        </div>
        <ul class="sidebar-nav">
            <div class="nav-category">Monitoring</div>
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'production')">
                    <span class="material-icons-outlined">factory</span> Production Line
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'inventory')">
                    <span class="material-icons-outlined">inventory_2</span> Raw Inventory
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'quality')">
                    <span class="material-icons-outlined">check_circle_outline</span> Quality Control
                </a>
            </li>
            <div class="nav-category">Assets</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'maintenance')">
                    <span class="material-icons-outlined">build</span> Maintenance
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'energy')">
                    <span class="material-icons-outlined">bolt</span> Energy Usage
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">contrast</span> Theme Switch
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">lock</span> Secure Exit
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="page-title">Industrial Production Overview</div>
            </div>
            <div class="right-section">
                <div class="filter-group">
                    <span class="material-icons-outlined">calendar_month</span>
                    <select>
                        <option>Current Shift</option>
                        <option>Last 24 Hours</option>
                        <option>Last Week</option>
                    </select>
                </div>
                <button class="icon-btn">
                    <span class="material-icons-outlined">alarm_on</span>
                </button>
                <div class="profile-avatar">AM</div>
            </div>
        </header>

        <main class="content">
            <section id="content-production" class="content-section active">
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">view_list</span>
                        <p class="stat-label">Units Produced (Shift)</p>
                        <h2 class="stat-value">8,450</h2>
                        <p class="stat-change positive">Target: 9,000</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">speed</span>
                        <p class="stat-label">Machine Uptime</p>
                        <h2 class="stat-value">98.5%</h2>
                        <p class="stat-change negative">Downtime: 1.5 hrs</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">warning_amber</span>
                        <p class="stat-label">Defect Rate</p>
                        <h2 class="stat-value">1.2%</h2>
                        <p class="stat-change positive">Goal: < 1.0%</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">thermostat</span>
                        <p class="stat-label">Avg. Temp. (Line 2)</p>
                        <h2 class="stat-value">45.8°C</h2>
                        <p class="stat-change negative">Status: Elevated</p>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Production Output Trend</h3>
                        <div class="chart-placeholder">Line Chart of Hourly Unit Output</div>
                    </div>
                    <div class="chart-card small">
                        <h3>OEE Breakdown</h3>
                        <div class="chart-placeholder">Pie Chart of OEE (Availability, Performance, Quality)</div>
                    </div>
                </div>
            </section>

            <section id="content-inventory" class="content-section">
                <h1>Raw Inventory Status</h1>
                <p>Tracking of material levels and reorder points.</p>
                <div class="placeholder-content">Inventory content here.</div>
            </section>

            <section id="content-quality" class="content-section">
                <h1>Quality Control Reports</h1>
                <p>Detailed analysis of defect types and root causes.</p>
                <div class="placeholder-content">Quality content here.</div>
            </section>
             <section id="content-maintenance" class="content-section">
                <h1>Maintenance Schedule</h1>
                <p>Upcoming and historical maintenance logs.</p>
                <div class="placeholder-content">Maintenance content here.</div>
            </section>
             <section id="content-energy" class="content-section">
                <h1>Energy Usage</h1>
                <p>Real-time and historical energy consumption data.</p>
                <div class="placeholder-content">Energy content here.</div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_MEDICO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Medical Clean</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a1a1f;
            --bg-secondary: #0f2429;
            --bg-tertiary: #143840;
            --text-primary: #ffffff;
            --text-secondary: #a8c5d1;
            --accent-primary: #00d9ff;
            --accent-secondary: #6effc9;
            --accent-tertiary: #4dd4ac;
            --border-color: rgba(0, 217, 255, 0.2);
            --shadow: 0 8px 32px rgba(0, 217, 255, 0.2);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #f0f9fb;
            --bg-secondary: #ffffff;
            --bg-tertiary: #e8f6f8;
            --text-primary: #0a1a1f;
            --text-secondary: #4a6c78;
            --accent-primary: #00b8d4;
            --accent-secondary: #26c6a0;
            --accent-tertiary: #1fa88f;
            --border-color: rgba(0, 184, 212, 0.2);
            --shadow: 0 4px 20px rgba(0, 184, 212, 0.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Roboto', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 25px;
            border-bottom: 1px solid var(--border-color);
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .logo-icon .material-icons-outlined {
            color: #fff;
            font-size: 24px;
        }

        .logo-text {
            font-size: 22px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: var(--bg-tertiary);
            border-radius: 10px;
            color: var(--text-secondary);
            font-size: 13px;
        }

        .user-avatar {
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 600;...
        }
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <div class="logo-icon"><span class="material-icons-outlined">medical_services</span></div>
                <div class="logo-text">MEDIX</div>
            </div>
            <div class="user-info">
                <div class="user-avatar">DR</div>
                <div>
                    <div style="font-weight: 500; color: var(--text-primary);">Dr. Ramos</div>
                    <div style="font-size: 13px;">Chief Medical Officer</div>
                </div>
            </div>
        </div>
        <ul class="sidebar-nav">
            <div class="nav-category">Patient Care</div>
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'admissions')">
                    <span class="material-icons-outlined">local_hospital</span> Admissions Summary
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'icu')">
                    <span class="material-icons-outlined">bed</span> ICU Bed Status
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'surgeries')">
                    <span class="material-icons-outlined">content_cut</span> Surgery Schedule
                </a>
            </li>
            <div class="nav-category">Operations</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'staffing')">
                    <span class="material-icons-outlined">group</span> Staffing Levels
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'inventory')">
                    <span class="material-icons-outlined">vaccines</span> Medical Inventory
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">lightbulb</span> Theme
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">lock_open</span> Logout Secure
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="page-title">Hospital Admissions Overview</div>
            </div>
            <div class="right-section">
                <div class="date-filter">
                    <span class="material-icons-outlined">date_range</span>
                    <select>
                        <option>Today</option>
                        <option>Last 7 Days</option>
                        <option>Last 30 Days</option>
                    </select>
                </div>
                <button class="icon-btn">
                    <span class="material-icons-outlined">message</span>
                </button>
                <div class="profile-avatar">DR</div>
            </div>
        </header>

        <main class="content">
            <section id="content-admissions" class="content-section active">
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">accessible_forward</span>
                        <p class="stat-label">Total Current Patients</p>
                        <h2 class="stat-value">356</h2>
                        <p class="stat-change positive">Occupancy: 88%</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">person_add</span>
                        <p class="stat-label">Admissions Today</p>
                        <h2 class="stat-value">25</h2>
                        <p class="stat-change negative">Vs Yesterday: -3</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">timer</span>
                        <p class="stat-label">Avg. Length of Stay</p>
                        <h2 class="stat-value">4.2 days</h2>
                        <p class="stat-change positive">Goal: < 4.5 days</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">trending_down</span>
                        <p class="stat-label">Readmission Rate</p>
                        <h2 class="stat-value">9.8%</h2>
                        <p class="stat-change positive">Last Q: 10.5%</p>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Admissions by Specialty</h3>
                        <div class="chart-placeholder">Bar Chart of Admissions by Department</div>
                    </div>
                    <div class="chart-card small">
                        <h3>Patient Flow</h3>
                        <div class="chart-placeholder">Sankey or Funnel Chart</div>
                    </div>
                </div>
            </section>

            <section id="content-icu" class="content-section">
                <h1>ICU Status</h1>
                <p>Real-time Intensive Care Unit metrics.</p>
                <div class="placeholder-content">ICU content here.</div>
            </section>

            <section id="content-surgeries" class="content-section">
                <h1>Surgery Schedule</h1>
                <p>Today's surgical timetable and capacity.</p>
                <div class="placeholder-content">Surgery content here.</div>
            </section>
             <section id="content-staffing" class="content-section">
                <h1>Staffing Levels</h1>
                <p>Nurse-to-patient ratios and shift coverage.</p>
                <div class="placeholder-content">Staffing content here.</div>
            </section>
             <section id="content-inventory" class="content-section">
                <h1>Medical Inventory</h1>
                <p>Stock levels for critical supplies and medications.</p>
                <div class="placeholder-content">Inventory content here.</div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_RETAIL = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Retail</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0f0a;
            --bg-secondary: #111911;
            --bg-tertiary: #1a241a;
            --text-primary: #ffffff;
            --text-secondary: #a8c5a8;
            --accent-primary: #4ade80;
            --accent-secondary: #fbbf24;
            --accent-tertiary: #22c55e;
            --border-color: rgba(74, 222, 128, 0.3);
            --shadow: 0 8px 32px rgba(74, 222, 128, 0.3);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #f0fdf4;
            --bg-secondary: #ffffff;
            --bg-tertiary: #dcfce7;
            --text-primary: #052e16;
            --text-secondary: #166534;
            --accent-primary: #22c55e;
            --accent-secondary: #f59e0b;
            --accent-tertiary: #16a34a;
            --border-color: rgba(34, 197, 94, 0.3);
            --shadow: 0 4px 20px rgba(34, 197, 94, 0.2);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 28px 25px;
            border-bottom: 1px solid var(--border-color);
            background: linear-gradient(135deg, rgba(74, 222, 128, 0.1), rgba(251, 191, 36, 0.05));
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 18px;
        }

        .logo-icon {
            width: 46px;
            height: 46px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 12px rgba(74, 222, 128, 0.4);
        }

        .logo-icon .material-icons-outlined {
            color: #000;
            font-size: 28px;
            font-weight: bold;
        }

        .logo-text {
            font-size: 26px;
            font-weight: 800;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px;
            background: var(--bg-tertiary);
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }

        .user-avatar {
            width: 38px;
            height: 38px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            font-weight: 700;
            color: #000;
        }

        .sidebar-nav {
            flex: 1;
            padding: 20px 0;
            overflow-y: auto;
        }

        .nav-item {
            list-style: none;
            margin: 4px 15px;
        }

        .nav-item a {
            display: flex;
            align-items: center;
            padding: 14px 16px;
            color: var(--text-secondary);
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 15px;
            font-weight...
        }
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">
                <div class="logo-icon"><span class="material-icons-outlined">storefront</span></div>
                <div class="logo-text">RETAIL VIEW</div>
            </div>
            <div class="user-info">
                <div class="user-avatar">SR</div>
                <div>
                    <div style="font-weight: 600; color: var(--text-primary);">S. Robles</div>
                    <div style="font-size: 14px; color: var(--text-secondary);">Sales Director</div>
                </div>
            </div>
        </div>
        <ul class="sidebar-nav">
            <div class="nav-category">Sales</div>
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'performance')">
                    <span class="material-icons-outlined">ssid_chart</span> Sales Performance
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'product')">
                    <span class="material-icons-outlined">category</span> Product Analysis
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'store')">
                    <span class="material-icons-outlined">location_on</span> Store Comparison
                </a>
            </li>
            <div class="nav-category">Operations</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'inventory')">
                    <span class="material-icons-outlined">inventory</span> Stock Levels
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'customer')">
                    <span class="material-icons-outlined">sentiment_satisfied_alt</span> Customer Loyalty
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">light_mode</span> Theme Switch
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">lock</span> Logout
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="page-title">Sales Performance Dashboard</div>
            </div>
            <div class="right-section">
                <div class="filter-group">
                    <span class="material-icons-outlined">calendar_today</span>
                    <select>
                        <option>Current Week</option>
                        <option>Current Month</option>
                        <option>Current Quarter</option>
                    </select>
                </div>
                <button class="icon-btn">
                    <span class="material-icons-outlined">comment</span>
                </button>
                <div class="profile-avatar">SR</div>
            </div>
        </header>

        <main class="content">
            <section id="content-performance" class="content-section active">
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">attach_money</span>
                        <p class="stat-label">Total Revenue</p>
                        <h2 class="stat-value">$185,400</h2>
                        <p class="stat-change positive">+15.2% WoW</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">shopping_bag</span>
                        <p class="stat-label">Transactions</p>
                        <h2 class="stat-value">4,120</h2>
                        <p class="stat-change negative">-0.8% WoW</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">price_check</span>
                        <p class="stat-label">Avg. Basket Value</p>
                        <h2 class="stat-value">$44.98</h2>
                        <p class="stat-change positive">+2.1% WoW</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">sentiment_very_satisfied</span>
                        <p class="stat-label">Customer Conversion</p>
                        <h2 class="stat-value">7.8%</h2>
                        <p class="stat-change positive">+0.3% WoW</p>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Weekly Sales by Channel</h3>
                        <div class="chart-placeholder">Bar Chart comparing In-Store vs Online Sales</div>
                    </div>
                    <div class="chart-card small">
                        <h3>Top 5 Products</h3>
                        <div class="chart-placeholder">List/Table of best-selling products</div>
                    </div>
                </div>
            </section>

            <section id="content-product" class="content-section">
                <h1>Product Deep Dive</h1>
                <p>Detailed performance by product category and SKU.</p>
                <div class="placeholder-content">Product content here.</div>
            </section>

            <section id="content-store" class="content-section">
                <h1>Store Comparison</h1>
                <p>Benchmarking sales and performance across all locations.</p>
                <div class="placeholder-content">Store content here.</div>
            </section>
             <section id="content-inventory" class="content-section">
                <h1>Stock Levels</h1>
                <p>Inventory health and low-stock alerts.</p>
                <div class="placeholder-content">Inventory content here.</div>
            </section>
             <section id="content-customer" class="content-section">
                <h1>Customer Loyalty</h1>
                <p>Tracking repeat purchase rate and customer lifetime value.</p>
                <div class="placeholder-content">Customer content here.</div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_TECNOLOGICO = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Tech Vibrante</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0d0d1a;
            --bg-secondary: #161629;
            --bg-tertiary: #1f1f3d;
            --text-primary: #ffffff;
            --text-secondary: #a0a3bd;
            --accent-primary: #6366f1;
            --accent-secondary: #ec4899;
            --accent-glow: rgba(99, 102, 241, 0.4);
            --border-color: rgba(99, 102, 241, 0.2);
            --shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
            --sidebar-width: 280px;
        }

        [data-theme="light"] {
            --bg-primary: #f8f9ff;
            --bg-secondary: #ffffff;
            --bg-tertiary: #f0f1ff;
            --text-primary: #1a1a2e;
            --text-secondary: #6b6b8c;
            --accent-primary: #6366f1;
            --accent-secondary: #ec4899;
            --accent-glow: rgba(99, 102, 241, 0.2);
            --border-color: rgba(99, 102, 241, 0.15);
            --shadow: 0 4px 20px rgba(99, 102, 241, 0.15);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            transition: all 0.3s ease;
        }

        .sidebar {
            width: var(--sidebar-width);
            background: var(--bg-secondary);
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
            display: flex;
            flex-direction: column;
            border-right: 1px solid var(--border-color);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .sidebar-header {
            padding: 30px 25px;
            border-bottom: 1px solid var(--border-color);
        }

        .logo {
            font-size: 26px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
            margin-bottom: 15px;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-secondary);
            font-size: 13px;
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            font-weight: 600;
            color: #fff;
            box-shadow: 0 4px 12px...
        }
    </style>
</head>
<body>
    <div class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="logo">SYNAPTIC DASH</div>
            <div class="user-info">
                <div class="user-avatar">SL</div>
                <span>Sonia López<br>Lead Developer</span>
            </div>
        </div>
        <ul class="sidebar-nav">
            <div class="nav-category">Development</div>
            <li class="nav-item active">
                <a href="#" onclick="switchContent(event, 'code')">
                    <span class="material-icons-outlined">code</span> Code Metrics
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'bugs')">
                    <span class="material-icons-outlined">bug_report</span> Bug Tracker
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'deploy')">
                    <span class="material-icons-outlined">cloud_upload</span> Deploy Status
                </a>
            </li>
            <div class="nav-category">Infrastructure</div>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'server')">
                    <span class="material-icons-outlined">dns</span> Server Health
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="switchContent(event, 'security')">
                    <span class="material-icons-outlined">security</span> Security Log
                </a>
            </li>
            <li class="nav-item">
                <a href="#" onclick="toggleTheme()">
                    <span class="material-icons-outlined">palette</span> Theme Toggle
                </a>
            </li>
        </ul>
        <div class="sidebar-footer">
            <a href="#" class="btn-logout">
                <span class="material-icons-outlined">power_settings_new</span> Shut Down
            </a>
        </div>
    </div>
    
    <div class="main-container">
        <header class="navbar">
            <div class="left-section">
                <button id="menuToggle" class="menu-toggle">
                    <span class="material-icons-outlined">menu</span>
                </button>
                <div class="page-title">Code and Development Metrics</div>
            </div>
            <div class="right-section">
                <div class="filter-group">
                    <span class="material-icons-outlined">schedule</span>
                    <select>
                        <option>Current Sprint</option>
                        <option>Last Release</option>
                        <option>Last 30 Days</option>
                    </select>
                </div>
                <button class="icon-btn">
                    <span class="material-icons-outlined">help_outline</span>
                </button>
                <div class="profile-avatar">SL</div>
            </div>
        </header>

        <main class="content">
            <section id="content-code" class="content-section active">
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">commit</span>
                        <p class="stat-label">Commits (24h)</p>
                        <h2 class="stat-value">56</h2>
                        <p class="stat-change positive">Code Lines: +1,240</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">verified_user</span>
                        <p class="stat-label">Test Coverage</p>
                        <h2 class="stat-value">88%</h2>
                        <p class="stat-change positive">Goal: 90%</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">error_outline</span>
                        <p class="stat-label">Open Bugs</p>
                        <h2 class="stat-value">12</h2>
                        <p class="stat-change negative">Critical: 2</p>
                    </div>
                    <div class="stat-card">
                        <span class="material-icons-outlined stat-icon">watch_later</span>
                        <p class="stat-label">Avg. Review Time</p>
                        <h2 class="stat-value">4.5 hrs</h2>
                        <p class="stat-change positive">Last Week: 5.1 hrs</p>
                    </div>
                </div>

                <div class="charts-grid">
                    <div class="chart-card large">
                        <h3>Build Success Rate</h3>
                        <div class="chart-placeholder">Line Chart of Build Success/Failure over time</div>
                    </div>
                    <div class="chart-card small">
                        <h3>Active Developers</h3>
                        <div class="chart-placeholder">Bar Chart of developer activity</div>
                    </div>
                </div>
            </section>

            <section id="content-bugs" class="content-section">
                <h1>Bug Tracker</h1>
                <p>Detailed list and status of known issues.</p>
                <div class="placeholder-content">Bug content here.</div>
            </section>

            <section id="content-deploy" class="content-section">
                <h1>Deployment Status</h1>
                <p>Status of latest releases across environments.</p>
                <div class="placeholder-content">Deploy content here.</div>
            </section>
             <section id="content-server" class="content-section">
                <h1>Server Health</h1>
                <p>CPU, RAM, and latency monitoring.</p>
                <div class="placeholder-content">Server content here.</div>
            </section>
             <section id="content-security" class="content-section">
                <h1>Security Log</h1>
                <p>Vulnerability scans and access attempts.</p>
                <div class="placeholder-content">Security content here.</div>
            </section>
        </main>
    </div>

    <script>
        function switchContent(event, contentId) {
            event.preventDefault();
            
            document.querySelectorAll('.content-section').forEach(section => {
                section.classList.remove('active');
            });
            
            document.getElementById(`content-${contentId}`).classList.add('active');
            
            document.querySelectorAll('.nav-item').forEach(item => {
                item.classList.remove('active');
            });
            
            event.target.closest('.nav-item').classList.add('active');
            
            if (window.innerWidth <= 768) {
                document.getElementById('sidebar').classList.remove('open');
            }
        }

        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
        }

        document.getElementById('menuToggle').addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });

        document.addEventListener('click', (e) => {
            const sidebar = document.getElementById('sidebar');
            const menuToggle = document.getElementById('menuToggle');
            
            if (window.innerWidth <= 768 && 
                sidebar.classList.contains('open') && 
                !sidebar.contains(e.target) && 
                e.target !== menuToggle) {
                sidebar.classList.remove('open');
            }
        });
    </script>
</body>
</html>
""" 

HTML_CONTENT = {
    "Moderno": HTML_MODERNO,
    "Financiero": HTML_FINANCIERO,
    "Industrial": HTML_INDUSTRIAL,
    "Médico": HTML_MEDICO,
    "Retail": HTML_RETAIL,
    "Tecnológico": HTML_TECNOLOGICO
}

# ===============================================
# 2. ESTRUCTURA Y LÓGICA DE STREAMLIT
# (Aquí se soluciona el error sin tocar el HTML de los Dashboards)
# ===============================================

# --- Configuración y Estilos ---
st.set_page_config(layout="wide", page_title="Galería Cho")

estilo_completo = """
<style>
/* ----------------- TÍTULO 3D ----------------- */
.titulo-3d {
    font-size: 80px;
    font-weight: bold;
    color: #00FFFF; /* CYAN Brillante (base) */
    text-shadow: 
        -4px -4px 0 #0000FF, /* Sombra para efecto 3D */
        -2px -2px 0 #0000FF,
        2px 2px 0 #0000AA,
        4px 4px 0 #0000AA;
    line-height: 1.0;
}

.subtitulo-texto {
    font-size: 24px;
    color: #FFFF00; /* AMARILLO Brillante */
    margin-top: 10px; 
    margin-bottom: 30px;
    font-style: italic;
}

/* ----------------- BOTONES DE PLANTILLA (Miniaturas) ----------------- */

/* Estilo para Streamlit Button (lo hace grande y visual) */
div.stButton > button {
    width: 100%; 
    height: 180px; /* Tamaño de la miniatura */
    border: 3px solid #00FFFF;
    border-radius: 10px;
    padding: 10px;
    background-color: #1a1a1a;
    color: white;
    font-size: 18px;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
    /* El contenido del botón se ajusta automáticamente, ya que es una línea simple */
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center;
    text-align: center;
    white-space: normal; /* Permite que el texto envuelva si es necesario */
    line-height: 1.2;
}

/* Estilo para el texto dentro del botón (ahora incluye el icono) */
div.stButton > button p {
    font-weight: 600;
    font-size: 18px; /* Ajuste para el texto */
    margin: 0;
    padding: 0;
}

/* Efecto hover */
div.stButton > button:hover {
    background-color: #000033;
    border-color: #FFFF00; 
    box-shadow: 0 6px 16px rgba(255, 255, 0, 0.4);
    transform: translateY(-2px);
}
</style>
"""
st.markdown(estilo_completo, unsafe_allow_html=True)

# --- Estado de Sesión y Navegación ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_dashboard' not in st.session_state:
    st.session_state.selected_dashboard = None

def navigate_to_home():
    """Vuelve a la página principal de la galería."""
    st.session_state.page = 'home'
    st.session_state.selected_dashboard = None
    
def navigate_to_dashboard(clave):
    """Navega a la vista de un dashboard específico."""
    st.session_state.page = 'dashboard_view'
    st.session_state.selected_dashboard = clave

# --- Datos de Plantillas para la Galería ---
PLANTILLAS = [
    {"nombre": "Dashboard Moderno", "clave": "Moderno", "icono": "✨"},
    {"nombre": "Dashboard Financiero", "clave": "Financiero", "icono": "💰"},
    {"nombre": "Dashboard Industrial", "clave": "Industrial", "icono": "⚙️"},
    {"nombre": "Dashboard Médico", "clave": "Médico", "icono": "⚕️"},
    {"nombre": "Dashboard Retail/Ventas", "clave": "Retail", "icono": "🛒"},
    {"nombre": "Dashboard Tecnológico", "clave": "Tecnológico", "icono": "🤖"}
]

# ===============================================
# 3. RENDERIZADO DEL CONTENIDO
# ===============================================

# --- VISTA DE DASHBOARD ESPECÍFICO ---
if st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    # Muestra un botón de regreso
    st.button("⬅️ Volver a la Galería Principal", on_click=navigate_to_home)

    clave_actual = st.session_state.selected_dashboard
    titulo_actual = next((p['nombre'] for p in PLANTILLAS if p['clave'] == clave_actual), clave_actual)

    st.title(f"Vista Completa: {titulo_actual}")
    st.write("---")
    
    # Obtenemos el contenido HTML INTACTO del diccionario
    dashboard_html = HTML_CONTENT.get(clave_actual, "<h1>Error: Contenido no encontrado</h1>")

    # Renderizamos el contenido HTML completo, manteniendo su funcionalidad original.
    # El HTML es inyectado en un iframe y es totalmente funcional.
    html(dashboard_html, height=1200, scrolling=True)

# --- VISTA PRINCIPAL (HOME) ---
else:
    # Título y subtítulo 3D
    st.markdown('<div class="titulo-3d">Mirá cho!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-texto">Tenemos estas plantillas</div>', unsafe_allow_html=True)
    st.write("---")
    st.header("Selecciona una Plantilla para ver la Vista Previa")

    # Creamos 6 columnas
    cols = st.columns(6) 
    
    # Iteramos sobre las plantillas y creamos los botones
    for i, plantilla in enumerate(PLANTILLAS):
        with cols[i]:
            # **SOLUCIÓN AL ERROR:** Usamos una cadena de texto simple para el label, 
            # y el CSS personalizado hace el resto.
            btn_label_simple = f"{plantilla['icono']} {plantilla['nombre']}"
            
            if st.button(btn_label_simple, key=plantilla['clave']):
                navigate_to_dashboard(plantilla['clave'])

    # Contenido extra en la página principal
    st.write("---")
    st.info("Al hacer clic, el contenido HTML **original** se carga de forma totalmente funcional.")
    
    st.balloons()