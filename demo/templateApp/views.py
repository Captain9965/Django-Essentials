from django.shortcuts import render


"""                     More on templates: 
     <!--    1.{{}} }} is used to render variables from the dict-like context object
                2.{% %} is used for tags..which provide arbitrary logic for the rendering process.
                    Tags can even accept arguments like so -> {% cycle 'odd' 'even' %} 
                    Tags cannot be used to modify values unless filters are used like so->
                    {{ value | length }}

                3. For comments:->
                    {% comment 'comment_name' %}
                    {% endcomment %}
                4. For templage inheritance:
                    {% extends 'template_name.html' %} useful if you have similar looking web pages -->
"""
class templates():
    def intro(request):
        context ={
            "data": "This is a demo of Django templates",
            "list": ["James", "Cephas", "Orengo", "Morris", "King"]
        }
        return render(request, "templates.html", context)