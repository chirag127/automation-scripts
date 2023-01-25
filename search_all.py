import os
import webbrowser
string = """1. Burdman, Jessica, “Collaborative Web Development” Addison Wesley
2. Xavier, C, “ Web Technology and Design” , New Age International
3. Ivan Bayross,” HTML, DHTML, Java Script, Perl & CGI”, BPB Publication
4. Bhave, “Programming with Java”, Pearson Education
5. Herbert Schieldt, “The Complete Reference:Java”, McGraw Hill.
6. Hans Bergsten, “Java Server Pages”, SPD O’Reilly
7. Margaret Levine Young, “The Complete Reference Internet”, McGraw Hill.
8. Naughton, Schildt, “The Complete Reference JAVA2”, McGraw Hill.
9. Balagurusamy E, “Programming in JAVA”, McGraw Hill"""

search_term = string.split("\n")
for i in search_term:

    webbrowser.open("https://neeva.com/search?q="+i+" book summary")
