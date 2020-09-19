__author__ = 'benwillett'

def thirtyDay():
    thirtyma = (priceHist / 30)
    return render_template('main.html', THIRTYMA=thirtyma)

def sixtyDay():
    thirtyma = (priceHist / 60)
    return render_template('main.html', SIXTYMA=sixtyma)

def ninetyDay():
    thirtyma = (priceHist / 90)
    return render_template('main.html', NINETYMA=ninetyma)



