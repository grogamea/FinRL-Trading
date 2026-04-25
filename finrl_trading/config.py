"""Configuration settings for FinRL-Trading.

Loads environment variables and defines default constants used across
the trading pipeline (data, model, and execution layers).
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# API / Broker credentials
# ---------------------------------------------------------------------------
ALPACA_API_KEY: str = os.getenv("ALPACA_API_KEY", "")
ALPACA_API_SECRET: str = os.getenv("ALPACA_API_SECRET", "")
ALPACA_API_BASE_URL: str = os.getenv(
    "ALPACA_API_BASE_URL", "https://paper-api.alpaca.markets"
)

# ---------------------------------------------------------------------------
# Data settings
# ---------------------------------------------------------------------------
DATA_START_DATE: str = os.getenv("DATA_START_DATE", "2018-01-01")
DATA_END_DATE: str = os.getenv("DATA_END_DATE", "2023-12-31")

# Train / validation / test split dates
TRAIN_START_DATE: str = os.getenv("TRAIN_START_DATE", "2018-01-01")
TRAIN_END_DATE: str = os.getenv("TRAIN_END_DATE", "2021-12-31")
VAL_START_DATE: str = os.getenv("VAL_START_DATE", "2022-01-01")
VAL_END_DATE: str = os.getenv("VAL_END_DATE", "2022-12-31")
TEST_START_DATE: str = os.getenv("TEST_START_DATE", "2023-01-01")
TEST_END_DATE: str = os.getenv("TEST_END_DATE", "2023-12-31")

# Default ticker universe (Dow-30 subset for quick experiments)
DEFAULT_TICKERS: list[str] = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "META",
    "TSLA", "NVDA", "JPM", "V", "JNJ",
]

# Technical indicators computed during feature engineering
INDICATOR_LIST: list[str] = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
]

# ---------------------------------------------------------------------------
# Environment / simulation settings
# ---------------------------------------------------------------------------
INITIAL_AMOUNT: float = float(os.getenv("INITIAL_AMOUNT", "1_000_000"))
TRANSACTION_COST_PCT: float = float(os.getenv("TRANSACTION_COST_PCT", "0.001"))
REWARD_SCALING: float = float(os.getenv("REWARD_SCALING", "1e-4"))

# Maximum number of shares that can be traded in a single action
MAX_STOCK_QUANTITY: int = int(os.getenv("MAX_STOCK_QUANTITY", "100"))

# Turbulence threshold used to switch to risk-off mode
TURBULENCE_THRESHOLD: float = float(os.getenv("TURBULENCE_THRESHOLD", "140"))

# ---------------------------------------------------------------------------
# RL training settings
# ---------------------------------------------------------------------------
RL_ALGORITHM: str = os.getenv("RL_ALGORITHM", "PPO")  # PPO | A2C | DDPG | SAC | TD3
TOTAL_TIMESTEPS: int = int(os.getenv("TOTAL_TIMESTEPS", "500_000"))
N_ENVS: int = int(os.getenv("N_ENVS", "4"))  # parallel environments

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR: str = os.path.join(ROOT_DIR, "data")
MODEL_DIR: str = os.path.join(ROOT_DIR, "trained_models")
RESULTS_DIR: str = os.path.join(ROOT_DIR, "results")
LOG_DIR: str = os.path.join(ROOT_DIR, "logs")

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
