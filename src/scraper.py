from typing import Dict, List
import requests as _requests
import bs4 as _bs4

def _get_page_url(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def charts_of_the_day() -> List[List]:
    '''
    Return charts of the current day
    '''
    page = _get_page_url("https://genius.com/#top-songs")
    #Titles
    raw_titles = page.find_all(class_="ChartSongdesktop__Title-sc-18658hh-3 fODYHn")
    titles = [title.text for title in raw_titles]
    #Artists
    raw_artists = page.find_all(class_="ChartSongdesktop__Artist-sc-18658hh-5 kiggdb")
    artists = [artist.text for artist in raw_artists]
    #Streams
    raw_streams = page.find_all(class_="IconWithLabel__Container-sc-141ao6c-0 hliVmp")
    streams = [stream.text for stream in raw_streams]

    charts = [{"placement":i+1,"title":titles[i],"artist":artists[i],"streams":streams[i]} for i in range(len(titles))]
    return charts

print(charts_of_the_day())