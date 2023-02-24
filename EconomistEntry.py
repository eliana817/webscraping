class Economist:
    def __init__(self, id, theme, sourceUrl, articleLink, summary, date, title):
        self.id = id
        self.theme = theme
        self.sourceUrl = sourceUrl
        self.articleLink = articleLink
        self.summary = summary
        self.date = date
        self.title = title

    def dictEntry(self, rows, id, c, links, h, allLinks, i, allP, allDates, allTitles):
        row = {}
        row[self.id] = id
        row[self.theme] = c
        row[self.sourceUrl] = links[h]

        row[self.articleLink] = allLinks[c][i]           
        row[self.summary] = allP[c][i]           
        row[self.date] = allDates[c][i]       
        row[self.title] = allTitles[c][i]

        rows.append(row)
        return rows

    def getEntry(self, list, column, value): #takes a list of dictionnaries as an argument and prints the lines 
        nbr = 0                              #where 'value' appears in the specified 'column' with the number of times it appears / can also change directly in a csv file
        try: #if list is indeed a list                             
            for k in range(len(list)):           
                if list[k][column] == value:
                    print(list[k])
                    nbr = nbr + 1
        except: #if list is data read from csv file
            for k in range(len(list.index)):           
                if list[column].iloc[k] == value:
                    print(list.loc[[k],:])
                    nbr = nbr + 1
        print("'",value, "' appears", nbr, "times in the '", column, "' column")
        return nbr

    def setEntry(self, list, column, old, new): #takes a list of dictionnaries and replaces the 'old' value where it exists in the specified
        nbr = 0                                 #column with the 'new' value / can also change directly in a csv file     
        try: #if list is indeed a list                 
            for k in range(len(list)):           
                if list[k][column] == old:
                    nbr = nbr + 1
                    list[k][column] = new
        except: #if list is data read from csv file
            for k in range(len(list.index)):           
                if list[column].iloc[k] == old:
                    nbr = nbr + 1
                    list[column][k] = new
                    list.to_csv('file.csv',index=False)
        print(nbr, "row has/have successfully been updated")
        return

