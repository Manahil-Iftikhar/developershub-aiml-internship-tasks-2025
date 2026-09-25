"""Build next-session forecasting features and evaluate chronological holdouts."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


def prepare_prices(frame):
    frame = frame.copy()
    if isinstance(frame.columns, pd.MultiIndex):
        if len(frame.columns.get_level_values(-1).unique()) != 1:
            raise ValueError('Provide exactly one ticker.')
        frame.columns = frame.columns.get_level_values(0)
    required = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not set(required).issubset(frame.columns):
        raise ValueError(f'Required columns: {required}')
    frame = frame.sort_index()
    if frame.index.has_duplicates:
        raise ValueError('Each trading date must appear once.')
    values = frame[required].apply(pd.to_numeric, errors='raise')
    values['target'] = values['Close'].shift(-1)
    values['target_date'] = pd.Series(values.index, index=values.index).shift(-1)
    values = values.dropna()
    if len(values) < 30 or not np.isfinite(values[required + ['target']].to_numpy()).all():
        raise ValueError('At least 30 complete finite price rows are required.')
    return values


def evaluate(frame, seed=42):
    data = prepare_prices(frame)
    a, b = int(len(data) * 0.6), int(len(data) * 0.8)
    # One-row gaps keep training targets strictly before evaluation input dates.
    train, validation, test = data.iloc[:a-1], data.iloc[a:b-1], data.iloc[b:]
    features = ['Open', 'High', 'Low', 'Close', 'Volume']
    models = {'linear_regression': LinearRegression(),
              'random_forest': RandomForestRegressor(n_estimators=100, random_state=seed, n_jobs=1)}
    validation_rmse = {'persistence': float(np.sqrt(mean_squared_error(
        validation['target'], validation['Close'])))}
    for name, model in models.items():
        model.fit(train[features], train['target'])
        validation_rmse[name] = float(np.sqrt(mean_squared_error(
            validation['target'], model.predict(validation[features]))))
    winner = min(validation_rmse, key=validation_rmse.get)
    if winner == 'persistence':
        prediction = test['Close'].to_numpy()
    else:
        final_train = data.iloc[:b-1]
        models[winner].fit(final_train[features], final_train['target'])
        prediction = models[winner].predict(test[features])
    def score(pred):
        return {'mae': float(mean_absolute_error(test['target'], pred)),
                'rmse': float(np.sqrt(mean_squared_error(test['target'], pred)))}
    report = {'selected_model': winner, 'validation_rmse': validation_rmse,
              'test': {'selected_model': score(prediction), 'persistence': score(test['Close'])},
              'split': 'chronological 60/20/20 with a one-session boundary gap',
              'prediction_time': 'After market close, for the next observed trading session',
              'train_last_target_date': str(train['target_date'].iloc[-1]),
              'validation_first_input_date': str(validation.index[0]),
              'final_train_last_target_date': str(data.iloc[b-2]['target_date']),
              'test_first_input_date': str(test.index[0])}
    results = pd.DataFrame({'target_date': test['target_date'], 'actual': test['target'],
                            'prediction': prediction, 'persistence': test['Close']})
    return report, results
