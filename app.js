const $=(s,r=document)=>r.querySelector(s);
const $$=(s,r=document)=>[...r.querySelectorAll(s)];
const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)');
let motionPaused=reduceMotion.matches;
const chapters=$$('[data-chapter]');
const stops=$$('[data-stop]');
const road=$('#road');
const roadLength=road.getTotalLength();
const vbw=1750;const centers=[214,539,869,1198,1566];
let positions=[];
function computePositions(){positions=centers.map(x=>{let lo=0,hi=1;for(let i=0;i<24;i++){const mid=(lo+hi)/2;if(road.getPointAtLength(roadLength*mid).x<x)lo=mid;else hi=mid;}return lo;});}
computePositions();
const thoughts=['Curiosity','Consumer insight','CTR · AOP · ROAS','Build · Test · Learn','Brand · Creators · Growth'];
const buildingIds=['school','college','phonepe','masters','damensch'];
let activeStop=-1;
let walkPosition=positions[0];
let inCar=false;
let walkTarget=positions[0];
let navigationLockUntil=0;
let sceneVisible=true;
let frameTime=0;
function paintWalker(){
 const p=road.getPointAtLength(roadLength*walkPosition);
 inCar=walkPosition>(positions[3]+positions[4])/2;
 $('#car').style.display=inCar?'':'none';
 $('#girlSprite').style.display=inCar?'none':'';
 $('#walker').setAttribute('transform',`translate(${p.x} ${p.y-3})`);
 $('#thoughtBubble').setAttribute('transform',`translate(${Math.max(30,Math.min(vbw-175,p.x+(inCar?-20:24)))} ${p.y-(inCar?160:127)})`);
}
function setStop(i){
 if(i===activeStop)return;
 activeStop=i;walkTarget=positions[i];
 stops.forEach((s,n)=>{s.classList.toggle('active',i===n);if(i===n)s.setAttribute('aria-current','step');else s.removeAttribute('aria-current');});
 buildingIds.forEach((name,n)=>$('#building-'+name).classList.toggle('active',i===n));
 $('#thoughtText').textContent=thoughts[i];
 if(innerWidth<=1000){const w=$('#world').getBoundingClientRect().width;const cw=$('#world').parentElement.clientWidth;const lim=Math.max(0,(w-cw)/2);const s=Math.max(-lim,Math.min(lim,(vbw/2-centers[i])*w/vbw));$('#world').style.transform=`translateX(${s}px)`;}else $('#world').style.transform='';
 if(motionPaused){walkPosition=walkTarget;paintWalker();}
}
function updateChapter(){
 if(Date.now()<navigationLockUntil)return;
 const stageBottom=$('#journeyStage').getBoundingClientRect().bottom;
 let selected=0;
 for(let i=0;i<chapters.length;i++)if(chapters[i].getBoundingClientRect().top<=stageBottom+85)selected=i;
 setStop(selected);
}
function animate(t){
 if(t-frameTime>24){
  const distance=walkTarget-walkPosition;
  if(Math.abs(distance)>.0002){walkPosition=motionPaused?walkTarget:walkPosition+distance*.105;paintWalker();$('#walker').classList.toggle('walking',!motionPaused&&sceneVisible);}
  else{$('#walker').classList.remove('walking');}
  frameTime=t;
 }
 requestAnimationFrame(animate);
}
function updateMotion(){document.body.classList.toggle('motion-paused',motionPaused);$('#motionToggle').setAttribute('aria-pressed',String(motionPaused));$('#motionToggle').textContent=motionPaused?'Resume motion ▷':'Pause motion Ⅱ';if(motionPaused){walkPosition=walkTarget;paintWalker();}}
$('#motionToggle').addEventListener('click',()=>{motionPaused=!motionPaused;updateMotion();});
reduceMotion.addEventListener('change',e=>{motionPaused=e.matches;updateMotion();});
// Stop selection follows the chapter being read below the stable scene.
stops.forEach(a=>a.addEventListener('click',()=>{navigationLockUntil=Date.now()+900;setStop(Number(a.dataset.stop));setTimeout(updateChapter,950);}));
addEventListener('scroll',updateChapter,{passive:true});
addEventListener('resize',()=>{const i=activeStop;activeStop=-1;setStop(i<0?0:i);updateChapter();});
new IntersectionObserver(entries=>{sceneVisible=entries[0].isIntersecting;},{threshold:0}).observe($('#journey'));
// Pause a recording when it is off screen or another recording starts.
const videos=$$('video');
videos.forEach(v=>v.addEventListener('play',()=>videos.forEach(other=>{if(other!==v)other.pause();})));
const videoObserver=new IntersectionObserver(entries=>entries.forEach(e=>{if(!e.isIntersecting)e.target.pause();}),{threshold:0});
videos.forEach(v=>videoObserver.observe(v));
setStop(0);paintWalker();updateMotion();requestAnimationFrame(animate);updateChapter();
addEventListener('load',updateChapter);
const mediaDialog=$('#mediaDialog');let mediaOpener;
document.addEventListener('click',e=>{
 const button=e.target.closest('[data-image]');
 if(!button)return;
 mediaOpener=button;
 $('#largeImage').src=button.dataset.image;$('#largeImage').alt=button.dataset.caption;
 $('#mediaTitle').textContent=button.dataset.caption;
 mediaDialog.showModal();document.body.classList.add('modal-open');$('#closeMedia').focus();
});
$('#closeMedia').addEventListener('click',()=>mediaDialog.close());
mediaDialog.addEventListener('close',()=>{document.body.classList.remove('modal-open');mediaOpener?.focus();});
mediaDialog.addEventListener('click',e=>{if(e.target!==mediaDialog)return;const b=mediaDialog.getBoundingClientRect();if(e.clientX<b.left||e.clientX>b.right||e.clientY<b.top||e.clientY>b.bottom)mediaDialog.close();});
const rounds=[
 {title:'Pick the hero message.',brief:'You’re launching a summer innerwear range. One line goes on every ad, creator brief and product page. Which one?',choices:[['“The softest fabric we’ve ever made.”','Every brand in the drawer can say this. It’s hard to remember and harder to prove.'],['“Still comfortable at hour sixteen.”','A moment people have lived, and a promise a creator can show on camera.'],['“30% off, this week only.”','It moves units this week, but teaches people to wait for the next sale and says nothing about the product.']],takeaway:'Proof beats adjectives.'},
 {title:'One creator budget. How do you spend it?',brief:'Same money either way. Think about reach, trust and what you’ll learn from the launch.',choices:[['Two big stars','Huge reach, but only two data points. If one misses, you’ve learned little and spent half the budget.'],['One macro, 25 micro, and seeding to customers','Reach, trust and reviews at once, and enough creators to see which tier brings the cheapest repeat customers.'],['40 micro creators, nothing else','Great trust and plenty of tests, but slow to build awareness for a launch moment.']],takeaway:'Mix the roster, then let repeat decide.'},
 {title:'Clicks are up. So are size returns.',brief:'Week two of the launch. Click-through is strong, but returns for the wrong size are climbing. What do you do on Monday?',choices:[['Raise spend while it’s hot','More clicks into a leaky size experience means more returns and a higher real CAC.'],['Hold spend and fix fit first','Add a fit finder and a clearer size chart, test them, then scale. In a repeat category, the second order is where the money is.'],['Swap the creative','The creative is working. The problem is after the click, so new creative won’t fix it.']],takeaway:'Fix the leak before you scale.'}
];
let round=0;let gameChoices=[];
function renderGame(){
 $('#gameProgress').textContent=round<3?`0${round+1} / 03`:'COMPLETE';
 if(round===3){$('#gameContent').innerHTML=`<h3>A good instinct.<br>An even better question.</h3><p>Your route through the lab: ${gameChoices.map(i=>String.fromCharCode(65+i)).join(' → ')}. Each choice opened a different trade-off.</p><div class="game-feedback"><strong>The thread through it all</strong><p>Lead with proof. Mix the creator roster. Fix the leak before you scale. Judge it all on the second order, not the first click.</p></div><p style="margin-top:17px">That’s the kind of work I want to keep doing.</p><a href="#contact" class="text-link">Let’s plan the first launch <span>↗</span></a>`;return;}
 const q=rounds[round];$('#gameContent').innerHTML=`<h3>${q.title}</h3><p>${q.brief}</p><div class="game-options">${q.choices.map((c,i)=>`<button class="game-option" data-choice="${i}"><span>${String.fromCharCode(65+i)}</span>${c[0]}<b>↗</b></button>`).join('')}</div><div id="feedback" aria-live="polite"></div>`;
}
$('#gameContent').addEventListener('click',e=>{const option=e.target.closest('[data-choice]');if(option){const i=Number(option.dataset.choice);gameChoices[round]=i;$$('.game-option').forEach(b=>b.disabled=true);option.style.background='#f6ece6';$('#feedback').innerHTML=`<div class="game-feedback"><strong>${rounds[round].takeaway}</strong><p>${rounds[round].choices[i][1]}</p></div><button class="game-next" id="nextRound">${round===2?'Finish the experiment':'Next decision'} →</button>`;}if(e.target.closest('#nextRound')){round++;renderGame();}});
$('#resetGame').addEventListener('click',()=>{round=0;gameChoices=[];renderGame();});
renderGame();

// Opening: "Hi DaMENSCH," then "I’m DaMENSCH" becomes "I’m DaISHANI."
(function(){
 const screen=$('#introScreen');if(!screen)return;
 document.body.classList.add('intro-open');
 const hi=$('#typeHi'),me=$('#typeMe'),cH=$('#caretHi'),cM=$('#caretMe'),role=$('#introRole'),go=$('#introGo');
 let done=false,timers=[];
 const later=(fn,ms)=>timers.push(setTimeout(fn,ms));
 const FINAL='I’m Da<b>ISHANI.</b>';
 function finish(){
  if(done)return;done=true;timers.forEach(clearTimeout);
  hi.textContent='Hi DaMENSCH,';me.innerHTML=FINAL;
  screen.classList.add('leaving');document.body.classList.remove('intro-open');document.body.classList.add('hero-in');
  setTimeout(()=>screen.classList.add('gone'),650);
 }
 function type(el,pre,text,speed,cb){let i=0;(function step(){el.innerHTML=pre+text.slice(0,i);if(i++<text.length)later(step,speed);else cb&&cb();})();}
 function erase(el,pre,text,speed,cb){let i=text.length;(function step(){el.innerHTML=pre+'<s>'+text.slice(0,i)+'</s>';if(i-->0)later(step,speed);else cb&&cb();})();}
 if(reduceMotion.matches){hi.textContent='Hi DaMENSCH,';me.innerHTML=FINAL;role.classList.add('show');go.classList.add('show');later(finish,1600);}
 else{
  cH.classList.add('on');
  later(()=>type(hi,'','Hi DaMENSCH,',70,()=>{cH.classList.remove('on');cM.classList.add('on');
   later(()=>type(me,'','I’m DaMENSCH',70,()=>{
    later(()=>erase(me,'I’m Da','MENSCH',60,()=>{
     later(()=>type(me,'I’m Da<b>','ISHANI.',85,()=>{
      me.innerHTML=FINAL;cM.classList.remove('on');
      later(()=>role.classList.add('show'),250);later(()=>go.classList.add('show'),600);later(finish,3400);
     }),200);
    }),450);
   }),250);
  }),400);
 }
 go.addEventListener('click',finish);$('#introSkip').addEventListener('click',finish);
 addEventListener('keydown',e=>{if(e.key==='Escape'||e.key==='Enter')finish();});
})();
