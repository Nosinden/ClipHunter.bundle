####################################################################################################
#                                                                                                  #
#                                     ClipHunter Plex Channel                                      #
#                                                                                                  #
####################################################################################################
#from updater import Updater

TITLE = L('title')
PREFIX = '/video/cliphunter'
BASE_URL = 'http://www.cliphunter.com'
#CACHE_TIME = CACHE_1HOUR
CACHE_TIME = 0

ICON = 'icon-default.png'
ICON_BM = 'icon-bookmarks.png'
ICON_BM_ADD = 'icon-add-bookmark.png'
ICON_BM_REMOVE = 'icon-remove-bookmark.png'
ICON_CAT = 'icon-tags.png'
ICON_LIST = 'icon-explore.png'
ICON_TV = 'icon-tv.png'
ICON_STARS = 'icon-stars.png'
ICON_PSTARS = 'icon-babe.png'
ICON_PLAYLIST = 'icon-playlist.png'
ART = 'art-default.jpg'

#/page/sort/all/rating/uploaded/duration/hd
SORT = [
    ('date', 'Date'), ('rel', 'Relevance'), ('views', 'Views'), ('rating', 'Rating')
    ]
RATING = [
    ('all/all', 'All'), ('all/super', 'Super High'), ('all/high', 'High'), ('all/medium', 'Medium')
    ]
DURATION = [
    ('all', 'All'), ('300', 'Short'), ('900', 'Medium'), ('1800', 'Long')
    ]
UPLOADED = [
    ('all', 'Any Time'), ('today', 'Today'), ('yesterday', 'Yesterday'), ('week', 'This Week'),
    ('month', 'This Month'), ('3months', '3 Months'), ('year', 'This Year')
    ]
CHANNELS = [
    ('alphabetical', 'A-Z'), ('recently-updated', 'Recently Updated'),
    ('most-popular', 'Most Popular'), ('top-rated', 'Top Rated'), ('most-viewed', 'Most Viewed'),
    ('video-duration', 'Video Duration')
    ]
CHANNEL_OPT = [('rating', 'Best'), ('date', 'Newest'), ('views', 'Most Views')]

####################################################################################################
def Start():
    HTTP.CacheTime = 0

    ObjectContainer.title1 = TITLE
    ObjectContainer.art = R(ART)

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)

    InputDirectoryObject.art = R(ART)

    VideoClipObject.art = R(ART)

    #ValidatePrefs()

####################################################################################################
@handler(PREFIX, TITLE, thumb=ICON, art=ART)
def MainMenu():
    """Setup Main Menu, Includes Updater"""

    oc = ObjectContainer(title2=TITLE, no_cache=True)

    #Updater(PREFIX + '/updater', oc)

    oc.add(DirectoryObject(
        key=Callback(HDOpt, title='Explore', href='/categories/All'),
        title='Explore', thumb=R(ICON_LIST)
        ))
    oc.add(DirectoryObject(
        key=Callback(CategoryList, title='Categories'),
        title='Categories', thumb=R(ICON_CAT)
        ))
    oc.add(DirectoryObject(
        key=Callback(ChannelList, title='Channels', href='/channels'),
        title='Channels', thumb=R(ICON_TV)
        ))
    oc.add(DirectoryObject(
        key=Callback(PopularList, title='Popular', href='/popular/ratings'),
        title='Popular', thumb=R(ICON_STARS)
        ))
    oc.add(DirectoryObject(
        key=Callback(PornstarOpt, title='Pornstars', href='/pornstars'),
        title='Pornstars', thumb=R(ICON_PSTARS)
        ))
    #oc.add(DirectoryObject(key=Callback(Playlists, title='Playlists'), title='Playlists', thumb=R(ICON_PLAYLIST)))
    #oc.add(DirectoryObject(key=Callback(MyBookmarks), title='My Bookmarks', thumb=R(ICON_BM)))
    #oc.add(PrefsObject(title='Preferences'))
    oc.add(InputDirectoryObject(
        key=Callback(Search),
        title='Search', summary='Search ClipHunter', prompt='Search for...', thumb=R('icon-search.png')))

    return oc

####################################################################################################
@route(PREFIX + '/validateprefs')
def ValidatePrefs():
    """
    Validate Prefs
    No Prefs to validate yet
    """

####################################################################################################
@route(PREFIX + '/categorylist')
def CategoryList(title):
    """Setup Category List"""

    oc = ObjectContainer(title2=title)
    url = BASE_URL + '/categories/'
    html = HTML.ElementFromURL(url, cacheTime=CACHE_TIME)
    for node in html.xpath('//div[@class="list-group"]/a'):
        href = node.get('href')
        name = node.get('title')
        if not name == 'All':
            oc.add(DirectoryObject(
                key=Callback(HDOpt, title='Category / %s' %name, href=href.replace(' ', '%20')),
                title=name
                ))
    return oc

####################################################################################################
@route(PREFIX + '/hd-opt')
def HDOpt(title, href):
    """
    Default, Channels
    All, HD
    """

    oc = ObjectContainer(title2=title)
    if 'Channels' in title:
        oc.add(DirectoryObject(
            key=Callback(ChannelOpt, title='%s / All' %title, href=href, hd=0),
            title='All (SD & HD)'))
        oc.add(DirectoryObject(
            key=Callback(ChannelOpt, title='%s / HD' %title, href=href, hd=1),
            title='HD (HD Only)'))
    else:
        oc.add(DirectoryObject(
            key=Callback(SortBy, title='%s / All' %title, href=href, hd=0),
            title='All (SD & HD)'))
        oc.add(DirectoryObject(
            key=Callback(SortBy, title='%s / HD' %title, href=href, hd=1),
            title='HD (HD Only)'))
    return oc

####################################################################################################
@route(PREFIX + '/sortby')
def SortBy(title, href, hd):
    """Sort By (Date, Relevance, Views, Rating)"""

    oc = ObjectContainer(title2=title)
    for h, s in SORT:
        oc.add(DirectoryObject(
            key=Callback(Rating, title='%s / %s' %(title, s), href='%s/1/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/rating')
def Rating(title, href, hd):
    """Rating (All, Super High, High, Medium)"""

    oc = ObjectContainer(title2=title)
    for h, s in RATING:
        oc.add(DirectoryObject(
            key=Callback(Uploaded, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/uploaded')
def Uploaded(title, href, hd):
    """Uploaded (Any Time, Today, Yesterday, This Week, This Month, 3 Months, This Year)"""

    oc = ObjectContainer(title2=title)
    for h, s in UPLOADED:
        oc.add(DirectoryObject(
            key=Callback(Duration, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/duration')
def Duration(title, href, hd):
    """Duration (All, Short, Medium, Long)"""

    oc = ObjectContainer(title2=title)
    for h, s in DURATION:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/%s/%s' %(href, h, hd), page=1),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/channel/list')
def ChannelList(title, href):
    """Recently Updated, Most Popular, Top Rated, Most Viewed, A-Z"""

    oc = ObjectContainer(title2=title)
    for h, s in CHANNELS:
        if h != 'alphabetical':
            oc.add(DirectoryObject(
                key=Callback(Channels, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
                title=s))
        else:
            oc.add(DirectoryObject(
                key=Callback(Alphabetical, title='%s / A-Z' %title, href='%s/alphabetical' %href),
                title='A-Z'))
    return oc

####################################################################################################
@route(PREFIX + '/abc')
def Alphabetical(title, href):
    """All, A-Z"""

    oc = ObjectContainer(title2=title)
    if 'channels' in href:
        oc.add(DirectoryObject(
            key=Callback(Channels, title='%s / All' %title, href=href),
            title='All'))
        for c in ['#'] + map(chr, range(ord('A'), ord('Z')+1)):
            oc.add(DirectoryObject(
                key=Callback(
                    Channels, title='%s / %s' %(title, c),
                    href='%s/1/%s' %(href, c.lower() if c != '#' else '1')),
                title=c))
    else:
        oc.add(DirectoryObject(
            key=Callback(PornstarList, title='%s / All' %title, href=href),
            title='All'))
        for c in map(chr, range(ord('A'), ord('Z')+1)):
            oc.add(DirectoryObject(
                key=Callback(
                    PornstarList, title='%s / %s' %(title, c),
                    href='%s/%s/overview' %(href, c.lower())),
                title=c))
    return oc

####################################################################################################
@route(PREFIX + '/channels', page=int)
def Channels(title, href, page=None):
    """List channels"""

    oc = ObjectContainer(title2=title)

    html = HTML.ElementFromURL(BASE_URL + href)

    for node in html.xpath('//ul[@class="moviethumbs bigthumbs channelList resizable ignoreViewSwitch"]/li'):
        anode = node.xpath('./a[@class="chtl"]')[0]
        chref = anode.get('href')
        name = anode.text

        bthumb = node.xpath('./a[@class="t"]/img/@src')[0]
        athumb = node.xpath('./a[@class="chtlgx"]/img/@src')[0]

        sum_string = []
        for s in node.xpath('./a[@class="chtlgx"]/b'):
            sum_string.append(s.text)
        summary = ' | '.join([s for s in sum_string])

        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='%s / %s' %(title, name), href=chref),
            title=name, thumb=athumb if athumb else bthumb))

    nextpg_node = html.xpath('//li/a[@rel="next"]')
    if nextpg_node:
        href = nextpg_node[0].get('href')
        nextpg = int(href.split('/')[3])
        oc.add(NextPageObject(
            key=Callback(Channels, title=title, href=href, page=nextpg),
            title='Next Page>>'))

    return oc

####################################################################################################
@route(PREFIX + '/channel/opt')
def ChannelOpt(title, href, hd):
    """Best, Newest, Most Views"""

    oc = ObjectContainer(title2=title)
    for h, s in CHANNEL_OPT:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/1/%s/%s' %(href, h, hd), page=1),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/popular')
def PopularList(title, href):
    """Today, Yesterday, Week, Month, Year, Hall of Fame"""

    oc = ObjectContainer(title2=title)
    plist = ['Today', 'Yesterday', 'Week', 'Month', 'Year', 'Hall of Fame']
    for s in plist:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList,
                title='%s / %s' %(title, s),
                href='%s/%s/1' %(href, s.lower() if s != 'Hall of Fame' else 'all'), page=1),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/pornstar/opt')
def PornstarOpt(title, href):
    """Ratings, Followers, A-Z"""

    oc = ObjectContainer(title2=title)
    pslist = [('top', 'Ratings'), ('mostfollowed', 'Followers')]
    oc.add(DirectoryObject(
        key=Callback(Alphabetical, title='%s / A-Z' %title, href=href),
        title='A-Z'))
    for (h, s) in pslist:
        oc.add(DirectoryObject(
            key=Callback(PornstarList, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s))
    return oc

####################################################################################################
@route(PREFIX + '/pornstar/list', page=int)
def PornstarList(title, href, page=None):
    """List Pornstars"""

    oc = ObjectContainer(title2=title)
    html = HTML.ElementFromURL(BASE_URL + href)
    for node in html.xpath('//div[@class="paper paperSpacings xs-fullscreen photoGrid"]/a'):
        phref = node.get('href')
        thumb = node.xpath('./img/@src')[0]
        name = node.xpath('./div/span/text()')[0]

        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='%s / %s' %(title, name), href='%s/movies' %phref),
            title=name, thumb=thumb))
    nextpg_node = html.xpath('//li/a[@rel="next"]')
    if nextpg_node:
        nhref = nextpg_node[0].get('href')
        nextpg = int(nhref.split('/')[4])
        oc.add(NextPageObject(
            key=Callback(PornstarList, title=title, href=nhref, page=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(PREFIX + '/search')
def Search(query=''):
    """Search ClipHunter"""

    href = '/search/%s' %String.Quote(query.strip(), usePlus=True)
    title = 'Search / %s' %query

    return HDOpt(title, href)

####################################################################################################
@route(PREFIX + '/bookmarks')
def MyBookmarks():
    """List Custom Bookmarks"""
    bm = Dict['Bookmarks']
    if not bm:
        return MessageContainer('Bookmarks', 'Bookmark List Empty')

    oc = ObjectContainer(title2='My Bookmarks')

    for b in sorted(Dict['Bookmarks'].keys()):
        summary = bm[b]['summary']
        video_info = {
            'id': bm[b]['id'],
            'title': bm[b]['title'],
            'duration': bm[b]['duration'],
            'thumb': bm[b]['thumb'],
            'url': bm[b]['url']
            }

        oc.add(DirectoryObject(
            key=Callback(VideoPage, video_info=video_info),
            title=video_info['title'], summary=summary if summary else None,
            tagline=str(Datetime.Delta(milliseconds=video_info['duration'])),
            thumb=video_info['thumb']))

    if len(oc) > 0:
        return oc
    else:
        return MessageContainer('Bookmarks', 'Bookmark List Empty')

####################################################################################################
@route(PREFIX + '/directorylist', page=int)
def DirectoryList(title, href, page):
    """List Videos by page"""

    url = BASE_URL + href

    #html = HTML.ElementFromURL(url, cacheTime=CACHE_TIME)
    html = HTML.ElementFromURL(url)

    nextpg_node = html.xpath('//li/a[@rel="next"]')
    if page == 1 and not nextpg_node:
        main_title = title
    else:
        main_title = '%s | Page %i' %(title, page) if nextpg_node else '%s | Page %i | Last Page' %(title, page)

    oc = ObjectContainer(title2=main_title)

    #html.xpath('//li[@itemtype]/a[@class="t"]/img/@src')[0]

    for node in html.xpath('//li[@itemtype]'):
        anode = node.xpath('./a[@class="t"]')[0]
        href = anode.get('href')
        vhref = BASE_URL + href
        vid = href.split('/')[2]
        thumb = anode.xpath('./img/@src')[0].strip()

        dur_node = anode.xpath('./div[@class="tr"]/text()')[0].split(':')
        duration = (int(dur_node[0])*60000) + (int(dur_node[1])*1000)

        vtitle = node.xpath('./a[@class="vttl"]/text()')[0].strip()
        tagline = node.xpath('./div[@class="info"]/text()')[0].strip()

        video_info = {
            'id': vid,
            'title': vtitle,
            'duration': duration,
            'tagline': tagline,
            'thumb': thumb,
            'url': vhref
            }

        oc.add(DirectoryObject(
            key=Callback(VideoPage, video_info=video_info),
            title=vtitle, thumb=thumb, tagline=tagline
            ))

    if nextpg_node:
        href = nextpg_node[0].get('href')
        if ('popular' in href) or ('pornstars' in href):
            nextpg = int(href.split('/')[4])
        else:
            nextpg = int(href.split('/')[3])
        oc.add(NextPageObject(
            key=Callback(DirectoryList, title=title, href=href, page=nextpg),
            title='Next Page>>'))

    if len(oc) > 0:
        return oc
    else:
        return MessageContainer('Video List', 'Video List Empty')

####################################################################################################
@route(PREFIX + '/videopage', video_info=dict)
def VideoPage(video_info):
    """
    Video Sub Page
    Includes Similar Videos and Bookmark Option
    """

    #html = HTML.ElementFromURL(video_info['url'], cacheTime=CACHE_TIME)
    html = HTML.ElementFromURL(video_info['url'])

    #bm = Dict['Bookmarks']
    header = None
    message = None
    """
    match = ((True if video_info['id'] in bm else False) if bm else False)
    video_removed = html.xpath('//div[@id="video_removed"]')

    if match and video_removed:
        header = video_info['title']
        message = 'This video is no longer available.'
    elif not match and video_removed:
        return MessageContainer('Warning', 'This video is no longer available.')
    """

    oc = ObjectContainer(title2=video_info['title'], header=header, message=message, no_cache=True)

    #if not video_removed:
    oc.add(VideoClipObject(
        title=video_info['title'],
        duration=video_info['duration'],
        summary=video_info['tagline'],
        thumb=video_info['thumb'],
        url=video_info['url']
        ))

    related_thumb = html.xpath('//li[@itemtype]/a[@class="t"]/img/@src')[0]
    oc.add(DirectoryObject(
        key=Callback(DirectoryList, title='Related', href=video_info['url'].split(BASE_URL)[1], page=1),
        title='Related', thumb=related_thumb))

    """
    similar_node = html.xpath('//div[@class="video-similar video-rotate"]')
    if similar_node:
        for i, node in enumerate(similar_node[0].xpath('./div[@class="video-item"]')):
            a_node = node.xpath('./a')[0]
            vhref = BASE_URL + a_node.get('href')
            vid = vhref.split('/')[-1]
            thumb = 'http:' + a_node.xpath('./img/@src')[0]
            name = a_node.xpath('./img/@alt')[0].strip()
            duration = 1000 * int(a_node.xpath('./span[@class="len"]/text()')[0].strip())
            hd_node = node.xpath('./span[@class="i-hd"]')
            if hd_node:
                name = name + ' (HD)'

            if i == 0:
                info = [{
                    'id': vid, 'title': name, 'duration': duration,
                    'thumb': thumb, 'url': vhref}]
            else:
                info.append({
                    'id': vid, 'title': name, 'duration': duration,
                    'thumb': thumb, 'url': vhref})
        oc.add(DirectoryObject(
            key=Callback(SimilarVideos, title='Videos Similar to \"%s\"' %video_info['title'], info=info),
            title='Similar Videos', thumb=info[0]['thumb']))

    if match:
        oc.add(DirectoryObject(
            key=Callback(RemoveBookmark, video_info=video_info),
            title='Remove Bookmark',
            summary='Remove \"%s\" from your Bookmarks list.' %video_info['title'],
            thumb=R(ICON_BM_REMOVE)
            ))
    else:
        oc.add(DirectoryObject(
            key=Callback(AddBookmark, video_info=video_info),
            title='Add Bookmark',
            summary='Add \"%s\" to your Bookmarks list.' %video_info['title'],
            thumb=R(ICON_BM_ADD)
            ))
    """

    return oc

####################################################################################################
@route(PREFIX + '/similarvideos', info=list)
def SimilarVideos(title, info):
    """Display similar videos"""

    oc = ObjectContainer(title2=title)

    for item in info:
        oc.add(DirectoryObject(
            key=Callback(VideoPage, video_info=item),
            title=item['title'], thumb=item['thumb']))

    return oc

####################################################################################################
@route(PREFIX + '/addbookmark', video_info=dict)
def AddBookmark(video_info):
    """Add Bookmark"""

    html = HTML.ElementFromURL(video_info['url'], cacheTime=CACHE_TIME)

    bm = Dict['Bookmarks']
    summary = ''
    genres = ''
    for node in html.xpath('//div[@class="content"][@id="about"]/div[@class="info"]'):
        summary = node.xpath('./p[@class="desc"]/text()')
        if summary:
            summary = summary[0].strip()

        genres = node.xpath('./p[@class="cat"]')
        if genres:
            genre_list = genres[0].text_content().strip().replace('Category:', '').replace(' ', '').split(',')
            genres = ' '.join([g.replace(' ', '_') for g in genre_list])

    new_bookmark = {
        'id': video_info['id'], 'url': video_info['url'], 'title': video_info['title'],
        'duration': video_info['duration'], 'summary': summary if summary else '',
        'genres': genres if genres else '', 'thumb': video_info['thumb']
        }

    if not bm:
        Dict['Bookmarks'] = {video_info['id']: new_bookmark}
        Dict.Save()

        return MessageContainer('Bookmarks',
                '\"%s\" has been added to your bookmarks.' %video_info['title'])
    else:
        if video_info['url'] in bm.keys():
            return MessageContainer('Warning',
                '\"%s\" is already in your bookmarks.' %video_info['title'])
        else:
            Dict['Bookmarks'].update({video_info['id']: new_bookmark})
            Dict.Save()

            return MessageContainer('Bookmarks',
                '\"%s\" has been added to your bookmarks.' %video_info['title'])

####################################################################################################
@route(PREFIX + '/removebookmark', video_info=dict)
def RemoveBookmark(video_info):
    """Remove Bookmark from Bookmark Dictionary"""

    bm = Dict['Bookmarks']

    if (True if video_info['id'] in bm.keys() else False) if bm else False:
        del Dict['Bookmarks'][video_info['id']]
        Dict.Save()

        return MessageContainer('Remove Bookmark',
            '\"%s\" has been removed from your bookmarks.' %video_info['title'])
    else:
        return MessageContainer('Remove Bookmark Error',
            'ERROR \"%s\" cannot be removed. The Bookmark does not exist!' %video_info['title'])
