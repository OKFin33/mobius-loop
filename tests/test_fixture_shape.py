from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class FixtureShapeTest(unittest.TestCase):
    def test_basic_fixture_has_agent_config(self):
        path = ROOT / "fixtures" / "vault-basic" / "projects" / "demo" / ".agent" / "config.yaml"
        self.assertTrue(path.exists())

    def test_v0_skills_present(self):
        for name in ["mobius-loop", "wiki-retrieval", "wiki-bridge", "wiki-fy"]:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").exists(), name)


if __name__ == "__main__":
    unittest.main()

