def alphacode(ac):
    # how many ways can I partition this alphacode
    result = []
    LIMIT = len(ac)
    alpha_h = {}
    def alpha_generate(ac,i,g,s,combinations):
        if i >= len(ac):
            k = ""
            for n in g::
                k += alpha_h[n]
            combinations.append(k)
        
        if len(g) < 2:
            
            alpha_generate(ac,i+1,g,s,combinations)
        if len(g) < 1:
            alpha_generate(ac,i+1,g,s,combinations)
        
