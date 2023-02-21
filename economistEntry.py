class economist:
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

#get + set

