# ********** Codul PYTHON PENTRU SITEUL MEU === DREAMCODE LABELS SRL ********** #

from flask import Flask, render_template, request
import post_conn as pcn

app = Flask("My_app")


# ********** Conexiunea cu baza de date ( PostgreSQL ) ********** #
def get_db_connection():
    conn = pcn.connection_postgres()
    return conn


# ********** Inceputul Rutelor ********** #

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', home=home)


@app.route('/about/')
def about():
    return render_template('about.html', about=about)


@app.route('/contact/')
def contact():
    return render_template('contact.html', contact=contact)


# ********** Pagina Form (Contact) care comunica cu baza de date ( PostgreSQL ) ********** #
@app.route('/form/', methods=['POST'])
def form():
    if request.method == 'POST':
        name = request.form["user"]
        mail = request.form["email"]
        subject = request.form["subject"]
        quantity = request.form["quantity"]
        size = request.form["size"]
        company = request.form["company"]
        material = request.form["natural"]

        if name and mail and subject and quantity and size and company and material != '':
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("insert into clients(client_name, client_mail, client_subject, client_quantity, client_size, "
                        "client_company, client_material) values (%s, %s, %s, %s, %s, %s, %s)",
                        (name, mail, subject, quantity, size, company, material))

            conn.commit()
            conn.close()
        else:
            render_template('contact.html')
        return render_template('contact.html', name=name, mail=mail, subject=subject,
                               quantity=quantity, size=size, company=company, material=material)


# ********** Pagina - Calculator De Preturi ********** #
@app.route('/calculator/')
def calcule():
    return render_template('calculator.html', calcule=calcule)


@app.route('/calculation1/', methods=['POST'])
def calculation1():
    if request.method == 'POST':
        eticha = 0.15
        eth_input = float(request.form["canta"].strip() or 0)
        price_eticha = round(float(eticha * eth_input), 2)

        if eth_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_eticha=price_eticha)


@app.route('/calculation2/', methods=['POST'])
def calculation2():
    if request.method == 'POST':
        etichb = 0.25
        etp_input = float(request.form["cantb"].strip() or 0)
        price_etichb = round(float(etichb * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichb=price_etichb)


@app.route('/calculation3/', methods=['POST'])
def calculation3():
    if request.method == 'POST':
        etichc = 0.40
        etp_input = float(request.form["cantc"].strip() or 0)
        price_etichc = round(float(etichc * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichc=price_etichc)


@app.route('/calculation4/', methods=['POST'])
def calculation4():
    if request.method == 'POST':
        etichd = 0.80
        etp_input = float(request.form["cantd"].strip() or 0)
        price_etichd = round(float(etichd * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichd=price_etichd)


@app.route('/calculation5/', methods=['POST'])
def calculation5():
    if request.method == 'POST':
        etiche = 1.1
        etp_input = float(request.form["cante"].strip() or 0)
        price_etiche = round(float(etiche * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etiche=price_etiche)


@app.route('/calculation6/', methods=['POST'])
def calculation6():
    if request.method == 'POST':
        etichf = 0.08
        etp_input = float(request.form["cantf"].strip() or 0)
        price_etichf = round(float(etichf * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichf=price_etichf)


@app.route('/calculation7/', methods=['POST'])
def calculation7():
    if request.method == 'POST':
        etichg = 0.12
        etp_input = float(request.form["cantg"].strip() or 0)
        price_etichg = round(float(etichg * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichg=price_etichg)


@app.route('/calculation8/', methods=['POST'])
def calculation8():
    if request.method == 'POST':
        etichh = 0.2
        etp_input = float(request.form["canth"].strip() or 0)
        price_etichh = round(float(etichh * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichh=price_etichh)


@app.route('/calculation9/', methods=['POST'])
def calculation9():
    if request.method == 'POST':
        etichi = 0.4
        etp_input = float(request.form["canti"].strip() or 0)
        price_etichi = round(float(etichi * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichi=price_etichi)


@app.route('/calculation10/', methods=['POST'])
def calculation10():
    if request.method == 'POST':
        etichj = 0.55
        etp_input = float(request.form["cantj"].strip() or 0)
        price_etichj = round(float(etichj * etp_input), 2)

        if etp_input == "":
            return render_template('calculator.html')
        else:
            return render_template('calculator.html', price_etichj=price_etichj)


if __name__ == '__main__':
    app.run(debug=True)
