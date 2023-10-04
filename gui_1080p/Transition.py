def Transition(after, before, window):
    #before.__del__()
    del before
    #after.__init__(window)
    after(window)
    window.show()