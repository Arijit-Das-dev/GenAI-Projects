import streamlit as st
import streamlit.components.v1 as components

def render_about_page():
    
    about_page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Jarvis AI - About</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
            
            /* 🔥 Smooth Scroll */
            html {
                scroll-behavior: smooth;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                background: #0d0d12;
                color: #ffffff;
                overflow-x: hidden;
                line-height: 1.6;
            }
            
            /* Gradient background */
            .gradient-bg {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: radial-gradient(ellipse at top, #1a1a2e 0%, #0d0d12 50%);
                z-index: 0;
            }
            
            /* ⚡ Thunder/Lightning Background Effect */
            .thunder-canvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 0;
                pointer-events: none;
                opacity: 0.4;
            }
            
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 24px;
                position: relative;
                z-index: 1;
            }
            
            /* Hero Section - n8n style */
            .hero {
                text-align: center;
                padding: 120px 24px 80px;
                position: relative;
            }
            
            .hero-badge {
                display: inline-block;
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                color: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: 600;
                margin-bottom: 24px;
                letter-spacing: 0.5px;
                text-transform: uppercase;
            }
            
            .hero-title {
                font-size: clamp(42px, 7vw, 72px);
                font-weight: 900;
                line-height: 1.1;
                margin-bottom: 24px;
                letter-spacing: -0.02em;
            }
            
            .hero-title .gradient-text {
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .hero-description {
                font-size: 20px;
                color: #a1a1aa;
                max-width: 700px;
                margin: 0 auto 40px;
                line-height: 1.7;
                font-weight: 400;
            }
            
            .hero-buttons {
                display: flex;
                gap: 16px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 40px;
            }
            
            .btn-primary {
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                color: white;
                padding: 16px 32px;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                text-decoration: none;
                transition: all 0.3s;
                border: none;
                cursor: pointer;
                display: inline-flex;
                align-items: center;
                gap: 8px;
            }
            
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 20px 40px rgba(99, 102, 241, 0.3);
            }
            
            .btn-secondary {
                background: rgba(255, 255, 255, 0.05);
                color: white;
                padding: 16px 32px;
                border-radius: 12px;
                font-size: 16px;
                font-weight: 600;
                text-decoration: none;
                transition: all 0.3s;
                border: 1px solid rgba(255, 255, 255, 0.1);
                cursor: pointer;
            }
            
            .btn-secondary:hover {
                background: rgba(255, 255, 255, 0.1);
                border-color: rgba(255, 255, 255, 0.2);
            }
            
            /* Stats Section */
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 24px;
                margin: 80px 0;
                padding: 0 24px;
            }
            
            .stat-card {
                text-align: center;
                padding: 32px 24px;
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 16px;
                transition: all 0.3s;
            }
            
            .stat-card:hover {
                background: rgba(255, 255, 255, 0.05);
                border-color: rgba(99, 102, 241, 0.3);
                transform: translateY(-4px);
            }
            
            .stat-number {
                font-size: 48px;
                font-weight: 900;
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                line-height: 1.2;
            }
            
            .stat-label {
                font-size: 14px;
                color: #a1a1aa;
                margin-top: 8px;
                font-weight: 500;
            }
            
            /* Section Title */
            .section {
                padding: 80px 24px;
            }
            
            .section-header {
                text-align: center;
                margin-bottom: 64px;
            }
            
            .section-title {
                font-size: clamp(32px, 5vw, 48px);
                font-weight: 800;
                margin-bottom: 16px;
                letter-spacing: -0.02em;
            }
            
            .section-subtitle {
                font-size: 18px;
                color: #a1a1aa;
                max-width: 600px;
                margin: 0 auto;
            }
            
            /* Features Grid - n8n style cards */
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
                gap: 24px;
                margin-bottom: 48px;
            }
            
            .feature-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 20px;
                padding: 40px;
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                position: relative;
                overflow: hidden;
            }
            
            .feature-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
                transform: scaleX(0);
                transform-origin: left;
                transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            }
            
            .feature-card:hover {
                background: rgba(255, 255, 255, 0.05);
                border-color: rgba(99, 102, 241, 0.3);
                transform: translateY(-8px);
            }
            
            .feature-card:hover::before {
                transform: scaleX(1);
            }
            
            .feature-icon {
                font-size: 48px;
                margin-bottom: 20px;
                display: block;
            }
            
            .feature-title {
                font-size: 24px;
                font-weight: 700;
                margin-bottom: 12px;
                color: #ffffff;
            }
            
            .feature-description {
                font-size: 15px;
                color: #a1a1aa;
                line-height: 1.7;
                margin-bottom: 20px;
            }
            
            .feature-list {
                list-style: none;
                padding: 0;
            }
            
            .feature-list li {
                font-size: 14px;
                color: #d4d4d8;
                padding: 8px 0;
                padding-left: 24px;
                position: relative;
            }
            
            .feature-list li::before {
                content: '✓';
                position: absolute;
                left: 0;
                color: #6366f1;
                font-weight: bold;
            }
            
            /* Tech Stack - Clean grid */
            .tech-section {
                background: rgba(255, 255, 255, 0.02);
                border-radius: 24px;
                padding: 64px 40px;
                margin: 80px 24px;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }
            
            .tech-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
                gap: 16px;
                margin-top: 48px;
            }
            
            .tech-item {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                padding: 24px;
                text-align: center;
                transition: all 0.3s;
            }
            
            .tech-item:hover {
                background: rgba(99, 102, 241, 0.1);
                border-color: rgba(99, 102, 241, 0.3);
                transform: translateY(-4px);
            }
            
            .tech-icon {
                font-size: 32px;
                margin-bottom: 8px;
            }
            
            .tech-name {
                font-size: 14px;
                color: #d4d4d8;
                font-weight: 500;
            }
            
            /* CTA Section */
            .cta-section {
                text-align: center;
                padding: 100px 24px;
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);
                border-radius: 24px;
                margin: 80px 24px;
                border: 1px solid rgba(99, 102, 241, 0.2);
            }
            
            .cta-title {
                font-size: clamp(32px, 5vw, 48px);
                font-weight: 800;
                margin-bottom: 16px;
                letter-spacing: -0.02em;
            }
            
            .cta-subtitle {
                font-size: 18px;
                color: #a1a1aa;
                margin-bottom: 32px;
                max-width: 600px;
                margin-left: auto;
                margin-right: auto;
            }
            
            /* Social Links */
            .social-section {
                text-align: center;
                padding: 80px 24px;
            }
            
            .social-grid {
                display: flex;
                justify-content: center;
                gap: 24px;
                margin-top: 32px;
                flex-wrap: wrap;
            }
            
            .social-link {
                width: 56px;
                height: 56px;
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: all 0.3s;
                text-decoration: none;
            }
            
            .social-link:hover {
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                border-color: transparent;
                transform: translateY(-4px);
            }
            
            .social-link img {
                width: 24px;
                height: 24px;
                opacity: 0.7;
                transition: opacity 0.3s;
            }
            
            .social-link:hover img {
                opacity: 1;
                filter: brightness(2);
            }
            
            /* Footer */
            .footer {
                text-align: center;
                padding: 40px 24px;
                border-top: 1px solid rgba(255, 255, 255, 0.08);
                margin-top: 80px;
            }
            
            .footer-text {
                font-size: 14px;
                color: #71717a;
            }
            
            /* Scrollbar */
            ::-webkit-scrollbar {
                width: 8px;
            }
            
            ::-webkit-scrollbar-track {
                background: #1a1a2e;
            }
            
            ::-webkit-scrollbar-thumb {
                background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
                border-radius: 4px;
            }
            
            /* Responsive */
            @media (max-width: 768px) {
                .hero {
                    padding: 80px 16px 60px;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                }
                
                .tech-grid {
                    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
                }
                
                .stats-grid {
                    grid-template-columns: repeat(2, 1fr);
                }
            }
        </style>
    </head>
    <body>
        <div class="gradient-bg"></div>
        
        <!-- ⚡ Thunder Background Canvas -->
        <canvas class="thunder-canvas" id="thunderCanvas"></canvas>
        
        <div class="container">
            <!-- Hero Section -->
            <div class="hero">
                <div class="hero-badge">AI for Developers</div>
                <h1 class="hero-title">
                    <span class="gradient-text">JARVIS AI</span><br>
                    Your Next-Generation AI Assistant
                </h1>
                <p class="hero-description">
                    Experience the future of artificial intelligence with Jarvis AI - a comprehensive platform 
                    that combines voice interaction, intelligent code assistance, and creative image generation 
                    in one seamless interface.
                </p>
                <div class="hero-buttons">
                    <a href="#features" class="btn-primary">Explore Features →</a>
                    <a href="#tech" class="btn-secondary">View Technology</a>
                </div>
            </div>
            
            <!-- Stats Grid -->
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number">3</div>
                    <div class="stat-label">Core Features</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Availability</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">∞</div>
                    <div class="stat-label">Possibilities</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">AI-Powered</div>
                </div>
            </div>
            
            <!-- Features Section -->
            <div class="section" id="features">
                <div class="section-header">
                    <h2 class="section-title">Powerful Capabilities</h2>
                    <p class="section-subtitle">Everything you need in an AI assistant, built with cutting-edge technology</p>
                </div>
                
                <div class="features-grid">
                    <!-- Feature 1 -->
                    <div class="feature-card">
                        <span class="feature-icon">🎙️</span>
                        <h3 class="feature-title">Voice Assistant</h3>
                        <p class="feature-description">
                            Engage in natural conversations with advanced voice-enabled AI. Speak naturally and receive human-like audio responses.
                        </p>
                        <ul class="feature-list">
                            <li>Real-time voice interaction</li>
                            <li>Natural, human-like responses</li>
                            <li>Advanced STT & TTS integration</li>
                            <li>Object detection via webcam</li>
                            <li>Context-aware conversations</li>
                        </ul>
                    </div>
                    
                    <!-- Feature 2 -->
                    <div class="feature-card">
                        <span class="feature-icon">💻</span>
                        <h3 class="feature-title">Jarvis Editor</h3>
                        <p class="feature-description">
                            Revolutionary code editor with built-in AI compiler and copilot. Write code in any language with instant feedback.
                        </p>
                        <ul class="feature-list">
                            <li>All programming languages supported</li>
                            <li>AI-powered code compilation</li>
                            <li>Real-time error detection</li>
                            <li>Step-by-step coding assistance</li>
                            <li>Detailed dry runs & explanations</li>
                            <li>Save code to local device</li>
                        </ul>
                    </div>
                    
                    <!-- Feature 3 -->
                    <div class="feature-card">
                        <span class="feature-icon">🎨</span>
                        <h3 class="feature-title">Jarvis Lab</h3>
                        <p class="feature-description">
                            Transform your imagination into stunning visuals with AI-powered image generation from simple text prompts.
                        </p>
                        <ul class="feature-list">
                            <li>Prompt-based image generation</li>
                            <li>High-quality AI-generated images</li>
                            <li>Multiple artistic styles</li>
                            <li>Fast rendering engine</li>
                            <li>Download & save creations</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Tech Stack Section -->
            <div class="tech-section" id="tech">
                <div class="section-header">
                    <h2 class="section-title">Built With Cutting-Edge Technology</h2>
                    <p class="section-subtitle">Powered by the latest in AI and web technologies</p>
                </div>
                
                <div class="tech-grid">
                    <div class="tech-item">
                        <div class="tech-icon">💻</div>
                        <div class="tech-name">Code Editor</div>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🤖</div>
                        <div class="tech-name">AI Models</div>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🎤</div>
                        <div class="tech-name">Speech Recognition</div>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🔊</div>
                        <div class="tech-name">Text-to-Speech</div>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">🎨</div>
                        <div class="tech-name">Image Generation</div>
                    </div>
                    <div class="tech-item">
                        <div class="tech-icon">⚙️</div>
                        <div class="tech-name">NLP</div>
                    </div>
                </div>
            </div>
            
            <!-- CTA Section -->
            <div class="cta-section">
                <h2 class="cta-title">Ready to Experience the Future?</h2>
                <p class="cta-subtitle">
                    Start your journey with Jarvis AI today and unlock intelligent assistance for all your tasks
                </p>
            </div>
            
            <!-- Social Section -->
            <div class="social-section">
                <h2 class="section-title">Connect With Me</h2>
                <p class="section-subtitle">Find me across social platforms</p>
                
                <div class="social-grid">
                    <a href="https://instagram.com/self.__arijittt" target="_blank" class="social-link">
                        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram">
                    </a>
                    <a href="https://www.linkedin.com/in/arijit-das-b912842a0" target="_blank" class="social-link">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
                    </a>
                    <a href="https://github.com/Arijit-Das-dev" target="_blank" class="social-link">
                        <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
                    </a>
                    <a href="https://facebook.com/" target="_blank" class="social-link">
                        <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook">
                    </a>
                </div>
            </div>
            
            <!-- Footer -->
            <div class="footer">
                <p class="footer-text">© 2025 Jarvis AI | All right reserved.</p>
            </div>
        </div>

        <!-- ⚡ Thunder Animation Script -->
        <script>
            const canvas = document.getElementById('thunderCanvas');
            const ctx = canvas.getContext('2d');
            
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
            
            window.addEventListener('resize', () => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            });
            
            class Lightning {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = 0;
                    this.segments = [];
                    this.maxSegments = Math.floor(Math.random() * 15) + 10;
                    this.displacement = 80;
                    this.alpha = 1;
                    this.fadeSpeed = 0.02;
                    this.branches = [];
                    this.color = this.getRandomColor();
                }
                
                getRandomColor() {
                    const colors = [
                        'rgba(99, 102, 241, ',    // indigo
                        'rgba(168, 85, 247, ',    // purple
                        'rgba(236, 72, 153, ',    // pink
                        'rgba(139, 92, 246, '     // violet
                    ];
                    return colors[Math.floor(Math.random() * colors.length)];
                }
                
                generate() {
                    let startX = this.x;
                    let startY = this.y;
                    let endX = this.x;
                    let endY = canvas.height;
                    
                    this.segments = [{x: startX, y: startY}];
                    
                    for (let i = 0; i < this.maxSegments; i++) {
                        const t = i / this.maxSegments;
                        const midX = startX + (endX - startX) * t;
                        const midY = startY + (endY - startY) * t;
                        
                        const offsetX = (Math.random() - 0.5) * this.displacement;
                        const offsetY = (Math.random() - 0.5) * this.displacement * 0.3;
                        
                        this.segments.push({
                            x: midX + offsetX,
                            y: midY + offsetY
                        });
                        
                        // Create branches
                        if (Math.random() > 0.7 && i > 3) {
                            this.createBranch(midX + offsetX, midY + offsetY, i);
                        }
                    }
                    
                    this.segments.push({x: endX, y: endY});
                }
                
                createBranch(x, y, segmentIndex) {
                    const branch = [];
                    const branchLength = Math.floor(Math.random() * 5) + 3;
                    let bx = x;
                    let by = y;
                    
                    for (let i = 0; i < branchLength; i++) {
                        bx += (Math.random() - 0.5) * 60;
                        by += Math.random() * 40 + 20;
                        branch.push({x: bx, y: by});
                    }
                    
                    this.branches.push(branch);
                }
                
                draw() {
                    if (this.alpha <= 0) return;
                    
                    // Main lightning bolt
                    ctx.strokeStyle = this.color + this.alpha + ')';
                    ctx.lineWidth = 3;
                    ctx.shadowBlur = 20;
                    ctx.shadowColor = this.color + this.alpha + ')';
                    ctx.lineCap = 'round';
                    ctx.lineJoin = 'round';
                    
                    ctx.beginPath();
                    ctx.moveTo(this.segments[0].x, this.segments[0].y);
                    for (let i = 1; i < this.segments.length; i++) {
                        ctx.lineTo(this.segments[i].x, this.segments[i].y);
                    }
                    ctx.stroke();
                    
                    // Glow effect
                    ctx.strokeStyle = this.color + (this.alpha * 0.3) + ')';
                    ctx.lineWidth = 8;
                    ctx.shadowBlur = 40;
                    ctx.beginPath();
                    ctx.moveTo(this.segments[0].x, this.segments[0].y);
                    for (let i = 1; i < this.segments.length; i++) {
                        ctx.lineTo(this.segments[i].x, this.segments[i].y);
                    }
                    ctx.stroke();
                    
                    // Draw branches
                    ctx.lineWidth = 2;
                    ctx.shadowBlur = 15;
                    this.branches.forEach(branch => {
                        ctx.strokeStyle = this.color + (this.alpha * 0.7) + ')';
                        ctx.beginPath();
                        ctx.moveTo(branch[0].x, branch[0].y);
                        for (let i = 1; i < branch.length; i++) {
                            ctx.lineTo(branch[i].x, branch[i].y);
                        }
                        ctx.stroke();
                    });
                    
                    ctx.shadowBlur = 0;
                }
                
                update() {
                    this.alpha -= this.fadeSpeed;
                    this.draw();
                }
            }
            
            const lightnings = [];
            let lastLightning = 0;
            
            function animate(timestamp) {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Create new lightning periodically
                if (timestamp - lastLightning > Math.random() * 2000 + 1000) {
                    const lightning = new Lightning();
                    lightning.generate();
                    lightnings.push(lightning);
                    lastLightning = timestamp;
                }
                
                // Update and draw all lightnings
                for (let i = lightnings.length - 1; i >= 0; i--) {
                    lightnings[i].update();
                    if (lightnings[i].alpha <= 0) {
                        lightnings.splice(i, 1);
                    }
                }
                
                requestAnimationFrame(animate);
            }
            
            animate(0);
            
            // Smooth scroll
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href'))
                        .scrollIntoView({ behavior: 'smooth', block: 'start' });
                });
            });
        </script>

    </body>
    </html>
    """
    
    components.html(about_page_html, height=3800, scrolling=True)