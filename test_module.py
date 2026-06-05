import unittest
import sea_level_predictor
import matplotlib as mpl

class DataAnalysisTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected plot title to be 'Rise in Sea Level'")

    def test_plot_labels(self):
        actual_x = self.ax.get_xlabel()
        expected_x = "Year"
        self.assertEqual(actual_x, expected_x, "Expected x label to be 'Year'")
        
        actual_y = self.ax.get_ylabel()
        expected_y = "Sea Level (inches)"
        self.assertEqual(actual_y, expected_y, "Expected y label to be 'Sea Level (inches)'")

    def test_plot_data_lines(self):
        # Verify that lines of best fit are correctly drawn
        lines = self.ax.get_lines()
        self.assertEqual(len(lines), 2, "Expected two regression lines to be plotted.")
        
        # Check if the first line extends to 2050
        x_data_line1 = lines[0].get_xdata()
        self.assertEqual(x_data_line1[-1], 2050, "The first line of best fit should extend to 2050.")
        
        # Check if the second line starts at 2000 and ends at 2050
        x_data_line2 = lines[1].get_xdata()
        self.assertEqual(x_data_line2[0], 2000, "The second line of best fit should start at year 2000.")
        self.assertEqual(x_data_line2[-1], 2050, "The second line of best fit should extend to 2050.")

if __name__ == "__main__":
    unittest.main()
