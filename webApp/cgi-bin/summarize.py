import summarizer
import cgi

form = cgi.FieldStorage()
dataset = form.getvalue('text')

prediction = summarizer.predict(dataset)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>Summarized Text is :</h1>
<p> {} </p>

</body>

</html>
""".format(prediction))