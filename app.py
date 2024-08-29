from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


# Routing

@app.route('/main')
def main():
    # Wypełnianie danych
    # df['contributors'] = df['repo_url'].apply(get_contributors_count)
    # df['commits'] = df['repo_url'].apply(get_commit_count)
    # df['used_by'] = df['repo_url'].apply(get_used_by_count)

    # df.to_csv('processed_data.txt', sep='\t', index=False)

    # # Przygotowanie danych do wyświetlenia

    df = pd.read_csv('processed_data.txt', sep='\t')

    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)


@app.route('/')
def index():
    return render_template('main.html')



@app.route('/commits')
def plot():
    # df['contributors'] = df['repo_url'].apply(get_contributors_count)
    # df['commits'] = df['repo_url'].apply(get_commit_count)
    # df['used_by'] = df['repo_url'].apply(get_used_by_count)

    # palette_color = sns.color_palette('pastel')
    # df_sorted = df.sort_values(by='commits', ascending=False)
    # plt.figure(figsize=(8, 10))
    # sns.barplot(y=df_sorted['commits'], x=df_sorted['repo_name'], palette=palette_color)
    # plt.title('Number of commits comparison')
    # plt.ylabel('Number of commits')
    # plt.xlabel('Repository')
    # plt.xticks(rotation=90)

    # # Zapisz wykres jako plik PNG
    # image_path = '/static/images/plot.png'
    # plt.savefig(f'.{image_path}')
    # plt.close()

    # Przekazanie ścieżki do wykresu do szablonu
    # return render_template('commits.html', image_url=image_path)
    return render_template('commits.html')


@app.route('/contributors')
def contributors():
    # df_sorted = df.sort_values(by='contributors', ascending=False)

    # palette_color = sns.color_palette('pastel')
    # plt.figure(figsize=(8, 10))
    # plt.pie(df_sorted['contributors'], labels=df_sorted['repo_name'], autopct='%1.1f%%', startangle=140, colors = palette_color)
    # plt.axis('equal')
    # plt.title('Contributors comparison')
    # plt.show()

    # total_contributors = df['contributors'].sum()
    # one_percent = total_contributors / 100

    # # Zapisz wykres jako plik PNG
    # image_path = '/static/images/contributors.png'
    # plt.savefig(f'.{image_path}')
    # plt.close()

    # return render_template('contributors.html', image_url=image_path)
    return render_template('contributors.html')


@app.route('/usedby')
def usedby():
    # palette_color = sns.color_palette('pastel')

    # df_used = df[df['used_by']!=0]

    # df_used = df_used.sort_values(by='used_by', ascending=False)
    # plt.figure(figsize=(8, 10))
    # sns.barplot(y=df_used['used_by'], x=df_used['repo_name'], palette=palette_color)
    # plt.title('Number of people using a Repository/Framework/App')
    # plt.ylabel('Number of commits in mln')
    # plt.xlabel('Repository')
    # plt.xticks(rotation=90)
    # plt.show()

    # # Zapisz wykres jako plik PNG
    # image_path = '/static/images/usedby.png'
    # plt.savefig(f'.{image_path}')
    # plt.close()

    # return render_template('usedby.html', image_url=image_path)
    return render_template('usedby.html')


@app.route('/stars')
def stars():
    return render_template('stars.html')


@app.route('/circlesstars')
def circlesstars():
    return render_template('circlesstars.html')


@app.route('/starsByDateFCC')
def starsByDateFCC():
    return render_template('starsByDateFCC.html')


@app.route('/issuesByDateFCC')
def issuesByDate():
    return render_template('issuesByDateFCC.html')


@app.route('/forksByDateFCC')
def forksByDate():
    return render_template('forksByDateFCC.html')


@app.route('/mostShare')
def mostShare():
    return render_template('mostShare.html')


@app.route('/numberOfStarsT20')
def numberOfStarsT20():
    return render_template('numberOfStarsT20.html')


@app.route('/numberOfForksT20')
def numberOfForksT20():
    return render_template('numberOfForksT20.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12142, debug=True)
