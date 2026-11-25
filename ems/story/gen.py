IC={
'inbox':'<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
'alert':'<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'trend':'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
'checkCircle':'<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.5 2.5L16 9.5"/>',
'review':'<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5M8.5 11l2 2 3.5-3.5"/>',
'brief':'<path d="M4 4h16v16H4z"/><path d="M8 9h8M8 13h8M8 17h5"/>',
'send':'<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>',
'lock':'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.8 3 2.8 15 0 18M12 3c-2.8 3-2.8 15 0 18"/>',
'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
'layers':'<path d="M12 3 2 8l10 5 10-5z"/><path d="M2 13l10 5 10-5"/>',
'summary':'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h6"/>',
'chat':'<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
'amb':'<path d="M2 7h11v10H2zM13 10h4l4 4v3h-8z"/><circle cx="6.5" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/><path d="M7.5 9.5v5M5 12h5"/>',
'map':'<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
'heart':'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/><path d="M3.5 12h4l2-3 3 6 2-3h6"/>',
'hospital':'<path d="M4 21V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v16M2 21h20M12 7v6M9 10h6M10 21v-4h4v4"/>',
'timer':'<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2M9 2h6"/>',
'database':'<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
'spark':'<path d="M12 3l2 5.5L19.5 10 14 12l-2 6-2-6-5.5-2L10 8.5z"/>',
'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
'grid':'<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
'file':'<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/>',
'bell':'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 8 3 8H3s3-1 3-8M10.3 20a2 2 0 0 0 3.4 0"/>',
}
def ic(n,cls='ic'): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{IC[n]}</svg>'
BAR='WaveTech · EMS Intelligence'
def frame(img,alt,url=BAR,cls='frame',lazy=True):
    return f'<figure class="{cls}"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><img src="img/{img}.jpg?v={{IMGV}}" alt="{alt}"{" loading=\"lazy\"" if lazy else ""}></figure>'
def shot_slide(tone,step,role,title,lede,points,img,alt,chips):
    lis=''.join(f'<li style="--d:{6+i}">{p}</li>' for i,p in enumerate(points))
    ch=''.join(f'<span class="chip {"alert" if c[0]=="alert" else "c"+str(i)}" style="--d:{10+i*2}">{ic(c[0],"ic sm")}{c[1]}</span>' for i,c in enumerate(chips))
    return f'''<section class="slide shot {tone}" aria-label="{title}">
<div class="txt">
<p class="tag r" style="--d:0">{step}</p>
<p class="eye r" style="--d:1">{role}</p>
<h2 class="r" style="--d:2">{title}</h2>
<p class="lede r" style="--d:4">{lede}</p>
<ul class="pts">{lis}</ul>
</div>
<div class="stage3d">{frame(img,alt)}{ch}</div>
</section>'''
def cards(tone,eye,h2,lede,items):
    cc=''.join(f'<article class="card flip" style="--d:{3+i*2}">{ic(a,"ic lg")}<h3>{b}</h3><p>{c}</p></article>' for i,(a,b,c) in enumerate(items))
    lp=f'<p class="lede r" style="--d:2">{lede}</p>' if lede else ''
    return f'''<section class="slide cards4 {tone}" aria-label="{h2}">
<div class="head"><p class="eye r" style="--d:0">{eye}</p><h2 class="r" style="--d:1">{h2}</h2>{lp}</div>
<div class="grid4">{cc}</div>
</section>'''
S=[]
# 1 cover
S.append(f'''<section class="slide cover dark" aria-label="WaveTech EMS Intelligence">
<div class="txt">
<img class="wtlogo" src="img/wtmark.png" alt="WaveTech">
<p class="eye r" style="--d:2">WaveTech · طبقة تحليلية فوق Wave</p>
<h1 class="title en"><span style="--d:3">EMS</span> <span style="--d:4">Intelligence</span></h1>
<p class="lede r" style="--d:7">من البلاغ إلى المستشفى، كل دقيقة محسوبة.</p>
<p class="hint r" style="--d:10"><kbd>←</kbd> أو المسافة للتالي</p>
</div>
<div class="stage3d float">{frame("cmd","مركز القيادة التنفيذي",lazy=False)}</div>
</section>''')
# 2 problem
prob=[('database','البيانات موجودة، والصورة غائبة','كل بلاغ وتقرير محفوظ في Wave، لكن كل سؤال من الإدارة يعني استعلاماً وتقريراً يدوياً.'),
('clock','المتوسط يخفي المتأخر','الرقم العام يبدو مريحاً، والحالة الحرجة التي وصلناها متأخرين لا تظهر فيه.'),
('alert','النقص يُكتشف متأخراً','توقيت عودة النبض أو مستلم المريض في المستشفى ينقص، ولا يُعرف إلا عند التدقيق.'),
('file','الامتثال عمل يدوي','NEMSIS والملف السعودي يحتاجان ربط حقول وتحققاً، تقريراً بعد تقرير.')]
pc=''.join(f'<article class="card flip" style="--d:{4+i*2}">{ic(a,"ic lg")}<h3>{b}</h3><p>{c}</p></article>' for i,(a,b,c) in enumerate(prob))
S.append(f'''<section class="slide problem dark" aria-label="المشكلة">
<div class="head"><p class="eye r" style="--d:0">المشكلة</p><h2 class="r" style="--d:1">الدقائق تضيع، ولا أحد يراها في وقتها</h2><p class="lede r" style="--d:2">في الإسعاف كل دقيقة لها ثمن، ومع ذلك تُقرأ الأرقام بعد أن ينتهي الشهر:</p></div>
<div class="grid4">{pc}</div>
<p class="cost r" style="--d:13">{ic("trend","ic sm")}والنتيجة: تأخير في الطريق والتسليم يتكرر، لأنه لا يظهر إلا بعد أسابيع.</p>
</section>''')
# 3 solve
rows=[('تقرير يدوي لكل سؤال','شاشات حيّة من بيانات Wave تتحدث تلقائياً، لكل دور ما يخصه'),
('متوسط يخفي الحالات المتأخرة','الزمن المعتاد وزمن 90% من البلاغات، مقابل المستهدف لكل مستوى فرز ومدينة'),
('نقص التوثيق يظهر عند التدقيق','مراجع ذكي يقرأ نص المسعف ويقترح التصحيح، والطاقم يعتمد'),
('امتثال يدوي تقريراً بتقرير','قاموس بيانات مربوط بـ NEMSIS v3.5 والملف السعودي، وقواعد تحقق تلقائية')]
ba=''.join(f'<li style="--k:{k}"><span class="was">{a}</span><span class="arrow" aria-hidden="true"></span><span class="now">{ic("checkCircle","ic sm")}{b}</span></li>' for k,(a,b) in enumerate(rows))
S.append(f'''<section class="slide solve light" aria-label="الحل">
<div class="head"><p class="eye r" style="--d:0">الحل</p><h2 class="r" style="--d:1">من بيانات محفوظة إلى قرار في وقته</h2></div>
<div class="ba"><p class="ba__h"><span>اليوم</span><span></span><span>مع WaveTech</span></p><ol>{ba}</ol></div>
</section>''')
# 4 idea
S.append(f'''<section class="slide idea mint" aria-label="الفكرة">
<div class="head"><p class="eye r" style="--d:0">الفكرة</p><h2 class="r" style="--d:1">لا نظام جديد، بل طبقة فوق ما تملكونه</h2><p class="lede r" style="--d:2">تبقى Wave كما هي عند الطواقم. الطبقة تقرأ منها، وتنظّف وتربط، ثم تعرض لكل دور ما يحتاجه.</p></div>
<div class="flowmap">
<svg class="wires" viewBox="0 0 1200 300" preserveAspectRatio="none" aria-hidden="true">
<path id="w1" d="M1080 150 C 960 150 900 150 780 150"/><path id="w2" d="M600 150 C 500 150 420 150 320 150"/>
<circle r="7" class="pulse"><animateMotion dur="2.4s" repeatCount="indefinite" begin="1.2s"><mpath href="#w1"/></animateMotion></circle>
<circle r="7" class="pulse"><animateMotion dur="2.4s" repeatCount="indefinite" begin="2.4s"><mpath href="#w2"/></animateMotion></circle>
</svg>
<article class="node n1 pop" style="--d:3">{ic("database","ic lg")}<h3>Wave</h3><p>البلاغات وتقارير ePCR كما تُسجَّل اليوم. لا تغيير على الطواقم.</p></article>
<article class="node n2 pop gate" style="--d:5">{ic("layers","ic lg")}<h3>طبقة WaveTech</h3><p>تربط كل حقل بـ NEMSIS والملف السعودي، وتتحقق من كل تقرير.</p><span class="gatebadge">طبقة البيانات</span></article>
<article class="node n3 pop" style="--d:7">{ic("grid","ic lg")}<h3>القرار</h3><p>القيادة والعمليات والجودة، كل دور يرى شاشاته وأرقامه.</p></article>
</div>
</section>''')
# 5 journey
steps=[('phone','استلام البلاغ','والفرز حسب CTAS'),('send','الإسناد','1.1 دقيقة معتادة'),('amb','الانطلاق','0.9 دقيقة'),('map','الطريق للموقع','9.4 دقيقة'),('heart','في الموقع والنقل','12.6 ثم 14.1 دقيقة'),('hospital','التسليم','13.0 دقيقة')]
st=''.join(f'<li class="step" style="--k:{i}"><span class="dotn">{i+1}</span>{ic(a,"ic")}<b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(steps))
S.append(f'''<section class="slide journey light" aria-label="رحلة البلاغ">
<div class="head"><p class="eye r" style="--d:0">رحلة البلاغ</p><h2 class="r" style="--d:1">كل مرحلة من البلاغ لها ساعة</h2><p class="lede r" style="--d:2">الزمن المعتاد لكل مرحلة في منطقة الرياض، من الاستلام حتى إتمام التسليم.</p></div>
<div class="track"><div class="rail"><i class="runner"></i></div><ol class="steps">{st}</ol></div>
</section>''')
# 6 command
S.append(shot_slide('light','مركز القيادة','المدير التنفيذي','الوردية تبدأ بملخص مكتوب','يُكتب تلقائياً من بيانات Wave ويراجعه مشرف المناوبة، ثم يعرض ما تغيّر عن الليلة السابقة وأين تبدأ.',['أكبر تغيير أولاً، ومن أين تبدأ','يُسمع في 40 ثانية أو يُرسل للمدير','كل رقم يفتح ما خلفه'],'cmd','ملخص بداية الوردية',[('clock','آخر تحديث 08:42'),('alert','التسليم (أ) صار أبطأ 8 دقائق')]))
# 7 stats
S.append(f'''<section class="slide shot light stats" aria-label="المؤشرات">
<div class="txt">
<p class="tag r" style="--d:0">مركز القيادة</p><p class="eye r" style="--d:1">المؤشرات</p>
<h2 class="r" style="--d:2">أربعة أرقام تقول أين نقف</h2>
<p class="lede r" style="--d:3">كل رقم بجملة يفهمها الجميع، ومقابل مستهدفه، وما تغيّر عن الشهر الماضي.</p>
<div class="kpis">
<div class="kpi good r" style="--d:5"><b data-count="11.4" data-dec="1">0</b><span>دقيقة: الزمن المعتاد للاستجابة</span></div>
<div class="kpi bad r" style="--d:6"><b data-count="78" data-suf="%">0%</b><span>الحالات الحرجة ضمن المستهدف</span></div>
<div class="kpi good r" style="--d:7"><b data-count="91.2" data-dec="1" data-suf="%">0%</b><span>اكتمال تقارير ePCR</span></div>
<div class="kpi info r" style="--d:8"><b data-count="84" data-suf="%">0%</b><span>التسليم خلال 30 دقيقة</span></div>
</div>
</div>
<div class="stage3d">{frame("kpis","مؤشرات مركز القيادة")}<span class="chip c0 live" style="--d:10"><i class="dotlive"></i>متصل بنظام Wave · قبل دقيقتين</span></div>
</section>''')
# 8 map
S.append(shot_slide('mint','العمليات','الخريطة التشغيلية','المملكة بـ 13 منطقة، ثم المراكز','اختر المؤشر: حجم البلاغات أو زمن الاستجابة أو الجاهزية، ثم افتح المنطقة لترى مراكزها.',['ترتيب المناطق بجانب الخريطة','افتح الرياض وشاهد 42 مركزاً','تتبّع آخر بلاغ لأي مركز'],'map','الخريطة التشغيلية',[('map','13 منطقة · 270 مركزاً')]))
# 9 dispatch
S.append(shot_slide('light','العمليات','البلاغات والاستجابة','أين تضيع الدقائق؟','زمن كل مرحلة، وزمن الاستجابة لكل مستوى فرز ولكل مدينة، مقابل المستهدف.',['CTAS II فوق المستهدف بالليل','الحالات الاستثنائية: إلغاء ورفض نقل','خريطة حرارية: يوم الأسبوع × الساعة'],'dispatch','شاشة البلاغات والاستجابة',[('timer','الطريق للموقع 9.4 دقيقة')]))
# 10 duo fleet+alerts
S.append(f'''<section class="slide duo mint" aria-label="الأسطول والتنبيهات">
<div class="head"><p class="tag r" style="--d:0">العمليات</p><p class="eye r" style="--d:1">الأسطول والتنبيهات</p><h2 class="r" style="--d:2">ما يحتاج تدخلاً الآن، قبل أن يصير تأخيراً</h2><p class="lede r" style="--d:3">كل مركبة في مربع بحالتها. والتنبيهات مرتبة حسب الخطورة، وعدّادها يسخن كلما طال الوقت.</p></div>
<div class="pair">
<figure class="frame tiltR" style="--d:5"><div class="bar"><i></i><i></i><i></i><span>الأسطول والفرق</span></div><img src="img/fleet.jpg?v={{IMGV}}" alt="الأسطول والفرق" loading="lazy"></figure>
<figure class="frame tiltL" style="--d:8"><div class="bar"><i></i><i></i><i></i><span>التنبيهات</span></div><img src="img/alerts.jpg?v={{IMGV}}" alt="مركز التنبيهات" loading="lazy"></figure>
<span class="chip alert" style="--d:12">{ic("alert","ic sm")}مركز الخرج 3 بلا إسعاف: 0 من 3 متاحة</span>
</div>
</section>''')
# 11 gate
S.append('''<section class="slide gate dark" aria-label="الطبقة السريرية">
<div class="gatefx" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
<div class="center">
<p class="eye r" style="--d:0">السريري والجودة</p>
<h1 class="big r" style="--d:2">كل تقرير <span class="under">موثّق ومُتحقق منه</span></h1>
<p class="lede r" style="--d:5">من هنا تبدأ شاشات المسارات الحرجة والتسليم والجودة.</p>
</div>
</section>''')
# 12 pathways
S.append(shot_slide('light','السريري','المسارات الحرجة','توقف القلب والجلطات والإصابات، حلقة بحلقة','سلسلة الرعاية لكل مسار مع نسبة تحقق كل خطوة، والأزمنة الحرجة مقابل المستهدف.',['أضعف حلقة تظهر أولاً','الاتجاه خلال 6 أشهر','قراءة تحليلية تُولد من البيانات'],'pathways','المسارات السريرية الحرجة',[('heart','عودة النبض 24% · +3 نقاط'),('alert','الإنعاش من المارة 31%، والمستهدف 50%')]))
# 13 handover
S.append(shot_slide('mint','السريري','التسليم للمستشفى','كم ينتظر الطاقم عند الطوارئ؟','توزيع زمن التسليم، ومآلات المرضى من الربط مع أنظمة المستشفيات، وأداء كل مستشفى.',['16% من التسليمات فوق 30 دقيقة','التنبيه المسبق للمستشفى 61%','مآل المريض: تنويم أو عناية أو خروج'],'handover','التسليم للمستشفى',[('hospital','المستشفى (أ): 21% فوق 30 دقيقة')]))
# 14 quality
S.append(shot_slide('light','الجودة','جودة التقارير والامتثال','جاهزية NEMSIS v3.5 والملف السعودي في شاشة','اكتمال ePCR، والامتثال للملف السعودي، وجاهزية التصدير، والتغطية لكل دومين من 26.',['404 حقول مربوطة بمصدرها في Wave','أكثر قواعد التحقق فشلاً','الاكتمال حسب نوع الحالة'],'quality','جودة التقارير والامتثال',[('checkCircle','اكتمال ePCR 91.2%'),('shield','2,214 من 2,600 تجتاز التحقق')]))
# 15 records
S.append(shot_slide('light','الجودة','جميع التقارير','كل تقرير ePCR، ورحلة حالته','ابحث برقم التقرير أو المدينة أو الشكوى، ورتّب حسب الأحدث أو الأقل اكتمالاً، وصدّر CSV.',['حالة كل تقرير: مكتمل، مسودة، معدّل','نسبة الاكتمال لكل تقرير','رحلة الحالة من الاستلام للتسليم'],'records','جميع تقارير ePCR',[('file','196 مسودة تحتاج إكمال')]))
# 16 AI chat
tools=[('layers','الاستجابة حسب المدينة',1),('clock','الوردية الليلية',1),('amb','جاهزية الأسطول',1),('trend','توقع 12 ساعة',1),('summary','تفاصيل البلاغات',0),('bell','التنبيهات',0)]
tl=''.join(f'<span class="tool{" use" if u else ""}" style="--t:{i}">{ic(a,"ic sm")}{b}</span>' for i,(a,b,u) in enumerate(tools))
S.append(f'''<section class="slide ai dark" aria-label="اسأل ويف">
<div class="txt">
<p class="tag r" style="--d:0">الذكاء الاصطناعي</p>
<p class="eye r" style="--d:1">اسأل ويف</p>
<h2 class="r" style="--d:2">اسأل بلغتك، والجواب من أرقام Wave</h2>
<p class="lede r" style="--d:4">ويف يقرأ من نفس المؤشرات التي تعرضها الشاشات، فأي رقم يقوله تجده في صفحته.</p>
<ul class="pts"><li style="--d:6">يذكر من أين أخذ كل رقم</li><li style="--d:7">يقترح إجراءً، والمشرف يعتمد</li><li style="--d:8">يقترح السؤال التالي</li></ul>
</div>
<div class="chat" aria-hidden="true">
<div class="q"><span class="typed">ليش الخرج أبطأ بعد الساعة 8 مساءً؟</span></div>
<div class="reads"><small>يقرأ من</small><div class="tools">{tl}</div></div>
<div class="ans">
<p class="a0"><b>حالات CTAS II في الخرج بعد 8 مساءً وسيطها 14.2 دقيقة مقابل 10.2 للمنطقة، في 47 حالة.</b></p>
<p class="a1 h">السبب</p>
<p class="a2 li">3 من 6 مراكز فيها مركبة متاحة واحدة أو أقل.</p>
<p class="a3 li">AMB-KHJ-07 في الورشة منذ 52 ساعة.</p>
<p class="a4 h">المقترح</p>
<p class="a5 li">حرّك AMB-KHJ-01 إلى STN-KHJ-03 قبل 17:30، فترتفع التغطية من 81% إلى 94%.</p>
<p class="a6 src">{ic("layers","ic sm")}من: الاستجابة حسب المدينة، جاهزية الأسطول، توقع 12 ساعة</p>
</div>
<div class="follow"><span class="f0">أي المراكز أعلى ضغطاً؟</span><span class="f1">وش يصير لو أجّلنا صيانة AMB-KHJ-12؟</span></div>
</div>
</section>''')
# 17 forecast
S.append(shot_slide('mint','الذكاء الاصطناعي','توقع الـ 12 ساعة الجاية','نعرف الذروة قبل أن تصل','البلاغات المتوقعة ساعة بساعة، من 3 سنوات من بيانات Wave والمواسم والفعاليات، مقابل سعة الأسطول.',['اقتراح جاهز: أي مركبة تتحرك ومتى','كل اقتراح يحتاج اعتماد المشرف','دقة آخر 30 يوماً: 91% ضمن ±8 بلاغات'],'forecast','توقع الـ 12 ساعة الجاية',[('trend','18:00 · متوقع 126 بلاغاً، فوق السعة')]))
# 18 reviewer
S.append(shot_slide('light','الذكاء الاصطناعي','مراجع التقارير الذكي','يقرأ ما كتبه المسعف ويقارنه بالحقول','كتب المسعف «أُعطي أدرينالين» وحقل الأدوية فاضي؟ يقترح ويف الإضافة، والطاقم يعتمد ويوقّع.',['41 تعارضاً مفتوحاً من 2,600 تقرير','الاكتمال بعد التصحيح 93.4%','لا يُعدّل أي تقرير تلقائياً'],'reviewer','مراجع التقارير الذكي',[('spark','اقتراح: CTAS I وفتح نموذج eArrest')]))
# 19 AI control
S.append(cards('light','الذكاء الاصطناعي','ذكاء تحت السيطرة','يساعد الفرق على الفهم والتحرك، ولا يقرر بدلها.',[
('users','يقترح ولا ينفّذ','كل اقتراح بتحريك مركبة أو تفعيل فريق يحتاج اعتماد المشرف.'),
('lock','لا يغيّر تقريراً','كل تصحيح يرجع للطاقم للتوقيع، ويُسجَّل في سجل التدقيق.'),
('checkCircle','أرقامه أرقام الشاشات','يقرأ من نفس المؤشرات المعروضة، ويذكر مصدر كل رقم.'),
('trend','دقته معلنة','دقة التوقع في آخر 30 يوماً معروضة على الشاشة نفسها.')]))
# 20 devices
S.append('''<section class="slide devices mint" aria-label="في كل مكان">
<div class="head"><p class="eye r" style="--d:0">في كل مكان</p><h2 class="r" style="--d:1">لغتان، ووضعان، وكل الشاشات</h2></div>
<div class="devs">
<figure class="frame laptop" style="--d:3"><div class="bar"><i></i><i></i><i></i><span>English · Dark</span></div><img src="img/endark.jpg?v={IMGV}" alt="الواجهة بالإنجليزي والوضع الداكن" loading="lazy"></figure>
<figure class="phone p1" style="--d:6"><img src="img/m1.jpg?v={IMGV}" alt="ملخص الوردية على الجوال" loading="lazy"></figure>
<figure class="phone p2" style="--d:8"><img src="img/m2.jpg?v={IMGV}" alt="التنبيهات على الجوال" loading="lazy"></figure>
<figure class="phone p3" style="--d:10"><img src="img/m3.jpg?v={IMGV}" alt="التسليم للمستشفى على الجوال" loading="lazy"></figure>
</div>
</section>''')
# 21 value
vals=[('grid','للقيادة',['صورة واحدة موثوقة لكل الوردية','ترى المتأخر، لا المتوسط فقط','تعرف أين تبدأ كل صباح']),
('amb','لمركز العمليات',['يرى نقص التغطية قبل الذروة','تنبيهات مرتبة حسب الخطورة','اقتراح جاهز بالمركبة والتوقيت']),
('shield','لمشرف الجودة',['يعرف ما ينقص قبل التدقيق','الامتثال للملف السعودي في شاشة','تصحيح بنقرة، والطاقم يوقّع'])]
vc=''.join(f'<article class="card flip val" style="--d:{3+i*3}">{ic(a,"ic lg")}<h3>{b}</h3><ul>'+''.join(f'<li>{x}</li>' for x in xs)+'</ul></article>' for i,(a,b,xs) in enumerate(vals))
S.append(f'''<section class="slide value light" aria-label="القيمة">
<div class="head"><p class="eye r" style="--d:0">القيمة</p><h2 class="r" style="--d:1">دقائق أقل في الطريق، وقرار في وقته</h2></div>
<div class="grid3">{vc}</div>
<p class="band r" style="--d:13">{ic("send","ic sm")}الأرقام تصل الفرق خلال الوردية، لا بعد نهاية الشهر.</p>
</section>''')
# 22 offer
offer=[('brief','ملخص الوردية','مكتوب ومراجع'),('grid','مؤشرات الأداء','مقابل المستهدف'),('map','الخريطة التشغيلية','13 منطقة ومراكزها'),('phone','البلاغات والاستجابة','زمن كل مرحلة'),('amb','الأسطول والفرق','كل مركبة بحالتها'),
('heart','المسارات الحرجة','حلقة بحلقة'),('hospital','التسليم للمستشفى','ومآلات المرضى'),('bell','التنبيهات','قبل أن تتأخر'),('shield','جودة التقارير','NEMSIS والملف السعودي'),('chat','اسأل ويف','يجاوب بالأرقام ومصدرها')]
oc=''.join(f'<li class="tile" style="--d:{3+i}">{ic(a,"ic")}<b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(offer))
S.append(f'''<section class="slide offer mint" aria-label="ما تقدمه WaveTech">
<div class="head"><p class="eye r" style="--d:0">ما تقدمه WaveTech</p><h2 class="r" style="--d:1">عشر شاشات فوق Wave، من البلاغ إلى الجودة</h2><p class="lede r" style="--d:2">كل شاشة لها دور، وكل رقم له مصدر.</p></div>
<ol class="tiles">{oc}</ol>
</section>''')
# 23 trust
S.append(cards('dark','الثقة','ضوابط مبنية في الطبقة، لا في التعليمات','',[
('users','صلاحيات حسب الدور','المدير التنفيذي والجودة والعمليات وفريق البيانات، كل دور يرى شاشاته.'),
('file','NEMSIS v3.5 والملف السعودي','قاموس بيانات يربط كل حقل بمصدره، وCTAS أساس الفرز.'),
('summary','سجل تدقيق','كل تصحيح وكل اعتماد مسجّل: من، ومتى، وماذا.'),
('database','Wave لا يتغيّر','الطبقة تقرأ من Wave، والطواقم تعمل كما تعمل اليوم.')]))
# 24 plan
plan=[('المرحلة 1','ربط Wave','قراءة البيانات وربط الحقول بالقاموس'),('المرحلة 2','قواعد التحقق','الحقول الإلزامية والشرطية للملف السعودي'),('المرحلة 3','الشاشات والأدوار','بيانات حقيقية وصلاحيات لكل دور'),('المرحلة 4','التشغيل','تدريب الفرق ومتابعة أول شهر معكم')]
pc=''.join(f'<li style="--k:{i}"><span class="when">{a}</span><b>{b}</b><small>{c}</small></li>' for i,(a,b,c) in enumerate(plan))
S.append(f'''<section class="slide plan light" aria-label="الخطوات القادمة">
<div class="head"><p class="eye r" style="--d:0">الخطوات القادمة</p><h2 class="r" style="--d:1">من النموذج إلى التشغيل في أربع مراحل</h2></div>
<div class="tl"><div class="tlrail"><i></i></div><ol>{pc}</ol></div>
</section>''')
# 25 close
S.append('''<section class="slide close dark" aria-label="شكرًا">
<div class="center">
<img class="wtlogo big" src="img/wtmark.png" alt="WaveTech">
<h1 class="big r" style="--d:2">شكرًا</h1>
<p class="lede r" style="--d:4">جرّبوا النموذج</p>
<a class="cta r" style="--d:6" href="https://maazmajid.com/ems/" rel="noopener">maazmajid.com/ems</a>
<p class="by r" style="--d:8">نموذج تصميمي ببيانات اصطناعية</p>
</div>
</section>''')
IMGV='202611250130'
html=open('/home/claude/ems-story/shell.html').read()
old="const to = +el.dataset.count, suf = el.dataset.suf || '', t0 = performance.now(), d = 1400;"
assert old in html
html=html.replace(old,"const to = +el.dataset.count, suf = el.dataset.suf || '', dec = +(el.dataset.dec || 0), t0 = performance.now(), d = 1400;")
html=html.replace("el.textContent = Math.round(to * e) + suf;","el.textContent = (to * e).toFixed(dec) + suf;")
html=html.replace('<!--SLIDES-->','\n'.join(S)).replace('__TOTAL__',str(len(S))).replace('{IMGV}',IMGV)
open('/home/claude/maaaz123.github.io/ems/story/index.html','w').write(html)
print(len(S),len(html))
