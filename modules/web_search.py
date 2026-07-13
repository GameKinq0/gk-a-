#!/usr/bin/env python3
"""Web Search Module for GK AI"""

import requests
import json
from typing import List, Dict, Optional
from urllib.parse import quote

class WebSearch:
    """Web araması yapan modül"""
    
    def __init__(self):
        self.timeout = 10
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search(self, query: str, num_results: int = 5) -> List[Dict]:
        """Google'da ara"""
        try:
            # DuckDuckGo API'si kullan (ücretsiz, API key gerekmez)
            url = f"https://api.duckduckgo.com/?q={quote(query)}&format=json"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            results = []
            
            # Abstract'tan sonuçlar al
            if 'AbstractText' in data and data['AbstractText']:
                results.append({
                    'title': data.get('Heading', 'Arama Sonucu'),
                    'snippet': data['AbstractText'],
                    'link': data.get('AbstractURL', '#')
                })
            
            # Related Topics'ten sonuçlar al
            if 'RelatedTopics' in data:
                for topic in data['RelatedTopics'][:num_results-1]:
                    if 'Text' in topic:
                        results.append({
                            'title': topic.get('Text', 'Konu')[:100],
                            'snippet': topic.get('Text', 'Açıklama')[:300],
                            'link': topic.get('FirstURL', '#')
                        })
            
            return results[:num_results]
        
        except requests.exceptions.RequestException as e:
            return [{"title": "❌ Hata", "snippet": f"Arama yapılamadı: {str(e)}", "link": "#"}]
        except Exception as e:
            return [{"title": "❌ Hata", "snippet": f"Beklenmeyen hata: {str(e)}", "link": "#"}]
    
    def search_wikipedia(self, query: str) -> Dict[str, str]:
        """Wikipedia'da ara"""
        try:
            import wikipedia
            wikipedia.set_lang('tr')
            
            results = wikipedia.search(query)
            if results:
                page = wikipedia.page(results[0])
                return {
                    'title': page.title,
                    'content': page.content[:1000],
                    'url': page.url
                }
        except:
            pass
        
        return {'title': 'Bulunamadı', 'content': '', 'url': ''}