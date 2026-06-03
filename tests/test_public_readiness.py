import subprocess
import sys
import unittest


class PublicReadinessTest(unittest.TestCase):
    def test_public_readiness_check_passes(self):
        result = subprocess.run(
            [sys.executable, "tools/public_readiness_check.py"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

