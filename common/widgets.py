from django.contrib.admin.widgets import AdminFileWidget


class ImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        image = '<a href="{url}"><img src="{url}" height="150px"></a><br>'.format(url=value.url) if value else ''
        html = '''<p class="file-upload">
                  {img}<input type="file" name="{name}" id="id_file">
                  </p>'''.format(img=image, name=name)
        return html
