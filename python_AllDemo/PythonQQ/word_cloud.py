from wordcloud import WordCloud
import matplotlib.pyplot as plt
with open('zone_text.txt','r') as f:
    mytext = f.read()

font = r'C:\Windows\Fonts\simfang.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2).generate(mytext)
wc.to_file('zone.png')
plt.imshow(wc)
plt.axis("off")
plt.show()
plt.show()