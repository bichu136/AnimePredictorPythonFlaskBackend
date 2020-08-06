import flask as flk
import numpy as np
import json
# import keras
# import keras.layers as layers
# import keras.models as models
import tensorflow as tf

app = flk.Flask(__name__)
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(input_details[0]["shape"])

@app.route("/")
def index():
    return flk.render_template("index.html")
@app.route("/AnimeScorePredictor")
def anime_score_predictor():
    genres = ['Action',
            'Adventure',
            'Cars',
            'Comedy',
            'Dementia',
            'Demons',
            'Drama',
            'Ecchi',
            'Fantasy',
            'Game',
            'Harem',
            'Hentai',
            'Historical',
            'Horror',
            'Josei',
            'Kids',
            'Magic',
            'Martial Arts',
            'Mecha',
            'Military',
            'Music',
            'Mystery',
            'Parody',
            'Police',
            'Psychological',
            'Romance',
            'Samurai',
            'School',
            'Sci-Fi',
            'Seinen',
            'Shoujo',
            'Shoujo Ai',
            'Shounen',
            'Shounen Ai',
            'Slice of Life',
            'Space',
            'Sports',
            'Super Power',
            'Supernatural',
            'Thriller',
            'Vampire']
    studio = ['10Gauge',
        '8bit',
        'A-1 Pictures',
        'A-Real',
        'A.C.G.T.',
        'ACC Production',
        'AIC',
        'AIC A.S.T.A.',
        'AIC Build',
        'AIC Classic',
        'AIC Plus+',
        'AIC Spirits',
        'APPP',
        'AXsiZ',
        'Actas',
        'Ajia-Do',
        'Animaruya',
        'Anime R',
        'Anpro',
        'Arms',
        'Artland',
        'Artmic',
        'Asahi Production',
        'Ascension',
        'Ashi Production',
        'Asread',
        'Aubec',
        'B&amp;T',
        'Bandai Namco Pictures',
        'Barnum Studio',
        'Bee Media',
        'Bee Train',
        'Beijing Rocen Digital',
        'Blade',
        'Bones',
        'Bouncy',
        'Brain&#039;s Base',
        'Bridge',
        'Buemon',
        'C-Station',
        'C2C',
        'Calf Studio',
        'Chaos Project',
        'Charaction',
        'CoMix Wave Films',
        'Craftar',
        'Creators in Pack',
        'D &amp; D Pictures',
        'DAX Production',
        'DLE',
        'Daewon Media',
        'Daichi Doga',
        'Daume',
        'David Production',
        'Digital Frontier',
        'Diomedea',
        'Doga Kobo',
        'Dongwoo A&amp;E',
        'Dwango',
        'Dynamo Pictures',
        'E&amp;G Films',
        'EMT²',
        'Echo',
        'Egg',
        'Eiken',
        'Ekura Animal',
        'Emon',
        'Encourage Films',
        'Enoki Films',
        'Fanworks',
        'Front Line',
        'Fuji TV',
        'Fukushima Gainax',
        'Future Planet',
        'G&amp;G Entertainment',
        'G.CMay Animation &amp; Film',
        'Gainax',
        'Gakken Eigakyoku',
        'Gathering',
        'Genco',
        'Geno Studio',
        'Ginga Ya',
        'GoHands',
        'Gonzo',
        'Graphinica',
        'Group TAC',
        'HS Pictures Studio',
        'Hal Film Maker',
        'Haoliners Animation League',
        'Heewon Entertainment',
        'Hoods Drifters Studio',
        'Hoods Entertainment',
        'Hotline',
        'ILCA',
        'Imagin',
        'Ishimori Entertainment',
        'J.C.Staff',
        'JCF',
        'Japan Taps',
        'Japan Vistec',
        'Jinnis Animation Studios',
        'Joker Films',
        'KAGAYA Studio',
        'KOO-KI',
        'Kachidoki Studio',
        'Kamikaze Douga',
        'Kanaban Graphics',
        'Karaku',
        'Kazami Gakuen Koushiki Douga-bu',
        'Kenji Studio',
        'Khara',
        'Kinema Citrus',
        'Knack Productions',
        'Kokusai Eigasha',
        'Kyoto Animation',
        'Kyotoma',
        'LIDENFILMS',
        'LMD',
        'LandQ studios',
        'Lay-duce',
        'Lerche',
        'Life Work',
        'Light Chaser Animation Studios',
        'Lilix',
        'M.S.C',
        'M2',
        'MAPPA',
        'Madhouse',
        'Magic Bus',
        'Manglobe',
        'Marza Animation Planet',
        'Mili Pictures',
        'Milky Cartoon',
        'Millepensee',
        'Mook DLE',
        'Mushi Production',
        'NAZ',
        'NHK',
        'NUT',
        'Namu Animation',
        'Nexus',
        'Nice Boat Animation',
        'Nippon Animation',
        'Nomad',
        'OLM',
        'OLM Digital',
        'October Media',
        'Oddjob',
        'Odolttogi',
        'Office DCI',
        'Oh! Production',
        'Opera House',
        'Orange',
        'Ordet',
        'Oxybot',
        'P.A. Works',
        'PRA',
        'Palm Studio',
        'Panmedia',
        'Passione',
        'Pastel',
        'Phoenix Entertainment',
        'Picograph',
        'Picture Magic',
        'Pie in The Sky',
        'Pierrot Plus',
        'Pine Jam',
        'Planet',
        'Platinum Vision',
        'Plum',
        'Pollyanna Graphics',
        'Polygon Pictures',
        'Production I.G',
        'Production IMS',
        'Production Reed',
        'Project No.9',
        'Puzzle Animation Studio Limited',
        'Qualia Animation',
        'RG Animation Studios',
        'Radix',
        'Remic',
        'Ripromo',
        'Rising Force',
        'SANZIGEN',
        'Sanrio',
        'Satelight',
        'Science SARU',
        'Seven',
        'Seven Arcs',
        'Seven Arcs Pictures',
        'Shaft',
        'Shanghai Animation Film Studio',
        'Shin-Ei Animation',
        'Shirogumi',
        'Shochiku Animation Institute',
        'Shuka',
        'Signal. MD',
        'Silver Link.',
        'Sotsu',
        'Sparkly Key Animation Studio',
        'Square Enix',
        'Steve N&#039; Steven',
        'Sting Ray',
        'Strawberry Meets Pictures',
        'Studio 3Hz',
        'Studio 4°C',
        'Studio A-CAT',
        'Studio Bogey',
        'Studio Chizu',
        'Studio Colorido',
        'Studio Comet',
        'Studio Deen',
        'Studio Egg',
        'Studio Fantasia',
        'Studio Flad',
        'Studio Flag',
        'Studio Gallop',
        'Studio Ghibli',
        'Studio Gokumi',
        'Studio Hibari',
        'Studio Junio',
        'Studio Korumi',
        'Studio Kyuuma',
        'Studio Live',
        'Studio Matrix',
        'Studio Meditation With a Pencil',
        'Studio Pierrot',
        'Studio Ponoc',
        'Studio PuYUKAI',
        'Studio Rikka',
        'Studio Sign',
        'Studio Zero',
        'Studio! Cucuri',
        'Sunrise',
        'Sunwoo Entertainment',
        'SynergySP',
        'TMS Entertainment',
        'TNK',
        'TROYCA',
        'TYO Animations',
        'TYPHOON GRAPHICS',
        'Tama Production',
        'Tamura Shigeru Studio',
        'Tatsunoko Production',
        'Team YokkyuFuman',
        'Tele-Cartoon Japan',
        'Telecom Animation Film',
        'Telescreen BV',
        'Tengu Kobo',
        'Tezuka Productions',
        'The Answer Studio',
        'Think Corporation',
        'Toei Animation',
        'Tokyo Kids',
        'Tokyo Movie Shinsha',
        'Tomovies',
        'Tomoyasu Murata Company',
        'Tonko House',
        'Topcraft',
        'Trans Arts',
        'Triangle Staff',
        'Trigger',
        'Trinet Entertainment',
        'Tsuchida Productions',
        'Usagi Ou',
        'Vega Entertainment',
        'View Works',
        'Visual 80',
        'W-Toon Studio',
        'WAO World',
        'White Fox',
        'Wit Studio',
        'Xebec',
        'Xebec Zwei',
        'Yamamura Animation',
        'Yamato Works',
        'Yaoyorozu',
        'Yumeta Company',
        'Zero-G',
        'Zexcs',
        'drop',
        'dwarf',
        'feel.',
        'helo.inc',
        'ixtl',
        'pH Studio',
        'production doA',
        'ufotable']
    source = ['4-koma manga', 'Book', 'Card game',
        'Digital manga', 'Game', 'Light novel',
        'Manga', 'Music', 'Novel', 'Original',
        'Picture book', 'Radio', 'Visual novel',
        'Web manga']
    return flk.render_template("AnimePredictor.html",genre_list=genres,studio_list = studio, source_list = source)
@app.route("/api",methods=["POST"])
def testJSONPOST():
    data = flk.request.get_json()
    inp = np.array([data["array"]],dtype=np.float32)
    print(inp.shape)
    interpreter.set_tensor(input_details[0]['index'], inp)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    result = float(output_data[0][0])
    return flk.jsonify(result)
@app.route("/result")
def result():
    x = flk.request.args.get("score")
    return flk.render_template("result.html",score = x)
if __name__ == '__main__':
    app.run(debug=True)

