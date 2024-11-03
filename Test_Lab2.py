import pytest
import numpy as np
from Lab2 import calc_min_max_temperature, calc_average_temperature, calc_median_temperature

def test_calc_min_max_temperature():
    temperature = [5, 67, 32, 45, 21]
    result = calc_min_max_temperature(temperature)
    assert result == [5, 67], f"Expected [5, 67], but got {result}"

def test_calc_average_temperature():
    temperature = [5, 67, 32, 45, 21]
    result = calc_average_temperature(temperature)
    expected = np.average(temperature)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_calc_median_temperature():
    temperature = [5, 67, 32, 45, 21]
    result = calc_median_temperature(temperature)
    expected = np.median(temperature)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    pytest.main()
