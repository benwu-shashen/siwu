from Auto_wed_current.Auto_Post.GUI_Post_Template import tem_property_data
from Auto_wed_current.Auto_Post.GUI_Post_Template.GUI_Post_Template_Thread.post_template_delete import \
    post_template_delete


class delete_file(tem_property_data):
    def __init__(self):
        super().__init__()

    def original_file(self):
        post_template_delete(self.listWidget_original).del_listwidget()