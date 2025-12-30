import re

def normalize_answer(answer: str) -> str:
    """VQA 官方标准化"""
    answer = answer.replace('\n', ' ').replace('\t', ' ').strip()
    answer = answer.lower()
    
    # 标点处理（官方逻辑）
    punct = [';', r'/', '[', ']', '"', '{', '}', '(', ')', '=', '+', '\\', '_', '-', '>', '<', '@', '`', ',', '?', '!']
    comma_strip = re.compile(r'(\d)(\,)(\d)')
    period_strip = re.compile(r'(?!<=\d)(\.)(?!\d)')
    
    for p in punct:
        if (p + ' ' in answer or ' ' + p in answer) or comma_strip.search(answer):
            answer = answer.replace(p, '')
        else:
            answer = answer.replace(p, ' ')
    answer = period_strip.sub('', answer)
    
    # 数字映射 + 冠词移除
    manual_map = {'none':'0','zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}
    articles = ['a', 'an', 'the']
    contractions = {"aint":"ain't","arent":"aren't","cant":"can't","couldve":"could've","couldnt":"couldn't","couldn'tve":"couldn't've","couldnt've":"couldn't've","didnt":"didn't","doesnt":"doesn't","dont":"don't","hadnt":"hadn't","hadnt've":"hadn't've","hadn'tve":"hadn't've","hasnt":"hasn't","havent":"haven't","hed":"he'd","hed've":"he'd've","he'dve":"he'd've","hes":"he's","howd":"how'd","howll":"how'll","hows":"how's","Id've":"I'd've","I'dve":"I'd've","Im":"I'm","Ive":"I've","isnt":"isn't","itd":"it'd","itd've":"it'd've","it'dve":"it'd've","itll":"it'll","let's":"let's","maam":"ma'am","mightnt":"mightn't","mightnt've":"mightn't've","mightn'tve":"mightn't've","mightve":"might've","mustnt":"mustn't","mustve":"must've","neednt":"needn't","notve":"not've","oclock":"o'clock","oughtnt":"oughtn't","ow's'at":"'ow's'at","'ows'at":"'ow's'at","'ow'sat":"'ow's'at","shant":"shan't","shed've":"she'd've","she'dve":"she'd've","she's":"she's","shouldve":"should've","shouldnt":"shouldn't","shouldnt've":"shouldn't've","shouldn'tve":"shouldn't've","somebody'd":"somebodyd","somebodyd've":"somebody'd've","somebody'dve":"somebody'd've","somebodyll":"somebody'll","somebodys":"somebody's","someoned":"someone'd","someoned've":"someone'd've","someone'dve":"someone'd've","someonell":"someone'll","someones":"someone's","somethingd":"something'd","somethingd've":"something'd've","something'dve":"something'd've","somethingll":"something'll","thats":"that's","thered":"there'd","thered've":"there'd've","there'dve":"there'd've","therere":"there're","theres":"there's","theyd":"they'd","theyd've":"they'd've","they'dve":"they'd've","theyll":"they'll","theyre":"they're","theyve":"they've","twas":"'twas","wasnt":"wasn't","wed've":"we'd've","we'dve":"we'd've","weve":"we've","werent":"weren't","whatll":"what'll","whatre":"what're","whats":"what's","whatve":"what've","whens":"when's","whered":"where'd","wheres":"where's","whereve":"where've","whod":"who'd","whod've":"who'd've","who'dve":"who'd've","wholl":"who'll","whos":"who's","whove":"who've","whyll":"why'll","whyre":"why're","whys":"why's","wont":"won't","wouldve":"would've","wouldnt":"wouldn't","wouldnt've":"wouldn't've","wouldn'tve":"wouldn't've","yall":"y'all","yall'll":"y'all'll","y'allll":"y'all'll","yall'd've":"y'all'd've","y'alld've":"y'all'd've","y'all'dve":"y'all'd've","youd":"you'd","youd've":"you'd've","you'dve":"you'd've","youll":"you'll","youre":"you're","youve":"you've"}
    
    words = answer.split()
    out_words = []
    for word in words:
        word = manual_map.get(word, word)
        if word not in articles:
            out_words.append(word)
    
    for i, word in enumerate(out_words):
        if word in contractions:
            out_words[i] = contractions[word]
    
    return ' '.join(out_words)

def accuracy_reward(completions: list[list[dict[str, str]]], solution: list[list[str]], **kwargs) -> list[float]:
    scores = []
    for comp, refs in zip(completions, solution):
        try:
            def _collect_text(node) -> list[str]:
                if isinstance(node, str):
                    return [node]
                if isinstance(node, dict):
                    texts = []
                    if "text" in node and isinstance(node["text"], str):
                        texts.append(node["text"])
                    if "content" in node:
                        texts.extend(_collect_text(node["content"]))
                    return texts
                if isinstance(node, list):
                    return sum([_collect_text(item) for item in node], [])
                return []
            
            text = "\n".join(_collect_text(comp)) or str(comp)
            match = re.search(r'<answer>(.*?)</answer>', text, re.DOTALL | re.IGNORECASE)
            
            if not match:
                scores.append(0.0)
                continue
            
            pred = match.group(1).strip().replace('\n', ' ').replace('\t', ' ').strip()
            
            pred = normalize_answer(pred)
            refs = [normalize_answer(r) for r in refs]
            
            match_count = sum(1 for r in refs if r == pred)
            # 对一个0.2，两个0.5，全对1分
            if match_count == 0:
                scores.append(0.0)
            elif match_count == 1:
                scores.append(0.2)
            elif match_count == 2:
                scores.append(0.5)
            else:  # match_count >= 3
                scores.append(1.0)
            
        except Exception:
            scores.append(0.0)
    
    return scores
