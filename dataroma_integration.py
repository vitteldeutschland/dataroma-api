"""
Gemini AI와의 통합을 위한 모듈
"""

from portfolio_research import DataromaPortfolioResearch
import json

class DataromaGeminiTool:
    """Gemini를 위한 Dataroma 포트폴리오 분석 도구"""
    
    @staticmethod
    def get_investor_portfolio_tool():
        """투자자 포트폴리오 조회 Tool 정의"""
        return {
            "name": "get_investor_portfolio",
            "description": "Dataroma에서 특정 투자자의 포트폴리오 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "investor_id": {
                        "type": "string",
                        "description": "투자자 ID (예: buffett, soros, dalio 등)"
                    }
                },
                "required": ["investor_id"]
            }
        }
    
    @staticmethod
    def get_stock_info_tool():
        """주식 정보 조회 Tool 정의"""
        return {
            "name": "get_stock_info",
            "description": "Dataroma에서 특정 주식의 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, BRK.B 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def get_investors_holding_stock_tool():
        """주식 보유 투자자 조회 Tool 정의"""
        return {
            "name": "get_investors_holding_stock",
            "description": "Dataroma에서 특정 주식을 보유한 투자자 목록을 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "주식 종목코드 (예: AAPL, MSFT, BRK.B 등)"
                    }
                },
                "required": ["ticker"]
            }
        }
    
    @staticmethod
    def execute_investor_portfolio(investor_id: str) -> str:
        """투자자 포트폴리오 조회 실행"""
        return DataromaPortfolioResearch.get_investor_portfolio(investor_id)
    
    @staticmethod
    def execute_stock_info(ticker: str) -> str:
        """주식 정보 조회 실행"""
        return DataromaPortfolioResearch.get_stock_info(ticker)
    
    @staticmethod
    def execute_investors_holding_stock(ticker: str) -> str:
        """주식 보유 투자자 조회 실행"""
        return DataromaPortfolioResearch.get_investors_holding_stock(ticker)
    
    @staticmethod
    def analyze_portfolio(investor_id: str) -> str:
        """포트폴리오 분석 실행"""
        return DataromaPortfolioResearch.analyze_portfolio(investor_id)
