import datetime
import numpy as np

from midas import mix
from midas.midas import estimate, forecast


def test_estimate(gdp_data, farmpay_data):

    y, yl, x, yf, ylf, xf = mix.mix_freq(gdp_data.gdp, farmpay_data.farmpay, 3, 1, 1,
                                         start_date=datetime.datetime(1985, 1, 1),
                                         end_date=datetime.datetime(2009, 1, 1))

    res = estimate(y, yl, x)

    fc = forecast(xf, ylf, res)

    print(fc)

    assert np.isclose(fc.loc['2011-04-01'][0], 1.336844, rtol=1e-6)