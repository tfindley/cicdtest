from django.http import HttpResponse


def home(request):
    text = """<h1>Welcome to our mind blowing home page</h1>
        <br>
        <iframe src="https://giphy.com/embed/QMHoU66sBXqqLqYvGO"
        width="480" height="270" frameBorder="0"
        class="giphy-embed" allowFullScreen></iframe>
        <p>
        <a href="https://giphy.com/gifs/this-is-fine-QMHoU66sBXqqLqYvGO">
        via GIPHY</a>
        </p>"""
    return HttpResponse(text)
