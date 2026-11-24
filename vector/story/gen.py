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
S.append(f'''<section class="slide cards3 light" data-n="2" aria-label="لماذا The Vector">
<div class="head"><p class="eye r" style="--d:0">لماذا The Vector</p><h2 class="r" style="--d:1">متابعة المبادرات تتعثر في ثلاثة أماكن</h2></div>
<div class="grid3">
<article class="card flip" style="--d:3">{ic("inbox","ic lg")}<h3>الأرقام متفرقة</h3><p>ملفات وإيميلات من كل جهة، ومكتب البرنامج يجمعها يدويًا كل شهر.</p></article>
<article class="card flip" style="--d:5">{ic("clock","ic lg")}<h3>القيادة ترى متأخرًا</h3><p>الصورة تصل بعد أسابيع، وأحيانًا قبل أن يراجعها أحد.</p></article>
<article class="card flip" style="--d:7">{ic("decision","ic lg")}<h3>القرارات تضيع</h3><p>ما تحتاجه المبادرة من القيادة يبقى في محضر أو رسالة، فلا يُتابع.</p></article>
</div>
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
S.append(shot_slide(18,'dark','للقيادة','اسأل The Vector','مساعد يجاوب بالأرقام ويذكر مصدرها','يجاوب من البيانات المنشورة فقط، ويقول من أين أخذ كل رقم.',['عربي وإنجليزي','يقرأ المنشور ولا يعدّل','كل سؤال في سجل تدقيق'],'assistant','إجابة المساعد',[('chat','Claude على Amazon Bedrock')]))
S.append('''<section class="slide devices mint" data-n="19" aria-label="في كل مكان">
<div class="head"><p class="eye r" style="--d:0">في كل مكان</p><h2 class="r" style="--d:1">لغتان، ووضعان، وكل الشاشات</h2></div>
<div class="devs">
<figure class="frame laptop" style="--d:3"><div class="bar"><i></i><i></i><i></i><span>English · Dark</span></div><img src="img/endark.jpg" alt="المنصة بالإنجليزي والوضع الداكن" loading="lazy"></figure>
<figure class="phone p1" style="--d:6"><img src="img/m1.jpg" alt="خلاصة القيادة على الجوال" loading="lazy"></figure>
<figure class="phone p2" style="--d:8"><img src="img/m2.jpg" alt="مهام المدير على الجوال" loading="lazy"></figure>
<figure class="phone p3" style="--d:10"><img src="img/m3.jpg" alt="صفحة المبادرة على الجوال" loading="lazy"></figure>
</div>
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
