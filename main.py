from aiohttp import web

#   Core functions
async def home(request):
    """ Returns an "OK response to the client confirming C2 callbacks are working """
    return web.Response(text='OK')

async def check_in(request):
    """ """
    pass

async def get_screenshot(request):
    """ """
    pass

#   Framework Routes
app = web.Application()
app.add_routes([web.get('/welcome/home', home),
                web.get('/validate/status', check_in),
                web.get('/validate/status/1', get_screenshot)])

#   Start yer engines
web.run_app(app)


