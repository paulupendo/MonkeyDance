import webapp2


class MonkeyDance(webapp2.RequestHandler):
    def post(self):
        emoji = self.request.get('text')
        make_me_dance(emoji, self)


def make_me_dance(emoji, self):
    try:
        emoji = int(emoji)
        if isinstance(emoji, int):
            self.response.write(":monkey-dancing:"*emoji)
        elif emoji == "help":
            self.response.write("Helping you")
        else:
            self.response.write("You can do better than that!")

    except ValueError:
        self.response.write("Monkey dances with integers only")


app = webapp2.WSGIApplication([
        (r'/', MonkeyDance)
])


def main():
    from paste import httpserver
    httpserver.serve(app, host='https://monkeydance.herokuapp.com', port='8080')

if __name__ == '__main__':
    main()
