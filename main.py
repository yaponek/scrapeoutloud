import lxml
import requests
import bs4
import re
import win32com.client as wincl
    
  #set the example url
res = requests.get("https://en.wikipedia.org/wiki/Magnetic-core_memory")

#res.text

data_result = bs4.BeautifulSoup(res.text, 'html.parser')
#type(data_result)

all_paragraphs = data_result.find_all('p');

intro = 7
full = len(all_paragraphs)
# For window specific ofline TTS 
text2speech = wincl.Dispatch("SAPI.SpVoice")

for index in range(intro):
    clean_data = all_paragraphs[index].get_text()
    clean_data = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", clean_data)
    print(clean_data)
    text2speech.Speak(clean_data)
