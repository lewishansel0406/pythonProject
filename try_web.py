# Import modules
import webbrowser

# HTML code on the try.html file
html_template = """
    <!DOCTYPE html>
    <html lang='en' 
    style='background-color: #000; color: #fff; scroll: smooth;
    font-size: 24px ;font-family: monospace; padding: 15px 30px'>
    <head>
        <meta charset='utf-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel="icon" href="icon_try.png" type="image/x-icon">
        <title id='static-webpage'>
            Static webpage
        </title>
    </head>
    <body>
        <header>
            <h2 id='h2'>
                Welcome To This Static Webpage
            </h2>
        </header>
        <section>
        <p id='block' style='padding: 30px'>
            <pre>
                HTML (HyperText Markup Language) is the most basic building block 
                of the Web. It defines the meaning and structure of web content. 
                Other technologies besides HTML are generally used to describe a
                web page's appearance/presentation (CSS) or functionality/behavior
                (JavaScript).
            </pre>
            <pre>
                "Hypertext" refers to links that connect web pages to one another, 
                either within a single website or between websites. Links are a 
                fundamental aspect of the Web. By uploading content to the Internet 
                and linking it to pages created by other people, you become an active
                participant in the World Wide Web.
            </pre>
            <pre>
                HTML uses 'markup' to annotate text, images, and other content for 
                display in a Web browser. HTML markup includes special 'elements' 
                such as 'head', 'title', 'body', 'header', 'footer', 
                'article', 'section', 'p', 'div', 'span', 'img', 'aside',
                'audio', 'canvas', 'datalist', 'details', 'embed', 'nav', 
                'search', 'output', 'progress', 'video', 'ul', 'ol', 'li' 
                and many others.
            </pre>
            <br><br>
        </p>
        </section>
        <aside>
            <form id='type-anything' action='try.html' method='post' style='padding: 10px'>
                <label>
                    Type anything :
                </label>
                <br><br> 
                <input name='type-anything' type='text' placeholder='Type anything' 
                style='background-color: #000; color: #fff; padding: 10px; font-size: 18px; 
                font-family: monospace '>
                <br><br> 
                <input name='submit' type='submit' value='Submit' 
                style='background-color: #000; color: #fff; padding: 10px 30px; text-decoration: none; 
                display:inline-block; font-size: 18px; font-family: monospace; cursor: pointer'>
            </form>
        <br>        
        </aside>
        <hr>
        <br>
        <br>
        <footer>
            <a href='#h2' style='background-color: #333; color: #fff; font-family: monospace; padding: 20px 34px;
                   text-align: center; text-decoration: none; display: inline-block;
                   font-size: 22px; margin: 2px 1px; cursor: pointer;'>
                Top
            </a>
            <br><br>
            <a href='#block' style='background-color: #333; color: #fff; font-family: monospace;padding: 20px 34px;
                   text-align: center; text-decoration: none; display: inline-block;
                   font-size: 22px; margin: 2px 1px; cursor: pointer;'>
                Paragraph header
            </a>
            <wbr>
            <a href='#type-anything' style='background-color: #333; color: #fff; font-family: monospace;padding: 
                   20px 30px; text-align: center; text-decoration: none; display: inline-block;
                   font-size: 22px; margin: 2px 1px; cursor: pointer;'>
                Type anything
            </a>
            <br><br>
            <a href='https://developer.mozilla.org/en-US/docs/Web/HTML' target='_blank'
                   style='background-color: #333; color: #fff; font-family: monospace;padding: 
                   20px 30px; text-align: center; text-decoration: none; display: inline-block;
                   font-size: 22px; margin: 2px 1px; cursor: pointer;'>
                Reference:- HTML: Hyper Text Markup Language | MDN
            </a>
        </footer>       
    </body>
    </html>
"""


class Webfile:
    def __init__(self, f, html_file):
        self.f = f
        self.html_file = html_file

    def __str__(self):
        # Create / open an HTML file
        self.f = open("try.html", "r+")
        self.f.truncate()

        # writing the code into the file
        self.f.write(html_template)

        # Open HTML file in browser
        webbrowser.open("try.html")

        # close the file
        self.f.close()

        # Return string.
        return "Your web file will open in your default web browser shortly."


if __name__ == "__main__":
    file = ""
    print(Webfile(f=file, html_file=html_template))
    