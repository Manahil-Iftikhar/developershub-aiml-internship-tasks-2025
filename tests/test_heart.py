import tempfile
from pathlib import Path
import unittest

from portfolio.heart import parse_cleveland, load_cleveland


class ClevelandDataTests(unittest.TestCase):
    def test_target_mapping_missing_values_and_categorical_codes(self):
        rows = [f'63,1,1,145,233,1,2,150,0,2.3,3,?, ?,{label}'
                for label in range(5)]
        raw = ('\n'.join(rows).replace(' ?,', '?,')).encode()
        frame, missing = parse_cleveland(raw)
        self.assertEqual(frame.target.tolist(), [0, 1, 1, 1, 1])
        self.assertNotIn('num', frame)
        self.assertEqual(frame.cp.tolist(), ['code_1'] * 5)
        self.assertEqual(frame.thal.tolist(), ['missing'] * 5)
        self.assertEqual(missing['ca'], 5)
        self.assertTrue(frame.ca.isna().all())

    def test_rejects_invalid_target_category_and_shape(self):
        valid = '63,1,1,145,233,1,2,150,0,2.3,3,0,6,0'
        for raw in (valid[:-1] + '5', valid[:-1] + '?',
                    valid.replace('63,1,1', '63,1,9'), '1,2,3'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                parse_cleveland(raw.encode())

    def test_rejects_unreviewed_source_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'data'
            path.write_bytes(b'changed source')
            with self.assertRaisesRegex(ValueError, 'SHA-256'):
                load_cleveland(path)
