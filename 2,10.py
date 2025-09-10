verdier = [1,2,3,4,5,6,7,8,9]
radLengde = round(len(verdier)**0.5)
for i in range(0,len(verdier),radLengde):
    print(*verdier[i:i+radLengde])