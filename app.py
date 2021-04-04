from StockSentimentAnalysis import getStockSentiment
from Covid19TwitterSentimentAnalysis import getCovidSentiment
from Covid19Visualization import getCovidVisualization
from StockAnalysisPredictor import getStockPrediction


user = input("Enter what you want to see today: ")

if user == "StockSentiment":
    getStockSentiment()

if user == "CovidSentiment":
    getCovidSentiment()

if user == "StockPrediction":
    getStockPrediction()

if user == "CovidVisualization":
    getCovidVisualization()

