import unittest
from pathlib import Path
import main  # deine main.py

class TestAudit(unittest.TestCase):
    def test_comma_decimal_and_le_zero(self):
        rows = [
            {"kunde":"1","stadt":"Köln","betrag":"24,50","kanal":"online"},
            {"kunde":"2","stadt":"Bonn","betrag":"0.00","kanal":"filiale"},
        ]
        # Parsing wie im echten Code:
        for r in rows:
            val = str(r.get("betrag","")).replace(",", ".")
            try: r["betrag"] = float(val)
            except: r["betrag"] = None

        res = main.audit(rows)
        self.assertEqual(res["pos_count"], 1)
        self.assertAlmostEqual(res["umsatz"], 24.50, places=2)

    def test_group_summaries(self):
        rows = [
            {"kunde":"1001","stadt":"Köln","betrag":39.90,"kanal":"online"},
            {"kunde":"1002","stadt":"Bonn","betrag":12.00,"kanal":"filiale"},
        ]
        res = main.audit(rows)
        self.assertAlmostEqual(res["by_stadt"]["Köln"], 39.90, places=2)
        self.assertAlmostEqual(res["by_kanal"]["filiale"], 12.00, places=2)

if __name__ == "__main__":
    unittest.main()
