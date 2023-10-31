import bottle

@bottle.route("/")
def clock():
    # Get the current time
    time = datetime.datetime.now()

    # Format the time as a string
    formatted_time = time.strftime("%H:%M:%S")

    # Return the HTML code for the clock
    html = """
    <html>
    <head>
        <title>Clock</title>
    </head>
    <body>
        <h1>Clock</h1>
        <p>The current time is: {}</p>
    </body>
    </html>
    """.format(formatted_time)

    return html

if __name__ == "__main__":
    bottle.run(host="localhost", port=8080)
