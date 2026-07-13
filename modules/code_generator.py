#!/usr/bin/env python3
"""Code Generation Module for GK AI"""

import re
from typing import Optional

class CodeGenerator:
    """Kod üretimi yapan modül"""
    
    def __init__(self):
        self.code_templates = self._load_templates()
    
    def _load_templates(self) -> dict:
        """Kod şablonlarını yükle"""
        return {
            "fibonacci": self._fibonacci_code,
            "factorial": self._factorial_code,
            "palindrome": self._palindrome_code,
            "sorting": self._sorting_code,
            "rest_api": self._rest_api_code,
            "web_scraper": self._web_scraper_code,
        }
    
    def generate(self, prompt: str) -> str:
        """Prompt'a göre kod üret"""
        prompt_lower = prompt.lower()
        
        # Şablonları kontrol et
        for key, generator in self.code_templates.items():
            if key in prompt_lower:
                return generator()
        
        # Özel prompt işleme
        return self._generate_custom_code(prompt)
    
    def _fibonacci_code(self) -> str:
        return '''# Fibonacci Sayı Dizisi

def fibonacci(n: int) -> list:
    """İlk n Fibonacci sayısını döndür"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Kullanım
if __name__ == "__main__":
    print(f"İlk 10 Fibonacci: {fibonacci(10)}")
    # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
    
    def _factorial_code(self) -> str:
        return '''# Faktöriyel Hesapla

def factorial(n: int) -> int:
    """n! hesapla"""
    if n < 0:
        raise ValueError("Negatif sayı")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Kullanım
if __name__ == "__main__":
    print(f"5! = {factorial(5)}")
    # Output: 5! = 120
'''
    
    def _palindrome_code(self) -> str:
        return '''# Palindrome Kontrolü

def is_palindrome(text: str) -> bool:
    """Metin palindrome mi kontrol et"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Kullanım
if __name__ == "__main__":
    test_words = ["racecar", "hello", "a man a plan a canal panama"]
    for word in test_words:
        print(f"{word}: {is_palindrome(word)}")
'''
    
    def _sorting_code(self) -> str:
        return '''# Çeşitli Sıralama Algoritmaları

def bubble_sort(arr: list) -> list:
    """Bubble Sort"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: list) -> list:
    """Quick Sort"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Kullanım
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Bubble Sort: {bubble_sort(arr.copy())}")
    print(f"Quick Sort: {quick_sort(arr.copy())}")
'''
    
    def _rest_api_code(self) -> str:
        return '''# Flask REST API

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Veritabanı simülasyonu
data = {"users": []}

@app.route('/api/users', methods=['GET'])
def get_users():
    """Tüm kullanıcıları getir"""
    return jsonify(data["users"])

@app.route('/api/users', methods=['POST'])
def create_user():
    """Yeni kullanıcı oluştur"""
    user = request.json
    data["users"].append(user)
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Belirli kullanıcıyı getir"""
    if user_id < len(data["users"]):
        return jsonify(data["users"][user_id])
    return jsonify({"error": "Kullanıcı bulunamadı"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''
    
    def _web_scraper_code(self) -> str:
        return '''# Web Scraper

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url: str) -> dict:
    """Website'den veri çek"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Başlıkları çek
        titles = [h1.get_text() for h1 in soup.find_all('h1')[:5]]
        
        # Linkleri çek
        links = [a.get('href') for a in soup.find_all('a')[:10]]
        
        return {
            'status': 'success',
            'titles': titles,
            'links': links,
            'title': soup.title.string if soup.title else 'N/A'
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

# Kullanım
if __name__ == "__main__":
    result = scrape_website("https://example.com")
    print(result)
'''
    
    def _generate_custom_code(self, prompt: str) -> str:
        """Özel prompt'a göre kod üret"""
        return f'''# {prompt}
# GK AI tarafından üretildi

def main():
    """Ana fonksiyon"""
    # Kodunuzu buraya yazın
    pass

if __name__ == "__main__":
    main()

# Not: Daha spesifik kod için lütfen daha detaylı açıklama yapın
# Örn: "Python'da REST API yaz", "JavaScript'te React component", vb.
'''