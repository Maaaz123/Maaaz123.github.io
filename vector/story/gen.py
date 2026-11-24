import json
IC=json.load(open('/tmp/icons.json'))
def ic(n,cls='ic'): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{IC[n]}</svg>'
def shot_slide(n,tone,step,role,title,lede,points,img,alt,chips):
    lis=''.join(f'<li style="--d:{6+i}">{p}</li>' for i,p in enumerate(points))
    ch=''.join(f'<span class="chip c{i}" style="--d:{10+i*2}">{ic(c[0],"ic sm")}{c[1]}</span>' for i,c in enumerate(chips))
    return f'''<section class="slide shot {tone}" data-n="{n}" aria-label="{title}">
<div class="txt">
<p class="tag r" style="--d:0">{step}</p>
<p class="eye r" style="--d:1">{role}</p>
<h2 class="r" style="--d:2">{title}</h2>
<p class="lede r" style="--d:4">{lede}</p>
<ul class="pts">{lis}</ul>
</div>
<div class="stage3d">
<figure class="frame"><div class="bar"><i></i><i></i><i></i><span>vector.datavital.io</span></div><img src="img/{img}.jpg" alt="{alt}" loading="lazy"></figure>
{ch}
</div>
</section>'''
S=[]
S.append(f'''<section class="slide cover dark" data-n="1" aria-label="The Vector">
<div class="txt">
<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><rect x="2" y="2" width="60" height="60" rx="16" class="mk-bg"/><path d="M14 46 L27 33 L35 41 L50 22" class="mk-line"/><circle cx="50" cy="22" r="5.5" class="mk-dot"/></svg>
<p class="eye r" style="--d:2">منصة متابعة المبادرات</p>
<h1 class="title"><span style="--d:3">The</span> <span style="--d:4">Vector</span></h1>
<p class="lede r" style="--d:7">من تحديث مدير المبادرة إلى قرار القيادة، في دورة واحدة واضحة كل شهر.</p>
<p class="hint r" style="--d:10"><kbd>←</kbd> أو المسافة للتالي</p>
</div>
<div class="stage3d float">
<figure class="frame"><div class="bar"><i></i><i></i><i></i><span>vector.datavital.io</span></div><img src="img/welcome.jpg" alt="الصفحة الرئيسية لمنصة The Vector"></figure>
</div>
</section>''')
S.append(f'''<section class="slide problem dark" data-n="2" aria-label="المشكلة">
<div class="head"><p class="eye r" style="--d:0">المشكلة</p><h2 class="r" style="--d:1">التعثر يُكتشف بعد أن يقع</h2><p class="lede r" style="--d:2">في كثير من الجهات تُتابع المبادرات بملفات Excel وعروض ورسائل، ويتكرر المشهد نفسه كل شهر:</p></div>
<div class="grid4">
<article class="card flip" style="--d:4">{ic("inbox","ic lg")}<h3>الأرقام متفرقة</h3><p>ملف من كل جهة بصيغة مختلفة، ومكتب البرنامج يجمعها وينسقها يدويًا.</p></article>
<article class="card flip" style="--d:6">{ic("alert","ic lg")}<h3>لا أحد يراجعها</h3><p>الرقم يصل القيادة كما كتبه صاحبه، بلا مقارنة بالشهر الماضي.</p></article>
<article class="card flip" style="--d:8">{ic("clock","ic lg")}<h3>القيادة ترى متأخرًا</h3><p>الصورة تصل بعد أسابيع، فيظهر التأخر فيها بعد أن صار واقعًا.</p></article>
<article class="card flip" style="--d:10">{ic("decision","ic lg")}<h3>القرارات تضيع</h3><p>ما تحتاجه المبادرة من القيادة يبقى في محضر أو رسالة، ولا يتابعه أحد.</p></article>
</div>
<p class="cost r" style="--d:13">{ic("trend","ic sm")}والنتيجة: وقت يضيع في الجمع، وقرارات تتأخر، ومبادرات تتعثر دون أن يراها أحد في وقتها.</p>
</section>''')
rows=[('ملفات من كل جهة بصيغ مختلفة','تحديث شهري واحد في المنصة، بنفس الخطوات لكل مبادرة'),('رقم يصل القيادة بلا مراجعة','بوابة نشر: مكتب البرنامج يراجع، ومن أدخل التحديث لا يراجعه'),('القيادة ترى التأخر بعد أسابيع','خلاصة القيادة تتحدث لحظة النشر، والإنذار المبكر يرى التعثر قبل أن يقع'),('طلبات القرار تضيع في المحاضر','طلب القرار جزء من التحديث، ويُدرج في اجتماع القيادة بضغطة')]
ba=''.join(f'<li style="--k:{k}"><span class="was">{a}</span><span class="arrow" aria-hidden="true"></span><span class="now">{ic("checkCircle","ic sm")}{b}</span></li>' for k,(a,b) in enumerate(rows))
S.append(f'''<section class="slide solve light" data-n="3" aria-label="الحل">
<div class="head"><p class="eye r" style="--d:0">الحل</p><h2 class="r" style="--d:1">مكان واحد للمتابعة، من التحديث إلى القرار</h2></div>
<div class="ba"><p class="ba__h"><span>اليوم</span><span></span><span>مع The Vector</span></p><ol>{ba}</ol></div>
</section>''')
S.append(f'''<section class="slide idea mint" data-n="3" aria-label="الفكرة">
<div class="head"><p class="eye r" style="--d:0">الفكرة</p><h2 class="r" style="--d:1">ثلاثة أدوار، وبوابة نشر واحدة</h2><p class="lede r" style="--d:2">لا يصل القيادة إلا ما راجعه مكتب البرنامج ونشره، فكل رقم في الطبقة الذكية رقم معتمد.</p></div>
<div class="flowmap">
<svg class="wires" viewBox="0 0 1200 300" preserveAspectRatio="none" aria-hidden="true">
<path id="w1" d="M1080 150 C 960 150 900 150 780 150"/><path id="w2" d="M600 150 C 500 150 420 150 320 150"/>
<circle r="7" class="pulse"><animateMotion dur="2.4s" repeatCount="indefinite" begin="1.2s"><mpath href="#w1"/></animateMotion></circle>
<circle r="7" class="pulse"><animateMotion dur="2.4s" repeatCount="indefinite" begin="2.4s"><mpath href="#w2"/></animateMotion></circle>
</svg>
<article class="node n1 pop" style="--d:3">{ic("edit","ic lg")}<h3>مدير المبادرة</h3><p>يحدّث مبادرته كل شهر: النسب، ما تم، القادم، والعوائق.</p></article>
<article class="node n2 pop gate" style="--d:5">{ic("review","ic lg")}<h3>مكتب البرنامج</h3><p>يراجع كل تحديث، ثم ينشره أو يُرجعه بملاحظة.</p><span class="gatebadge">بوابة النشر</span></article>
<article class="node n3 pop" style="--d:7">{ic("brief","ic lg")}<h3>رئيس الجهة</h3><p>يقرأ الخلاصة والتوقعات، ويقرر فيما ينتظره.</p></article>
</div>
</section>''')
steps=[('folder','الإعداد والاعتماد','مكتب البرنامج يُدخل البرنامج وزميله يعتمد'),('calendar','فتح الدورة','بطاقة لكل مبادرة والمخطط يُحسب تلقائيًا'),('edit','تحديث المدير','النسب والخطوات والعوائق وطلب القرار'),('review','المراجعة','مكتب البرنامج يدقق قبل النشر'),('send','النشر','يصل الطبقة الذكية فورًا'),('decision','القيادة تقرر','القرار يُدرج في اجتماع القيادة')]
st=''.join(f'<li class="step" style="--k:{i}"><span class="dotn">{i+1}</span>{ic(a,"ic")}<b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(steps))
S.append(f'''<section class="slide journey light" data-n="4" aria-label="الرحلة">
<div class="head"><p class="eye r" style="--d:0">الرحلة</p><h2 class="r" style="--d:1">دورة شهرية في ست خطوات</h2></div>
<div class="track"><div class="rail"><i class="runner"></i></div><ol class="steps">{st}</ol></div>
</section>''')
S.append(shot_slide(5,'light','كل الأدوار','البداية','دخول واحد، وكل شخص يرى دوره','صفحة دخول بهوية المنصة. بعد الدخول يفتح كل مستخدم على الصفحة التي تخصه.',['الدور والصلاحيات من الحساب تلقائيًا','عربي وإنجليزي، فاتح وداكن','خروج تلقائي عند انتهاء الجلسة'],'login','صفحة تسجيل الدخول',[('lock','اتصال مشفّر'),('globe','عربي · English')]))
S.append(shot_slide(6,'light','الخطوة 1','مكتب البرنامج','يومه يبدأ بما يحتاج انتباهه','الرئيسية ترتب المهام: ما ينتظر المراجعة، والبطاقات التي لم تبدأ، والقرارات المعلّقة.',['حالة الدورة بالأرقام','تذكير بضغطة للمتأخرين','كل رقم يفتح ما خلفه'],'home','الرئيسية لمكتب البرنامج',[('tasks','3 مهام اليوم'),('flag','قراران ينتظران القيادة')]))
S.append(shot_slide(7,'mint','الخطوة 1','إعداد البرنامج','البرنامج والحزم والمبادرات في ثلاث خطوات','خطوة بخطوة أو من Excel، ولكل مبادرة جهتها ومديرها.',['تُحفظ المسودة تلقائيًا','مراجعة أخيرة تنبّه لأي نقص','المدير يصله الوصول بعد الاعتماد'],'setup','شاشة الحزم والمبادرات',[('user','مدير لكل مبادرة'),('checkCircle','حفظ تلقائي')]))
S.append(shot_slide(8,'light','الخطوة 2','الاعتماد','من يُنشئ البرنامج لا يعتمده','يعتمده زميل آخر. عند الاعتماد تُنشأ بطاقة متابعة لكل مبادرة وتُفتح أول دورة.',['مبدأ الشخصين داخل النظام','أول دورة مع أول شهر في البرنامج','الإعادة للتعديل بملاحظة'],'approve','نافذة اعتماد البرنامج',[('shield','مبدأ الشخصين')]))
S.append(shot_slide(9,'light','الخطوة 3','مدير المبادرة','قائمة واحدة بما عليه هذا الشهر','ما أُعيد له بملاحظة أولًا، ثم ما لم يبدأ. وتحت كل بطاقة آخر أرقام منشورة.',['الموعد والأيام المتبقية واضحة','ملاحظة المكتب على البطاقة نفسها','مبادراته فقط'],'tasks','قائمة مهام المدير',[('calendar','7 أيام متبقية')]))
S.append(f'''<section class="slide duo mint" data-n="10" aria-label="التحديث الشهري">
<div class="head"><p class="tag r" style="--d:0">الخطوة 3</p><p class="eye r" style="--d:1">التحديث الشهري</p><h2 class="r" style="--d:2">أربع خطوات، وكل رقم يُقرأ في لحظته</h2><p class="lede r" style="--d:3">يكتب المدير الإنجاز فيرى الانحراف والحالة فورًا. وإذا احتاج قرارًا كتبه بصيغة تقرؤها القيادة.</p></div>
<div class="pair">
<figure class="frame tiltR" style="--d:5"><div class="bar"><i></i><i></i><i></i><span>النسب</span></div><img src="img/figures.jpg" alt="خطوة النسب" loading="lazy"></figure>
<figure class="frame tiltL" style="--d:8"><div class="bar"><i></i><i></i><i></i><span>القادم والعوائق</span></div><img src="img/blocker.jpg" alt="خطوة العوائق وطلب القرار" loading="lazy"></figure>
<span class="chip alert" style="--d:12">{ic("alert","ic sm")}80% والموعد نهاية الشهر: متأخرة جدًا</span>
</div>
</section>''')
S.append(shot_slide(11,'light','الخطوات 4 و5','المراجعة والنشر','مكتب البرنامج يدقق قبل أن ترى القيادة','يقارن التحديث بآخر رقم منشور، ويقرأ الخطوات والعوائق، ثم ينشر أو يُرجع بملاحظة.',['طلبات القيادة أولًا','لا تعديل بعد النشر','من أدخل التحديث لا يراجعه'],'review','شاشة المراجعة',[('review','+6 نقاط عن الشهر الماضي')]))
S.append('''<section class="slide gate dark" data-n="12" aria-label="الطبقة الذكية">
<div class="gatefx" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="center">
<p class="eye r" style="--d:0">الطبقة الذكية</p>
<h1 class="big r" style="--d:2">كل رقم تراه القيادة <span class="under">منشور ومُراجع</span></h1>
<p class="lede r" style="--d:5">من هنا تبدأ الشاشات التي يقرأ منها رئيس الجهة.</p>
</div>
</section>''')
S.append(f'''<section class="slide shot light stats" data-n="13" aria-label="خلاصة القيادة">
<div class="txt">
<p class="tag r" style="--d:0">الخطوة 6</p><p class="eye r" style="--d:1">رئيس الجهة</p>
<h2 class="r" style="--d:2">خلاصة القيادة في صفحة واحدة</h2>
<p class="lede r" style="--d:3">أول جملة تقول ما يحتاج قراره، ثم الأرقام، ثم القرارات وأين التأخر.</p>
<div class="kpis">
<div class="kpi good r" style="--d:5"><b data-count="53" data-suf="%">0%</b><span>الإنجاز حتى اليوم</span></div>
<div class="kpi good r" style="--d:6"><b data-count="16">0</b><span>على المسار</span></div>
<div class="kpi bad r" style="--d:7"><b data-count="7">0</b><span>تحتاج تدخلًا</span></div>
<div class="kpi info r" style="--d:8"><b data-count="45" data-suf="%">0%</b><span>المصروف</span></div>
</div>
</div>
<div class="stage3d"><figure class="frame"><div class="bar"><i></i><i></i><i></i><span>vector.datavital.io/intel</span></div><img src="img/leader.jpg" alt="خلاصة القيادة" loading="lazy"></figure></div>
</section>''')
S.append(shot_slide(14,'mint','الخطوة 6','قرارات القيادة','القرار يُدرج في الاجتماع بضغطة','مرتبة حسب أثرها: كم مبادرة تتوقف عليها ومنذ متى.',['من طلب القرار ولأي مبادرة','المبادرات المتوقفة عليه','يظهر فور نشر التحديث'],'decision','إدراج قرار في الاجتماع',[('checkCircle','أُدرج في اجتماع 25 نوفمبر')]))
S.append(shot_slide(15,'light','للقيادة','الملخص التنفيذي','أين ينتهي البرنامج بنهاية السنة؟','بوتيرة آخر ثلاثة أشهر نحسب التوقع ومداه، لكل حزمة وللبرنامج كله.',['المخطط والفعلي والمتوقع على شريط واحد','لكل حزمة سبب الفجوة','التوقع تقدير بمدى'],'brief','الملخص التنفيذي',[('trend','توقع نهاية السنة')]))
S.append(shot_slide(16,'light','للقيادة','صفحة المبادرة','كل مبادرة بقصتها وأرقامها','الإنجاز والمتوقع والموعد والمصروف والوتيرة، وما تحتاجه الآن مرتبًا حسب أثره.',['ما تعتمد عليه وما ينتظرها','المناطق التي تُنفّذ فيها','سؤال المساعد عنها بضغطة'],'initiative','صفحة المبادرة',[('link','الاعتماديات')]))
S.append(shot_slide(17,'mint','للقيادة','محاكاة الميزانية','ماذا لو خُفّضت الميزانية المتبقية؟','اختر نسبة الخفض وما تحميه، فتقترح المحاكاة ما يستمر وما يُقلّص وما يُؤجّل.',['لا تغيّر شيئًا في البيانات','تنبّه للآثار الجانبية','تجاوب فورًا أثناء النقاش'],'budget','محاكاة الميزانية',[('trend','أثر الخفض على التوقع')]))
S.append(f'''<section class="slide shot light" data-n="18" aria-label="الإنذار المبكر">
<div class="txt">
<p class="tag r" style="--d:0">للقيادة</p>
<p class="eye r" style="--d:1">الإنذار المبكر</p>
<h2 class="r" style="--d:2">نعرف المبادرة المتعثرة قبل أن تتأخر</h2>
<p class="lede r" style="--d:4">بعد كل نشر تُقرأ كل مبادرة بست إشارات: هل تلحق خطتها بوتيرتها الحالية، هل تتباطأ، هل يسبق الصرف الإنجاز، هل تنتظر مبادرة متعثرة أو قرارًا طال، وهل تحديثاتها منتظمة.</p>
<ul class="pts"><li style="--d:6">كل تنبيه يقول السبب بجملة واحدة</li><li style="--d:7">يصل القيادة في خلاصتها، والمدير على بطاقته</li><li style="--d:8">«لماذا؟ وماذا نفعل؟» يسأل المساعد بضغطة</li></ul>
</div>
<div class="stage3d">
<figure class="frame"><div class="bar"><i></i><i></i><i></i><span>vector.datavital.io</span></div><img src="img/risks.jpg" alt="صفحة الإنذار المبكر" loading="lazy"></figure>
<span class="chip c0" style="--d:10">{ic("trend","ic sm")}على المسار اليوم، لكنها في خطر</span>
<span class="chip alert" style="--d:12">{ic("alert","ic sm")}بوتيرتها الحالية تصل إلى 37%، والمخطط 54%</span>
</div>
</section>''')
tools=[('layers','الأرقام الرئيسية والمناطق',1),('trend','توقع نهاية السنة',1),('folder','قائمة المبادرات',0),('summary','تفاصيل مبادرة',0),('flag','القرارات المعلّقة',0),('settings','محاكاة الميزانية',0)]
tl=''.join(f'<span class="tool{" use" if u else ""}" style="--t:{i}">{ic(a,"ic sm")}{b}</span>' for i,(a,b,u) in enumerate(tools))
S.append(f'''<section class="slide ai dark" data-n="18" aria-label="اسأل The Vector">
<div class="txt">
<p class="tag r" style="--d:0">الذكاء الاصطناعي</p>
<p class="eye r" style="--d:1">اسأل The Vector</p>
<h2 class="r" style="--d:2">اسأل بلغتك، والجواب من أرقامك</h2>
<p class="lede r" style="--d:4">المساعد لا يرى الجداول. يقرأ من نفس الحسابات التي تعرضها الشاشات، فأي رقم يقوله تجده في صفحته.</p>
<ul class="pts"><li style="--d:6">يذكر من أين أخذ كل رقم</li><li style="--d:7">إذا لم تكن المعلومة موجودة يقولها صراحة</li><li style="--d:8">يقترح السؤال التالي</li></ul>
</div>
<div class="chat" aria-hidden="true">
<div class="q"><span class="typed">لماذا يُتوقع أن ينتهي البرنامج عند 67% بدل 72%؟</span></div>
<div class="reads"><small>يقرأ من</small><div class="tools">{tl}</div></div>
<div class="ans">
<p class="a0"><b>البرنامج عند 53% مقابل 58% مخطط، وبالوتيرة الحالية يصل إلى نحو 67% بنهاية السنة بدلًا من 72%.</b></p>
<p class="a1 h">السبب</p>
<p class="a2 li">7 مبادرات متأخرة، منها 3 متأخرة جدًا.</p>
<p class="a3 li">أكبر فجوة في حزمة التحول المؤسسي.</p>
<p class="a4 h">المقترح</p>
<p class="a5 li">البت في 3 قرارات معلّقة لدى القيادة.</p>
<p class="a6 src">{ic("layers","ic sm")}من: الأرقام الرئيسية والمناطق، توقع نهاية السنة لكل حزمة</p>
</div>
<div class="follow"><span class="f0">ما أكثر مبادرة متأخرة؟</span><span class="f1">ماذا لو خُفّضت الميزانية 20%؟</span></div>
</div>
</section>''')
S.append(shot_slide(19,'mint','الذكاء الاصطناعي','حاضر في كل صفحة','السؤال جاهز من الصفحة التي أنت فيها','لا تحتاج تعرف كيف تسأل. في الملخص وصفحة المبادرة زر يفتح المساعد بسؤال عن نفس الأرقام التي أمامك.',['من الملخص: «ما الذي يرفع هذه النسبة؟»','من صفحة المبادرة: سؤال عنها بضغطة','بعد كل جواب سؤالان للمتابعة'],'brief','الملخص التنفيذي مع زر اسأل المساعد',[('chat','اسأل المساعد: ما الذي يرفع هذه النسبة؟'),('trend','67% من 72%')]))
cards=[('lock','يقرأ ولا يعدّل','يرى ما نشره مكتب البرنامج فقط، ولا يستطيع تغيير أي رقم أو حالة.'),('checkCircle','أرقامه أرقام الشاشات','ست أدوات قراءة هي نفس حسابات الصفحات، فلا رقم يخالف ما تعرضه المنصة.'),('review','كل سؤال مسجّل','من سأل، ومتى، وماذا سأل، وأي أدوات استخدم، دون حفظ الأرقام التي قرأها.'),('shield','داخل حساب المنصة','Claude على Amazon Bedrock في نفس حساب AWS، ولا تُستخدم البيانات لتدريب أي نموذج.')]
cc=''.join(f'<article class="card flip" style="--d:{3+i*2}">{ic(a,"ic lg")}<h3>{b}</h3><p>{c}</p></article>' for i,(a,b,c) in enumerate(cards))
S.append(f'''<section class="slide cards4 light" data-n="20" aria-label="المساعد تحت السيطرة">
<div class="head"><p class="eye r" style="--d:0">الذكاء الاصطناعي</p><h2 class="r" style="--d:1">مساعد تحت السيطرة</h2><p class="lede r" style="--d:2">بُني ليساعد القيادة على فهم الأرقام، لا ليقرر بدلها.</p></div>
<div class="grid4">{cc}</div>
</section>''')
S.append('''<section class="slide devices mint" data-n="19" aria-label="في كل مكان">
<div class="head"><p class="eye r" style="--d:0">في كل مكان</p><h2 class="r" style="--d:1">لغتان، ووضعان، وكل الشاشات</h2></div>
<div class="devs">
<figure class="frame laptop" style="--d:3"><div class="bar"><i></i><i></i><i></i><span>English · Dark</span></div><img src="img/endark.jpg" alt="المنصة بالإنجليزي والوضع الداكن" loading="lazy"></figure>
<figure class="phone p1" style="--d:6"><img src="img/m1.jpg" alt="خلاصة القيادة على الجوال" loading="lazy"></figure>
<figure class="phone p2" style="--d:8"><img src="img/m2.jpg" alt="مهام المدير على الجوال" loading="lazy"></figure>
<figure class="phone p3" style="--d:10"><img src="img/m3.jpg" alt="صفحة المبادرة على الجوال" loading="lazy"></figure>
</div>
</section>''')
vals=[('brief','للقيادة',['صورة واحدة موثوقة كل شهر، كل رقم فيها مُراجع','تعرف ما ينتظر قرارها، وكم مبادرة تتوقف عليه','ترى المبادرة المتعثرة قبل أن تتأخر']),
('review','لمكتب البرنامج',['لا جمع يدوي ولا تنسيق ملفات','يراجع ما تغيّر عن الشهر الماضي فقط','يذكّر المتأخرين بضغطة، ويعرف من بقي']),
('edit','لمدير المبادرة',['قائمة واحدة بما عليه هذا الشهر','تحديث بأربع خطوات واضحة','يعرف أن طلبه وصل القيادة ومتى أُدرج'])]
vc=''.join(f'<article class="card flip val" style="--d:{3+i*3}">{ic(a,"ic lg")}<h3>{b}</h3><ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul></article>' for i,(a,b,xs) in enumerate(vals))
S.append(f'''<section class="slide value light" data-n="v" aria-label="القيمة">
<div class="head"><p class="eye r" style="--d:0">القيمة</p><h2 class="r" style="--d:1">وقت أقل في الجمع، وقرار في وقته</h2></div>
<div class="grid3">{vc}</div>
<p class="band r" style="--d:13">{ic("send","ic sm")}الأرقام تصل القيادة يوم نشرها، لا بعد أسابيع من جمعها.</p>
</section>''')
offer=[('folder','إعداد البرنامج','خطوة بخطوة أو من Excel'),('shield','الاعتماد','مبدأ الشخصين'),('calendar','دورات شهرية','بطاقة لكل مبادرة'),('edit','التحديث','النسب والخطوات والعوائق'),('review','المراجعة والنشر','قبل أن ترى القيادة'),
('brief','خلاصة القيادة','والقرارات المطلوبة'),('trend','الملخص التنفيذي','توقع نهاية السنة'),('alert','الإنذار المبكر','قبل أن تتأخر'),('settings','محاكاة الميزانية','ماذا لو خُفّضت؟'),('chat','المساعد الذكي','يجاوب بالأرقام ومصدرها')]
oc=''.join(f'<li class="tile" style="--d:{3+i}">{ic(a,"ic")}<b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(offer))
S.append(f'''<section class="slide offer mint" data-n="o" aria-label="ما يقدمه The Vector">
<div class="head"><p class="eye r" style="--d:0">ما يقدمه The Vector</p><h2 class="r" style="--d:1">منصة واحدة تغطي الدورة كاملة</h2><p class="lede r" style="--d:2">من إعداد البرنامج إلى قرار القيادة، في مكان واحد.</p></div>
<ol class="tiles">{oc}</ol>
</section>''')
trust=[('lock','الدخول','Amazon Cognito بصفحة دخول خاصة بالمنصة، واتصال مشفّر'),('shield','مبدأ الشخصين','من يُنشئ لا يعتمد، ومن يُدخل لا يراجع'),('summary','سجل تدقيق','كل إجراء وكل سؤال للمساعد مسجّل'),('layers','على AWS','خادم وقاعدة بيانات وذكاء اصطناعي في حساب واحد')]
tc=''.join(f'<article class="card flip" style="--d:{3+i*2}">{ic(a,"ic lg")}<h3>{b}</h3><p>{c}</p></article>' for i,(a,b,c) in enumerate(trust))
S.append(f'''<section class="slide cards4 dark" data-n="20" aria-label="الثقة">
<div class="head"><p class="eye r" style="--d:0">الثقة</p><h2 class="r" style="--d:1">ضوابط مبنية في النظام، لا في التعليمات</h2></div>
<div class="grid4">{tc}</div>
</section>''')
plan=[('حتى 30 نوفمبر','تجربة المنصة','حسابات للتجربة وبيئة نظيفة لبياناتكم'),('1 إلى 14 ديسمبر','التشغيل الذاتي','فتح الدورات وإدارة المستخدمين والإشعارات بالإيميل'),('15 إلى 21 ديسمبر','دائرة القرار','تسجيل قرار القيادة، وخلاصة الاجتماع PDF، والمرفقات'),('22 إلى 31 ديسمبر','دورة ديسمبر','تشغيل الدورة كاملة معكم، ثم التشغيل الرسمي')]
pc=''.join(f'<li style="--k:{i}"><span class="when">{a}</span><b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(plan))
S.append(f'''<section class="slide plan light" data-n="21" aria-label="الخطوات القادمة">
<div class="head"><p class="eye r" style="--d:0">الخطوات القادمة</p><h2 class="r" style="--d:1">من التجربة إلى التشغيل الرسمي في 31 ديسمبر</h2></div>
<div class="tl"><div class="tlrail"><i></i></div><ol>{pc}</ol></div>
</section>''')
S.append('''<section class="slide close dark" data-n="22" aria-label="شكرًا">
<div class="center">
<svg class="mark big" viewBox="0 0 64 64" aria-hidden="true"><rect x="2" y="2" width="60" height="60" rx="16" class="mk-bg"/><path d="M14 46 L27 33 L35 41 L50 22" class="mk-line"/><circle cx="50" cy="22" r="5.5" class="mk-dot"/></svg>
<h1 class="big r" style="--d:2">شكرًا</h1>
<p class="lede r" style="--d:4">جرّبوا المنصة</p>
<a class="cta r" style="--d:6" href="https://vector.datavital.io" rel="noopener">vector.datavital.io</a>
</div>
</section>''')
html=open('/home/claude/maaaz123.github.io/vector/story/shell.html').read().replace('<!--SLIDES-->','\n'.join(S)).replace('__TOTAL__',str(len(S)))
open('/home/claude/maaaz123.github.io/vector/story/index.html','w').write(html)
print(len(S), len(html))
