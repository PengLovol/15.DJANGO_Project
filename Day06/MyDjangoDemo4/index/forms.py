from django import forms

# 为topic控件初始化数据
TOPIC_CHOICE = (
  ('1','好评'),
  ('2','中评'),
  ('3','差评'),
)
#表示评论内容的表单控件们
#控件1 - 评论标题　- 文本框
#控件2 - Email - Email框
#控件3 - 评论内容 - Textarea
#控件4 - 评论级别　- Select
#控件5 - 是否保存　- Checkbox
class RemarkForm(forms.Form):
    # subject - input type='text'
    # label 表示的是控件前的文本
    subject=forms.CharField(label='标题')
    # email - input type='email'
    email = forms.EmailField(label='邮箱')
    # message - Textarea
    # widget=forms.Textarea,表示将当前属性变为多行文本域
    message = forms.CharField(label='内容', widget=forms.Textarea)
    # topic - Select
    topic = forms.ChoiceField(label='级别', choices=TOPIC_CHOICE)
    # isSaved - checkbox
    isSaved = forms.BooleanField(label='是否保存')