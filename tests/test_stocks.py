import unittest
import numpy as np
import pandas as pd
from portfolio.stocks import evaluate, prepare_prices


class ForecastTests(unittest.TestCase):
    def frame(self):
        prices = 100 + np.arange(100)*0.1
        return pd.DataFrame({'Open': prices, 'High': prices+1, 'Low': prices-1,
                             'Close': prices+0.2, 'Volume': np.arange(100)+1000},
                            index=pd.bdate_range('2020-01-01', periods=100))

    def test_target_is_next_observed_session(self):
        frame = self.frame()
        prepared = prepare_prices(frame)
        self.assertEqual(prepared.iloc[0]['target'], frame.iloc[1]['Close'])
        self.assertEqual(prepared.iloc[0]['target_date'], frame.index[1])
        self.assertEqual(len(prepared), 99)

    def test_gap_excludes_boundary_targets(self):
        report, predictions = evaluate(self.frame())
        self.assertLess(pd.Timestamp(report['train_last_target_date']),
                        pd.Timestamp(report['validation_first_input_date']))
        self.assertLess(pd.Timestamp(report['final_train_last_target_date']),
                        pd.Timestamp(report['test_first_input_date']))
        self.assertIn('persistence', report['validation_rmse'])
        self.assertTrue(np.isfinite(predictions['prediction']).all())

    def test_duplicate_dates_rejected(self):
        frame = self.frame()
        with self.assertRaises(ValueError):
            prepare_prices(pd.concat([frame, frame.iloc[[0]]]))

    def test_multiple_tickers_rejected(self):
        frame = self.frame()
        combined = pd.concat({'A': frame, 'B': frame}, axis=1).swaplevel(axis=1)
        with self.assertRaises(ValueError):
            prepare_prices(combined)


if __name__ == '__main__':
    unittest.main()
