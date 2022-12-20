from flask import Flask, render_template, request, redirect, jsonify
import pickle, random, string
import os.path

def randomstring(length):
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=length
        )
    )

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/newurl', methods=['GET', 'POST'])
def shortenurl():
    if request.method == 'POST':
      reqjson = request.json
      absolute = reqjon.get('url')
      shorten = randomstring(8)
      
      filename = "urlmap.pkl"
      if os.path.exists(filename):
        urlmapfile = open(filename, "rb")
        urlmapdict = pickle.load(urlmapfile)
        urlmapfile.close()
      else:
        urlmapdict = {}
      
      urlmapdict[shorten] = absolute
      urlmapfile = open(filename, "wb")
      pickle.dump(urlmapdict, urlmapfile)
      urlmapfile.close()
      
      return jsonify(
        url=absolute,
        shortenUrl=f"https://shortenurl.org/{shorten}"
      )
    
@app.route('/<shortpath>')
def travel(shortpath):
    filename = "urlmap.pkl"
    if os.path.exists(filename):
        urlmapfile = open(filename, "rb")
        urlmapdict = pickle.load(urlmapfile)
        if shortpath in urlmapdict:
            fullurl = urlmapdict[shortpath]
            urlmapfile.close()
            return redirect(fullurl)
        else:
            return(f"Short URL ({shortpath}) is not found!\n")
    else:
        return "URL mapping file does not exist!\n"
