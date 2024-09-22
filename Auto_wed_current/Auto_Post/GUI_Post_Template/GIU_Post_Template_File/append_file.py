from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Template.GUI_Post_Template_Thread.post_template_append import \
    post_template_append


class append_file(tem_property_data):
    def __init__(self):
        super().__init__()

    def original_file(self):
        post_template_append(self.listWidget_original).filedialog()



