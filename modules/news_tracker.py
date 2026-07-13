#!/usr/bin/env python3
"""News Tracker Module for GK AI"""

import requests
from typing import List, Dict
from datetime import datetime, timedelta

class NewsTracker:
    """Haberleri takip eden modül"""
    
    def __init__(self):
        self.timeout = 10
    
    def get_news(self, topic: str) -> List[Dict]:
        """Konuyla ilgili haberleri getir"""
        try:
            # NewsAPI kullan (ücretsiz plan var)
            # Alternatif: RSS feeds kullan
            return self._get_news_from_feeds(topic)
        except Exception as e:
            return [{"title": "❌ Hata", "description": f"Haberler alınamadı: {str(e)}"}]
    
    def _get_news_from_feeds(self, topic: str) -> List[Dict]:
        """RSS feed'lerden haberler al"""
        news = []
        
        # Örnek haberler (gerçek uygulamada RSS parse edilir)
        sample_news = [
            {
                "title": f"{topic}: Yeni Gelişmeler - {datetime.now().strftime('%d.%m.%Y')}",
                "description": f"{topic} ile ilgili en son haberler ve güncellemeler.",
                "published_at": datetime.now().isoformat(),
                "source": "GK News"
            },
            {
                "title": f"{topic}: Uzmanlar Ne Düşünüyor?",
                "description": f"Sektör uzmanları {topic} konusunda görüş bildirdiler.",
                "published_at": (datetime.now() - timedelta(hours=2)).isoformat(),
                "source": "GK News"
            }
        ]
        
        return sample_news
    
    def get_trending(self) -> List[str]:
        """Günün trendingi konuları getir"""
        return [
            "Yapay Zeka",
            "Teknoloji",
            "Programlama",
            "Cybersecurity",
            "Web Geliştirme"
        ]