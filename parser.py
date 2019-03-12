def find_links(path, name):
    """ Finds existing links that the given page refers to
    :path: string
    :name: string
    :rtype: list[n]
    """
    
    with open('{}{}'.format(path, name)) as data:
        soup = BeautifulSoup(data, 'lxml')
        links = [link.get('href') for link in soup.find_all('a')]
        existing_links = []
        for link in links:
            if os.path.isfile('.{}'.format(link)) \
                        and link.split('/')[2] not in existing_links:
                existing_links.append(link.split('/')[2])
        
    return existing_links

def find_common_links(links, link_to_find):
    """ Finds out whether there is a link we're looking for in a list
    :links: list[n]
    :link_to_find: string
    :rtype: bool
    """
    
    for link in links:
        if link == link_to_find:
            return True
    return False

path_ = []

def check(start, link_to_find, path, count=1, checked_links=set()):
    """ Finds the links bridge from start page to the end one
    :start: string
    :link_to_find: string
    :path: string
    :__count: int
    :__checked_links: set
    """
    
    #path = []
    #checked_links = set()
    if find_common_links(find_links('./wiki/', start), link_to_find):
        path_.append(start)
        return True
    elif count < 3:
        for link in find_links('./wiki/', start):
            if link not in checked_links:
                checked_links.add(link)
                if check(link, link_to_find, './wiki/', (count+1), checked_links):
                    path_.append(start)

def build_bridge(start, end, path):
    """ Finds the links bridge from start page to the end one
    :start: string
    :end: string
    :path: string
    :rtype: list[n]
    """
    
    bridge = check(start, end, path)
    return bridge

start = 'Stone_Age'
end = 'Python_(programming_language)'
path = './wiki/'

bridge = build_bridge(start, end, path)

path_.append(start)
path_.append(end)
print(path_)