import unittest
import sea_level_predictor

class SeaLevelTestCase(unittest.TestCase):
    def test_plot_exists(self):
        ax = sea_level_predictor.draw_plot()
        self.assertIsNotNone(ax)

if __name__ == "__main__":
    unittest.main()
