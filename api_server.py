#!/usr/bin/env python3
"""
GK AI - REST API Server
Web uygulamalarıyla entegrasyon için
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime
from modules.web_search import WebSearch
from modules.code_generator import CodeGenerator
from modules.news_tracker import NewsTracker

app = Flask(__name__)
CORS(app)

# Modülleri başlat
web_search = WebSearch()
code_gen = CodeGenerator()
news_tracker = NewsTracker()

@app.route('/api/health', methods=['GET'])
def health():
    """Sunucu sağlık durumu"""
    return jsonify({
        "status": "healthy",
        "service": "GK AI API",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/search', methods=['GET'])
def search():
    """Web araması"""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({"error": "Query parametresi gerekli"}), 400
    
    results = web_search.search(query)
    return jsonify({
        "query": query,
        "results": results,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/code/generate', methods=['POST'])
def generate_code():
    """Kod üret"""
    data = request.get_json()
    
    if not data or 'prompt' not in data:
        return jsonify({"error": "prompt gerekli"}), 400
    
    prompt = data['prompt']
    code = code_gen.generate(prompt)
    
    return jsonify({
        "prompt": prompt,
        "code": code,
        "language": "python",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/news', methods=['GET'])
def get_news():
    """Haberleri getir"""
    topic = request.args.get('topic', 'technology')
    
    news = news_tracker.get_news(topic)
    trending = news_tracker.get_trending()
    
    return jsonify({
        "topic": topic,
        "news": news,
        "trending": trending,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/info', methods=['GET'])
def info():
    """GK AI Bilgisi"""
    return jsonify({
        "name": "GK AI",
        "version": "1.0.0",
        "description": "Gelişmiş Yapay Zeka Asistanı",
        "features": [
            "Web Search",
            "Code Generation",
            "News Tracking",
            "Natural Language Processing"
        ],
        "endpoints": [
            "/api/health",
            "/api/search",
            "/api/code/generate",
            "/api/news",
            "/api/info"
        ],
        "timestamp": datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    """404 Hatası"""
    return jsonify({"error": "Endpoint bulunamadı"}), 404

@app.errorhandler(500)
def internal_error(error):
    """500 Hatası"""
    return jsonify({"error": "İç sunucu hatası"}), 500

if __name__ == '__main__':
    print("\n🚀 GK AI API Server başlatılıyor...")
    print("📡 URL: http://localhost:5000")
    print("📚 API Docs: http://localhost:5000/api/info\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )