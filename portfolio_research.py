import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

class DataromaPortfolioResearch:
    """Dataroma 포트폴리오 분석 도구"""
    
    BASE_URL = "https://www.dataroma.com/m"
    
    @staticmethod
    def get_investor_portfolio(investor_id):
        """특정 투자자의 포트폴리오 정보 가져오기"""
        try:
            url = f"{DataromaPortfolioResearch.BASE_URL}/holdings.php?m={investor_id}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'investor_id': investor_id,
                'url': url,
                'status': 'found'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_stock_info(ticker):
        """특정 주식의 정보 가져오기"""
        try:
            url = f"{DataromaPortfolioResearch.BASE_URL}/stock.php?s={ticker.upper()}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'ticker': ticker.upper(),
                'url': url,
                'status': 'found'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_investors_holding_stock(ticker):
        """특정 주식을 보유한 투자자 목록 가져오기"""
        try:
            url = f"{DataromaPortfolioResearch.BASE_URL}/stock.php?s={ticker.upper()}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'ticker': ticker.upper(),
                'url': url,
                'status': 'found',
                'description': f'{ticker.upper()}를 보유한 투자자 정보'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def analyze_portfolio(investor_id):
        """포트폴리오 분석 (투자자 ID 기반)"""
        portfolio_data = DataromaPortfolioResearch.get_investor_portfolio(investor_id)
        return json.dumps({
            'analysis': 'Portfolio analysis in progress',
            'investor_id': investor_id,
            'data': json.loads(portfolio_data)
        }, ensure_ascii=False, indent=2)
