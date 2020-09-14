#
from pypinyin import lazy_pinyin
import jieba
json_path='emoji.json'
def translate_to_chouxiang(abstract_str,level='slight'):
    with open(json_path,encoding='utf8') as j:
        emoji_json=eval(j.read())
    #先分词
    result=''
    jiebastr = jieba.lcut(abstract_str)
    if level=='slight':
        #简单版的抽象很简单，就直接对比就行
        for jb in jiebastr:
            if jb in emoji_json.keys():
                result+=emoji_json[jb]
            else:
                result+=jb
    elif level=='severe':
        abstract_words=list()
        pinyin_to_words=dict()
        for emoji_key in emoji_json.keys():
            piny=lazy_pinyin(emoji_key)
            pinyin_to_words[piny[0]]=emoji_key
            abstract_words.append(piny[0][0])
        for jbstr in jiebastr:
            for jb in jbstr:
                if jb in emoji_json:
                    result+=emoji_json[jb]
                else:#用拼音
                    word_py = lazy_pinyin(jb)
                    #如果没有抽象翻译就用拼音顶他
                    jb_pinyin=lazy_pinyin(jb)[0]

                    #然后比对
                    if jb_pinyin in pinyin_to_words:
                        result+=emoji_json[pinyin_to_words[jb_pinyin]]
                    else:
                        result+=jb
    else:
        raise Warning('请选择是轻度(slight)还是重度(severe)')
    return result
def add_chouxiang(word,emoji):
    if word=='' or emoji=='':
        raise Warning('word 和 emoji不能为空！')
    with open(json_path,'r',encoding='utf8') as j:
        emoji_json = eval(j.read())
        if word in emoji_json:
            raise Warning('🐜🐋🈶🌶️这个🚲啦带哥🇨🇷')
        else:
            emoji_json[word] = emoji
    with open(json_path,'w',encoding='utf8')as j:
        j.write(str(emoji_json))
    print(f'成功添加  {word}->{emoji}')

print('cmd不支持输出emoji表情，但可以复制出去用，所以不要慌')
while 1:
    select_mode = input('输入1选择轻度抽象，输入2选择高度抽象,输入3添加抽象字符')
    if select_mode=='3':
        word=input('输入需要添加的字')
        emoji=input('输入需要补充的emoji')
        add_chouxiang(word,emoji)
        continue
    chouxiang_str = input('输入需要抽象的句子\n例如.我真的就不信了，哪来的这么多的抽象字== 👴💉💧9️⃣8️⃣✉🌶️，🌶️来💧这么多💧抽🐘字')
    if select_mode=='1':
        r=translate_to_chouxiang(chouxiang_str, level='slight')
    elif select_mode=='2':
        r=translate_to_chouxiang(chouxiang_str,level='severe')
    print(r)
