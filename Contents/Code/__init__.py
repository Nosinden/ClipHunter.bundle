####################################################################################################
#                                                                                                  #
#                               (Clip/Pic)Hunter Plex Channel                                      #
#                                                                                                  #
####################################################################################################
from updater import Updater

# ClipHunter
CH_TITLE = L('ch_title')
CH_PREFIX = '/video/cliphunter'
CH_BASE_URL = 'http://www.cliphunter.com'
ICON_CH = 'icon-default-ch.png'
ICON_BM_CH = 'icon-bookmarks-ch.png'
ICON_BM_ADD_CH = 'icon-add-bookmark-ch.png'
ICON_BM_REMOVE_CH = 'icon-remove-bookmark-ch.png'
ICON_CAT_CH = 'icon-tags-ch.png'
ICON_LIST = 'icon-explore.png'
ICON_TV = 'icon-tv.png'
ICON_STARS = 'icon-stars.png'
ICON_PSTARS_CH = 'icon-babe-ch.png'
ICON_PLAYLIST = 'icon-playlist.png'
ICON_UPDATE_CH = 'icon-update-ch.png'
ART_CH = 'art-default-ch.jpg'

# PicHunter
PH_TITLE = L('ph_title')
PH_PREFIX = '/photos/pichunter'
PH_BASE_URL = 'http://www.pichunter.com'
ICON_PH = 'icon-default-ph.png'
ICON_BM_PH = 'icon-bookmarks-ph.png'
ICON_BM_ADD_PH = 'icon-add-bookmark-ph.png'
ICON_BM_REMOVE_PH = 'icon-remove-bookmark-ph.png'
ICON_CAT_PH = 'icon-tags-ph.png'
ICON_PSTARS_PH = 'icon-babe-ph.png'
ICON_STUDIO = 'icon-studio-ph.png'
ICON_UPDATE_PH = 'icon-update-ph.png'
ART_PH = 'art-default-ph.jpg'

#CACHE_TIME = CACHE_1HOUR
CACHE_TIME = 0

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
    #HTTP.CacheTime = 0
    HTTP.CacheTime = CACHE_1HOUR

    #ObjectContainer.title1 = TITLE_CH
    #ObjectContainer.art = R(ART_CH)

    #DirectoryObject.thumb = R(ICON_CH)
    #DirectoryObject.art = R(ART_CH)

    #InputDirectoryObject.art = R(ART_CH)

    #VideoClipObject.art = R(ART_CH)
    #PhotoObject.art = R(ART_PH)

    #ValidatePrefs()

####################################################################################################
@handler(CH_PREFIX, CH_TITLE, thumb=ICON_CH, art=ART_CH)
def VideoMainMenu():
    """Setup Main Menu, Includes Updater"""

    oc = ObjectContainer(title2=CH_TITLE, art=R(ART_CH), no_cache=True)

    Updater(CH_PREFIX + '/updater', oc, ICON_UPDATE_CH)

    oc.add(DirectoryObject(
        key=Callback(HDOpt, title='Explore', href='/categories/All'),
        title='Explore', thumb=R(ICON_LIST)
        ))
    oc.add(DirectoryObject(
        key=Callback(CategoryList, title='Categories'),
        title='Categories', thumb=R(ICON_CAT_CH)
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
        title='Pornstars', thumb=R(ICON_PSTARS_CH)
        ))
    #oc.add(DirectoryObject(key=Callback(Playlists, title='Playlists'), title='Playlists', thumb=R(ICON_PLAYLIST)))
    #oc.add(DirectoryObject(key=Callback(MyBookmarks), title='My Bookmarks', thumb=R(ICON_BM_CH)))
    #oc.add(PrefsObject(title='Preferences'))
    oc.add(InputDirectoryObject(
        key=Callback(ClipSearch),
        title='Search', summary='Search ClipHunter', prompt='Search for...',
        thumb=R('icon-search.png'), art=R(ART_CH)))

    return oc

####################################################################################################
@handler(PH_PREFIX, PH_TITLE, thumb=ICON_PH, art=ART_PH)
def PhotoMainMenu():
    """Setup Main Menu, Includes Updater"""

    oc = ObjectContainer(title2=PH_TITLE, art=R(ART_PH), no_cache=True)

    Updater(PH_PREFIX + '/updater', oc, ICON_UPDATE_PH)

    #oc.add(DirectoryObject(
        #key=Callback(PicHome, title='Home'),
        #title='Home', thumb=R(ICON_LIST)
        #))
    oc.add(DirectoryObject(
        key=Callback(TagsList, title='Categories', href='/tags'),
        title='Categories', thumb=R(ICON_CAT_PH)
        ))
    oc.add(DirectoryObject(
        key=Callback(PicPornstarOpt, title='Pornstars', href='/models/all'),
        title='Pornstars', thumb=R(ICON_PSTARS_PH)
        ))
    oc.add(DirectoryObject(
        key=Callback(StudioOpt, title='Studios', href='/sites/all'),
        title='Studios', thumb=R(ICON_STUDIO)
        ))
    #oc.add(DirectoryObject(key=Callback(MyBookmarks), title='My Bookmarks', thumb=R(ICON_BM_PH)))
    #oc.add(PrefsObject(title='Preferences'))
    oc.add(InputDirectoryObject(
        key=Callback(PicSearch),
        title='Search', summary='Search PicHunter', prompt='Search for...',
        thumb=R('icon-search.png'), art=R(ART_PH)))

    return oc

####################################################################################################
@route(CH_PREFIX + '/validateprefs')
def ValidatePrefs():
    """
    Validate Prefs
    No Prefs to validate yet
    """

####################################################################################################
@route(CH_PREFIX + '/categorylist')
def CategoryList(title):
    """Setup Category List"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    url = CH_BASE_URL + '/categories/'
    html = HTML.ElementFromURL(url)
    cat_list = []
    for node in html.xpath('//div[@class="list-group"]/a'):
        href = node.get('href').replace(' ', '%20')
        name = node.get('title').strip()
        if (name != 'All') and ((name, href) not in cat_list):
            cat_list.append((name, href))
    for (n, h) in sorted(cat_list):
        oc.add(DirectoryObject(
            key=Callback(HDOpt, title='Category / %s' %n, href=h),
            title=n))
    return oc

####################################################################################################
@route(PH_PREFIX + '/tags/list')
def TagsList(title, href):
    """Setup Tags List"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    tag_list = []
    for node in html.xpath('//div[@class="list-group"]/a'):
        phref = node.get('href').replace(' ', '%20')
        name = node.get('title').strip()
        if (name != 'All') and ((name, phref) not in tag_list):
            tag_list.append((name, phref))
    for (n, h) in sorted(tag_list):
        oc.add(DirectoryObject(
            key=Callback(Tag, title='Category / %s' %n, href=h),
            title=n))
    return oc

####################################################################################################
@route(PH_PREFIX + '/tag')
def Tag(title, href):
    """Photos in tag"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(PhotoAlbumObject(
            key=Callback(PhotoBin, title='%s / %s' %(title, n), href=h),
            rating_key=PH_BASE_URL + h, source_title='PicHunter', title=n, thumb=t))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Tag, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(CH_PREFIX + '/hd-opt')
def HDOpt(title, href):
    """
    Default, Channels
    All, HD
    """

    oc = ObjectContainer(title2=title, art=R(ART_CH))
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
@route(CH_PREFIX + '/sortby')
def SortBy(title, href, hd):
    """Sort By (Date, Relevance, Views, Rating)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in SORT:
        oc.add(DirectoryObject(
            key=Callback(Rating, title='%s / %s' %(title, s), href='%s/1/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/rating')
def Rating(title, href, hd):
    """Rating (All, Super High, High, Medium)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in RATING:
        oc.add(DirectoryObject(
            key=Callback(Uploaded, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/uploaded')
def Uploaded(title, href, hd):
    """Uploaded (Any Time, Today, Yesterday, This Week, This Month, 3 Months, This Year)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in UPLOADED:
        oc.add(DirectoryObject(
            key=Callback(Duration, title='%s / %s' %(title, s), href='%s/%s' %(href, h), hd=hd),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/duration')
def Duration(title, href, hd):
    """Duration (All, Short, Medium, Long)"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in DURATION:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/%s/%s' %(href, h, hd), page=1),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/channel/list')
def ChannelList(title, href):
    """Recently Updated, Most Popular, Top Rated, Most Viewed, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
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
@route(CH_PREFIX + '/abc')
def Alphabetical(title, href):
    """All, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    if 'channels' in href:
        oc.add(DirectoryObject(
            key=Callback(Channels, title='%s / All' %title, href=href),
            title='All'))
        for c in ['#'] + abc():
            oc.add(DirectoryObject(
                key=Callback(
                    Channels, title='%s / %s' %(title, c),
                    href='%s/1/%s' %(href, c.lower() if c != '#' else '1')),
                title=c))
    else:
        oc.add(DirectoryObject(
            key=Callback(PornstarList, title='%s / All' %title, href=href),
            title='All'))
        for c in abc():
            oc.add(DirectoryObject(
                key=Callback(
                    PornstarList, title='%s / %s' %(title, c),
                    href='%s/%s/overview' %(href, c.lower())),
                title=c))
    return oc

####################################################################################################
@route(CH_PREFIX + '/channels')
def Channels(title, href):
    """List channels"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    nextpg = nextpg_href(html)
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
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Channels, title=title, href=nextpg),
            title='Next Page>>'))

    return oc

####################################################################################################
@route(CH_PREFIX + '/channel/opt')
def ChannelOpt(title, href, hd):
    """Best, Newest, Most Views"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    for h, s in CHANNEL_OPT:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, title='%s / %s' %(title, s), href='%s/1/%s/%s' %(href, h, hd), page=1),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/popular')
def PopularList(title, href):
    """Today, Yesterday, Week, Month, Year, Hall of Fame"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    plist = ['Today', 'Yesterday', 'Week', 'Month', 'Year', 'Hall of Fame']
    for s in plist:
        oc.add(DirectoryObject(
            key=Callback(DirectoryList,
                title='%s / %s' %(title, s),
                href='%s/%s/1' %(href, s.lower() if s != 'Hall of Fame' else 'all'), page=1),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/opt')
def PornstarOpt(title, href):
    """Ratings, Followers, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
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
@route(PH_PREFIX + '/pornstar/opt')
def PicPornstarOpt(title, href):
    """Pichunter: Trending, Superstars, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    pslist = ['trending', 'superstars']
    oc.add(DirectoryObject(
        key=Callback(PicABC, title='%s / A-Z' %title, href=href),
        title='A-Z'))
    for s in pslist:
        oc.add(DirectoryObject(
            key=Callback(PicPornstarList, title='%s / %s' %(title, s.title()), href='%s/%s' %(href, s)),
            title=s.title()))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/abc')
def PicABC(title, href):
    """Pornstar ABC list"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    for c in abc():
        oc.add(DirectoryObject(
            key=Callback(PicPornstarList, title='%s / %s' %(title, c), href='%s/%s' %(href, c.lower())),
            title=c))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/list')
def PornstarList(title, href):
    """List Pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for node in html.xpath('//div[@class="paper paperSpacings xs-fullscreen photoGrid"]/a'):
        phref = node.get('href')
        thumb = node.xpath('./img/@src')[0]
        name = node.xpath('./div/span/text()')[0]

        oc.add(DirectoryObject(
            key=Callback(PornstarCH, title='%s / %s' %(title, name), href=phref),
            title=name, thumb=thumb))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PornstarList, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar')
def PornstarCH(title, href):
    """Videos, Photos"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    oc.add(DirectoryObject(
        key=Callback(HDOpt, title='%s / Videos' %title, href='%s/movies' %href),
        title='Videos'))
    oc.add(DirectoryObject(
        key=Callback(PhotoAlbumList,
            title='%s / Photos' %title,
            href='%s/photos/1' %href.replace('pornstars', 'models')),
        title='Photos'))
    oc.add(DirectoryObject(
        key=Callback(PornstarCHSimilar, title='%s / Similar' %title, href=href),
        title='Similar Pornstars'))
    return oc

####################################################################################################
@route(CH_PREFIX + '/pornstar/similar')
def PornstarCHSimilar(title, href):
    """List simialr pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_CH))
    html = HTML.ElementFromURL(CH_BASE_URL + href)
    for node in html.xpath('//div[@class="links"]'):
        simnode = node.xpath('./div[@class="frontpageCatTable"]')[0]
        for node2 in simnode.xpath('.//a'):
            phref = node2.get('href')
            name = node2.text
            oc.add(DirectoryObject(
                key=Callback(PornstarCH, title='%s / %s' %(title.rsplit('/', 2)[0], name), href=phref),
                title=name, thumb=))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/list')
def PicPornstarList(title, href):
    """PicHunter list pornstars"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(PornstarPH, title='%s / %s' %(title, n), href=h),
            title=n, thumb=t))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PicPornstarList, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar')
def PornstarPH(title, href):
    """Videos, Photos"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    oc.add(DirectoryObject(
        key=Callback(HDOpt,
            title='%s / Videos' %title,
            href='%s/movies' %href.replace('_', '+').replace('models', 'pornstars')),
        title='Videos'))
    oc.add(DirectoryObject(
        key=Callback(PhotoAlbumList, title=title, href='%s/photos' %href), title='Photos'))
    return oc

####################################################################################################
@route(PH_PREFIX + '/studio/opt')
def StudioOpt(title, href):
    """All, #, A-Z"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    oc.add(DirectoryObject(
        key=Callback(StudioList, title='%s / All' %title, href=href + '/everything/1'),
        title='All'
        ))
    for c in ['#'] + abc():
        oc.add(DirectoryObject(
            key=Callback(StudioList,
                title='%s / %s' %(title, c),
                href='%s/%s/1' %(href, c.lower() if c != '#' else '0')),
            title=c
            ))
    return oc

####################################################################################################
@route(PH_PREFIX + '/studio/list')
def StudioList(title, href):
    """List Studios"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(DirectoryObject(
            key=Callback(Studio, title='%s / %s' %(title, n), href=h),
            title=n, thumb=t))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(StudioList, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(PH_PREFIX + '/studio')
def Studio(title, href):
    """List Albums in Studio"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(PhotoAlbumObject(
            key=Callback(PhotoBin, title='%s / %s' %(title, n), href=h),
            rating_key = PH_BASE_URL + h, source_title='PicHunter', title=n, thumb=t))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(Studio, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
@route(PH_PREFIX + '/pornstar/photoalbumlist')
def PhotoAlbumList(title, href):
    """List Photo Albums for Pornstar"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    nextpg = nextpg_href(html)
    for (n, t, h) in pichunter_list(html):
        oc.add(PhotoAlbumObject(
            key=Callback(PhotoBin, title='%s / %s' %(title, n), href=h),
            rating_key = PH_BASE_URL + h, source_title='PicHunter', title=n, thumb=t))
    if nextpg:
        oc.add(NextPageObject(
            key=Callback(PhotoAlbumList, title=title, href=nextpg),
            title='Next Page>>'))
    return oc

####################################################################################################
def abc():
    return map(chr, range(ord('A'), ord('Z')+1))

####################################################################################################
def pichunter_list(html):
    palist = []
    for node in html.xpath('//a[@class="thumb"]'):
        href = node.get('href')
        title = node.xpath('./img/@alt')[0]
        thumb = node.xpath('./img/@src')[0]
        palist.append((title, thumb, href))
    return palist

####################################################################################################
def nextpg_href(html):
    nextpg_node = html.xpath('//li/a[@rel="next"]')
    href = None
    if nextpg_node:
        href = nextpg_node[0].get('href')
    return href

####################################################################################################
@route(CH_PREFIX + '/search')
def ClipSearch(query=''):
    """Search ClipHunter"""

    href = '/search/%s' %String.Quote(query.strip(), usePlus=True)
    title = 'Search / %s' %query

    return HDOpt(title, href)

####################################################################################################
@route(PH_PREFIX + '/search')
def PicSearch(query=''):
    """Search PicHunter"""

    href = '/search/%s/1' %String.Quote(query.strip(), usePlus=True)
    title = 'Search / %s' %query

    return PicSortBy(title, href)

####################################################################################################
@route(PH_PREFIX + '/search/sortby')
def PicSortBy(title, href):
    """Date, Relevancy, Rating"""

    oc = ObjectContainer(title2=title + ' / Sort By:', art=R(ART_PH))
    sort_list = [('rel', 'Relevancy'), ('date', 'Date'), ('rate', 'Rating')]
    for (h, s) in sort_list:
        oc.add(DirectoryObject(
            key=Callback(PicQuality, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s))
    return oc

####################################################################################################
@route(PH_PREFIX + '/search/quality')
def PicQuality(title, href):
    """All, HD"""

    oc = ObjectContainer(title2=title + ' / Quality:', art=R(ART_PH))
    oc.add(DirectoryObject(
        key=Callback(PicFreshness, title='%s / All', href=href + '/all'),
        title='All'))
    oc.add(DirectoryObject(
        key=Callback(PicFreshness, title='%s / HQ Only' %title, href=href + '/hq'),
        title='HQ Only'))
    return oc

####################################################################################################
@route(PH_PREFIX + '/search/freshness')
def PicFreshness(title, href):
    """Any Time, Today, This Week, This Month, Past 3 Months, This Year"""

    oc = ObjectContainer(title2=title + ' / Freshness:', art=R(ART_PH))
    freshness_list = [
            ('today', 'Today'), ('yesterday', 'This Week'), ('month', 'This Month'),
            ('3months', 'Past 3 Months'), ('year', 'This Year')]
    oc.add(DirectoryObject(
        key=Callback(PhotoAlbumList, title='%s / Any Time' %title, href=href),
        title='Any Time'))
    for (h, s) in freshness_list:
        oc.add(DirectoryObject(
            key=Callback(PhotoAlbumList, title='%s / %s' %(title, s), href='%s/%s' %(href, h)),
            title=s))
    return oc

####################################################################################################
@route(CH_PREFIX + '/bookmarks')
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
@route(CH_PREFIX + '/directorylist', page=int)
def DirectoryList(title, href, page):
    """List Videos by page"""

    url = CH_BASE_URL + href

    html = HTML.ElementFromURL(url)

    nextpg_node = html.xpath('//li/a[@rel="next"]')
    if page == 1 and not nextpg_node:
        main_title = title
    else:
        main_title = '%s | Page %i' %(title, page) if nextpg_node else '%s | Page %i | Last Page' %(title, page)

    oc = ObjectContainer(title2=main_title, art=R(ART_CH))

    for node in html.xpath('//li[@itemtype]'):
        anode = node.xpath('./a[@class="t"]')[0]
        href = anode.get('href')
        vhref = CH_BASE_URL + href
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
@route(PH_PREFIX + '/photo/bin')
def PhotoBin(title, href):
    """Create PhotoAlbum for photos in href"""

    oc = ObjectContainer(title2=title, art=R(ART_PH))
    html = HTML.ElementFromURL(PH_BASE_URL + href)
    for node in html.xpath('//figure[@itemtype]/a'):
        name = node.get('title')
        thumb = node.get('href')
        oc.add(CreatePhotoObject(title=name, url=thumb))
    return oc

####################################################################################################
@route(CH_PREFIX + '/videopage', video_info=dict)
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

    oc = ObjectContainer(title2=video_info['title'], header=header, message=message, art=R(ART_CH), no_cache=True)

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
        key=Callback(DirectoryList, title='Related', href=video_info['url'].split(CH_BASE_URL)[1], page=1),
        title='Related', thumb=related_thumb))

    """
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
@route(PH_PREFIX + '/create/photo/object', include_container=bool)
def CreatePhotoObject(title, url, include_container=False, *args, **kwargs):
    """create photo object for pichunter"""

    photo_object = PhotoObject(
        key=Callback(CreatePhotoObject, title=title, url=url, include_container=True),
            rating_key=url,
            source_title='PicHunter',
            title=title,
            thumb=url,
            art=R(ART_PH),
            items=[MediaObject(parts=[PartObject(key=url)])]
            )
    if include_container:
        return ObjectContainer(objects=[photo_object])
    else:
        return photo_object

####################################################################################################
@route(CH_PREFIX + '/bookmark/add', video_info=dict)
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
@route(CH_PREFIX + '/bookmark/remove', video_info=dict)
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
