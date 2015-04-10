#/usr/bin/python

def postToSMF(url,username,password,title,description,cat=["1"]):
        #cookie
        cookie = url.replace("http://","").replace(".","").strip()
        cookieFilenameLWP = "tmp/"+cookie+".txt";
        cookieJarFileLWP = cookielib.LWPCookieJar(cookieFilenameLWP);
        cookieJarFileLWP.save();
 
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarFileLWP))
        urllib2.install_opener(opener);
 
        #login
        form_data = {'user':username, 'passwrd' : password}
        form_data = urllib.urlencode(form_data)
        response = urllib2.urlopen(url+"/index.php?action=login2",form_data)
        cookieJarFileLWP.save();
 
        #get Seqnum
        response = urllib2.urlopen(url+"/index.php?action=post;board="+cat).read()
        seq = re.search('name="seqnum" value="(.+?)"',response).group(1)
        sesVar = re.search('sSessionVar: \'(.+?)\'',response).group(1)
        sesID = re.search('sSessionId: \'(.+?)\'',response).group(1)
 
        #post
        field = {'topic':'0','subject':title,'icon':'xx','sel_face':'','sel_size':'','sell_color':'','message':description,'message_mode':'0','notify':'0','lock':'0','sticky':'0','move':'0','additional_options':'0',sesVar:sesID,'seqnum':seq}
        field = urllib.urlencode(field)
        urllib2.urlopen(url+"/index.php?action=post2;start=0;board="+cat,field)