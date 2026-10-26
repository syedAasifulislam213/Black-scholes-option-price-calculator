import numpy as np
import scipy.stats as stats
class BS():
    def __init__(self,spot,strike,rate,days,volatility,multyplier=100):
        self.spot = spot
        self.strike = strike
        self.rate = rate
        self.days = days / 365
        self.volatility = volatility
        self.multyplier = multyplier

        self.d1 = (np.log(self.spot/self.strike)+ \
                   (self.rate+0.5*self.volatility**2)*(self.days)) \
                    / (self.volatility*np.sqrt(self.days))
        self.d2 = self.d1 - self.volatility*np.sqrt(self.days)
        self.N_tag_d1 = (np.exp(-0.5*self.d1**2)) / (np.sqrt(2*np.pi))

    def call_price(self):
        a = self.spot*stats.norm.cdf(self.d1)
        b = np.exp(-self.rate*self.days)*self.strike*stats.norm.cdf(self.d2)
        return '{:,.0f}'.format(round(a-b,2)*self.multyplier)

    def put_price(self):
        a = self.strike*np.exp(-self.rate*self.days)*stats.norm.cdf(-self.d2)
        b = self.spot*stats.norm.cdf(-self.d1)
        return '{:,.0f}'.format(round(a-b,2)*self.multyplier)

    def call_delta(self):
        return round(stats.norm.cdf(self.d1),2)

    def put_delta(self):
        return round(stats.norm.cdf(self.d1) -1,2)

    def call_gamma(self):
        return round(self.N_tag_d1 / (self.spot * self.volatility *np.sqrt(self.days)),4)

    def put_gamma(self):
        return round(self.call_gamma(),4)

    def call_vega(self):
        return round(np.sqrt((self.days)/2*np.pi))*(self.spot*np.exp(-0.5*(self.d1)**2))

    def put_vega(self):
        return round(self.call_vega(),2)

    def call_theta(self):
        return round(-(self.strike*np.exp(-self.rate*self.days))*self.rate*stats.norm.cdf(self.d2)\
                     -(self.spot*(self.volatility*np.exp(-0.5*(self.d1)**2)))/np.sqrt(8*np.pi*self.days),2)

    def put_theta(self):
        return round(-(self.strike*np.exp(-self.rate*self.days))*self.rate*stats.norm.cdf(self.d2)\
                     -(self.strike*np.exp(-self.rate*self.days))*(self.volatility*np.exp(-0.5*(self.d2)**2))/np.sqrt(8*np.pi*self.days)
                         +self.rate*self.strike*np.exp(-self.rate*self.days),2)

    def call_ro(self):
        return round(self.strike*self.days*np.exp(-self.rate*self.days)*stats.norm.cdf(self.d2),2)

    def put_ro(self):
        return round(self.strike*self.days*np.exp(-self.rate*self.days)*stats.norm.cdf(-self.d2),2)

if __name__ == '__main__':
    op1 = BS(1800,1800,0.01,30,0.2,1)
    op2 = BS(1800,1790,0.01,30,0.2,1)
    print('strike 1800'+op1.call_price())
    print('strike 1790'+op2.call_price())