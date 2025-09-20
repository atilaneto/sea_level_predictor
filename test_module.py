import unittest
import sea_level_predictor
import matplotlib as mpl

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected line plot title to be 'Rise in Sea Level'")
    
    def test_plot_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected line plot xlabel to be 'Year'")

    def test_plot_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected line plot ylabel to be 'Sea Level (inches)'")

    def test_plot_numlines(self):
        actual = len(self.ax.lines)
        expected = 2
        self.assertEqual(actual, expected, "Expected two lines on plot.")

if __name__ == "__main__":
    unittest.main()