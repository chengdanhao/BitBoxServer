from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField


class RadioForm(FlaskForm):
	radios = [('off', '关闭'),
	          ('http://ngcdn003.cnr.cn/live/yyzs48/index.m3u8', '音乐之声'),
	          ('http://ngcdn001.cnr.cn/live/zgzs48/index.m3u8', '中国之声')]
	choice = SelectField(label='选择你想收听的节目', choices=radios)
	submit = SubmitField('确认')
